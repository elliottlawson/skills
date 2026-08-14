#!/usr/bin/env python3
"""Render a codebase-diagram model (JSON) into a self-contained HTML page.

Usage: render.py <model.json> <out.html>

Validates the model first: unique node ids, edges reference real nodes,
group keys exist, node footprints don't overlap on the iso grid, and
required prose fields are present. Exits 1 with a list of errors if invalid.
"""
import json
import pathlib
import sys

REQUIRED_NODE = ["id", "key", "name", "group", "gx", "gy", "w", "d", "h", "blurb", "what", "how"]


def validate(m):
    errors = []
    for k in ("title", "stats", "groups", "nodes", "edges", "overview"):
        if k not in m:
            errors.append(f"missing top-level key: {k}")
    if errors:
        return errors

    ids = [n.get("id") for n in m["nodes"]]
    if len(ids) != len(set(ids)):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        errors.append(f"duplicate node ids: {dupes}")
    group_keys = {g.get("key") for g in m["groups"]}

    for n in m["nodes"]:
        for f in REQUIRED_NODE:
            if f not in n:
                errors.append(f"node {n.get('id', '?')}: missing field {f}")
        if n.get("group") not in group_keys:
            errors.append(f"node {n.get('id')}: unknown group '{n.get('group')}'")

    # footprint overlap: rectangles [gx, gx+w) x [gy, gy+d)
    placed = sorted(m["nodes"], key=lambda n: n.get("gx", 0))
    for i, a in enumerate(placed):
        for b in placed[i + 1:]:
            if all(k in a for k in ("gx", "gy", "w", "d")) and all(k in b for k in ("gx", "gy", "w", "d")):
                if (a["gx"] < b["gx"] + b["w"] and b["gx"] < a["gx"] + a["w"]
                        and a["gy"] < b["gy"] + b["d"] and b["gy"] < a["gy"] + a["d"]):
                    errors.append(f"nodes overlap on grid: {a['id']} and {b['id']}")

    for e in m["edges"]:
        if e.get("from") not in ids or e.get("to") not in ids:
            errors.append(f"edge references unknown node: {e.get('from')} -> {e.get('to')}")
        if e.get("from") == e.get("to"):
            errors.append(f"edge loops to itself: {e.get('from')}")
        if not e.get("dashed") and not e.get("snippets"):
            errors.append(f"live edge {e.get('from')} -> {e.get('to')} has no snippets (dots need data to carry)")
        for v in e.get("via", []):
            if not (isinstance(v, list) and len(v) == 2 and all(isinstance(c, (int, float)) for c in v)):
                errors.append(f"edge {e.get('from')} -> {e.get('to')}: bad via point {v!r} (want [gx, gy])")
    return errors


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    model_path, out_path = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    template = (pathlib.Path(__file__).parent / "template.html").read_text()
    model = json.loads(model_path.read_text())

    errors = validate(model)
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    marker = "/*__DIAGRAM_JSON__*/null"
    if marker not in template:
        sys.exit("template.html is missing the injection marker")
    html = template.replace(marker, json.dumps(model, ensure_ascii=False))
    out_path.write_text(html)
    print(f"wrote {out_path} ({len(html) // 1024} KB, "
          f"{len(model['nodes'])} nodes, {len(model['edges'])} edges)")


if __name__ == "__main__":
    main()
