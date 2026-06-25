# Reproducible Color Schemes

This document describes how the 12 color-scheme system works, how to modify existing schemes, and how to add new ones.

## Architecture

The theme ships with 12 built-in color schemes selectable via the Style Settings plugin. Each scheme derives its full set of Obsidian CSS variables (~80 declarations) from a 16-color ANSI terminal palette plus a background and foreground color.

### File layout

```
theme.css             -- unified theme: base styles + all 12 scheme overrides
colors.md             -- source palettes (terminal format, 16 colors + bg + fg)
colors-css.md         -- visual reference with color swatches and CSS mapping
scripts/
  build_unified.py    -- generates theme.css from colors.md + template
```

### How scheme switching works

1. The user installs the theme and the Style Settings plugin.
2. In Settings > Style Settings, a dropdown "Scheme" lists all 12 cities.
3. Selecting a scheme adds a class like `scheme-madrid` to `<body>`.
4. The CSS contains rules like `body.scheme-madrid.theme-light { --background-primary: #fafafa; ... }` that override the base variables.
5. The class persists across sessions (Style Settings handles persistence).

## Scheme definition format

Each scheme in `colors.md` follows this structure:

```json
{
    "color0":  "#0a0a0a",
    "color1":  "#fc618d",
    "color2":  "#7bd88f",
    "color3":  "#fce566",
    "color4":  "#fd9353",
    "color5":  "#948ae3",
    "color6":  "#5ad4e6",
    "color7":  "#f7f1ff",
    "color8":  "#0f0f0f",
    "color9":  "#fc618d",
    "color10": "#7bd88f",
    "color11": "#fce566",
    "color12": "#fd9353",
    "color13": "#948ae3",
    "color14": "#5ad4e6",
    "color15": "#f7f1ff",
    "background": "#050505",
    "foreground": "#f7f1ff"
}
```

## Color mapping: terminal to CSS

The build script maps each ANSI position to a semantic role:

| ANSI   | Role        | CSS variables                              |
|--------|-------------|--------------------------------------------|
| color0 | Base dark   | --background-secondary, --color-base-00    |
| color1 | Red/error   | --text-error, --color-red, --cm-error      |
| color2 | Green/support| --text-success, --color-green, --cm-string |
| color3 | Yellow/warm | --text-warning, --color-yellow, --cm-number|
| color4 | Accent      | --accent-color, --text-accent, --color-blue|
| color5 | Heading     | --h1-color, --color-purple, --cm-keyword   |
| color6 | Cyan/info   | --h4-color, --color-cyan, --cm-bool        |
| color7 | Light       | --text-on-accent, --color-base-100         |
| color8 | Faint       | --text-faint, --color-base-50              |
| color9 | Pink        | --color-pink                               |

background -> --background-primary
foreground -> --text-normal

## Derived variables

The build script generates approximately 80 CSS variables per scheme from the 6 semantic colors extracted from each palette:

| Category       | Variables                                                                 |
|----------------|---------------------------------------------------------------------------|
| Core           | accent-color, h1-color, h2-color, h3-color, italic-color                 |
| Backgrounds    | background-primary, primary-alt, secondary, secondary-alt, accent         |
| Text           | text-normal, text-muted, text-faint, text-accent, text-on-accent         |
| Borders        | border-color, border-color-hover, border-color-focus, divider-color      |
| Interactive    | interactive-normal, interactive-hover, interactive-accent, success        |
| Callouts       | callout-info, warning, error, success, tip, note (bg + border + text)     |
| Tags           | tag-background, tag-text, tag-border                                      |
| Highlights     | highlight-yellow, green, blue, pink, purple                                |
| Tables         | table-header-background, row-even, row-odd, border-color                   |
| Editor         | card-color, select-color, input-color                                      |
| Graph View     | graph-text, graph-line, graph-node, graph-node-unresolved, focused, tag, attachment |
| Syntax tokens  | ~30 CM6 tokens + ~28 Prism tokens (keyword, string, number, tag, attr-name, punctuation, operator, function, etc.) |
| Folder colors  | 24 folder border colors across 5 nesting levels, derived from scheme palette |
| Code blocks    | Generic and per-language backgrounds (javascript, python, css, html, json, markdown, bash) |

Every value uses `var(--background-opacity, 0.8)` for dark mode backgrounds, respecting the Style Settings opacity slider.

## Adding a new scheme

1. Add a new entry in `colors.md` with the 16 colors + background + foreground.
2. Run the build script:
   ```bash
   cp theme.css theme.css.bak && python3 scripts/build_unified.py
   ```
3. The script automatically:
   - Parses the new palette from `colors.md`
   - Generates all ~80 CSS variables
   - Generates all syntax token overrides
   - Generates per-language code block tints
   - Generates folder color borders
   - Adds the new scheme to the Style Settings dropdown
4. Copy the output to your vault:
   ```bash
   cp theme.css /path/to/vault/.obsidian/themes/X/theme.css
   ```

## Modifying an existing scheme

Edit the corresponding JSON block in `colors.md`, then rebuild:

```bash
python3 scripts/build_unified.py && cp theme.css /path/to/vault/.obsidian/themes/X/theme.css
```

## Light vs dark mode detection

The script automatically detects whether a scheme is light or dark based on the background color's luminance. Schemes with bright backgrounds are generated as `.theme-light` overrides; schemes with dark backgrounds use `.theme-dark`.

Current distribution:
- Dark schemes (9): X, Lahabana, Miami, Paris, Tokio, Oslo, Berlin, Praha, Bogota
- Light schemes (3): Madrid, Helsinki, London

## Build script internals

`scripts/build_unified.py` performs the following steps:

1. Parse `colors.md` -> extract all JSON palette blocks
2. Read the base `theme.css` as a template
3. For each scheme:
   - Extract 6 semantic colors (accent, heading, support, warm, error, info)
   - Derive all CSS variables using color mixing
   - Generate CM6 and Prism syntax token overrides
   - Generate per-language code block tints
   - Generate folder color borders
4. Replace the `@settings` block with one containing a `class-select` dropdown
5. Append all scheme overrides to the template
6. Write the unified `theme.css`

The derivation logic uses these color operations:
- `mix(a, b, ratio)` blends two hex colors
- `lighten(color, amount)` shifts toward white
- `darken(color, amount)` shifts toward black
- `alpha(color, opacity)` produces an rgba() string

## Style Settings integration

The `@settings` block at the top of `theme.css` defines:

- **Scheme selector**: `class-select` type dropdown with 12 options
- **Transparency section**: opacity slider, mica toggle, blur intensity
- **Colors section**: accent, h1, h2, h3, italic color pickers
- **Typography section**: font size and line height sliders
- **Interface section**: border radius slider and folder colors toggle

The scheme selector defaults to `scheme-x` (the "X" palette). When no scheme is selected, the base theme's hardcoded values apply.

## Requirements

- Python 3.8+ (standard library only, no dependencies)
- Style Settings plugin (for the scheme switcher UI)

## Verifying a build

After rebuilding, check that each scheme block is present:

```bash
grep -c "body.scheme-" theme.css
# Expected: ~1400+ (12 schemes x ~120 rules each)
```

Check that syntax tokens cover HTML/JSX:

```bash
grep "token.tag" theme.css | head -3
```
