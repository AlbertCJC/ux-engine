# Default Design Tokens

Use these only when the project has no system of its own. Define them once as CSS variables and reference them everywhere.

## Spacing (4px grid)
`--space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px; --space-6: 24px; --space-8: 32px; --space-12: 48px; --space-16: 64px`

## Radii
`--radius-sm: 6px; --radius-md: 10px; --radius-lg: 16px`
Rule: nested radius = outer radius - padding (a 16px card with 8px padding holds a 8px inner radius).

## Color (OKLCH, semantic names)
```
--bg:            oklch(99% 0.003 250);
--surface:       oklch(97% 0.005 250);
--border:        oklch(90% 0.008 250);
--text:          oklch(22% 0.02 250);
--text-muted:    oklch(48% 0.02 250);
--accent:        oklch(55% 0.19 255);
--accent-text:   oklch(99% 0 0);
--success:       oklch(55% 0.14 150);
--warning:       oklch(70% 0.15 75);
--danger:        oklch(55% 0.21 25);
```
Dark mode: redefine the same names under `@media (prefers-color-scheme: dark)`; never invert by filter. Verify 4.5:1 for text pairs.

## Type
Scale (rem): 0.75, 0.875, 1, 1.125, 1.25, 1.5, 2, 3. Body 1rem / 1.5 line height; headings 1.15-1.25. Inputs never below 16px on mobile.

## Motion
```
--ease-out:   cubic-bezier(0.22, 1, 0.36, 1);
--ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
--dur-fast: 150ms;   /* hover, press */
--dur-base: 250ms;   /* entrances */
--dur-slow: 350ms;   /* large layout shifts, max */
```
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

## Elevation
Prefer borders plus one soft shadow: `0 1px 2px oklch(20% 0.02 250 / 0.06), 0 4px 12px oklch(20% 0.02 250 / 0.08)`.
