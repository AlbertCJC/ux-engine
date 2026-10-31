---
name: ux-craft
description: Use when designing, building, reviewing or polishing any user interface (screens, components, forms, dashboards, settings, onboarding, pricing, tables, navigation, motion). Routes the UI module to proven patterns, applies design tokens, and runs a pre-ship checklist.
---

# UX Craft

Think like a senior product designer and design-systems engineer. Never start from a blank canvas: route the module to patterns, apply tokens, build, then audit.

## Workflow

1. **Route.** Identify the UI module (settings, data table, form, pricing, onboarding, dashboard, ...). Run:
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/ux_craft.py route "<module>"`
   This returns a primary pattern and supporting patterns from `data/modules.json`.
2. **Read the patterns.** For each returned slug run:
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/ux_craft.py pattern <slug>`
   Follow the rules and do/don't lists.
3. **Check what exists.** Before adding styles or motion, inspect the project's current tokens, Tailwind config, component library and `prefers-reduced-motion` handling. Match them; do not introduce a parallel system.
4. **Apply tokens.** Use `references/tokens.md` as the default when the project has none. Never hardcode one-off colors, spacing or durations.
5. **Design every state.** Loading, empty, partial, error, offline and success. A screen without these is unfinished.
6. **Build.**
7. **Audit.** Run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/ux_craft.py audit <path>`, fix findings, then walk `references/checklist.md`.

## Principles

- Every element earns its place: it gives feedback, orientation, focus, or (rarely) delight.
- Feedback within 400ms for every interaction; show progress for anything slower.
- Destructive actions are named, separated from safe actions, and undoable where possible.
- Error copy speaks in the user's terms and says what to do next. Never show raw exceptions.
- Motion uses transform and opacity only, with calibrated durations, and collapses to an instant state change under reduced motion.
- Accessibility is a build constraint, not a final pass: contrast, focus rings, 44px targets, labels, keyboard paths.

## When not to use

Pure backend work, CLI output, or copy-only tasks with no interface.
