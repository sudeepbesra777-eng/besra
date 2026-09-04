import subprocess, os, sys
FF = "/opt/pw-browsers/ffmpeg-1011/ffmpeg-linux"
OUT = "/home/user/besra/render/clips"; os.makedirs(OUT, exist_ok=True)
D, FPS = 10, 30
N = D*FPS

# Camera move per scene. No two consecutive shots move the same way - that single
# rule is what stops a stills-based film from reading as a slideshow.
def push(a, b):   return f"z='{a}+{b-a}*on/{N}'", "x='iw/2-(iw/zoom/2)'", "y='ih/2-(ih/zoom/2)'"
def pan(z, x0, x1, y0=0.5, y1=0.5):
    return (f"z='{z}'",
            f"x='(iw-iw/zoom)*({x0}+{x1-x0}*on/{N})'",
            f"y='(ih-ih/zoom)*({y0}+{y1-y0}*on/{N})'")

MOVES = {
 1: push(1.00,1.09),               2: push(1.02,1.14),
 3: pan(1.18,.5,.5,.15,.85),       4: push(1.00,1.06),
 5: pan(1.14,.05,.95),             6: pan(1.16,.5,.5,.05,.95),
 7: push(1.12,1.00),               8: pan(1.14,.95,.05),
 9: push(1.00,1.08),              10: pan(1.10,.35,.65,.5,.45),
11: pan(1.12,.10,.80),            12: push(1.00,1.11),
13: pan(1.12,.85,.15),            14: push(1.04,1.09),
15: push(1.16,1.00),              16: pan(1.18,.5,.5,.90,.10),
17: pan(1.16,.15,.80,.85,.25),    18: push(1.02,1.05),
19: push(1.00,1.10),              20: push(1.00,1.13),
21: pan(1.12,.05,.90),            22: pan(1.10,.60,.40,.4,.55),
23: push(1.02,1.06),              24: push(1.00,1.12),
25: push(1.05,1.05),              26: push(1.05,1.05),
27: push(1.00,1.07),              28: push(1.03,1.03),
29: push(1.00,1.09),              30: push(1.10,1.00),
}

files = []
for i in range(1, 31):
    z, x, y = MOVES[i]
    src = f"/home/user/besra/render/stills/s{i:02d}.png"
    dst = f"{OUT}/c{i:02d}.mp4"
    vf = (f"zoompan={z}:{x}:{y}:d={N}:s=2560x1440:fps={FPS},"
          f"scale=1920:1080:flags=lanczos,format=yuv420p")
    subprocess.run([FF, "-y", "-loglevel", "error", "-loop", "1", "-framerate", str(FPS),
                    "-i", src, "-vf", vf, "-t", str(D),
                    "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", dst], check=True)
    files.append(dst); print(f"{i:02d}", end=" ", flush=True)

with open(f"{OUT}/list.txt", "w") as f:
    for p in files: f.write(f"file '{p}'\n")
subprocess.run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                "-i", f"{OUT}/list.txt", "-c", "copy",
                "/home/user/besra/render/under-the-ice-visuals.mp4"], check=True)
print("\nconcat done")
