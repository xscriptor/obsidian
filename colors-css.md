# Colors → CSS

Documentación de mapeo desde paleta terminal ANSI (16 colores) a variables CSS de Obsidian.

---

## Paletas visuales por esquema

Cada bloque muestra los 16 colores ANSI + background + foreground del esquema.
Los 6 colores semánticos extraídos para el theme están marcados al final.

<style>
.color-swatch { display: inline-block; width: 32px; height: 32px; border-radius: 4px; border: 1px solid rgba(128,128,128,0.3); vertical-align: middle; margin: 1px; }
.color-swatch-sm { display: inline-block; width: 20px; height: 20px; border-radius: 3px; border: 1px solid rgba(128,128,128,0.2); vertical-align: middle; }
.scheme-block { background: var(--background-primary-alt, #f5f5f5); border-radius: 8px; padding: 12px 16px; margin: 12px 0; border: 1px solid var(--background-modifier-border, #ddd); }
.scheme-block h3 { margin-top: 0; }
.color-table { border-collapse: collapse; }
.color-table td { padding: 4px 8px; border: none; font-size: 0.85em; }
.code-label { font-family: monospace; font-size: 0.8em; color: var(--text-muted, #666); }
.semantic-row { background: rgba(128,128,128,0.08); }
</style>

### X (Dark)

<div class="scheme-block">

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#0a0a0a"></span> | <span class="color-swatch" style="background:#fc618d"></span> | <span class="color-swatch" style="background:#7bd88f"></span> | <span class="color-swatch" style="background:#fce566"></span> | <span class="color-swatch" style="background:#fd9353"></span> | <span class="color-swatch" style="background:#948ae3"></span> | <span class="color-swatch" style="background:#5ad4e6"></span> | <span class="color-swatch" style="background:#f7f1ff"></span> |
| **hex** | `#0a0a0a` | `#fc618d` | `#7bd88f` | `#fce566` | `#fd9353` | `#948ae3` | `#5ad4e6` | `#f7f1ff` |

| | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#0f0f0f"></span> | <span class="color-swatch" style="background:#fc618d"></span> | <span class="color-swatch" style="background:#7bd88f"></span> | <span class="color-swatch" style="background:#fce566"></span> | <span class="color-swatch" style="background:#fd9353"></span> | <span class="color-swatch" style="background:#948ae3"></span> | <span class="color-swatch" style="background:#5ad4e6"></span> | <span class="color-swatch" style="background:#f7f1ff"></span> |
| **hex** | `#0f0f0f` | `#fc618d` | `#7bd88f` | `#fce566` | `#fd9353` | `#948ae3` | `#5ad4e6` | `#f7f1ff` |

| Background | Foreground |
|---|---|
| <span class="color-swatch" style="background:#050505"></span> `#050505` | <span class="color-swatch" style="background:#f7f1ff"></span> `#f7f1ff` |

| Rol semántico | Color |
|---|---|
| <span class="color-swatch-sm" style="background:#fd9353"></span> **accent** (color4) | `#fd9353` |
| <span class="color-swatch-sm" style="background:#948ae3"></span> **heading** (color5) | `#948ae3` |
| <span class="color-swatch-sm" style="background:#7bd88f"></span> **support** (color2) | `#7bd88f` |
| <span class="color-swatch-sm" style="background:#fce566"></span> **warm** (color3) | `#fce566` |
| <span class="color-swatch-sm" style="background:#fc618d"></span> **error** (color1) | `#fc618d` |
| <span class="color-swatch-sm" style="background:#5ad4e6"></span> **info** (color6) | `#5ad4e6` |

</div>

### Madrid (Light)

<div class="scheme-block">

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#fafafa"></span> | <span class="color-swatch" style="background:#990026"></span> | <span class="color-swatch" style="background:#007a28"></span> | <span class="color-swatch" style="background:#8a6408"></span> | <span class="color-swatch" style="background:#007a9e"></span> | <span class="color-swatch" style="background:#4d2699"></span> | <span class="color-swatch" style="background:#007a9e"></span> | <span class="color-swatch" style="background:#1a1a1a"></span> |
| **hex** | `#fafafa` | `#990026` | `#007a28` | `#8a6408` | `#007a9e` | `#4d2699` | `#007a9e` | `#1a1a1a` |

| | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#4d4d4d"></span> | <span class="color-swatch" style="background:#990026"></span> | <span class="color-swatch" style="background:#007a28"></span> | <span class="color-swatch" style="background:#8a6408"></span> | <span class="color-swatch" style="background:#007a9e"></span> | <span class="color-swatch" style="background:#4d2699"></span> | <span class="color-swatch" style="background:#007a9e"></span> | <span class="color-swatch" style="background:#1a1a1a"></span> |
| **hex** | `#4d4d4d` | `#990026` | `#007a28` | `#8a6408` | `#007a9e` | `#4d2699` | `#007a9e` | `#1a1a1a` |

| Background | Foreground |
|---|---|
| <span class="color-swatch" style="background:#fafafa;border-color:#999"></span> `#fafafa` | <span class="color-swatch" style="background:#1a1a1a"></span> `#1a1a1a` |

| Rol semántico | Color |
|---|---|
| <span class="color-swatch-sm" style="background:#007a9e"></span> **accent** (color4) | `#007a9e` |
| <span class="color-swatch-sm" style="background:#4d2699"></span> **heading** (color5) | `#4d2699` |
| <span class="color-swatch-sm" style="background:#007a28"></span> **support** (color2) | `#007a28` |
| <span class="color-swatch-sm" style="background:#8a6408"></span> **warm** (color3) | `#8a6408` |

</div>

### Lahabana (Dark)

<div class="scheme-block">

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#19191a"></span> | <span class="color-swatch" style="background:#fc618d"></span> | <span class="color-swatch" style="background:#7bd88f"></span> | <span class="color-swatch" style="background:#e5ff9d"></span> | <span class="color-swatch" style="background:#fd9353"></span> | <span class="color-swatch" style="background:#948ae3"></span> | <span class="color-swatch" style="background:#5ad4e6"></span> | <span class="color-swatch" style="background:#f7f1ff"></span> |
| **hex** | `#19191a` | `#fc618d` | `#7bd88f` | `#e5ff9d` | `#fd9353` | `#948ae3` | `#5ad4e6` | `#f7f1ff` |

| | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#19191a"></span> | <span class="color-swatch" style="background:#fc618d"></span> | <span class="color-swatch" style="background:#7bd88f"></span> | <span class="color-swatch" style="background:#e5ff9d"></span> | <span class="color-swatch" style="background:#fd9353"></span> | <span class="color-swatch" style="background:#948ae3"></span> | <span class="color-swatch" style="background:#5ad4e6"></span> | <span class="color-swatch" style="background:#f7f1ff"></span> |
| **hex** | `#19191a` | `#fc618d` | `#7bd88f` | `#e5ff9d` | `#fd9353` | `#948ae3` | `#5ad4e6` | `#f7f1ff` |

| Background | Foreground |
|---|---|
| <span class="color-swatch" style="background:#19191a"></span> `#19191a` | <span class="color-swatch" style="background:#f7f1ff"></span> `#f7f1ff` |

| Rol semántico | Color |
|---|---|
| <span class="color-swatch-sm" style="background:#fd9353"></span> **accent** | `#fd9353` |
| <span class="color-swatch-sm" style="background:#948ae3"></span> **heading** | `#948ae3` |
| <span class="color-swatch-sm" style="background:#7bd88f"></span> **support** | `#7bd88f` |
| <span class="color-swatch-sm" style="background:#e5ff9d"></span> **warm** | `#e5ff9d` |

</div>

### Miami (Dark)

<div class="scheme-block">

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#000000"></span> | <span class="color-swatch" style="background:#FF4C8B"></span> | <span class="color-swatch" style="background:#7FFFD4"></span> | <span class="color-swatch" style="background:#FFD84C"></span> | <span class="color-swatch" style="background:#00FFA8"></span> | <span class="color-swatch" style="background:#D36CFF"></span> | <span class="color-swatch" style="background:#47CFFF"></span> | <span class="color-swatch" style="background:#f7f1ff"></span> |
| **hex** | `#000000` | `#FF4C8B` | `#7FFFD4` | `#FFD84C` | `#00FFA8` | `#D36CFF` | `#47CFFF` | `#f7f1ff` |

| | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#69676c"></span> | <span class="color-swatch" style="background:#FF4C8B"></span> | <span class="color-swatch" style="background:#7FFFD4"></span> | <span class="color-swatch" style="background:#FFD84C"></span> | <span class="color-swatch" style="background:#00FFA8"></span> | <span class="color-swatch" style="background:#D36CFF"></span> | <span class="color-swatch" style="background:#47CFFF"></span> | <span class="color-swatch" style="background:#f7f1ff"></span> |
| **hex** | `#69676c` | `#FF4C8B` | `#7FFFD4` | `#FFD84C` | `#00FFA8` | `#D36CFF` | `#47CFFF` | `#f7f1ff` |

| Background | Foreground |
|---|---|
| <span class="color-swatch" style="background:#000000"></span> `#000000` | <span class="color-swatch" style="background:#f7f1ff"></span> `#f7f1ff` |

| Rol semántico | Color |
|---|---|
| <span class="color-swatch-sm" style="background:#00FFA8"></span> **accent** | `#00FFA8` |
| <span class="color-swatch-sm" style="background:#D36CFF"></span> **heading** | `#D36CFF` |
| <span class="color-swatch-sm" style="background:#7FFFD4"></span> **support** | `#7FFFD4` |
| <span class="color-swatch-sm" style="background:#FFD84C"></span> **warm** | `#FFD84C` |

</div>

### Paris (Dark)

<div class="scheme-block">

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#1a0a30"></span> | <span class="color-swatch" style="background:#fc618d"></span> | <span class="color-swatch" style="background:#7bd88f"></span> | <span class="color-swatch" style="background:#fce566"></span> | <span class="color-swatch" style="background:#a3f3ff"></span> | <span class="color-swatch" style="background:#c4bdff"></span> | <span class="color-swatch" style="background:#a3f3ff"></span> | <span class="color-swatch" style="background:#1a0a30"></span> |
| **hex** | `#1a0a30` | `#fc618d` | `#7bd88f` | `#fce566` | `#a3f3ff` | `#c4bdff` | `#a3f3ff` | `#1a0a30` |

| | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#c4bdff"></span> | <span class="color-swatch" style="background:#fc618d"></span> | <span class="color-swatch" style="background:#7bd88f"></span> | <span class="color-swatch" style="background:#fce566"></span> | <span class="color-swatch" style="background:#a3f3ff"></span> | <span class="color-swatch" style="background:#c4bdff"></span> | <span class="color-swatch" style="background:#a3f3ff"></span> | <span class="color-swatch" style="background:#f7f1ff"></span> |
| **hex** | `#c4bdff` | `#fc618d` | `#7bd88f` | `#fce566` | `#a3f3ff` | `#c4bdff` | `#a3f3ff` | `#f7f1ff` |

| Background | Foreground |
|---|---|
| <span class="color-swatch" style="background:#1a0a30"></span> `#1a0a30` | <span class="color-swatch" style="background:#f7f1ff"></span> `#f7f1ff` |

| Rol semántico | Color |
|---|---|
| <span class="color-swatch-sm" style="background:#a3f3ff"></span> **accent** | `#a3f3ff` |
| <span class="color-swatch-sm" style="background:#c4bdff"></span> **heading** | `#c4bdff` |
| <span class="color-swatch-sm" style="background:#7bd88f"></span> **support** | `#7bd88f` |
| <span class="color-swatch-sm" style="background:#fce566"></span> **warm** | `#fce566` |

</div>

### Tokio (Dark)

<div class="scheme-block">

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#1c1c1d"></span> | <span class="color-swatch" style="background:#fc618d"></span> | <span class="color-swatch" style="background:#7bd88f"></span> | <span class="color-swatch" style="background:#fce566"></span> | <span class="color-swatch" style="background:#fd9353"></span> | <span class="color-swatch" style="background:#948ae3"></span> | <span class="color-swatch" style="background:#5ad4e6"></span> | <span class="color-swatch" style="background:#f7f1ff"></span> |
| **hex** | `#1c1c1d` | `#fc618d` | `#7bd88f` | `#fce566` | `#fd9353` | `#948ae3` | `#5ad4e6` | `#f7f1ff` |

| | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#1c1c1d"></span> | <span class="color-swatch" style="background:#fc618d"></span> | <span class="color-swatch" style="background:#7bd88f"></span> | <span class="color-swatch" style="background:#fce566"></span> | <span class="color-swatch" style="background:#fd9353"></span> | <span class="color-swatch" style="background:#948ae3"></span> | <span class="color-swatch" style="background:#5ad4e6"></span> | <span class="color-swatch" style="background:#f7f1ff"></span> |
| **hex** | `#1c1c1d` | `#fc618d` | `#7bd88f` | `#fce566` | `#fd9353` | `#948ae3` | `#5ad4e6` | `#f7f1ff` |

| Background | Foreground |
|---|---|
| <span class="color-swatch" style="background:#1c1c1d"></span> `#1c1c1d` | <span class="color-swatch" style="background:#f7f1ff"></span> `#f7f1ff` |

| Rol semántico | Color |
|---|---|
| <span class="color-swatch-sm" style="background:#fd9353"></span> **accent** | `#fd9353` |
| <span class="color-swatch-sm" style="background:#948ae3"></span> **heading** | `#948ae3` |
| <span class="color-swatch-sm" style="background:#7bd88f"></span> **support** | `#7bd88f` |
| <span class="color-swatch-sm" style="background:#fce566"></span> **warm** | `#fce566` |

</div>

### Oslo (Dark)

<div class="scheme-block">

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#3f4451"></span> | <span class="color-swatch" style="background:#e05561"></span> | <span class="color-swatch" style="background:#8cc265"></span> | <span class="color-swatch" style="background:#d18f52"></span> | <span class="color-swatch" style="background:#4aa5f0"></span> | <span class="color-swatch" style="background:#c162de"></span> | <span class="color-swatch" style="background:#42b3c2"></span> | <span class="color-swatch" style="background:#e6e6e6"></span> |
| **hex** | `#3f4451` | `#e05561` | `#8cc265` | `#d18f52` | `#4aa5f0` | `#c162de` | `#42b3c2` | `#e6e6e6` |

| | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#4f5666"></span> | <span class="color-swatch" style="background:#ff616e"></span> | <span class="color-swatch" style="background:#a5e075"></span> | <span class="color-swatch" style="background:#f0a45d"></span> | <span class="color-swatch" style="background:#4dc4ff"></span> | <span class="color-swatch" style="background:#de73ff"></span> | <span class="color-swatch" style="background:#4cd1e0"></span> | <span class="color-swatch" style="background:#ffffff"></span> |
| **hex** | `#4f5666` | `#ff616e` | `#a5e075` | `#f0a45d` | `#4dc4ff` | `#de73ff` | `#4cd1e0` | `#ffffff` |

| Background | Foreground |
|---|---|
| <span class="color-swatch" style="background:#3f4451"></span> `#3f4451` | <span class="color-swatch" style="background:#abb2bf"></span> `#abb2bf` |

| Rol semántico | Color |
|---|---|
| <span class="color-swatch-sm" style="background:#4aa5f0"></span> **accent** | `#4aa5f0` |
| <span class="color-swatch-sm" style="background:#c162de"></span> **heading** | `#c162de` |
| <span class="color-swatch-sm" style="background:#8cc265"></span> **support** | `#8cc265` |
| <span class="color-swatch-sm" style="background:#d18f52"></span> **warm** | `#d18f52` |

</div>

### Helsinki (Light)

<div class="scheme-block">

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#f8fafe;border-color:#999"></span> | <span class="color-swatch" style="background:#1faa9e"></span> | <span class="color-swatch" style="background:#733d9a"></span> | <span class="color-swatch" style="background:#2e70ad"></span> | <span class="color-swatch" style="background:#b55a0f"></span> | <span class="color-swatch" style="background:#3e9d21"></span> | <span class="color-swatch" style="background:#bd4c3d"></span> | <span class="color-swatch" style="background:#544d40"></span> |
| **hex** | `#f8fafe` | `#1faa9e` | `#733d9a` | `#2e70ad` | `#b55a0f` | `#3e9d21` | `#bd4c3d` | `#544d40` |

| | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#b0a999"></span> | <span class="color-swatch" style="background:#009e91"></span> | <span class="color-swatch" style="background:#5a1f8a"></span> | <span class="color-swatch" style="background:#0f5ba2"></span> | <span class="color-swatch" style="background:#b23b00"></span> | <span class="color-swatch" style="background:#218c00"></span> | <span class="color-swatch" style="background:#b32e1f"></span> | <span class="color-swatch" style="background:#000000"></span> |
| **hex** | `#b0a999` | `#009e91` | `#5a1f8a` | `#0f5ba2` | `#b23b00` | `#218c00` | `#b32e1f` | `#000000` |

| Background | Foreground |
|---|---|
| <span class="color-swatch" style="background:#f8fafe;border-color:#999"></span> `#f8fafe` | <span class="color-swatch" style="background:#544d40"></span> `#544d40` |

| Rol semántico | Color |
|---|---|
| <span class="color-swatch-sm" style="background:#b55a0f"></span> **accent** | `#b55a0f` |
| <span class="color-swatch-sm" style="background:#3e9d21"></span> **heading** | `#3e9d21` |
| <span class="color-swatch-sm" style="background:#733d9a"></span> **support** | `#733d9a` |
| <span class="color-swatch-sm" style="background:#2e70ad"></span> **warm** | `#2e70ad` |

</div>

### Berlin (Dark) — Grayscale

<div class="scheme-block">

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#000000"></span> | <span class="color-swatch" style="background:#999999"></span> | <span class="color-swatch" style="background:#bbbbbb"></span> | <span class="color-swatch" style="background:#dddddd"></span> | <span class="color-swatch" style="background:#888888"></span> | <span class="color-swatch" style="background:#aaaaaa"></span> | <span class="color-swatch" style="background:#cccccc"></span> | <span class="color-swatch" style="background:#ffffff"></span> |
| **hex** | `#000000` | `#999999` | `#bbbbbb` | `#dddddd` | `#888888` | `#aaaaaa` | `#cccccc` | `#ffffff` |

| | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#333333"></span> | <span class="color-swatch" style="background:#bbbbbb"></span> | <span class="color-swatch" style="background:#dddddd"></span> | <span class="color-swatch" style="background:#ffffff"></span> | <span class="color-swatch" style="background:#aaaaaa"></span> | <span class="color-swatch" style="background:#cccccc"></span> | <span class="color-swatch" style="background:#eeeeee"></span> | <span class="color-swatch" style="background:#ffffff"></span> |
| **hex** | `#333333` | `#bbbbbb` | `#dddddd` | `#ffffff` | `#aaaaaa` | `#cccccc` | `#eeeeee` | `#ffffff` |

| Background | Foreground |
|---|---|
| <span class="color-swatch" style="background:#000000"></span> `#000000` | <span class="color-swatch" style="background:#cccccc"></span> `#cccccc` |

| Rol semántico | Color |
|---|---|
| <span class="color-swatch-sm" style="background:#888888"></span> **accent** | `#888888` |
| <span class="color-swatch-sm" style="background:#aaaaaa"></span> **heading** | `#aaaaaa` |
| <span class="color-swatch-sm" style="background:#bbbbbb"></span> **support** | `#bbbbbb` |
| <span class="color-swatch-sm" style="background:#dddddd"></span> **warm** | `#dddddd` |

</div>

### London (Light) — Grayscale

<div class="scheme-block">

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#ffffff;border-color:#999"></span> | <span class="color-swatch" style="background:#333333"></span> | <span class="color-swatch" style="background:#444444"></span> | <span class="color-swatch" style="background:#555555"></span> | <span class="color-swatch" style="background:#666666"></span> | <span class="color-swatch" style="background:#777777"></span> | <span class="color-swatch" style="background:#888888"></span> | <span class="color-swatch" style="background:#333333"></span> |
| **hex** | `#ffffff` | `#333333` | `#444444` | `#555555` | `#666666` | `#777777` | `#888888` | `#333333` |

| | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#333333"></span> | <span class="color-swatch" style="background:#444444"></span> | <span class="color-swatch" style="background:#555555"></span> | <span class="color-swatch" style="background:#666666"></span> | <span class="color-swatch" style="background:#777777"></span> | <span class="color-swatch" style="background:#888888"></span> | <span class="color-swatch" style="background:#999999"></span> | <span class="color-swatch" style="background:#aaaaaa"></span> |
| **hex** | `#333333` | `#444444` | `#555555` | `#666666` | `#777777` | `#888888` | `#999999` | `#aaaaaa` |

| Background | Foreground |
|---|---|
| <span class="color-swatch" style="background:#ffffff;border-color:#999"></span> `#ffffff` | <span class="color-swatch" style="background:#333333"></span> `#333333` |

| Rol semántico | Color |
|---|---|
| <span class="color-swatch-sm" style="background:#666666"></span> **accent** | `#666666` |
| <span class="color-swatch-sm" style="background:#777777"></span> **heading** | `#777777` |
| <span class="color-swatch-sm" style="background:#444444"></span> **support** | `#444444` |
| <span class="color-swatch-sm" style="background:#555555"></span> **warm** | `#555555` |

</div>

### Praha (Dark)

<div class="scheme-block">

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#1A1A1A"></span> | <span class="color-swatch" style="background:#FF5555"></span> | <span class="color-swatch" style="background:#B8E6A0"></span> | <span class="color-swatch" style="background:#FFE4A3"></span> | <span class="color-swatch" style="background:#BD93F9"></span> | <span class="color-swatch" style="background:#FF9AA2"></span> | <span class="color-swatch" style="background:#8BE9FD"></span> | <span class="color-swatch" style="background:#FFFFFF"></span> |
| **hex** | `#1A1A1A` | `#FF5555` | `#B8E6A0` | `#FFE4A3` | `#BD93F9` | `#FF9AA2` | `#8BE9FD` | `#FFFFFF` |

| | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#6272A4"></span> | <span class="color-swatch" style="background:#FF6E6E"></span> | <span class="color-swatch" style="background:#B8E6A0"></span> | <span class="color-swatch" style="background:#FFE4A3"></span> | <span class="color-swatch" style="background:#D6ACFF"></span> | <span class="color-swatch" style="background:#FF9AA2"></span> | <span class="color-swatch" style="background:#A4FFFF"></span> | <span class="color-swatch" style="background:#FFFFFF"></span> |
| **hex** | `#6272A4` | `#FF6E6E` | `#B8E6A0` | `#FFE4A3` | `#D6ACFF` | `#FF9AA2` | `#A4FFFF` | `#FFFFFF` |

| Background | Foreground |
|---|---|
| <span class="color-swatch" style="background:#1A1A1A"></span> `#1A1A1A` | <span class="color-swatch" style="background:#FFFFFF"></span> `#FFFFFF` |

| Rol semántico | Color |
|---|---|
| <span class="color-swatch-sm" style="background:#BD93F9"></span> **accent** | `#BD93F9` |
| <span class="color-swatch-sm" style="background:#FF9AA2"></span> **heading** | `#FF9AA2` |
| <span class="color-swatch-sm" style="background:#B8E6A0"></span> **support** | `#B8E6A0` |
| <span class="color-swatch-sm" style="background:#FFE4A3"></span> **warm** | `#FFE4A3` |

</div>

### Bogota (Dark)

<div class="scheme-block">

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#200b0a"></span> | <span class="color-swatch" style="background:#fc618d"></span> | <span class="color-swatch" style="background:#7bd88f"></span> | <span class="color-swatch" style="background:#ffed89"></span> | <span class="color-swatch" style="background:#47e6ff"></span> | <span class="color-swatch" style="background:#ff9999"></span> | <span class="color-swatch" style="background:#47e6ff"></span> | <span class="color-swatch" style="background:#f7f1ff"></span> |
| **hex** | `#200b0a` | `#fc618d` | `#7bd88f` | `#ffed89` | `#47e6ff` | `#ff9999` | `#47e6ff` | `#f7f1ff` |

| | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| <span class="code-label">color</span> | <span class="color-swatch" style="background:#525053"></span> | <span class="color-swatch" style="background:#fc618d"></span> | <span class="color-swatch" style="background:#7bd88f"></span> | <span class="color-swatch" style="background:#ffed89"></span> | <span class="color-swatch" style="background:#47e6ff"></span> | <span class="color-swatch" style="background:#ff9999"></span> | <span class="color-swatch" style="background:#47e6ff"></span> | <span class="color-swatch" style="background:#f7f1ff"></span> |
| **hex** | `#525053` | `#fc618d` | `#7bd88f` | `#ffed89` | `#47e6ff` | `#ff9999` | `#47e6ff` | `#f7f1ff` |

| Background | Foreground |
|---|---|
| <span class="color-swatch" style="background:#200b0a"></span> `#200b0a` | <span class="color-swatch" style="background:#f7f1ff"></span> `#f7f1ff` |

| Rol semántico | Color |
|---|---|
| <span class="color-swatch-sm" style="background:#47e6ff"></span> **accent** | `#47e6ff` |
| <span class="color-swatch-sm" style="background:#ff9999"></span> **heading** | `#ff9999` |
| <span class="color-swatch-sm" style="background:#7bd88f"></span> **support** | `#7bd88f` |
| <span class="color-swatch-sm" style="background:#ffed89"></span> **warm** | `#ffed89` |

</div>

---

## Mapping: Terminal → CSS variable de Obsidian

| ANSI | Uso en CSS |
|------|------------|
| `color0` | Fondo base oscuro (`--color-base-00`) |
| `color1` | Rojo, error (`--color-red`) |
| `color2` | Verde, success, strings (`--color-green`, `--cm-string`) |
| `color3` | Amarillo, warning (`--color-yellow`, `--cm-attribute`) |
| `color4` | **Acento principal** (`--accent-color`, `--text-accent`, `--color-blue`) |
| `color5` | **Headings**, púrpura (`--h1-color`, `--color-purple`, `--cm-keyword`) |
| `color6` | Cian, info (`--color-cyan`, `--cm-bool`) |
| `color7` | Texto claro sobre acento (`--text-on-accent`) |
| `color8` | Gris medio, texto faint (`--text-faint`) |
| `color9` | Rosa brillante (`--color-pink`) |
| `color10` | Verde brillante |
| `color11` | Amarillo brillante |
| `color12` | Azul brillante |
| `color13` | Púrpura brillante |
| `color14` | Cian brillante |
| `color15` | Blanco/brillo máximo |
| `background` | `--background-primary` |
| `foreground` | `--text-normal` |

## Derivación de variables

Cada esquema genera ~80 variables CSS agrupadas así:

```
Core:        --accent-color, --h1-color, --h2-color, --h3-color, --italic-color
Backgrounds: --background-primary, primary-alt, secondary, secondary-alt, accent
Text:        --text-normal, text-muted, text-faint, text-accent, text-on-accent
Borders:     --border-color, border-color-hover/focus, divider-color
Interactive: --interactive-normal, hover, accent, accent-hover, success
Callouts:    --callout-info, warning, error, success, tip, note (bg + border + text)
Tags:        --tag-background, tag-text, tag-border
Highlights:  --highlight-yellow, green, blue, pink, purple
Tables:      --table-header-background, row-even, row-odd, border-color
Code:        --cm-keyword, cm-string, cm-number, cm-bool, cm-property, cm-comment
```
