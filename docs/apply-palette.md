<h1 align="center">apply_palette.py</h1>

<p align="center">A short guide to configure and run the theme palette generator for <code>x</code>.</p>

<h2 align="center">Overview</h2>

This script reads the editable configuration from `theme-palette.json` and applies it to `theme.css`.

It updates:

- core theme colors
- light mode variables
- dark mode variables
- code block colors
- focus shadows
- embedded font settings

<h2 align="center">Requirements</h2>

Before running the script, make sure you have:

- Python 3 installed
- the repository opened in your terminal
- `theme-palette.json` in the project root
- `theme.css` in the project root

<h2 align="center">Project Structure</h2>

The command assumes this layout:

```text
obsidian/
├── docs/
├── scripts/
│   └── apply_palette.py
├── theme-palette.json
└── theme.css
```

<h2 align="center">How To Run</h2>

From the project root, run:

```bash
python3 scripts/apply_palette.py --config theme-palette.json --input theme.css --output theme.css
```

This command:

- loads the configuration file
- reads the current CSS
- replaces the configured values
- writes the result back into `theme.css`

<h2 align="center">Arguments</h2>

The script supports these arguments:

- `--config`: path to the editable JSON configuration file
- `--input`: path to the source CSS file
- `--output`: path to the output CSS file

Example with custom paths:

```bash
python3 scripts/apply_palette.py \
  --config theme-palette.json \
  --input theme.css \
  --output theme.css
```

<h2 align="center">Editing Colors</h2>

Open `theme-palette.json` and edit the palette sections in order.

Main sections:

- `palette.core_colors`: main accent and heading colors, also linked to Style Settings
- `palette.light_mode`: variables used in light mode
- `palette.dark_mode`: variables used in dark mode
- `palette.code`: code block, inline code, and syntax colors
- `palette.focus_shadows`: regex-based replacements for focus outlines
- `palette.replacements`: direct string replacements for fixed CSS values

Example:

```json
{
  "name": "accent",
  "setting_id": "accent-color",
  "css_var": "--accent-color",
  "light": "#2563eb",
  "dark": "#7aa2ff"
}
```

<h2 align="center">Editing Fonts</h2>

The `font` section controls the font family and embedded font data used in `theme.css`.

Important fields:

- `family_name`: font family name written into the `@font-face` blocks
- `text_stack`: font stack for body text
- `interface_stack`: font stack for interface elements
- `monospace_stack`: font stack for code and monospace use
- `faces`: list of embedded font faces

Each font face supports:

- `label`: internal label for the face
- `style`: usually `normal` or `italic`
- `weight`: the CSS weight or range used by that face
- `format`: usually `woff2`
- `keep_existing_base64`: keeps the current base64 already stored in `theme.css`
- `source_path`: loads a local font file and converts it to base64
- `source_base64`: lets you paste the base64 string directly

<h2 align="center">Keeping The Current Embedded Font</h2>

If you want to preserve the current embedded font data, keep this:

```json
{
  "label": "regular",
  "style": "normal",
  "weight": "400 700",
  "format": "woff2",
  "keep_existing_base64": true,
  "source_path": "",
  "source_base64": ""
}
```

<h2 align="center">Replacing The Embedded Font From A File</h2>

If you want the script to embed a new font automatically, point `source_path` to a local `.woff2` file:

```json
{
  "label": "regular",
  "style": "normal",
  "weight": "400 700",
  "format": "woff2",
  "keep_existing_base64": false,
  "source_path": "fonts/YourFont-Regular.woff2",
  "source_base64": ""
}
```

Do the same for the italic face if needed.

<h2 align="center">Replacing The Embedded Font With Raw Base64</h2>

If you already have the encoded font, paste it into `source_base64`:

```json
{
  "label": "italic",
  "style": "italic",
  "weight": "400 700",
  "format": "woff2",
  "keep_existing_base64": false,
  "source_path": "",
  "source_base64": "PASTE_YOUR_BASE64_HERE"
}
```

<h2 align="center">Recommended Workflow</h2>

1. Edit `theme-palette.json`.
2. Save your changes.
3. Run `apply_palette.py`.
4. Reload the theme in Obsidian.
5. Repeat until the palette and fonts look right.

<h2 align="center">Troubleshooting</h2>

If the script fails:

- make sure you are running it from the project root
- confirm that `theme-palette.json` is valid JSON
- confirm that the CSS structure still matches the theme blocks the script expects
- verify that any `source_path` points to a real `.woff2` file
- check that `source_base64` is a valid base64 string if you use it

<h2 align="center">Notes</h2>

- The script overwrites the output file you provide.
- Using the same file for `--input` and `--output` is supported.
- If you edit `theme.css` structure heavily, some automated replacements may need to be updated in the script.
