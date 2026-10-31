#!/usr/bin/env python3
"""UX Craft CLI: route modules to patterns, search patterns, audit UI code, print checklist and tokens."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REFS = ROOT / "skills" / "ux-craft" / "references"


def load(name):
    with open(DATA / name, encoding="utf-8") as f:
        return json.load(f)


def by_slug():
    return {p["slug"]: p for p in load("patterns.json")}


def fmt_pattern(p):
    out = [f"# {p['title']}  [{p['category']}]  ({p['slug']})", f"> {p['hook']}", "", p["insight"], "", "Rules:"]
    out += [f"- {r}" for r in p["rules"]]
    out += ["", "Do:"] + [f"- {d}" for d in p["do"]]
    out += ["", "Don't:"] + [f"- {d}" for d in p["dont"]]
    return "\n".join(out)


def cmd_route(query):
    q = query.lower().strip()
    best, best_score = None, 0
    for m in load("modules.json"):
        names = [m["module"]] + m.get("aliases", [])
        score = 0
        for n in names:
            if q == n:
                score = max(score, 100)
            elif n in q or q in n:
                score = max(score, 60)
            else:
                score = max(score, 10 * len(set(q.split()) & set(n.split())))
        if score > best_score:
            best, best_score = m, score
    if not best:
        print(f"No module matched '{query}'. Known modules:")
        print(", ".join(m["module"] for m in load("modules.json")))
        return 1
    patterns = by_slug()
    print(f"Module: {best['module']}")
    print(f"Note: {best['note']}\n")
    print(f"PRIMARY: {best['primary']}  - {patterns[best['primary']]['hook']}")
    for s in best["secondary"]:
        print(f"secondary: {s}  - {patterns[s]['hook']}")
    print("\nInspect any with: ux_craft.py pattern <slug>")
    return 0


def cmd_search(query):
    q = query.lower()
    hits = [p for p in load("patterns.json") if q in json.dumps(p).lower()]
    if not hits:
        print("No patterns found.")
        return 1
    for p in hits:
        print(f"{p['slug']:24} [{p['category']}] {p['hook']}")
    return 0


def cmd_pattern(slug):
    p = by_slug().get(slug)
    if not p:
        print(f"Unknown pattern '{slug}'. Try: search <term>")
        return 1
    print(fmt_pattern(p))
    return 0


# (regex, message, applies-to-extensions)
RULES = [
    (r"outline\s*:\s*(none|0)\b(?![^;{]*(box-shadow|border))", "Focus outline removed without a replacement style", None),
    (r"transition\s*:\s*all\b", "'transition: all' animates layout properties; list specific properties", None),
    (r"transition(-property)?\s*:[^;]*\b(width|height|top|left|margin|padding)\b", "Animating layout properties; prefer transform/opacity", None),
    (r"<img(?![^>]*\balt=)[^>]*>", "<img> without alt attribute", {".html", ".jsx", ".tsx", ".vue", ".svelte"}),
    (r"<(div|span)[^>]*\bonClick=", "Clickable div/span; use <button> or add role, tabIndex and key handlers", {".jsx", ".tsx"}),
    (r"<(div|span)[^>]*@click=", "Clickable div/span; use <button> or add role and key handlers", {".vue"}),
    (r"<input(?![^>]*\b(aria-label|id)=)[^>]*>", "<input> with no id/aria-label to attach a label", {".html", ".jsx", ".tsx", ".vue", ".svelte"}),
    (r"<button[^>]*>\s*[☀-➿\U0001F300-\U0001FAFF]+\s*</button>", "Emoji used as button content; use an SVG icon with an accessible name", None),
    (r"font-size\s*:\s*(1[0-5]|[0-9])px[^}]*", "Font size below 16px; check inputs on mobile (iOS zoom)", {".css", ".scss", ".less"}),
    (r"(height|min-height)\s*:\s*(\d|[1-3]\d|4[0-3])px[^}]*(button|btn)", "Possible touch target under 44px", {".css", ".scss", ".less"}),
    (r"user-scalable\s*=\s*no|maximum-scale\s*=\s*1\b", "Viewport blocks zoom; hurts accessibility", None),
    (r"autoplay(?![^>]*muted)", "Autoplaying media should be muted and pausable", None),
    (r"\bAn error occurred\b|\bSomething went wrong\b|\bError:\s*\{?\s*message", "Generic or raw error copy; explain what happened and what to do", None),
]

EXTS = {".html", ".htm", ".css", ".scss", ".less", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte"}


def iter_files(path):
    p = Path(path)
    if p.is_file():
        yield p
        return
    for f in p.rglob("*"):
        if f.suffix.lower() in EXTS and not any(x in f.parts for x in ("node_modules", ".git", "dist", "build", ".next")):
            yield f


def cmd_audit(path):
    if not Path(path).exists():
        print(f"Path not found: {path}")
        return 2
    findings = 0
    has_reduced_motion = False
    uses_motion = False
    for f in iter_files(path):
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if "prefers-reduced-motion" in text:
            has_reduced_motion = True
        if re.search(r"@keyframes|animation\s*:|transition\s*:|framer-motion|gsap", text):
            uses_motion = True
        for i, line in enumerate(text.splitlines(), 1):
            for pattern, msg, exts in RULES:
                if exts and f.suffix.lower() not in exts:
                    continue
                if re.search(pattern, line, re.I):
                    print(f"{f}:{i}: {msg}")
                    findings += 1
    if uses_motion and not has_reduced_motion:
        print(f"{path}: Motion in use but no prefers-reduced-motion handling found")
        findings += 1
    print(f"\n{findings} finding(s). Heuristic scan only; follow with the checklist and a manual review.")
    return 1 if findings else 0


def cmd_checklist():
    print((REFS / "checklist.md").read_text(encoding="utf-8"))
    return 0


def cmd_tokens():
    print((REFS / "tokens.md").read_text(encoding="utf-8"))
    return 0


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        print("Usage: ux_craft.py route|search|pattern|audit|checklist|tokens [arg]")
        return 2
    cmd, arg = argv[1], " ".join(argv[2:])
    needs_arg = {"route", "search", "pattern", "audit"}
    if cmd in needs_arg and not arg:
        print(f"'{cmd}' needs an argument")
        return 2
    table = {"route": cmd_route, "search": cmd_search, "pattern": cmd_pattern, "audit": cmd_audit}
    if cmd in table:
        return table[cmd](arg)
    if cmd == "checklist":
        return cmd_checklist()
    if cmd == "tokens":
        return cmd_tokens()
    print(f"Unknown command '{cmd}'")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
