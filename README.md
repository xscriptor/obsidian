# x

`x` is a theme variation focused on reading, writing, and editorial work inside Obsidian. It keeps EB Garamond as its typographic base, while replacing the original colorful palette with parchment, ink, wine, bronze, and sage tones.

![Preview](./docs/preview/preview01.jpg)

## Focus
- A more restrained, literary palette for long reading sessions
- Warm contrast in both light and dark mode
- Code blocks that feel less neon and closer to ink on paper
- Folder accents that are muted instead of highly saturated
- Compatibility with the existing Style Settings and pseudo mica effect

## How Obsidian Themes Work
- Obsidian loads themes from a folder inside `.obsidian/themes/`
- An app theme requires at minimum `theme.css` and `manifest.json`
- `theme.css` contains CSS variables and visual rules for the interface
- `manifest.json` defines the theme name, version, author, and minimum Obsidian version
- `versions.json` maps theme versions to compatible Obsidian versions when you publish releases

## Repository Structure
- `theme.css`: palette, typography, components, and settings exposed to Style Settings
- `manifest.json`: theme metadata
- `versions.json`: version compatibility
- `docs/preview/`: reference screenshots

## Palette Workflows
- Full palette workflow: [apply-palette.md](./docs/apply-palette.md)
- Short palette workflow: [quick-palette.md](./docs/quick-palette.md)
- Typography-first workflow: [fast-palette.md](./docs/fast-palette.md)

## Changes In This Iteration
- The documented variant was renamed to `x`
- Base variables were adjusted in `:root`, `.theme-light`, and `.theme-dark`
- Bright accents were replaced with a warm editorial palette
- File explorer folder colors were softened
- The color treatment for inline code, code blocks, and tokens was reworked

## Manual Installation
- Copy this repository into `.obsidian/themes/`
- Select the theme from `Settings -> Appearance`
- If you plan to publish this variant as `x`, also align the folder name and `manifest.json` with that name, since Obsidian expects them to match

## Previews
- Mobile
<p align="center">
  <img src="./docs/preview/preview02.jpg" width="200" alt="Obsidian x Mobile Theme Dark Mode"/>
  <img src="./docs/preview/preview03.jpg" width="200" alt="Obsidian x Mobile Theme Dark Mode"/>
  <img src="./docs/preview/preview04.jpg" width="200" alt="Obsidian x Mobile Theme Light Mode"/>
  <img src="./docs/preview/preview05.jpg" width="200" alt="Obsidian x Mobile Theme Light Mode"/>
</p>

- Desktop
<p align="center">
  <img src="./docs/preview/preview06.png" width="700" alt="Obsidian x Desktop Theme Dark Mode"/>
  <img src="./docs/preview/preview07.png" width="700" alt="Obsidian x Desktop Theme Dark Mode"/>
</p>

## References
- Official theme documentation: [Build a theme](https://docs.obsidian.md/Themes/App+themes/Build+a+theme)
- Obsidian CSS variables: [About styling](https://docs.obsidian.md/Reference/CSS+variables/About+styling)
- Migration guide and best practices: [1.0 Theme migration guide](https://obsidian.md/blog/1-0-theme-migration-guide/)
- Official template: [obsidian-sample-theme](https://github.com/obsidianmd/obsidian-sample-theme)

## License
[MIT License](LICENSE)

## Credits
Typography: EB Garamond, licensed under the SIL Open Font License 1.1.
