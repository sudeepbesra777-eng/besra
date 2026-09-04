import sys; sys.path.insert(0, '/home/user/besra/render')
from style import *
from PIL import Image, ImageDraw, ImageFilter
import math

def _sky_and_plain(horizon=620, seed=1, sky_t=NAVY, sky_b=ICE_D):
    im = base(); vgrad(im, sky_t, sky_b, (0,0,W,horizon))
    vgrad(im, BONE, lerp(BONE, ICE, .55), (0,horizon,W,H))
    im = haze(im, .28, horizon)
    return snowdrift(im, horizon+40, H-40, seed=seed)

def _shaft(im, cx, top, w_top, w_bot, bottom, wall=ICE):
    d = ImageDraw.Draw(im, "RGBA")
    d.polygon([(cx-w_top,top),(cx+w_top,top),(cx+w_bot,bottom),(cx-w_bot,bottom)], fill=wall+(255,))
    for i in range(26):                       # translucent depth falloff
        t=i/26; y0=top+(bottom-top)*t
        d.polygon([(cx-w_top*(1-t*.7),y0),(cx+w_top*(1-t*.7),y0),
                   (cx+w_top*(1-(t+.04)*.7),y0+(bottom-top)/26),
                   (cx-w_top*(1-(t+.04)*.7),y0+(bottom-top)/26)],
                  fill=BLACK+(int(255*t*.95),))
    return im

def _xsec(bed_l, bed_r, ice_top=430, water=True, label_bed=ROCK):
    """Side-on cross-section diorama. Reused across blocks 7,8,24,25."""
    im = base(BLACK)
    vgrad(im, BLACK, lerp(BLACK, NAVY, .8))
    d = ImageDraw.Draw(im, "RGBA")
    if water:
        d.polygon([(1500,700),(W,700),(W,H),(1500,H)], fill=WATER+(255,))
    d.polygon([(0,bed_l),(W,bed_r),(W,H),(0,H)], fill=label_bed+(255,))     # bedrock
    d.polygon([(0,ice_top),(W,ice_top+60),(W,bed_r),(0,bed_l)], fill=ICE+(255,))
    d.polygon([(0,ice_top),(W,ice_top+60),(W,ice_top+130),(0,ice_top+80)], fill=BONE+(255,))
    return haze(im, .16, ice_top)

# ---------------- ACT 1 ----------------
def s01():                                   # vast plain, one dark dot
    im = _sky_and_plain(560, 11)
    d = ImageDraw.Draw(im, "RGBA")
    d.ellipse([W//2-26, 1010, W//2+26, 1040], fill=BLACK+(255,))
    d.ellipse([W//2-40, 1002, W//2+40, 1048], outline=ICE_D+(90,), width=3)
    return finish(im, 1)

def s02():                                   # the borehole, close
    im = _sky_and_plain(120, 12, NAVY, ICE)
    im = _shaft(im, W//2, 300, 300, 120, H)
    d = ImageDraw.Draw(im, "RGBA")
    d.ellipse([W//2-300, 200, W//2+300, 400], fill=ICE_D+(255,))
    d.ellipse([W//2-250, 232, W//2+250, 368], fill=BLACK+(255,))
    return finish(snowdrift(im, 60, 280, 90, 13), 2)

def s03():                                   # robot descending the shaft
    im = base(BLACK); vgrad(im, ICE_D, BLACK, (0,0,W,H))
    im = _shaft(im, W//2, 0, 520, 300, H)
    d = ImageDraw.Draw(im, "RGBA")
    d.line([(W//2,0),(W//2,700)], fill=ICE_D+(200,), width=5)               # cable
    d.rounded_rectangle([W//2-52, 700, W//2+52, 1000], 52, fill=AMBER+(255,))
    d.ellipse([W//2-30, 960, W//2+30, 1010], fill=BONE+(255,))
    im = beam(im, W//2, 1080, 460, BONE, .5)
    return finish(im, 3)

def s04():                                   # Antarctica from orbit  (TITLE)
    im = base(BLACK)
    d = ImageDraw.Draw(im, "RGBA")
    cx, cy, r = W//2, H//2+120, 620
    radial(im, cx, cy-60, r+220, lerp(NAVY,TEAL,.35), BLACK)
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=BONE+(255,))
    rnd = __import__("random").Random(4)
    for _ in range(90):                                                     # shelf texture
        a = rnd.random()*6.283; rr = rnd.random()*r*0.95
        x, y = cx+math.cos(a)*rr, cy+math.sin(a)*rr
        s = rnd.randint(30, 150)
        d.ellipse([x-s, y-s*.5, x+s, y+s*.5], fill=ICE+(rnd.randint(30,90),))
    d.arc([cx-r-8, cy-r-8, cx+r+8, cy+r+8], 190, 350, fill=ICE+(200,), width=9)
    return finish(im, 4, .60)

def s05():                                   # cross-section: rock under ice
    im = _xsec(1120, 1160, 430, water=True)
    return finish(im, 5)

def s06():                                   # vertical scale: jet above, bed below
    im = base(BLACK); vgrad(im, NAVY, ICE_D, (0,0,W,700))
    d = ImageDraw.Draw(im, "RGBA")
    d.polygon([(0,700),(W,700),(W,760),(0,760)], fill=BONE+(255,))          # surface
    d.polygon([(0,760),(W,760),(W,1240),(0,1240)], fill=ICE+(255,))         # ice column
    d.polygon([(0,1240),(W,1240),(W,H),(0,H)], fill=ROCK+(255,))            # bedrock
    for y in (300, 700, 1240):
        d.line([(300,y),(W-300,y)], fill=BONE+(70,), width=2)
    d.polygon([(W//2-46,292),(W//2+46,300),(W//2-46,308)], fill=BONE+(255,))# jet
    d.line([(W//2-70,300),(W//2+70,300)], fill=BONE+(180,), width=3)
    return finish(haze(im, .18, 700), 6)

def s07():                                   # Thwaites vs Great Britain
    im = base(BLACK); vgrad(im, BLACK, NAVY)
    d = ImageDraw.Draw(im, "RGBA")
    rnd = __import__("random").Random(7)
    pts = [(W//2+math.cos(a*.35)*(420+rnd.randint(-70,70)),
            H//2+math.sin(a*.35)*(300+rnd.randint(-60,60))) for a in range(18)]
    d.polygon(pts, fill=ICE+(255,))
    d.polygon(pts, outline=BONE+(220,), width=5)
    gb = [(1720,470),(1790,600),(1755,760),(1810,900),(1740,1010),(1690,900),(1715,740),(1670,600)]
    d.polygon(gb, fill=AMBER+(70,)); d.polygon(gb, outline=AMBER+(220,), width=4)
    return finish(im, 7)

def s08():                                   # bed below sea level, sloping inland
    return finish(_xsec(760, 1180, 400), 8)

def s09():                                   # warm water reaching underneath
    im = _xsec(760, 1180, 400)
    d = ImageDraw.Draw(im, "RGBA")
    for i, y in enumerate(range(820, 1160, 68)):                            # intruding arrows
        x0 = W-160 - i*40
        d.line([(x0, y), (x0-560, y-40)], fill=AMBER+(210,), width=7)
        d.polygon([(x0-560,y-40),(x0-500,y-66),(x0-498,y-16)], fill=AMBER+(230,))
    return finish(im, 9)

def s10():                                   # aerial: nothing looks wrong
    im = _sky_and_plain(300, 14, NAVY, ICE_D)
    return finish(haze(im, .34, 300), 10)

# ---------------- ACT 2 ----------------
def s11():                                   # field camp on the ice
    im = _sky_and_plain(640, 15)
    d = ImageDraw.Draw(im, "RGBA")
    d.polygon([(1180,700),(1240,560),(1300,700)], fill=ROCK+(255,))         # rig
    d.line([(1240,560),(1240,760)], fill=ROCK+(255,), width=8)
    for x in (900, 1000, 1520, 1620):                                       # crates + tents
        d.rectangle([x, 690, x+70, 740], fill=lerp(ROCK,ICE_D,.4)+(255,))
    d.polygon([(1660,740),(1730,660),(1800,740)], fill=lerp(BONE,ICE,.5)+(255,))
    return finish(im, 11)

def s12():                                   # hose into the hole, steam
    im = _sky_and_plain(420, 16, NAVY, ICE)
    im = _shaft(im, W//2+120, 700, 150, 70, H)
    d = ImageDraw.Draw(im, "RGBA")
    d.line([(300,300),(W//2+120,760)], fill=ROCK+(255,), width=16)          # hose
    st = Image.new("RGB", im.size, BLACK)
    radial(st, W//2+120, 700, 420, BONE, BLACK)
    im = Image.blend(im, ImageChops.screen(im, st.filter(ImageFilter.GaussianBlur(120))), .45)
    return finish(im, 12)

def s13():                                   # Icefin in profile
    im = base(BLACK); vgrad(im, NAVY, BLACK)
    d = ImageDraw.Draw(im, "RGBA")
    d.rounded_rectangle([620, H//2-70, 1940, H//2+70], 70, fill=AMBER+(255,))
    d.ellipse([1860, H//2-52, 1990, H//2+52], fill=BONE+(255,))             # lamp
    for x in (900, 1180, 1460):
        d.rectangle([x, H//2-110, x+58, H//2+110], fill=lerp(AMBER,ROCK,.55)+(255,))
    return finish(im, 13)

def s14():                                   # sensors + tether (callout frame)
    im = base(BLACK); vgrad(im, NAVY, BLACK)
    d = ImageDraw.Draw(im, "RGBA")
    d.rounded_rectangle([620, H//2-70, 1940, H//2+70], 70, fill=AMBER+(255,))
    d.ellipse([1860, H//2-52, 1990, H//2+52], fill=BONE+(255,))
    for x, up in ((820,1),(1240,0),(1700,1)):                               # leader lines
        y2 = H//2-330 if up else H//2+330
        d.line([(x, H//2), (x, y2)], fill=BONE+(150,), width=3)
        d.ellipse([x-9, y2-9, x+9, y2+9], fill=BONE+(230,))
    d.line([(620, H//2), (120, H//2-260)], fill=ICE_D+(200,), width=6)      # cable
    return finish(im, 14)

def s15():                                   # emerging into the cavity
    im = base(BLACK); vgrad(im, BLACK, WATER)
    d = ImageDraw.Draw(im, "RGBA")
    d.polygon([(0,0),(W,0),(W,300),(0,380)], fill=ICE_D+(255,))             # ceiling above
    d.rounded_rectangle([1100, 620, 1720, 740], 60, fill=AMBER+(255,))
    im = beam(im, 1900, 700, 720, BONE, .5)
    return finish(particles(im, 200, 15), 15)

# ---------------- ACT 3 ----------------
def _ceiling(terraced=True, seed=16):
    im = base(BLACK); vgrad(im, WATER, BLACK, (0,400,W,H))
    d = ImageDraw.Draw(im, "RGBA")
    rnd = __import__("random").Random(seed)
    if terraced:
        y = 120
        for i in range(7):                                                  # inverted staircase
            x0 = 0 if i%2 else 0
            d.polygon([(0,y),(W,y-40),(W,y+150),(0,y+190)], fill=lerp(ICE,ICE_D,i/7)+(255,))
            y += 120
        for x in range(200, W, 380):                                        # fissures
            d.polygon([(x,120),(x+70,120),(x+30,760+rnd.randint(-80,120))], fill=BLACK+(235,))
    else:
        d.polygon([(0,120),(W,90),(W,560),(0,600)], fill=ICE+(255,))
    return im

def s16():                                   # the ceiling was not flat
    im = _ceiling(False, 16)
    im = beam(im, 1150, 1180, 900, BONE, .55)
    return finish(particles(im, 240, 16), 16)

def s17():                                   # terraces, cracks, sloped walls
    im = _ceiling(True, 17)
    im = beam(im, 900, 1240, 1000, BONE, .6)
    return finish(particles(im, 300, 17), 17)

def s18():                                   # split screen: flat vs crevassed
    im = base(BLACK)
    L = _ceiling(False, 18).crop((0,0,W//2,H)); im.paste(L, (0,0))
    R = _ceiling(True, 19).crop((W//2,0,W,H)); im.paste(R, (W//2,0))
    d = ImageDraw.Draw(im, "RGBA")
    d.line([(W//2,0),(W//2,H)], fill=BONE+(200,), width=4)
    for i in range(3):                                                      # slow arrows left
        y = 900+i*130; d.line([(500,y),(500,y+70)], fill=ICE+(190,), width=6)
    for i in range(6):                                                      # fast arrows right
        y = 820+i*100; d.line([(1500+i*90,y),(1500+i*90,y+150)], fill=AMBER+(220,), width=7)
    return finish(im, 18)

def s19():                                   # flat ice, melting slower
    im = _ceiling(False, 20)
    d = ImageDraw.Draw(im, "RGBA")
    for i in range(5):
        x = 500+i*380; d.line([(x,760),(x,860)], fill=ICE+(200,), width=7)
        d.polygon([(x-16,860),(x+16,860),(x,900)], fill=ICE+(220,))
    return finish(particles(im, 160, 19), 19)

def s20():                                   # cracks, melting fast
    im = _ceiling(True, 21)
    d = ImageDraw.Draw(im, "RGBA")
    for i in range(9):
        x = 260+i*260; d.line([(x,700),(x,980)], fill=AMBER+(225,), width=9)
        d.polygon([(x-22,980),(x+22,980),(x,1040)], fill=AMBER+(240,))
    return finish(particles(im, 220, 20), 20)

def s21():                                   # even melt vs fracture
    im = base(BLACK); vgrad(im, NAVY, BLACK)
    d = ImageDraw.Draw(im, "RGBA")
    d.rounded_rectangle([300, 520, 1080, 1180], 90, fill=ICE+(255,))        # smooth block
    b = [(1500,520),(2260,540),(2240,1180),(1480,1160)]                     # fractured block
    d.polygon(b, fill=ICE+(255,))
    for x0,y0,x1,y1 in ((1640,520,1560,1170),(1880,540,1960,1175),(2110,535,2040,1178)):
        d.line([(x0,y0),(x1,y1)], fill=BLACK+(230,), width=12)
    return finish(im, 21)

# ---------------- ACT 4 ----------------
def s22():                                   # text beat, darkened ceiling
    im = _ceiling(True, 22)
    im = Image.blend(im, Image.new("RGB", im.size, BLACK), .55)
    return finish(im, 22, .80)

def s23():                                   # even melt: predictable curve
    im = base(BLACK); vgrad(im, NAVY, BLACK)
    d = ImageDraw.Draw(im, "RGBA")
    pts = [(300+i*22, 620+ (i*i)*0.055) for i in range(100)]
    d.line(pts, fill=BONE+(230,), width=8)
    d.line([(300,1150),(W-300,1150)], fill=ICE_D+(160,), width=3)
    d.line([(300,420),(300,1150)], fill=ICE_D+(160,), width=3)
    return finish(im, 23)

def s24():                                   # fracture: goes all at once
    im = base(BLACK); vgrad(im, NAVY, WATER, (0,700,W,H))
    d = ImageDraw.Draw(im, "RGBA")
    d.polygon([(0,300),(1500,260),(1560,940),(0,980)], fill=ICE+(255,))     # ice face
    d.polygon([(1560,300),(1900,340),(2100,1000),(1600,940)], fill=lerp(ICE,BONE,.3)+(255,))
    rnd = __import__("random").Random(24)
    for _ in range(26):                                                     # debris
        x, y = rnd.randint(1500, 2400), rnd.randint(700, 1200)
        s = rnd.randint(12, 60)
        d.polygon([(x,y),(x+s,y+s//2),(x+s//2,y+s)], fill=BONE+(210,))
    return finish(haze(im, .2, 900), 24)

def s25():                                   # grounding line retreat, step 1
    im = _xsec(700, 1200, 400)
    d = ImageDraw.Draw(im, "RGBA")
    d.line([(1500,300),(1500,1120)], fill=AMBER+(230,), width=8)
    d.ellipse([1460,1080,1540,1160], fill=AMBER+(255,))
    return finish(im, 25)

def s26():                                   # same frame, one step further back
    im = _xsec(700, 1200, 400)
    d = ImageDraw.Draw(im, "RGBA")
    d.line([(950,300),(950,1000)], fill=AMBER+(230,), width=8)
    d.ellipse([910,960,990,1040], fill=AMBER+(255,))
    d.line([(1500,300),(1500,1120)], fill=AMBER+(90,), width=4)             # ghost of before
    return finish(im, 26)

def s27():                                   # the feedback loop
    im = base(BLACK); vgrad(im, NAVY, BLACK)
    d = ImageDraw.Draw(im, "RGBA")
    cx, cy, r = W//2, H//2, 380
    d.arc([cx-r, cy-r, cx+r, cy+r], 20, 320, fill=AMBER+(235,), width=14)
    d.polygon([(cx+r-40,cy-120),(cx+r+50,cy-70),(cx+r-30,cy-10)], fill=AMBER+(255,))
    for a in (60, 180, 300):
        x, y = cx+math.cos(math.radians(a))*r, cy+math.sin(math.radians(a))*r
        d.ellipse([x-26, y-26, x+26, y+26], fill=BONE+(240,))
    return finish(im, 27)

# ---------------- ACT 5 ----------------
def s28():                                   # what we know / what we don't
    im = base(BLACK); vgrad(im, NAVY, BLACK)
    d = ImageDraw.Draw(im, "RGBA")
    d.line([(W//2, 380),(W//2, H-380)], fill=ICE_D+(150,), width=3)
    for x in (520, 1560):
        for i in range(3):
            d.line([(x, 560+i*150),(x+520, 560+i*150)], fill=BONE+(120 if x>1000 else 200,), width=7)
    return finish(im, 28, .78)

def s29():                                   # uncertainty cone
    im = base(BLACK); vgrad(im, NAVY, BLACK)
    d = ImageDraw.Draw(im, "RGBA")
    ox, oy = 420, 760
    d.line([(ox,300),(ox,1200)], fill=ICE_D+(160,), width=3)
    d.line([(ox,1200),(W-260,1200)], fill=ICE_D+(160,), width=3)
    for k, a in enumerate((-0.16, -0.06, 0.03, 0.13, 0.24)):
        pts = [(ox+i*20, oy + a*i*i*0.42) for i in range(100)]
        d.line(pts, fill=BONE+(90 + k*30,), width=6)
    return finish(im, 29)

def s30():                                   # Thwaites is a cork
    im = base(BLACK)
    d = ImageDraw.Draw(im, "RGBA")
    cx, cy, r = W//2, H//2+80, 600
    radial(im, cx, cy, r+240, lerp(NAVY,TEAL,.3), BLACK)
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=lerp(BONE,ICE,.35)+(255,))
    d.pieslice([cx-r, cy-r, cx+r, cy+r], 150, 205, fill=AMBER+(230,))       # Thwaites
    d.arc([cx-r-8, cy-r-8, cx+r+8, cy+r+8], 190, 350, fill=ICE+(190,), width=9)
    return finish(im, 30, .62)

def s31():                                   # looking up the shaft at daylight
    im = base(BLACK)
    radial(im, W//2, 380, 520, ICE, BLACK)
    im = _shaft(im, W//2, 0, 240, 900, H, ICE_D)
    d = ImageDraw.Draw(im, "RGBA")
    d.ellipse([W//2-150, 250, W//2+150, 430], fill=BONE+(255,))
    return finish(particles(im, 180, 31), 31)

SCENES = [s01,s02,s03,s04,s05,s06,s07,s08,s09,s10,s11,s12,s13,s14,s15,
          s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30]
