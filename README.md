# UX Craft: a Claude Code plugin

Senior UI/UX intelligence for Claude Code. Inspired by the UX Engine plugin from DesignMotionHQ; the content and code here are original.

## What's inside

| Part | What it does |
| --- | --- |
| `skills/ux-craft` | Auto-activates on UI work. Route, read patterns, apply tokens, build, audit. |
| `data/patterns.json` | 29 starter patterns (Visual, Interaction, Forms, Feedback, Content, Navigation, Motion). |
| `data/modules.json` | 14 module routes (settings, data-table, form, pricing, onboarding, dashboard...). |
| `scripts/ux_craft.py` | CLI: `route`, `search`, `pattern`, `audit`, `checklist`, `tokens`. |
| `commands/` | `/ux-craft:ux-route`, `ux-audit`, `ux-pattern`, `ux-checklist`, `ux-system`. |
| `agents/ux-reviewer.md` | Read-only reviewer subagent. |

## Install

Try it locally:

```bash
claude --plugin-dir ./ux-craft
```

Validate the manifest:

```bash
claude plugin validate ./ux-craft
```

To share it, push the folder to GitHub with a `.claude-plugin/marketplace.json` that points at it, then users run `/plugin marketplace add <you>/<repo>` and `/plugin install ux-craft@<marketplace>`.

## Grow it

- Add a pattern: append an object to `data/patterns.json` (slug, category, hook, insight, rules, do, dont).
- Add a module: append to `data/modules.json` and reference existing pattern slugs.
- Add an audit rule: add a `(regex, message, extensions)` tuple to `RULES` in `scripts/ux_craft.py`.
- Add stack-specific references (Tailwind, React Native, Godot UI) under `skills/ux-craft/references/` and link them from `SKILL.md`.

The auditor is a heuristic line scanner. It catches common mistakes quickly but does not replace the checklist or a human look.
