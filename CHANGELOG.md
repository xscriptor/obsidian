# Changelog

## 2.0.0

- 12 built-in color schemes (city-themed), switchable via Style Settings
- Each scheme controls backgrounds, text, headings, accent, callouts, tags, syntax highlighting (~60 token types), per-language code block tints, folder borders (5 nesting levels), and Graph View node colors
- Style Settings class-select dropdown for scheme switching
- Background opacity respects the Style Settings slider across all schemes
- Folder colors derived from the active scheme palette (no hardcoded vintage tones)
- Comprehensive syntax token coverage for CM6 editor and Prism preview modes
- Per-language code block tinting (javascript, python, css, html, json, markdown, bash)
- Graph View variables per scheme (graph-text, graph-line, graph-node, graph-node-unresolved, graph-node-focused, graph-node-tag, graph-node-attachment)
- File explorer background now matches the active scheme
- Subtle nav dividers using scheme-aware border colors
- Scripts for reproducible palette generation (scripts/build_unified.py)
- Documentation: reproducible-color-schemes.md, colors-css.md (visual reference with swatches)

## 1.0.0

- Initial release
- EB Garamond typography
- Light and dark mode
- Pseudo Mica (frosted glass) effect
- Style Settings integration
- Folder color borders
- Per-language code block backgrounds
