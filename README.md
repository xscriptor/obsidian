<h1 align="center">X Obsidian Theme Labs</h1>

<p align="center">Branch: <code>labs</code></p>
<p align="center"><a href="https://github.com/xscriptor/obsidian">github.com/xscriptor/obsidian</a></p>

<h2 align="center">Overview</h2>

This branch is a laboratory for building specialized Obsidian themes aimed at long-form writing, drafting, revision, and editorial workflows.

The goal is to keep experimentation reproducible: palettes and typography can be regenerated from small configuration files instead of manual CSS edits.

<h2 align="center">What’s In This Repo</h2>

- `theme.css`: the theme implementation (Obsidian app theme stylesheet)
- `manifest.json`: theme metadata for Obsidian
- `versions.json`: optional release compatibility mapping for Obsidian versions
- `docs/`: documentation and reference material
- `scripts/`: reproducible palette + typography generators

<h2 align="center">Core Ideas</h2>

- Writing-first UI decisions: fewer distractions, controlled contrast, stable hierarchy
- Typography-driven hierarchy: headings and emphasis communicate structure, not decoration
- Modern dark and clean light modes, tuned for long sessions
- Reproducibility: changes are defined in JSON and applied via scripts

<h2 align="center">Palette Workflows</h2>

This branch provides three levels of control:

1. Full control: edit the complete configuration and apply it.
2. Quick redesign: edit a short palette + font file, generate the full config automatically, apply it.
3. Typography-first: provide only two emphasis colors, compute the entire typographic hierarchy automatically, apply it.

<h2 align="center">Quick Start</h2>

All scripts use the Python standard library only. No virtual environment is required.

Run from the repository root:

```bash
python3 scripts/apply_palette.py --config theme-palette.json --input theme.css --output theme.css
```

```bash
python3 scripts/apply_quick_palette.py --quick-config quick-palette.json --full-config theme-palette.json --input theme.css --output theme.css
```

```bash
python3 scripts/apply_fast_palette.py --fast-config fast-palette.json --full-config theme-palette.json --input theme.css --output theme.css
```

<h2 align="center">Fonts</h2>

Fonts are embedded into `theme.css` as base64 to keep the theme self-contained.

Recommended workflow:

- Create a `fonts/` directory at the repository root.
- Place your `.woff2` files there.
- Point the JSON config to those file paths.

Example:

```text
fonts/
  YourFont-Regular.woff2
  YourFont-Italic.woff2
```

In `quick-palette.json` or `fast-palette.json`:

```json
{
  "font": {
    "regular_path": "fonts/YourFont-Regular.woff2",
    "italic_path": "fonts/YourFont-Italic.woff2",
    "keep_existing_base64": false
  }
}
```

If you want to keep the currently embedded font, set `keep_existing_base64` to `true`.

<h2 align="center">Obsidian Installation</h2>

To test locally:

1. Copy (or symlink) this theme folder into `.obsidian/themes/`.
2. In Obsidian, go to `Settings → Appearance → Themes` and select the theme.
3. After changing `theme.css`, reload the theme (or restart Obsidian) to ensure the UI refreshes.

<h2 align="center">Related Docs</h2>

- Full config workflow: [docs/apply-palette.md](./docs/apply-palette.md)
- Short config workflow: [docs/quick-palette.md](./docs/quick-palette.md)
- Typography-first workflow: [docs/fast-palette.md](./docs/fast-palette.md)

<h2 align="center">License</h2>

MIT License. See [LICENSE](./LICENSE).
