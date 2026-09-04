"""Shared visual system for 'Under the Ice'. One palette, one grain, one vignette."""
from PIL import Image, ImageDraw, ImageFilter, ImageChops
import math, random

W, H = 2560, 1440          # oversized: gives ffmpeg headroom to pan/zoom into
FPS = 30

# --- palette -------------------------------------------------------------
BONE   = (232, 237, 240)
ICE    = (168, 196, 208)
ICE_D  = (108, 141, 158)
TEAL   = (74, 122, 140)
NAVY   = (15, 26, 36)
BLACK  = (6, 10, 14)
ROCK   = (38, 44, 52)
AMBER  = (232, 184, 74)     # the only warm colour in the film - the robot
WATER  = (12, 30, 42)

def lerp(a, b, t): return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))

def vgrad(img, top, bottom, box=None):
    """Vertical gradient, optionally confined to a box."""
    x0, y0, x1, y1 = box or (0, 0, img.width, img.height)
    d = ImageDraw.Draw(img)
    span = max(1, y1-y0)
    for y in range(y0, y1):
        d.line([(x0, y), (x1, y)], fill=lerp(top, bottom, (y-y0)/span))

def radial(img, cx, cy, r, inner, outer, steps=90):
    d = ImageDraw.Draw(img, "RGBA")
    for i in range(steps, 0, -1):
        t = i/steps
        rr = r*t
        c = lerp(outer, inner, 1-t)
        d.ellipse([cx-rr, cy-rr, cx+rr, cy+rr], fill=c+(255,))

def haze(img, amount=0.20, y=None):
    """Atmospheric depth - a soft light band that separates layers."""
    y = img.height//2 if y is None else y
    lay = Image.new("RGB", img.size, BLACK)
    vgrad(lay, BLACK, ICE, (0, max(0, y-300), img.width, min(img.height, y+300)))
    lay = lay.filter(ImageFilter.GaussianBlur(180))
    return Image.blend(img, ImageChops.screen(img, lay), amount)

def grain(img, strength=9, seed=0):
    rnd = random.Random(seed)
    n = Image.new("L", (img.width//2, img.height//2))
    n.putdata([128 + rnd.randint(-strength, strength) for _ in range(n.width*n.height)])
    n = n.resize(img.size, Image.BILINEAR).filter(ImageFilter.GaussianBlur(0.4))
    return ImageChops.overlay(img, Image.merge("RGB", (n, n, n)))

def vignette(img, power=0.72):
    m = Image.new("L", img.size, 0)
    d = ImageDraw.Draw(m)
    d.ellipse([-img.width*0.22, -img.height*0.30,
               img.width*1.22,  img.height*1.30], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(340))
    dark = Image.new("RGB", img.size, BLACK)
    return Image.composite(img, Image.blend(img, dark, power), m)

def finish(img, seed=0, vig=0.72, grn=9):
    """Every scene ends here. This is what makes 30 shots look like one film."""
    return vignette(grain(img, grn, seed), vig)

def base(bg=NAVY):
    return Image.new("RGB", (W, H), bg)

def snowdrift(img, y0, y1, n=170, seed=1, col=BONE, alpha=70):
    """Wind-driven surface streaks. Cheap, and reads instantly as polar."""
    rnd = random.Random(seed)
    lay = Image.new("RGBA", img.size, (0,0,0,0))
    d = ImageDraw.Draw(lay)
    for _ in range(n):
        y = rnd.randint(y0, y1)
        x = rnd.randint(-200, W)
        L = rnd.randint(120, 620)
        w = rnd.choice([1,1,2])
        a = int(alpha * (0.3 + 0.7*rnd.random()))
        d.line([(x, y), (x+L, y+rnd.randint(-2,2))], fill=col+(a,), width=w)
    lay = lay.filter(ImageFilter.GaussianBlur(1.2))
    return Image.alpha_composite(img.convert("RGBA"), lay).convert("RGB")

def particles(img, n=260, seed=3, col=ICE, amax=120, rmax=4):
    """Suspended sediment for the underwater scenes."""
    rnd = random.Random(seed)
    lay = Image.new("RGBA", img.size, (0,0,0,0))
    d = ImageDraw.Draw(lay)
    for _ in range(n):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        r = rnd.randint(1, rmax)
        d.ellipse([x-r, y-r, x+r, y+r], fill=col+(rnd.randint(20, amax),))
    return Image.alpha_composite(img.convert("RGBA"), lay.filter(ImageFilter.GaussianBlur(1.0))).convert("RGB")

def beam(img, x, y, r, col=BONE, strength=0.55):
    """A lamp's pool of light."""
    lay = Image.new("RGB", img.size, BLACK)
    radial(lay, x, y, r, col, BLACK)
    lay = lay.filter(ImageFilter.GaussianBlur(90))
    return Image.blend(img, ImageChops.screen(img, lay), strength)
