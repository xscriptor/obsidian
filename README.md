# X Obsidian Theme Labs

Branch: `labs`

This branch is a laboratory for building specialized Obsidian themes aimed at long-form writing, drafting, revision, and editorial workflows.

The goal is to keep experimentation reproducible: palettes and typography can be regenerated from small configuration files instead of manual CSS edits.

## Features

- 12 built-in color schemes (city-themed), switchable via Style Settings
- Each scheme controls ~120 CSS declarations across all UI elements
- Per-language code block tinting follows the active scheme
- Folder colors adapt to each scheme's palette
- Graph View colors match the active scheme
- Pseudo Mica (frosted glass) effect
- EB Garamond typography throughout
- Full light and dark mode support

## What's In This Repo

- `theme.css`: unified theme with 12 scheme overrides embedded
- `manifest.json`: theme metadata for Obsidian
- `versions.json`: release compatibility mapping
- `colors.md`: source palettes (16-color terminal format + bg + fg)
- `colors-css.md`: visual reference with color swatches and CSS mapping
- `scripts/`
  - `build_unified.py`: generates theme.css from colors.md
  - `apply_palette.py`, `apply_quick_palette.py`, `apply_fast_palette.py`: individual palette generators
- `docs/`: documentation and reference material

## Quick Start

### For users

1. Install the [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) plugin.
2. Copy the theme folder into `.obsidian/themes/X/`.
3. In Obsidian, go to Settings > Appearance > Themes and select **X**.
4. Go to Settings > Style Settings and pick a scheme from the dropdown.

### For developers

```bash
# Regenerate theme.css from colors.md (adds/modifies schemes)
cp theme.css theme.css.bak && python3 scripts/build_unified.py

# Copy to vault for testing
cp theme.css /path/to/vault/.obsidian/themes/X/theme.css
```

Python 3.8+ required (standard library only, no dependencies).

## Color Schemes

| #  | Name | Mode | Background |
|----|------|------|------------|
| 1  | X | Dark | `#050505` |
| 2  | Madrid | Light | `#fafafa` |
| 3  | Lahabana | Dark | `#19191a` |
| 4  | Miami | Dark | `#000000` |
| 5  | Paris | Dark | `#1a0a30` |
| 6  | Tokio | Dark | `#1c1c1d` |
| 7  | Oslo | Dark | `#3f4451` |
| 8  | Helsinki | Light | `#f8fafe` |
| 9  | Berlin | Dark | `#000000` |
| 10 | London | Light | `#ffffff` |
| 11 | Praha | Dark | `#1a1a1a` |
| 12 | Bogota | Dark | `#200b0a` |

Each scheme controls: backgrounds, text, accent, headings, borders, interactive elements, callouts, tags, highlights, tables, syntax highlighting (~30 CM6 + ~28 Prism tokens), per-language code block tints, folder borders (5 nesting levels), and Graph View node colors.

## Docs

- [Reproducible color schemes](./docs/reproducible-color-schemes.md) -- how to add, modify, or understand the scheme system
- [Full config workflow](./docs/apply-palette.md)
- [Short config workflow](./docs/quick-palette.md)
- [Typography-first workflow](./docs/fast-palette.md)

## License

MIT License. See [LICENSE](./LICENSE).
