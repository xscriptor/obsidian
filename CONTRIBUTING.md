# Contributing

Thanks for considering contributing to Xscriptor.

## How to contribute

### Report bugs

Open an issue at https://github.com/xscriptor/obsidian/issues with:

- Your Obsidian version
- The theme version
- Steps to reproduce
- Screenshots if applicable

### Suggest features

Open an issue with the "enhancement" label describing what you would like to see
and why it would be useful.

### Submit changes

1. Fork the repository.
2. Create a branch from `labs` for development work.
3. Make your changes.
4. Test with Obsidian (copy `theme.css` to your vault's theme folder).
5. Submit a pull request against the `labs` branch.

## Development notes

- The theme is built from `colors.md` using `scripts/build_unified.py`.
- Run `python3 scripts/build_unified.py` to regenerate `theme.css`.
- Keep changes reproducible: modify the palette files, not the generated CSS.
