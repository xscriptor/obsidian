<h1 align="center">quick-palette</h1>

<p align="center">A fast workflow for changing the main theme palette and font without editing the full configuration file.</p>

<h2 align="center">Overview</h2>

`quick-palette.json` is the short configuration layer above `theme-palette.json`.

Instead of editing the full palette manually, you only define:

- four main light and dark accent groups
- four base background values
- font settings

The script expands those values into the complete theme configuration and then applies the result to `theme.css`.

<h2 align="center">Files</h2>

This workflow uses:

- `quick-palette.json`
- `scripts/apply_quick_palette.py`
- `theme-palette.json`
- `theme.css`

<h2 align="center">Quick Config</h2>

The short JSON is organized like this:

```json
{
  "colors": {
    "accent_light": "#2563eb",
    "accent_dark": "#7aa2ff",
    "heading_light": "#7c3aed",
    "heading_dark": "#a78bfa",
    "support_light": "#0f766e",
    "support_dark": "#2dd4bf",
    "warm_light": "#c2410c",
    "warm_dark": "#f5b971"
  },
  "backgrounds": {
    "light_base": "#ffffff",
    "light_surface": "#fcfdff",
    "dark_base": "#0a0a0a",
    "dark_surface": "#121212"
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

<h2 align="center">How To Run</h2>

From the project root:

```bash
python3 scripts/apply_quick_palette.py \
  --quick-config quick-palette.json \
  --full-config theme-palette.json \
  --input theme.css \
  --output theme.css
```

<h2 align="center">What It Generates</h2>

The script calculates and writes:

- the full `palette.core_colors` section
- light mode surfaces, borders, hover states, and tags
- dark mode surfaces, borders, hover states, and tags
- code block colors
- focus ring colors
- font settings

It writes the expanded result into `theme-palette.json` and applies it to `theme.css`.

<h2 align="center">Changing Fonts</h2>

You can keep the current embedded font:

```json
{
  "keep_existing_base64": true
}
```

Or replace it with local `.woff2` files:

```json
{
  "regular_path": "fonts/YourFont-Regular.woff2",
  "italic_path": "fonts/YourFont-Italic.woff2",
  "keep_existing_base64": false
}
```

Or paste the encoded font directly:

```json
{
  "regular_base64": "PASTE_BASE64_HERE",
  "italic_base64": "PASTE_BASE64_HERE",
  "keep_existing_base64": false
}
```

<h2 align="center">Recommended Use</h2>

Use `quick-palette` when you want to:

- redesign the theme palette quickly
- keep the current theme structure
- update both light and dark mode together
- avoid editing the full configuration manually

<h2 align="center">Notes</h2>

- `quick-palette.json` is the short editable source.
- `theme-palette.json` remains the expanded full configuration.
- Running the quick script overwrites the full configuration file.
