# spoonart1.github.io

Portfolio landing page for **Muhammad Lafran Pane** — Senior Android Engineer.

Live at **https://spoonart1.github.io/**

Plain static HTML and CSS. No framework, no build step, no tracking. Push to
`master` and GitHub Pages serves it.

---

## Files

```
index.html                     the whole page
.nojekyll                      tells GitHub Pages to skip Jekyll
assets/
  css/site.css                 all styles
  Lafran-Pane-CV-2026.pdf      résumé, linked from the page
  img/favicon.svg              tab icon
  img/og.png                   1200×630 share card for LinkedIn, Slack, X
  shots/
    swat-driver-2.svg          screenshot placeholders — replace these
    moka-pos.svg
    moladin-agent.svg
```

---

## Swapping in real screenshots

The frames are dimension-agnostic. **Any image size or aspect ratio fits** —
a tall phone screenshot, a wide tablet capture, a square crop. The frame keeps a
fixed aspect so the layout never shifts, shows your image whole via
`object-fit: contain`, and fills the leftover space with a blurred, dimmed copy
of the same image. Nothing gets stretched and nothing gets cropped.

**If your file is also `.svg`,** just overwrite the placeholder — no code change.

**If your file is `.png` or `.jpg`,** drop it in `assets/shots/` and update the two
`src` attributes for that project in `index.html`. They sit next to each other:

```html
<figure class="shot">
  <img class="shot-bg"  src="assets/shots/swat-driver-2.png" alt="" aria-hidden="true">
  <img class="shot-img" src="assets/shots/swat-driver-2.png" alt="SWAT Driver app screenshot">
  <figcaption>swat-driver-2.png</figcaption>
</figure>
```

Both `src` values point at the same file — one is the blurred backdrop, one is the
image itself. Update the `alt` text on `.shot-img` too; leave `.shot-bg` empty since
it is decorative.

Tips:
- Compress before committing. Aim under ~300&nbsp;KB per screenshot.
- Two or three screenshots stitched side by side in one image works well and reads
  better than a single cramped screen.
- To drop the filename caption once real screenshots are in, delete the
  `<figcaption>` line.

---

## Changing the aspect of the frames

One line in `assets/css/site.css`:

```css
.shot { aspect-ratio: 4 / 5; }   /* portrait-ish, suits phone screenshots */
```

`3 / 4` is taller, `1 / 1` is square, `16 / 10` is landscape. The responsive rules
further down override this on narrow viewports — search for `.shot` to find them.

---

## Regenerating the share card

`assets/img/og.png` is a plain 1200×630 PNG. Edit it in any image tool, or
regenerate it with the Pillow script kept in the commit that added it.
Keep the dimensions — LinkedIn and Slack both expect 1.91:1.

---

## Design notes

Direction is **"5 a.m. dashboard"** — the hour a driver opens a dispatch app.

- **Palette.** Material 3 tonal layering on green-tinted neutrals rather than flat
  black. Two accents only: `--route` (`#4FE0A8`, the nav route line) and
  `--horizon` (`#E8B25C`, the amber behind it). All tokens are at the top of
  `site.css`.
- **Type.** Archivo on its expanded width axis for display, IBM Plex Sans for body,
  IBM Plex Mono for every number and label. Mono numbers are tabular so the
  before/after figures line up.
- **The route track** is the signature device. A dim origin, a lit destination, the
  distance drawn between them. It repeats on every claim, and flexes to say two
  things: *moved* (82% → 99.3%) and *held* (`.vital.held`, for a sustained figure).
  Tracks draw once, on scroll, via one `IntersectionObserver`.
- **Accessibility.** Skip link, visible focus rings, decorative rails hidden from
  screen readers, and `prefers-reduced-motion` renders every track in its final
  state.

---

## Earlier work

Roles before 2018 — games at Agate Jogja, iOS and early Android at Indiva and
Docotel — are summarised in the *Before that* section of the page and detailed in
the [résumé](assets/Lafran-Pane-CV-2026.pdf).
