#!/usr/bin/env python3
"""
drawio_to_mermaid.py

Reverse of mermaid_to_drawio.py.

Convert inline draw.io SVG diagrams embedded in Markdown back into clean
```mermaid fenced flowchart blocks. The Mermaid is reconstructed from the
mxGraphModel embedded in each SVG's `content="..."` attribute (an mxfile), so
the result round-trips: re-running mermaid_to_drawio.py on the output
regenerates an equivalent draw.io SVG.

Each inline diagram in the source has the shape:

    <!-- diagram: {name}.drawio.svg -->

    <svg ... content="&lt;mxfile&gt;...&lt;/mxfile&gt;"> ... </svg>

This script replaces that comment + SVG with:

    ```mermaid
    flowchart TD
        A[Label] --> B{Decision}
        ...
    ```

Shape inference from the mxfile vertex style / role:
  - style contains `rhombus`            -> decision  `{label}`
  - vertex with no incoming edges       -> start     `([label])`
  - vertex with no outgoing edges       -> end       `([label])`
  - otherwise                            -> process   `[label]`

(The forward converter assigns start/end/decision colors by graph position and
by the rhombus shape, so these brackets reproduce the same colors.)

Usage:
  python3 drawio_to_mermaid.py <path> [<path> ...]   # convert in place
  python3 drawio_to_mermaid.py --dry-run <path> ...  # report only
  python3 drawio_to_mermaid.py --stdout <file.md>    # print result, no write

A <path> may be a Markdown file or a directory (searched recursively for *.md).
"""

import argparse
import html
import os
import re
import sys

# Block = optional provenance comment + blank line(s) + an inline <svg>...</svg>
DIAGRAM_BLOCK_RE = re.compile(
    r'(?:[ \t]*<!--\s*diagram:[^\n]*-->[ \t]*\n\s*)?'
    r'<svg\b[^>]*>.*?</svg>',
    re.DOTALL | re.IGNORECASE,
)

CONTENT_ATTR_RE = re.compile(r'\bcontent="([\s\S]*?)"', re.IGNORECASE)
MXFILE_RE = re.compile(r'<mxfile[\s>]', re.IGNORECASE)

# mxCell parsing
CELL_RE = re.compile(r'<mxCell\b([^>]*?)(?:/>|>(.*?)</mxCell>)', re.DOTALL | re.IGNORECASE)
ATTR_RE = re.compile(r'(\w+)="([^"]*)"')


def decode_entities(s):
    """Decode XML entities (mxfile content is double-escaped inside the SVG)."""
    if s is None:
        return ""
    # &amp; must be decoded LAST so we don't double-decode
    for ent, ch in (("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'),
                    ("&#39;", "'"), ("&#10;", "\n"), ("&#9;", "\t")):
        s = s.replace(ent, ch)
    s = s.replace("&amp;", "&")
    return s


def extract_mxfile(svg):
    m = CONTENT_ATTR_RE.search(svg)
    if not m:
        return None
    xml = decode_entities(m.group(1))
    if not MXFILE_RE.search(xml):
        return None
    return xml


def _attrs(attr_str):
    return {k: v for k, v in ATTR_RE.findall(attr_str)}


def _sanitize_id(raw, used):
    """Make a safe, stable Mermaid node id from an mxCell id."""
    nid = re.sub(r'[^A-Za-z0-9_]', '_', raw or '')
    if not nid or not re.match(r'[A-Za-z_]', nid[0]):
        nid = "n_" + nid
    base = nid
    i = 2
    while nid in used and used[nid] != raw:
        nid = f"{base}_{i}"
        i += 1
    return nid


_SPECIAL = set('[](){}|<>"#:;=&')


def _fmt_label(label):
    """Return a Mermaid-safe label body, quoted when it contains specials."""
    label = label.replace("\n", "<br/>")
    if any(c in _SPECIAL for c in label) or not label.strip():
        esc = label.replace('"', '&quot;')
        return f'"{esc}"', True
    return label, False


def _wrap(nid, label, kind):
    body, _ = _fmt_label(label)
    if kind == "decision":
        return f"{nid}{{{body}}}"
    if kind in ("start", "end"):
        return f"{nid}([{body}])"
    return f"{nid}[{body}]"


def parse_mxfile(xml):
    """Return (vertices, edges).

    vertices: dict id -> {"label": str, "rhombus": bool}
    edges:    list of (source_id, target_id, label)
    """
    vertices = {}
    edges = []
    for m in CELL_RE.finditer(xml):
        attrs = _attrs(m.group(1))
        cid = attrs.get("id")
        if cid in ("0", "1") or cid is None:
            continue
        style = attrs.get("style", "")
        value = decode_entities(attrs.get("value", ""))
        if attrs.get("edge") == "1":
            src = attrs.get("source")
            tgt = attrs.get("target")
            if src and tgt:
                edges.append((src, tgt, value))
        elif attrs.get("vertex") == "1":
            vertices[cid] = {
                "label": value,
                "rhombus": "rhombus" in style.lower(),
            }
    return vertices, edges


def build_mermaid(xml):
    vertices, edges = parse_mxfile(xml)
    if not vertices:
        return None

    indeg = {vid: 0 for vid in vertices}
    outdeg = {vid: 0 for vid in vertices}
    for src, tgt, _ in edges:
        if src in outdeg:
            outdeg[src] += 1
        if tgt in indeg:
            indeg[tgt] += 1

    def kind_of(vid):
        if vertices[vid]["rhombus"]:
            return "decision"
        if indeg.get(vid, 0) == 0 and outdeg.get(vid, 0) > 0:
            return "start"
        if outdeg.get(vid, 0) == 0 and indeg.get(vid, 0) > 0:
            return "end"
        return "process"

    # stable, readable ids
    idmap = {}
    used = {}
    for vid in vertices:
        nid = _sanitize_id(vid, used)
        used[nid] = vid
        idmap[vid] = nid

    lines = ["flowchart TD"]
    defined = set()

    def ref(vid):
        nid = idmap[vid]
        if nid not in defined:
            defined.add(nid)
            return _wrap(nid, vertices[vid]["label"], kind_of(vid))
        return nid

    if edges:
        for src, tgt, lbl in edges:
            if src not in vertices or tgt not in vertices:
                continue
            left = ref(src)
            right = ref(tgt)
            if lbl.strip():
                body, _ = _fmt_label(lbl)
                lines.append(f"    {left} -->|{body}| {right}")
            else:
                lines.append(f"    {left} --> {right}")

    # any vertices not touched by edges
    for vid in vertices:
        if idmap[vid] not in defined:
            lines.append(f"    {ref(vid)}")

    return "```mermaid\n" + "\n".join(lines) + "\n```"


def process_markdown(path, dry_run=False, return_content=False):
    with open(path, "r", encoding="utf-8") as fh:
        src = fh.read()

    results = {"converted": 0, "skipped": 0}

    def repl(m):
        block = m.group(0)
        svg = block[block.lower().index("<svg"):]
        xml = extract_mxfile(svg)
        if xml is None:
            results["skipped"] += 1
            return block
        mermaid = build_mermaid(xml)
        if mermaid is None:
            results["skipped"] += 1
            return block
        results["converted"] += 1
        return mermaid

    new_src = DIAGRAM_BLOCK_RE.sub(repl, src)

    if return_content:
        results["content"] = new_src
        return results
    if not dry_run and results["converted"] and new_src != src:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_src)
    return results


def iter_md_files(paths):
    for p in paths:
        if os.path.isdir(p):
            for root, _, files in os.walk(p):
                for fn in files:
                    if fn.endswith(".md"):
                        yield os.path.join(root, fn)
        elif p.endswith(".md"):
            yield p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--stdout", action="store_true",
                    help="convert a single .md file and print to stdout")
    args = ap.parse_args()

    if args.stdout:
        if len(args.paths) != 1 or not args.paths[0].endswith(".md"):
            sys.stderr.write("--stdout requires exactly one .md file path\n")
            sys.exit(2)
        res = process_markdown(args.paths[0], return_content=True)
        sys.stdout.write(res.get("content", ""))
        return

    total_files = 0
    total_conv = 0
    total_skip = 0
    for path in iter_md_files(args.paths):
        res = process_markdown(path, dry_run=args.dry_run)
        if res["converted"] or res["skipped"]:
            total_files += 1
            total_conv += res["converted"]
            total_skip += res["skipped"]
            tag = "DRY" if args.dry_run else "OK "
            print(f"[{tag}] {path}  converted={res['converted']} "
                  f"skipped={res['skipped']}")
    print(f"\nFiles touched: {total_files}  diagrams converted: {total_conv}  "
          f"skipped(no mxfile): {total_skip}")


if __name__ == "__main__":
    main()
