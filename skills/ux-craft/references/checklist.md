# Pre-Ship Checklist (12 points)

Walk every point before calling a screen done. Report each as pass, fail, or not applicable.

1. **State completeness**: loading, empty, partial, error and success states are all designed.
2. **Submit guard**: buttons disable or show pending on submit; double-clicks cannot send twice.
3. **Destructive friction**: dangerous actions are named, visually separated, and offer undo or confirmation.
4. **Human microcopy**: errors say what happened and what to do, in plain language.
5. **Offline and failure handling**: network loss and failed requests keep the user's input and offer retry.
6. **Concentric radii**: inner radius = outer radius - padding.
7. **No emoji as icons**: use one SVG icon set with consistent stroke and viewBox.
8. **Calibrated motion**: entrances 200-300ms ease-out, hover/press 120-200ms, exits shorter than entrances; transform/opacity only; reduced-motion respected.
9. **Contrast**: body text at least 4.5:1, large text and UI boundaries at least 3:1.
10. **Touch targets**: at least 44x44px hit area with spacing between neighbors.
11. **Mobile 390px**: no horizontal scroll; inputs at 16px or larger to avoid iOS zoom.
12. **Focus visible**: a 2px offset ring on every interactive element in keyboard traversal; logical tab order.
