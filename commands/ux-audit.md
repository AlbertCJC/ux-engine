---
description: Audit UI code for UX, accessibility and motion anti-patterns
argument-hint: <file-or-directory>
---

Audit "$ARGUMENTS" (default to the current directory if empty).

1. Run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/ux_craft.py audit "$ARGUMENTS"`.
2. Read the flagged files and discard false positives.
3. Review what the script cannot see: missing loading/empty/error states, unguarded submits, destructive actions without undo, weak microcopy.
4. Report findings grouped by severity (blocker, should fix, polish) with file:line and a concrete fix. Offer to apply the fixes.
