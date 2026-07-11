#!/usr/bin/env python3
"""Record the Telepatia Learning prototype as a 1280x720 mp4.

Usage:
    pip3 install playwright imageio-ffmpeg
    python3 -m playwright install chromium
    python3 tools/record_demo.py
Output: demo.mp4 in the repo root.
"""
import glob
import os
import subprocess
import tempfile

import imageio_ffmpeg
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "file://" + os.path.join(ROOT, "prototype", "index.html")
OUT = os.path.join(ROOT, "demo.mp4")
# autoplay scene durations in prototype/index.html (DUR array); keep in sync
TOTAL_MS = 6000 + 16000 + 9000 + 9000 + 14000 + 12000 + 9000 + 11000

with tempfile.TemporaryDirectory() as vid_dir:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(
            viewport={"width": 1280, "height": 720},
            record_video_dir=vid_dir,
            record_video_size={"width": 1280, "height": 720},
        )
        page = ctx.new_page()
        page.goto(SRC, wait_until="networkidle")
        # full-bleed for the recording: drop the desktop frame and operator controls
        page.add_style_tag(content="""
            body { padding:0 !important; background:var(--canvas) !important; }
            .stage { width:1280px !important; height:720px !important; border-radius:0 !important; box-shadow:none !important; }
            .ctrl { display:none !important; }
        """)
        page.wait_for_timeout(2500)  # let IBM Plex settle
        page.evaluate("go(0); toggleAuto();")
        page.wait_for_timeout(TOTAL_MS - 200)  # stop just before the loop restarts
        ctx.close()
        browser.close()

    webm = sorted(glob.glob(os.path.join(vid_dir, "*.webm")), key=os.path.getmtime)[-1]
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([
        ff, "-i", webm,
        "-c:v", "libx264", "-preset", "medium", "-crf", "19",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        "-r", "30", OUT, "-y", "-loglevel", "error",
    ], check=True)

print("wrote", OUT)
