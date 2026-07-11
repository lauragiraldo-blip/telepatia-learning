#!/usr/bin/env python3
"""Build single self-contained HTML pages: landing(s) + embedded prototype.

The prototype is inlined as base64 and mounted in an iframe via srcdoc when
the user clicks the demo launch button, so each output file can be pasted or
uploaded to any host (e.g. patonews.internal.telepatia.ai) with no other files.

Usage: python3 tools/build_onefile.py
Outputs in dist/: telepatia-learning-onefile.html (phase 1)
                  telepatia-learning-phase2-onefile.html (phase 2)
"""
import base64
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROTO = os.path.join(ROOT, "prototype", "index.html")
OUT_DIR = os.path.join(ROOT, "dist")

PAGES = [
    ("index.html", "telepatia-learning-onefile.html"),
    ("phase2.html", "telepatia-learning-phase2-onefile.html"),
]

proto_b64 = base64.b64encode(open(PROTO, "rb").read()).decode("ascii")

OLD_JS = """function launchDemo(){
  const body = document.getElementById('demobody');
  body.innerHTML = '<div class="demo-live" id="demolive">' +
    '<iframe id="demoframe" src="prototype/index.html" title="Telepatia Learning demo" ' +
    'allow="microphone; clipboard-write" allowfullscreen></iframe></div>';
  scaleDemo();
}"""
NEW_JS = """const PROTO_B64 = '%%PROTO_B64%%';
function protoHtml(){
  return new TextDecoder().decode(Uint8Array.from(atob(PROTO_B64), c => c.charCodeAt(0)));
}
function launchDemo(){
  const body = document.getElementById('demobody');
  body.innerHTML = '<div class="demo-live" id="demolive">' +
    '<iframe id="demoframe" title="Telepatia Learning demo" ' +
    'allow="microphone; clipboard-write" allowfullscreen></iframe></div>';
  document.getElementById('demoframe').srcdoc = protoHtml();
  scaleDemo();
}
function openDemoTab(){
  const url = URL.createObjectURL(new Blob([protoHtml()], {type: 'text/html'}));
  window.open(url, '_blank');
}"""
OLD_LINK = ('<a href="prototype/index.html" target="_blank" rel="noopener" '
            'style="color:inherit;text-decoration:underline;">abrirlo a pantalla completa</a>')
NEW_LINK = ('<a href="#demo" onclick="openDemoTab();return false;" '
            'style="color:inherit;text-decoration:underline;">abrirlo a pantalla completa</a>')

os.makedirs(OUT_DIR, exist_ok=True)
for src_name, out_name in PAGES:
    src_path = os.path.join(ROOT, src_name)
    if not os.path.exists(src_path):
        print("skip (missing):", src_name)
        continue
    page = open(src_path, encoding="utf-8").read()
    assert page.count(OLD_JS) == 1, f"launchDemo script not found in {src_name}"
    page = page.replace(OLD_JS, NEW_JS)
    assert page.count(OLD_LINK) == 1, f"fullscreen link not found in {src_name}"
    page = page.replace(OLD_LINK, NEW_LINK)
    page = page.replace("%%PROTO_B64%%", proto_b64)
    out = os.path.join(OUT_DIR, out_name)
    open(out, "w", encoding="utf-8").write(page)
    print("wrote", out, f"({os.path.getsize(out) // 1024} KB)")
