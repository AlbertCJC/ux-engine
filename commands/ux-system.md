---
description: Generate or adopt a semantic design-token system (color, spacing, radii, type, motion) for this project
argument-hint: [brand color or style notes]
---

Create a token system for this project. Notes from the user: "$ARGUMENTS".

1. Inspect the project first (Tailwind config, existing CSS variables, theme files). If a system exists, extend it instead of replacing it.
2. Run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/ux_craft.py tokens` for the defaults.
3. Adapt the accent hue to the user's notes, keep semantic names, and verify 4.5:1 text contrast in light and dark.
4. Write the tokens in the project's idiom (CSS variables, Tailwind theme, or a tokens file) and show a short usage example.
