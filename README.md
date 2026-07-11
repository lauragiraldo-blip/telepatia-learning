# Telepatía Learning

Hackathon project: the Telepatía Scribe + CDSS stack configured as a training
environment for medical schools. Students work simulated cases, write real
clinical records, and receive formative, guideline-cited feedback from the same
audit engine that runs in Telepatía's client hospitals.

## Contents

| Path | What it is |
|---|---|
| `prototype/index.html` | Interactive UI prototype (self-contained, no build step). Open it in a browser. |
| `tools/record_demo.py` | Renders the prototype's autoplay run to `demo.mp4` (1280x720, H.264). |
| `docs/proposal.md` | Full project proposal: market, ICP, pricing, CDSS configuration. |
| `docs/demo-plan.md` | Plan for the live demo on the production Audit module (backoffice configuration). |

## Prototype

Open `prototype/index.html` in any browser. Controls:

- Right/left arrows (or the floating pill): next / previous scene
- `A`: toggle autoplay (~73 s full run)
- Deep links: `index.html#4` jumps straight to a scene (0-6)

Scenes: case brief with two entry paths (live simulated consultation with
Scribe, or upload of a handwritten record as PDF/photo) → student note with
three planted errors → formative feedback (score gauge, per-section bars,
guideline-cited findings, red-severity gating) → corrected note → faculty
panel with cohort pain points and suggested teaching sessions.

## Live dictation and AI note generation (new cases)

In a new case's consultation, "Iniciar dictado" transcribes the interview live
using Chrome's speech recognition (Spanish; requires mic permission and
internet). On "Finalizar y generar nota":

- With an Anthropic API key configured ("Configurar clave de IA" in the
  sidebar), the transcript is sent to the Claude API and a real SOAP note is
  generated and loaded into the editable note.
- Without a key, the transcript lands in the S component to structure manually.

The key is stored only in the browser's localStorage: it is never committed to
this repository. Use a personal/workspace-scoped key and revoke it after the
demo if the laptop is shared.

## Rendering the demo video

```bash
pip3 install playwright imageio-ffmpeg
python3 -m playwright install chromium
python3 tools/record_demo.py   # writes demo.mp4
```

## Monorepo integration (pending)

This lives standalone until `lauragiraldo-blip` gets access to
`Telepatia-AI/monobloco`; then it moves into the monorepo following its app
conventions. The prototype is intentionally dependency-free to make that port
trivial.
