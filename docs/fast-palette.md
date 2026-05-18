<h1 align="center">fast-palette</h1>

<p align="center">A typography-focused workflow that uses only two emphasis colors and computes the heading hierarchy automatically.</p>

<h2 align="center">Overview</h2>

`apply_fast_palette.py` is designed for very fast visual changes when you only want to control typography.

It keeps the current light and dark palette structure, but recalculates:

- normal text
- muted text
- faint text
- text accent
- interactive accent used by text-facing UI elements
- `h1` to `h6`
- italic text

This workflow uses only two emphasis colors:

- one for light mode
- one for dark mode

The rest of the hierarchy is generated automatically from strong to soft.

<h2 align="center">How It Works</h2>

The script reads:

- `fast-palette.json`
- `theme-palette.json`
- `theme.css`

Then it:

1. keeps the current theme palette as the base
2. computes normal text as the inverse of the base background
3. computes muted and faint text from that normal color
4. computes heading colors from the emphasis color using a strength scale
5. derives text and interactive accents from the same hierarchy
6. computes italic color as an intermediate emphasis value
7. updates the font settings
8. writes the result back to `theme-palette.json` and `theme.css`

<h2 align="center">Fast Config</h2>

The short config is intentionally minimal:

```json
{
  "typography": {
    "light_emphasis": "#7c3aed",
    "dark_emphasis": "#a78bfa"
  },
  "font": {
    "family_name": "EB Garamond",
    "text_stack": "'EB Garamond', Georgia, serif",
    "interface_stack": "'EB Garamond', Georgia, serif",
    "monospace_stack": "'Courier New', monospace",
    "regular_path": "",
    "italic_path": "",
    "regular_base64": "",
    "italic_base64": "",
    "keep_existing_base64": true
  }
}
```

<h2 align="center">Hierarchy Scale</h2>

The heading intensity is calculated automatically with a descending scale:

- `h1`: strongest
- `h2`: very strong
- `h3`: medium-strong
- `h4`: medium
- `h5`: soft
- `h6`: softer
- `italic`: between medium and soft

This keeps the theme visually coherent without introducing too many different text colors.

<h2 align="center">How To Run</h2>

From the project root:

```bash
python3 scripts/apply_fast_palette.py \
  --fast-config fast-palette.json \
  --full-config theme-palette.json \
  --input theme.css \
  --output theme.css
```

You can also override the two emphasis colors directly from the command line:

```bash
python3 scripts/apply_fast_palette.py \
  --fast-config fast-palette.json \
  --full-config theme-palette.json \
  --input theme.css \
  --output theme.css \
  --light-emphasis "#b42318" \
  --dark-emphasis "#7dd3fc"
```

<h2 align="center">What Changes</h2>

This workflow updates only the typography-related color hierarchy and font setup.

It modifies:

- `--text-normal`
- `--text-muted`
- `--text-faint`
- `--text-accent`
- `--text-accent-hover`
- `--interactive-accent`
- `--interactive-accent-hover`
- `accent` in the core color settings
- heading colors
- italic color
- font family and embedded font sources

It does not redesign the whole UI palette like `quick-palette`.

<h2 align="center">When To Use It</h2>

Use `fast-palette` when you want:

- a cleaner literary hierarchy
- fewer text colors
- a faster typography-only workflow
- a heading system derived from one emphasis color per mode
- visible accent changes without redesigning the whole UI palette

Use `quick-palette` when you want to redesign the full theme palette.

<h2 align="center">Fonts</h2>

The font block works like the other scripts:

- keep the existing embedded base64 with `keep_existing_base64: true`
- load a local `.woff2` file with `regular_path` and `italic_path`
- paste raw base64 with `regular_base64` and `italic_base64`

<h2 align="center">Notes</h2>

- `fast-palette.json` is the minimal typography input.
- `theme-palette.json` remains the expanded configuration file.
- Running the script overwrites the full configuration and reapplies the CSS.
