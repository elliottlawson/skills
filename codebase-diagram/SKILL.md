---
name: codebase-diagram
description: Turn a codebase into an interactive visual system diagram — a single self-contained HTML page with isometric structures, a legend, an inspect panel, and animated dots carrying real data payloads along the flows. Use when the user wants a visual map of a repo to discuss it more easily, or asks to diagram/map/visualize a codebase.
---

# codebase-diagram

Output is one self-contained HTML file (zero dependencies, works from `file://` or any static server). The agent explores the repo, authors a **model JSON**, and injects it into `assets/template.html` (this skill's directory) via `scripts/render.py`. Never hand-edit the generated HTML — fix the model or the template and re-render.

## Step 1 — Explore the repo (delegate)

Read-only on the target repo. For anything non-trivial, delegate to a thorough explore sub-agent. The report must come back with:

1. **Subsystems** — 12–22 nodes: key (1–3 letters), name, responsibility (plain sentences), how built (classes/dirs/tech as evidence), rough size signal (LoC, file/route/model counts).
2. **Groups** — 3–7 logical groupings for the nodes (e.g. "THE CONVERSATION LOOP", "MEMORY", "CHANNELS").
3. **Flows** — 12–20 edges: from → to, label, a realistic one-line **example payload** (JSON fragment, log line — these ride the animated dots and must be real, not invented), and live vs. wired-but-disabled status.
4. **Header stats** — 5–8 real counted numbers (models, routes, tests, migrations…).
5. **The story** — one paragraph: what the repo IS, the central loop, what's mid-flight.
6. **Dead ends** — anything built but disabled/commented-out/mid-migration (dashed-line material).

Ground everything in the actual code — read the repo's AGENTS.md/docs first, then verify against source. No guessing.

## Step 2 — Author the model JSON

Schema (all top-level keys required):

```json
{
  "title": "repo-name · branch",
  "stats": [{"label": "MODELS", "value": "41"}],
  "groups": [{"key": "loop", "name": "THE CONVERSATION LOOP"}],
  "nodes": [{
    "id": "CH", "key": "CH", "name": "CHAT ENGINE", "group": "loop",
    "gx": 8, "gy": 6, "w": 3, "d": 3, "h": 40,
    "count": "~3,000 LoC",
    "blurb": "one line, shown on hover",
    "what": "prose paragraphs, \\n separated — what it does and why",
    "how": "prose — key classes, dirs, tech",
    "condition": "optional: what's currently wrong / in-progress",
    "dashed": false
  }],
  "edges": [{
    "from": "WB", "to": "CH", "label": "user message",
    "snippets": ["POST /chat/send {message: \"…\", session_id: \"…\"}"],
    "dashed": false, "via": [[4, 6]], "dots": 2, "note": "optional prose"
  }],
  "overview": {"title": "…", "subtitle": "…", "what": "…", "how": "…"}
}
```

Layout rules:

- `gx, gy` place the box on the iso grid; `w, d` its footprint in tiles; `h` its height in px (importance ≈ height, 14–46).
- **Cluster by group**; put the central loop near the middle, inputs left, outputs right, infra below.
- Footprints must not overlap — `scripts/render.py` rejects overlaps; nudge coordinates until clean.
- `via` adds right-angle waypoints in grid coords; use them to route around structures. Keep crossings minimal.
- `dashed: true` on nodes/edges that exist but are not switched on (commented-out routes, stubs, mid-migration). Dashed edges get no dots.
- Snippets: 1–4 per live edge, each one line, realistic. They are the dots' cargo — the whole point is inspecting them.
- Names/labels UPPERCASE in legend; prose in plain English, short sentences.

## Step 3 — Render and verify

```bash
python3 scripts/render.py model.json out.html
```

Fix every validation error before proceeding. Then open the page and actually look at it (headless screenshot if available — e.g. Playwright): check for box overlaps the validator can't see (visual crowding), unreadable label collisions, and dots following their lines.

## Step 4 — Hand over

Serve the file and share via the **share-server** skill (tailnet URL — never a bare `localhost` link or local path). Also keep `model.json` next to the output — it is the source for future edits.

## Notes

- "Go inside" (drill-down into a structure's internal steps) is a deliberate v2 gap — the schema has no children yet.
- The template is shared across all diagrams. Improve it once, re-render every model.
