#!/usr/bin/env python3
"""Build a single self-contained HTML: landing page + embedded prototype.

The prototype is inlined as base64 and mounted in an iframe via srcdoc when
the user clicks the demo launch button, so the output file can be pasted or
uploaded to any host (e.g. patonews.internal.telepatia.ai) with no other files.

Usage: python3 tools/build_onefile.py
Output: dist/telepatia-learning-onefile.html
"""
import base64
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANDING = os.path.join(ROOT, "index.html")
PROTO = os.path.join(ROOT, "prototype", "index.html")
OUT_DIR = os.path.join(ROOT, "dist")
OUT = os.path.join(OUT_DIR, "telepatia-learning-onefile.html")

landing = open(LANDING, encoding="utf-8").read()
proto_b64 = base64.b64encode(open(PROTO, "rb").read()).decode("ascii")

# Replace the file-based launch/scale script with a self-contained srcdoc version
old_js = """function launchDemo(){
  const body = document.getElementById('demobody');
  body.innerHTML = '<div class="demo-live" id="demolive">' +
    '<iframe id="demoframe" src="prototype/index.html" title="Telepatia Learning demo" ' +
    'allow="microphone; clipboard-write" allowfullscreen></iframe></div>';
  scaleDemo();
}"""
new_js = """const PROTO_B64 = '%%PROTO_B64%%';
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
assert landing.count(old_js) == 1, "launchDemo script not found; landing changed?"
landing = landing.replace(old_js, new_js)

# Fullscreen link: file path -> blob-URL opener
old_link = ('<a href="prototype/index.html" target="_blank" rel="noopener" '
            'style="color:inherit;text-decoration:underline;">abrirlo a pantalla completa</a>')
new_link = ('<a href="#demo" onclick="openDemoTab();return false;" '
            'style="color:inherit;text-decoration:underline;">abrirlo a pantalla completa</a>')
assert landing.count(old_link) == 1, "fullscreen link not found"
landing = landing.replace(old_link, new_link)

landing = landing.replace("%%PROTO_B64%%", proto_b64)

os.makedirs(OUT_DIR, exist_ok=True)
open(OUT, "w", encoding="utf-8").write(landing)
print("wrote", OUT, f"({os.path.getsize(OUT) // 1024} KB)")
