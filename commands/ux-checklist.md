---
description: Run the 12-point pre-ship UX checklist against a screen or component
argument-hint: [file-or-directory]
---

Run the pre-ship checklist on "$ARGUMENTS" (or the most recently changed UI files if empty).

1. Run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/ux_craft.py checklist`.
2. Inspect the code and mark each of the 12 points pass, fail or n/a, with evidence (file:line) for every fail.
3. End with the shortest list of fixes that would make it shippable.
