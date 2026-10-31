---
description: Route a UI module (settings, table, form, pricing...) to its primary and supporting UX patterns
argument-hint: <module>
---

Route the UI module "$ARGUMENTS" to patterns.

1. Run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/ux_craft.py route "$ARGUMENTS"`.
2. Run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/ux_craft.py pattern <slug>` for the primary and each secondary pattern.
3. Summarize as a short design brief: the primary pattern, how each secondary supports it, and the states to design. Keep it under 200 words unless asked for more.
