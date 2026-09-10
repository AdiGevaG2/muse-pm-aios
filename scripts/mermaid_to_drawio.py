#!/usr/bin/env python3
"""
mermaid_to_drawio.py

Convert Mermaid `flowchart`/`graph` code blocks inside Markdown files into
editable, transparent draw.io SVGs embedded **inline** in the same Markdown
file (replacing each fenced ```mermaid block with the SVG markup). No separate
`.drawio.svg` file is written.

Each embedded SVG is:
  - A valid SVG (renders in Markdown preview) with visual shapes.
  - A draw.io SVG (carries an mxfile in `content`, so it can be extracted back
    into a `.drawio.svg` file and edited in the Draw.io VS Code extension).
  - Transparent (no background rect; mxGraphModel background="none").

A short `<!-- diagram: {name}.drawio.svg -->` comment is written just above each
embedded SVG to preserve a stable name (used for provenance and for Confluence
attachment publishing).

Only `flowchart` / `graph` diagrams are handled. Any other Mermaid diagram type
is left untouched and reported.

Usage:
  python3 mermaid_to_drawio.py <path> [<path> ...]      # convert in place
  python3 mermaid_to_drawio.py --dry-run <path> ...     # report only

A <path> may be a Markdown file or a directory (searched recursively for *.md).
"""

import argparse
import html
import math
import os
import re
import sys

# ---- palette (draw.io light/pastel, transparent-friendly) ---------------
NODE_FILL = "#E1D5E7"      # lavender
NODE_STROKE = "#9673A6"
DECISION_FILL = "#FFF2CC"  # yellow
DECISION_STROKE = "#D6B656"
START_FILL = "#D5E8D4"     # green
START_STROKE = "#82B366"
END_FILL = "#DAE8FC"       # blue
END_STROKE = "#6C8EBF"
EDGE_COLOR = "#333333"
TEXT_COLOR = "#1a1a1a"

# ---- layout constants ---------------------------------------------------
NODE_W = 210
NODE_H = 56
DIAMOND_W = 220
DIAMOND_H = 100
HGAP = 50
VGAP = 44
MARGIN = 24
FONT_SIZE = 13
CHAR_W = 7.2  # approx px per char at FONT_SIZE

EDGE_OPS = [
    "==>", "===", "-.->", "-.-", "-->", "---", "--o", "--x", "o--o", "x--x",
]


class Node:
    __slots__ = ("nid", "label", "shape", "x", "y", "w", "h", "rank", "order",
                 "fill", "stroke", "_bary", "order_in_rank")

    def __init__(self, nid, label, shape):
        self.nid = nid
        self.label = label
        self.shape = shape
        self.x = 0.0
        self.y = 0.0
        self.w = NODE_W
        self.h = NODE_H
        self.rank = 0
        self.order = 0
        self.fill = NODE_FILL
        self.stroke = NODE_STROKE


def _shape_from_brackets(token):
    """Return (label, shape) from a bracketed node token body."""
    pairs = [
        ("([", "])", "stadium"),
        ("[[", "]]", "rect"),
        ("[(", ")]", "cylinder"),
        ("((", "))", "circle"),
        ("[", "]", "rect"),
        ("(", ")", "rounded"),
        ("{{", "}}", "hexagon"),
        ("{", "}", "diamond"),
        (">", "]", "rect"),
    ]
    for op, cl, shape in pairs:
        if token.startswith(op) and token.endswith(cl) and len(token) >= len(op) + len(cl):
            return token[len(op):len(token) - len(cl)].strip(), shape
    return None, None


def _clean_label(text):
    text = text.strip()
    if len(text) >= 2 and text[0] in "\"'" and text[-1] == text[0]:
        text = text[1:-1]
    text = text.replace("<br/>", "\n").replace("<br>", "\n").replace("<br />", "\n")
    return text.strip()


NODE_DEF_RE = re.compile(
    r'^([A-Za-z0-9_.-]+)\s*'
    r'(\(\[.*?\]\)|\[\[.*?\]\]|\[\(.*?\)\]|\(\(.*?\)\)|\{\{.*?\}\}|\[.*?\]|\(.*?\)|\{.*?\}|>.*?\])'
)


def parse_flowchart(lines):
    """Parse mermaid flowchart lines -> (direction, nodes dict, edges list)."""
    direction = "TD"
    nodes = {}
    edges = []
    order_counter = [0]

    def ensure_node(nid, label=None, shape=None):
        nid = nid.strip()
        if nid not in nodes:
            n = Node(nid, label if label is not None else nid, shape or "rect")
            n.order = order_counter[0]
            order_counter[0] += 1
            nodes[nid] = n
        else:
            if label is not None:
                nodes[nid].label = label
            if shape is not None and shape != "rect":
                nodes[nid].shape = shape
        return nodes[nid]

    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        low = line.lower()
        if low.startswith("flowchart") or low.startswith("graph"):
            m = re.search(r'\b(TD|TB|BT|LR|RL)\b', line)
            if m:
                direction = m.group(1)
            continue
        if low.startswith(("subgraph", "end", "classdef", "class ", "style ",
                            "linkstyle", "click ", "%%", "direction")):
            if low.startswith("direction"):
                m = re.search(r'\b(TD|TB|BT|LR|RL)\b', line)
                if m:
                    direction = m.group(1)
            continue

        # split a possibly-chained edge line into segments
        if any(op in line for op in EDGE_OPS):
            _parse_edge_line(line, ensure_node, edges)
        else:
            # standalone node definition
            m = NODE_DEF_RE.match(line)
            if m:
                label, shape = _shape_from_brackets(m.group(2))
                ensure_node(m.group(1), _clean_label(label), shape)
            else:
                tok = line.split()[0] if line.split() else None
                if tok and re.match(r'^[A-Za-z0-9_.-]+$', tok):
                    ensure_node(tok)
    return direction, nodes, edges


def _split_edges(line):
    """Yield (op, label, remainder_start_index) splits for a line."""
    result = []
    i = 0
    while i < len(line):
        matched = None
        for op in EDGE_OPS:
            if line.startswith(op, i):
                if matched is None or len(op) > len(matched):
                    matched = op
        if matched:
            result.append(("OP", matched, i))
            i += len(matched)
        else:
            i += 1
    return result


def _parse_edge_line(line, ensure_node, edges):
    # Normalize `-- label -->` style into `-->|label|`
    line = re.sub(r'--\s+([^->|]+?)\s+-->', lambda m: '-->|' + m.group(1).strip() + '|', line)
    line = re.sub(r'==\s+([^=|]+?)\s+==>', lambda m: '==>|' + m.group(1).strip() + '|', line)

    ops = _split_edges(line)
    if not ops:
        return
    # build segments: node, op(+label), node, op, node ...
    segments = []
    last = 0
    for _, op, idx in ops:
        segments.append(("NODE", line[last:idx]))
        # capture optional |label| right after op
        after = line[idx + len(op):]
        lbl = ""
        mlbl = re.match(r'\s*\|([^|]*)\|', after)
        consumed = len(op)
        if mlbl:
            lbl = mlbl.group(1).strip()
            consumed += mlbl.end()
        segments.append(("OP", lbl))
        last = idx + (consumed - len(op)) + len(op) if False else idx + len(op) + (mlbl.end() if mlbl else 0)
    segments.append(("NODE", line[last:]))

    # resolve node tokens to ids
    node_ids = []
    labels_between = []
    pending_label = None
    for kind, val in segments:
        if kind == "NODE":
            tok = val.strip()
            if not tok:
                node_ids.append(None)
                continue
            m = NODE_DEF_RE.match(tok)
            if m:
                label, shape = _shape_from_brackets(m.group(2))
                n = ensure_node(m.group(1), _clean_label(label), shape)
            else:
                first = re.match(r'^([A-Za-z0-9_.-]+)', tok)
                if not first:
                    node_ids.append(None)
                    continue
                n = ensure_node(first.group(1))
            node_ids.append(n.nid)
        else:
            labels_between.append(val)

    for k in range(len(node_ids) - 1):
        a, b = node_ids[k], node_ids[k + 1]
        if a and b:
            lbl = labels_between[k] if k < len(labels_between) else ""
            edges.append((a, b, lbl))


# ---- layout -------------------------------------------------------------
def assign_ranks(nodes, edges):
    succ = {nid: [] for nid in nodes}
    indeg = {nid: 0 for nid in nodes}
    pred = {nid: [] for nid in nodes}
    edge_set = set()
    for a, b, _ in edges:
        if a == b or (a, b) in edge_set:
            continue
        edge_set.add((a, b))
        succ[a].append(b)
        pred[b].append(a)
        indeg[b] += 1

    # Kahn longest-path; break cycles by processing remaining nodes by order
    from collections import deque
    rank = {nid: 0 for nid in nodes}
    q = deque([nid for nid in nodes if indeg[nid] == 0])
    if not q:  # pure cycle: seed with first node by order
        seed = min(nodes.values(), key=lambda n: n.order).nid
        q.append(seed)
    visited = set()
    indeg_work = dict(indeg)
    while q:
        nid = q.popleft()
        if nid in visited:
            continue
        visited.add(nid)
        for b in succ[nid]:
            if rank[b] < rank[nid] + 1:
                rank[b] = rank[nid] + 1
            indeg_work[b] -= 1
            if indeg_work[b] <= 0 and b not in visited:
                q.append(b)
    # any unvisited (in cycles) -> place after their max visited pred
    for nid in sorted(nodes, key=lambda x: nodes[x].order):
        if nid not in visited:
            preds = [rank[p] for p in pred[nid] if p in visited]
            rank[nid] = (max(preds) + 1) if preds else 0
            visited.add(nid)
    for nid, r in rank.items():
        nodes[nid].rank = r
    return succ, pred


def order_within_ranks(nodes, succ, pred):
    ranks = {}
    for n in nodes.values():
        ranks.setdefault(n.rank, []).append(n)
    for r in ranks:
        ranks[r].sort(key=lambda n: n.order)
    # a couple of barycenter sweeps to reduce crossings
    max_r = max(ranks) if ranks else 0
    pos = {n.nid: i for r in ranks for i, n in enumerate(ranks[r])}
    for _ in range(3):
        for r in range(1, max_r + 1):
            for n in ranks.get(r, []):
                ps = [pos[p] for p in pred[n.nid]] if pred.get(n.nid) else []
                n._bary = sum(ps) / len(ps) if ps else pos[n.nid]
            ranks[r].sort(key=lambda n: getattr(n, "_bary", pos[n.nid]))
            for i, n in enumerate(ranks[r]):
                pos[n.nid] = i
        for r in range(max_r - 1, -1, -1):
            for n in ranks.get(r, []):
                ss = [pos[s] for s in succ[n.nid]] if succ.get(n.nid) else []
                n._bary = sum(ss) / len(ss) if ss else pos[n.nid]
            ranks[r].sort(key=lambda n: getattr(n, "_bary", pos[n.nid]))
            for i, n in enumerate(ranks[r]):
                pos[n.nid] = i
    for r in ranks:
        for i, n in enumerate(ranks[r]):
            n.order_in_rank = i
    return ranks


def layout(nodes, edges, direction):
    succ, pred = assign_ranks(nodes, edges)
    # size nodes
    for n in nodes.values():
        if n.shape == "diamond":
            n.w, n.h = DIAMOND_W, DIAMOND_H
        else:
            lines = wrap_label(n.label, n.w)
            n.h = max(NODE_H, 22 + 16 * len(lines))
        # role colors
        if n.shape == "diamond":
            n.fill, n.stroke = DECISION_FILL, DECISION_STROKE
        elif not pred.get(n.nid):
            n.fill, n.stroke = START_FILL, START_STROKE
        elif not succ.get(n.nid):
            n.fill, n.stroke = END_FILL, END_STROKE
    ranks = order_within_ranks(nodes, succ, pred)

    horiz = direction in ("LR", "RL")
    # per-rank extent
    rank_keys = sorted(ranks)
    if horiz:
        # rank advances x; order advances y
        rank_x = {}
        x_cursor = MARGIN
        for r in rank_keys:
            rank_x[r] = x_cursor
            x_cursor += max((n.w for n in ranks[r]), default=NODE_W) + HGAP
        for r in rank_keys:
            col = ranks[r]
            total = sum(n.h for n in col) + VGAP * (len(col) - 1)
            y = MARGIN
            for n in col:
                n.x = rank_x[r] + (max(m.w for m in col) - n.w) / 2
                n.y = y
                y += n.h + VGAP
        if direction == "RL":
            maxx = max((n.x for n in nodes.values()), default=0)
            for n in nodes.values():
                n.x = maxx - (n.x - MARGIN)
    else:
        rank_y = {}
        y_cursor = MARGIN
        for r in rank_keys:
            rank_y[r] = y_cursor
            y_cursor += max((n.h for n in ranks[r]), default=NODE_H) + VGAP
        for r in rank_keys:
            row = ranks[r]
            for n in row:
                n.y = rank_y[r] + (max(m.h for m in row) - n.h) / 2
            total = sum(n.w for n in row) + HGAP * (len(row) - 1)
            x = MARGIN
            for n in row:
                n.x = x
                x += n.w + HGAP
        if direction == "BT":
            maxy = max((n.y for n in nodes.values()), default=0)
            for n in nodes.values():
                n.y = maxy - (n.y - MARGIN)

    width = max((n.x + n.w for n in nodes.values()), default=NODE_W) + MARGIN
    height = max((n.y + n.h for n in nodes.values()), default=NODE_H) + MARGIN
    return width, height


def wrap_label(label, width):
    out = []
    maxchars = max(8, int((width - 16) / CHAR_W))
    for para in label.split("\n"):
        words = para.split()
        if not words:
            out.append("")
            continue
        cur = ""
        for w in words:
            cand = (cur + " " + w).strip()
            if len(cand) > maxchars and cur:
                out.append(cur)
                cur = w
            else:
                cur = cand
        if cur:
            out.append(cur)
    return out or [""]


# ---- rendering ----------------------------------------------------------
def style_for(n):
    if n.shape == "diamond":
        base = "rhombus"
    elif n.shape in ("rounded", "stadium"):
        base = "rounded=1;whiteSpace=wrap;html=1"
    elif n.shape == "circle":
        base = "ellipse"
    elif n.shape == "cylinder":
        base = "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1"
    elif n.shape == "hexagon":
        base = "shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1"
    else:
        base = "rounded=0;whiteSpace=wrap;html=1"
    if n.shape == "diamond" or n.shape == "circle":
        base += ";whiteSpace=wrap;html=1"
    return f"{base};fillColor={n.fill};strokeColor={n.stroke};fontColor={TEXT_COLOR};"


def build_mxfile(nodes, edges, w, h):
    cells = ['<mxCell id="0" /><mxCell id="1" parent="0" />']
    idmap = {}
    for i, n in enumerate(nodes.values(), start=2):
        cid = f"n{i}"
        idmap[n.nid] = cid
        style = style_for(n)
        val = n.label.replace("\n", "&#10;")
        cells.append(
            f'<mxCell id="{cid}" value="{html.escape(val, quote=True)}" '
            f'style="{html.escape(style, quote=True)}" vertex="1" parent="1">'
            f'<mxGeometry x="{n.x:.0f}" y="{n.y:.0f}" width="{n.w:.0f}" '
            f'height="{n.h:.0f}" as="geometry" /></mxCell>'
        )
    for j, (a, b, lbl) in enumerate(edges):
        if a not in idmap or b not in idmap:
            continue
        style = (f"edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;"
                 f"strokeColor={EDGE_COLOR};fontColor={EDGE_COLOR};endArrow=block;")
        cells.append(
            f'<mxCell id="e{j}" value="{html.escape(lbl, quote=True)}" '
            f'style="{html.escape(style, quote=True)}" edge="1" parent="1" '
            f'source="{idmap[a]}" target="{idmap[b]}">'
            f'<mxGeometry relative="1" as="geometry" /></mxCell>'
        )
    model = (
        f'<mxGraphModel dx="{w:.0f}" dy="{h:.0f}" grid="1" gridSize="10" '
        f'guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" '
        f'pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0" '
        f'background="none"><root>{"".join(cells)}</root></mxGraphModel>'
    )
    return (f'<mxfile host="app.diagrams.net" agent="pm-workflow" '
            f'version="24.0.0" type="device"><diagram id="flow" name="Flow">'
            f'{model}</diagram></mxfile>')


def _box_intersect(cx, cy, w, hh, tx, ty):
    """Intersection of segment (center->target) with node box edge."""
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    hw, hhh = w / 2.0, hh / 2.0
    scale = float("inf")
    if dx != 0:
        scale = min(scale, hw / abs(dx))
    if dy != 0:
        scale = min(scale, hhh / abs(dy))
    return cx + dx * scale, cy + dy * scale


def _diamond_intersect(cx, cy, w, hh, tx, ty):
    """Intersection of segment (center->target) with a rhombus perimeter."""
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    hw, hhh = w / 2.0, hh / 2.0
    denom = abs(dx) / hw + abs(dy) / hhh
    if denom == 0:
        return cx, cy
    t = 1.0 / denom
    return cx + dx * t, cy + dy * t


def _ellipse_intersect(cx, cy, w, hh, tx, ty):
    """Intersection of segment (center->target) with an ellipse perimeter."""
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    rx, ry = w / 2.0, hh / 2.0
    denom = math.hypot(dx / rx, dy / ry)
    if denom == 0:
        return cx, cy
    t = 1.0 / denom
    return cx + dx * t, cy + dy * t


def _node_perimeter(n, tx, ty):
    """Point where an edge meets node n's actual perimeter (shape-aware)."""
    cx, cy = n.x + n.w / 2.0, n.y + n.h / 2.0
    if n.shape == "diamond":
        return _diamond_intersect(cx, cy, n.w, n.h, tx, ty)
    if n.shape == "circle":
        return _ellipse_intersect(cx, cy, n.w, n.h, tx, ty)
    return _box_intersect(cx, cy, n.w, n.h, tx, ty)


def _svg_body(nodes, edges):
    parts = []
    parts.append('<defs><marker id="arrow" markerWidth="10" markerHeight="10" '
                 'refX="8" refY="3" orient="auto" markerUnits="strokeWidth">'
                 '<path d="M0,0 L8,3 L0,6 z" fill="%s"/></marker></defs>' % EDGE_COLOR)
    # edges first
    for a, b, lbl in edges:
        if a not in nodes or b not in nodes:
            continue
        na, nb = nodes[a], nodes[b]
        ca = (na.x + na.w / 2, na.y + na.h / 2)
        cb = (nb.x + nb.w / 2, nb.y + nb.h / 2)
        x1, y1 = _node_perimeter(na, cb[0], cb[1])
        x2, y2 = _node_perimeter(nb, ca[0], ca[1])
        parts.append(
            f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
            f'stroke="{EDGE_COLOR}" stroke-width="1.5" marker-end="url(#arrow)"/>'
        )
        if lbl:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            parts.append(
                f'<rect x="{mx - len(lbl) * 3.2 - 3:.0f}" y="{my - 9:.0f}" '
                f'width="{len(lbl) * 6.4 + 6:.0f}" height="14" fill="none"/>'
                f'<text x="{mx:.0f}" y="{my + 3:.0f}" '
                f'font-family="Helvetica,Arial,sans-serif" font-size="11" '
                f'fill="{EDGE_COLOR}" text-anchor="middle">{html.escape(lbl)}</text>'
            )
    # nodes
    for n in nodes.values():
        cx = n.x + n.w / 2
        if n.shape == "diamond":
            top = (cx, n.y)
            right = (n.x + n.w, n.y + n.h / 2)
            bot = (cx, n.y + n.h)
            left = (n.x, n.y + n.h / 2)
            pts = f"{top[0]:.0f},{top[1]:.0f} {right[0]:.0f},{right[1]:.0f} {bot[0]:.0f},{bot[1]:.0f} {left[0]:.0f},{left[1]:.0f}"
            parts.append(f'<polygon points="{pts}" fill="{n.fill}" stroke="{n.stroke}" stroke-width="1.5"/>')
        elif n.shape == "circle":
            parts.append(f'<ellipse cx="{cx:.0f}" cy="{n.y + n.h/2:.0f}" rx="{n.w/2:.0f}" ry="{n.h/2:.0f}" fill="{n.fill}" stroke="{n.stroke}" stroke-width="1.5"/>')
        else:
            rx = 14 if n.shape in ("rounded", "stadium") else 6
            parts.append(f'<rect x="{n.x:.0f}" y="{n.y:.0f}" width="{n.w:.0f}" height="{n.h:.0f}" rx="{rx}" ry="{rx}" fill="{n.fill}" stroke="{n.stroke}" stroke-width="1.5"/>')
        lines = wrap_label(n.label, n.w)
        total = len(lines) * 16
        start_y = n.y + n.h / 2 - total / 2 + 12
        for i, ln in enumerate(lines):
            parts.append(
                f'<text x="{cx:.0f}" y="{start_y + i*16:.0f}" '
                f'font-family="Helvetica,Arial,sans-serif" font-size="{FONT_SIZE}" '
                f'fill="{TEXT_COLOR}" text-anchor="middle">{html.escape(ln)}</text>'
            )
    return parts


def render_svg(nodes, edges, w, h):
    parts = _svg_body(nodes, edges)
    mxfile = build_mxfile(nodes, edges, w, h)
    content_attr = html.escape(mxfile, quote=True)
    svg = (
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}" '
        f'content="{content_attr}">\n'
        + "\n".join(parts) + "\n</svg>\n"
    )
    return svg


def mermaid_to_svg(block_lines):
    direction, nodes, edges = parse_flowchart(block_lines)
    if not nodes:
        return None
    w, h = layout(nodes, edges, direction)
    return render_svg(nodes, edges, w, h)


# ---- markdown processing ------------------------------------------------
MERMAID_BLOCK_RE = re.compile(r'(^|\n)([ \t]*)```mermaid[ \t]*\n(.*?)\n[ \t]*```', re.DOTALL)


def slugify_heading(text):
    text = re.sub(r'[^A-Za-z0-9]+', '-', text.strip().lower()).strip('-')
    return text or "flow"


def process_markdown(path, dry_run=False, return_content=False):
    with open(path, "r", encoding="utf-8") as fh:
        src = fh.read()

    stem = os.path.splitext(os.path.basename(path))[0]
    results = {"converted": 0, "skipped": 0, "names": []}

    # find headings to name diagrams
    matches = list(MERMAID_BLOCK_RE.finditer(src))
    if not matches:
        if return_content:
            results["content"] = src
        return results

    out = []
    last = 0
    idx = 0
    for m in matches:
        body = m.group(3)
        first = next((l.strip() for l in body.splitlines() if l.strip()), "")
        if not re.match(r'^(flowchart|graph)\b', first, re.IGNORECASE):
            results["skipped"] += 1
            continue
        idx += 1
        svg = mermaid_to_svg(body.splitlines())
        if svg is None:
            results["skipped"] += 1
            continue
        # nearby preceding heading for the provenance name
        pre = src[:m.start()]
        hmatch = None
        for hm in re.finditer(r'(?m)^#{2,4}\s+(.+)$', pre):
            hmatch = hm
        heading = hmatch.group(1).strip() if hmatch else stem
        suffix = slugify_heading(heading)
        name = f"{stem}-{suffix}.drawio.svg"
        if name in results["names"]:
            name = f"{stem}-{suffix}-{idx}.drawio.svg"
        results["names"].append(name)

        # strip the XML declaration so the SVG embeds cleanly inside Markdown
        svg_inline = re.sub(r'^<\?xml[^>]*\?>\s*', '', svg).strip()

        out.append(src[last:m.start()])
        prefix_nl = m.group(1) or "\n"
        # embed the editable transparent draw.io SVG directly in the Markdown
        out.append(f"{prefix_nl}<!-- diagram: {name} -->\n\n{svg_inline}")
        last = m.end()
        results["converted"] += 1

    out.append(src[last:])
    content = "".join(out)
    if return_content:
        results["content"] = content
        return results
    if not dry_run and results["converted"]:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
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
                    help="convert a single .md file in memory and print the "
                         "result to stdout without modifying the source file")
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
            print(f"[{tag}] {path}  converted={res['converted']} skipped={res['skipped']}")
    print(f"\nFiles touched: {total_files}  diagrams converted: {total_conv}  skipped(non-flowchart): {total_skip}")


if __name__ == "__main__":
    main()
