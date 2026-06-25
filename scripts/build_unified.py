#!/usr/bin/env python3
"""
Build unified theme.css from colors.md palettes.

Parses all 12 terminal color schemes from colors.md, maps each to
Obsidian CSS variables, and generates a unified theme.css with
Style Settings class-select for switching between schemes.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLORS_MD = ROOT / "colors.md"
THEME_CSS = ROOT / "theme.css"


# ── Color utilities ──────────────────────────────────────────────

def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb: tuple[float, float, float]) -> str:
    return "#" + "".join(f"{max(0, min(255, round(c))):02x}" for c in rgb)


def mix(a: str, b: str, ratio: float) -> str:
    ra, ga, ba = hex_to_rgb(a)
    rb, gb, bb = hex_to_rgb(b)
    return rgb_to_hex((
        ra * (1 - ratio) + rb * ratio,
        ga * (1 - ratio) + gb * ratio,
        ba * (1 - ratio) + bb * ratio,
    ))


def lighten(h: str, amount: float) -> str:
    r, g, b = hex_to_rgb(h)
    return rgb_to_hex((
        r + (255 - r) * amount,
        g + (255 - g) * amount,
        b + (255 - b) * amount,
    ))


def darken(h: str, amount: float) -> str:
    r, g, b = hex_to_rgb(h)
    return rgb_to_hex((
        r * (1 - amount),
        g * (1 - amount),
        b * (1 - amount),
    ))


def alpha(h: str, a: float | str) -> str:
    r, g, b = hex_to_rgb(h)
    return f"rgba({r}, {g}, {b}, {a})"


def rgb_str(h: str) -> str:
    r, g, b = hex_to_rgb(h)
    return f"{r}, {g}, {b}"


def is_light(hex_color: str) -> bool:
    r, g, b = hex_to_rgb(hex_color)
    return (r * 0.299 + g * 0.587 + b * 0.114) > 128


# ── Parse colors.md ──────────────────────────────────────────────

def parse_schemes(text: str) -> list[dict]:
    """Extract all terminal palettes from colors.md."""
    schemes = []
    for match in re.finditer(
        r'<h2[^>]*>(.*?)</h2>\s*```json\s*\n(.*?)\n```',
        text, re.S
    ):
        name = match.group(1).strip()
        data = json.loads(match.group(2))
        schemes.append({
            "name": name,
            "id": name.lower().replace(" ", "-"),
            "colors": [data[f"color{i}"] for i in range(16)],
            "background": data["background"],
            "foreground": data["foreground"],
        })
    return schemes


# ── Derive CSS variables per scheme ──────────────────────────────

def derive_scheme_vars(scheme: dict) -> str:
    """Generate CSS variable override block for one scheme."""
    c = scheme["colors"]
    bg = scheme["background"]
    fg = scheme["foreground"]
    sid = scheme["id"]
    light_mode = is_light(bg)
    mode_class = ".theme-light" if light_mode else ".theme-dark"
    selector = f"body.scheme-{sid}{mode_class}"

    accent = c[4]
    heading = c[5]
    warm = c[3]
    support = c[2]
    error_red = c[1]
    cyan_info = c[6]

    op_var = "var(--background-opacity, 0.8)"

    if light_mode:
        bg_alt = darken(bg, 0.02)
        bg_sec = darken(bg, 0.04)
        bg_sec_alt = darken(bg, 0.07)
        border = mix(bg, accent, 0.12)
        border_hover = mix(bg, accent, 0.18)
        border_focus = mix(bg, accent, 0.25)
        divider = mix(bg, accent, 0.06)
        divider_hover = mix(bg, accent, 0.12)
        interactive_normal = bg
        interactive_hover = mix(bg, accent, 0.04)
        note_bg = mix(bg, accent, 0.015)
        code_bg = mix(bg, accent, 0.04)
        inline_bg = mix(bg_sec, accent, 0.06)
        code_border = mix(bg, accent, 0.12)
        op = "1"
    else:
        bg_alt = lighten(bg, 0.03)
        bg_sec = lighten(bg, 0.06)
        bg_sec_alt = lighten(bg, 0.10)
        border = "#2a2a2a"
        border_hover = "#3a3a3a"
        border_focus = "#4b5563"
        divider = "#26262b"
        divider_hover = "#3a3a3a"
        interactive_normal = alpha(bg_sec, 0.88)
        interactive_hover = alpha(mix(bg_sec, accent, 0.08), 0.92)
        note_bg = mix(bg, accent, 0.06)
        code_bg = mix(bg, accent, 0.08)
        inline_bg = mix(bg_sec, accent, 0.06)
        code_border = mix(bg_sec, accent, 0.25)
        op = "0.8"

    if light_mode:
        text_normal = fg
        text_muted = mix(fg, bg, 0.35)
        text_faint = mix(fg, bg, 0.55)
        text_on_accent = "#ffffff"
    else:
        text_normal = fg
        text_muted = mix(fg, bg, 0.30)
        text_faint = mix(fg, bg, 0.50)
        text_on_accent = "#000000"

    text_accent = accent
    text_accent_hover = lighten(accent, 0.12) if light_mode else mix(accent, "#ffffff", 0.18)
    h1 = heading
    h2 = mix(warm, accent, 0.5)
    h3 = support
    h4 = cyan_info
    h5 = mix(text_normal, accent, 0.35) if light_mode else mix(text_normal, heading, 0.35)
    h6 = mix(text_faint, accent, 0.15) if light_mode else mix(text_faint, heading, 0.12)
    interactive_accent = accent
    interactive_accent_hover = lighten(accent, 0.10) if light_mode else mix(accent, "#ffffff", 0.18)

    callout_info = mix(bg, accent, 0.08) if light_mode else mix(bg, accent, 0.12)
    callout_info_border = accent
    callout_info_text = lighten(accent, 0.25) if light_mode else mix(accent, "#ffffff", 0.15)
    callout_warning = mix(bg, warm, 0.08) if light_mode else mix(bg, warm, 0.12)
    callout_warning_border = warm
    callout_warning_text = lighten(warm, 0.25) if light_mode else mix(warm, "#ffffff", 0.25)
    callout_error = mix(bg, error_red, 0.08) if light_mode else mix(bg, error_red, 0.12)
    callout_error_border = error_red
    callout_error_text = lighten(error_red, 0.30) if light_mode else mix(error_red, "#ffffff", 0.20)
    callout_success = mix(bg, support, 0.08) if light_mode else mix(bg, support, 0.12)
    callout_success_border = support
    callout_success_text = lighten(support, 0.20) if light_mode else mix(support, "#ffffff", 0.20)
    callout_tip = mix(bg, heading, 0.08) if light_mode else mix(bg, heading, 0.12)
    callout_tip_border = heading
    callout_tip_text = lighten(heading, 0.20) if light_mode else mix(heading, "#ffffff", 0.18)
    callout_note = note_bg
    callout_note_border = mix(bg, text_muted, 0.5)
    callout_note_text = text_muted

    tag_bg = callout_info
    tag_text = mix(accent, text_normal, 0.1) if light_mode else mix(accent, "#ffffff", 0.15)
    tag_border = mix(bg, accent, 0.20) if light_mode else mix(bg_sec, accent, 0.30)

    highlight_yellow = mix(bg, warm, 0.25) if light_mode else mix("#4b3b15", warm, 0.15)
    highlight_green = mix(bg, support, 0.25) if light_mode else "#123524"
    highlight_blue = mix(bg, accent, 0.25) if light_mode else "#172554"
    highlight_pink = mix(bg, error_red, 0.20) if light_mode else "#4a1d3f"
    highlight_purple = mix(bg, heading, 0.20) if light_mode else "#312e81"

    table_header = note_bg
    table_even = note_bg
    table_odd = bg
    table_border = border
    card = bg if light_mode else alpha(bg, 0.8)
    select_color = bg if light_mode else alpha(bg, 0.8)
    input_color = note_bg if light_mode else alpha(bg_alt, 0.8)

    if not light_mode:
        bg_mod_error = mix(bg, error_red, 0.25)
        bg_mod_error_hover = mix(bg_mod_error, error_red, 0.25)
        bg_mod_success = mix(bg, support, 0.25)
    else:
        bg_mod_error = mix("#fee2e2", error_red, 0.05)
        bg_mod_error_hover = mix(bg_mod_error, error_red, 0.08)
        bg_mod_success = mix("#d4edda", support, 0.05)

    lines = [f"{selector} {{"]
    lines.append(f"  --accent-color: {accent};")
    lines.append(f"  --h1-color: {h1};")
    lines.append(f"  --h2-color: {h2};")
    lines.append(f"  --h3-color: {h3};")
    lines.append(f"  --italic-color: {cyan_info};")
    lines.append(f"  --background-opacity: {op};")
    lines.append(f"  --background-primary-rgb: {rgb_str(bg)};")
    lines.append(f"  --background-secondary-rgb: {rgb_str(bg_sec)};")

    if light_mode:
        lines.append(f"  --background-primary: {bg};")
        lines.append(f"  --background-primary-alt: {bg_alt};")
        lines.append(f"  --background-secondary: {bg_sec};")
        lines.append(f"  --background-secondary-alt: {bg_sec_alt};")
        lines.append(f"  --background-accent: {bg};")
        lines.append(f"  --background-modifier-form-field: {bg};")
        lines.append(f"  --background-modifier-form-field-highlighted: {note_bg};")
    else:
        lines.append(f"  --background-primary: {alpha(bg, op_var)};")
        lines.append(f"  --background-primary-alt: {alpha(bg_alt, op_var)};")
        lines.append(f"  --background-secondary: {alpha(bg_sec, op_var)};")
        lines.append(f"  --background-secondary-alt: {alpha(bg_sec_alt, op_var)};")
        lines.append(f"  --background-accent: {alpha(bg, op_var)};")
        lines.append(f"  --background-modifier-form-field: {alpha('#000000', op_var)};")
        lines.append(f"  --background-modifier-form-field-highlighted: {alpha(bg, op_var)};")

    lines.append(f"  --background-modifier-border: {border};")
    lines.append(f"  --background-modifier-box-shadow: {'rgba(15, 23, 42, 0.08)' if light_mode else 'rgba(0, 0, 0, 0.32)'};")
    lines.append(f"  --background-modifier-success: {bg_mod_success};")
    lines.append(f"  --background-modifier-error: {bg_mod_error};")
    lines.append(f"  --background-modifier-error-rgb: {rgb_str(bg_mod_error)};")
    lines.append(f"  --background-modifier-error-hover: {bg_mod_error_hover};")
    lines.append(f"  --background-modifier-cover: {'rgba(15, 23, 42, 0.5)' if light_mode else 'rgba(0, 0, 0, 0.9)'};")
    lines.append(f"  --text-normal: {text_normal};")
    lines.append(f"  --text-muted: {text_muted};")
    lines.append(f"  --text-faint: {text_faint};")
    lines.append(f"  --text-accent: {text_accent};")
    lines.append(f"  --text-accent-hover: {text_accent_hover};")
    lines.append(f"  --text-on-accent: {text_on_accent};")
    lines.append(f"  --text-error: {error_red};")
    lines.append(f"  --text-warning: {warm};")
    lines.append(f"  --text-success: {support};")
    lines.append(f"  --h4-color: {h4};")
    lines.append(f"  --h5-color: {h5};")
    lines.append(f"  --h6-color: {h6};")

    if not light_mode:
        lines.append(f"  --color-red-rgb: {rgb_str(error_red)};")
        lines.append(f"  --color-orange-rgb: {rgb_str(warm)};")
        lines.append(f"  --color-yellow-rgb: {rgb_str(mix(warm, '#facc15', 0.5))};")
        lines.append(f"  --color-green-rgb: {rgb_str(support)};")
        lines.append(f"  --color-cyan-rgb: {rgb_str(cyan_info)};")
        lines.append(f"  --color-blue-rgb: {rgb_str(accent)};")
        lines.append(f"  --color-purple-rgb: {rgb_str(heading)};")
        lines.append(f"  --color-pink-rgb: {rgb_str(error_red)};")

    lines.append(f"  --border-color: {border};")
    lines.append(f"  --border-color-hover: {border_hover};")
    lines.append(f"  --border-color-focus: {border_focus};")
    lines.append(f"  --divider-color: {divider};")
    lines.append(f"  --divider-color-hover: {divider_hover};")
    lines.append(f"  --interactive-normal: {interactive_normal};")
    lines.append(f"  --interactive-hover: {interactive_hover};")
    lines.append(f"  --interactive-accent: {interactive_accent};")
    lines.append(f"  --interactive-accent-hover: {interactive_accent_hover};")
    lines.append(f"  --interactive-success: {support};")
    lines.append(f"  --callout-info: {callout_info};")
    lines.append(f"  --callout-info-border: {callout_info_border};")
    lines.append(f"  --callout-info-text: {callout_info_text};")
    lines.append(f"  --callout-warning: {callout_warning};")
    lines.append(f"  --callout-warning-border: {callout_warning_border};")
    lines.append(f"  --callout-warning-text: {callout_warning_text};")
    lines.append(f"  --callout-error: {callout_error};")
    lines.append(f"  --callout-error-border: {callout_error_border};")
    lines.append(f"  --callout-error-text: {callout_error_text};")
    lines.append(f"  --callout-success: {callout_success};")
    lines.append(f"  --callout-success-border: {callout_success_border};")
    lines.append(f"  --callout-success-text: {callout_success_text};")
    lines.append(f"  --callout-tip: {callout_tip};")
    lines.append(f"  --callout-tip-border: {callout_tip_border};")
    lines.append(f"  --callout-tip-text: {callout_tip_text};")
    lines.append(f"  --callout-note: {callout_note};")
    lines.append(f"  --callout-note-border: {callout_note_border};")
    lines.append(f"  --callout-note-text: {callout_note_text};")
    lines.append(f"  --tag-background: {tag_bg};")
    lines.append(f"  --tag-text: {tag_text};")
    lines.append(f"  --tag-border: {tag_border};")
    lines.append(f"  --highlight-yellow: {highlight_yellow};")
    lines.append(f"  --highlight-green: {highlight_green};")
    lines.append(f"  --highlight-blue: {highlight_blue};")
    lines.append(f"  --highlight-pink: {highlight_pink};")
    lines.append(f"  --highlight-purple: {highlight_purple};")
    lines.append(f"  --table-header-background: {table_header};")
    lines.append(f"  --table-row-even: {table_even};")
    lines.append(f"  --table-row-odd: {table_odd};")
    lines.append(f"  --table-border-color: {table_border};")
    lines.append(f"  --card-color: {card};")
    lines.append(f"  --select-color: {select_color};")
    lines.append(f"  --input-color: {input_color};")
    # Graph View colors derived from scheme
    lines.append(f"  --graph-text: {text_normal};")
    lines.append(f"  --graph-line: {mix(fg, bg, 0.45)};")
    lines.append(f"  --graph-node: {accent};")
    lines.append(f"  --graph-node-unresolved: {mix(fg, bg, 0.35)};")
    lines.append(f"  --graph-node-focused: {heading};")
    lines.append(f"  --graph-node-tag: {warm};")
    lines.append(f"  --graph-node-attachment: {support};")
    lines.append("}")
    # Force file explorer background to match scheme (base CSS excludes it via :not())
    lines.append("")
    if light_mode:
        lines.append(f"{selector} .workspace-leaf-content[data-type=\"file-explorer\"] {{")
        lines.append(f"  background-color: {bg_sec} !important;")
        lines.append("}")
    else:
        lines.append(f"{selector} .workspace-leaf-content[data-type=\"file-explorer\"] {{")
        lines.append(f"  background-color: {alpha(bg_sec, op_var)} !important;")
        lines.append("}")
    return "\n".join(lines)


def derive_folder_colors(scheme: dict) -> str:
    """Generate folder color borders derived from scheme's palette."""
    c = scheme["colors"]
    bg = scheme["background"]
    sid = scheme["id"]
    light_mode = is_light(bg)
    mode_class = ".theme-light" if light_mode else ".theme-dark"
    base_sel = f"body.scheme-{sid}{mode_class}"

    accent = c[4]
    heading = c[5]
    support = c[2]
    warm = c[3]
    error_red = c[1]
    cyan_info = c[6]

    # Generate 8 L1 colors by cycling through semantic colors + mixes
    l1 = [
        error_red,                            # 1: red/coral
        cyan_info,                            # 2: cyan
        lighten(accent, 0.15) if light_mode else mix(accent, "#ffffff", 0.15),  # 3: accent lighter
        warm,                                 # 4: warm
        heading,                              # 5: heading
        mix(support, cyan_info, 0.5),         # 6: support-cyan mix
        mix(accent, warm, 0.5),               # 7: accent-warm mix
        support,                              # 8: support
    ]

    l2 = [
        heading, mix(accent, bg, 0.3), warm, support,
        mix(cyan_info, bg, 0.3), mix(error_red, bg, 0.3), mix(heading, bg, 0.3),
    ]

    l3 = [
        accent, heading, support, warm, mix(accent, bg, 0.3), cyan_info,
    ]

    l4 = [
        mix(accent, bg, 0.3), mix(support, bg, 0.3),
        mix(warm, bg, 0.3), mix(heading, bg, 0.3), mix(cyan_info, bg, 0.3),
    ]

    l5 = [
        mix(accent, bg, 0.25), mix(heading, bg, 0.25), mix(support, bg, 0.25),
    ]

    lines = [f"/* ── Folder colors for {scheme['name']} ── */"]

    # Level 1 (main folders)
    for idx, col in enumerate(l1):
        n = idx + 1
        lines.append(f"{base_sel} .nav-files-container > div > .nav-folder:nth-child(8n+{n}) > .tree-item-self {{")
        lines.append(f"  border-left: 3px solid {col} !important;")
        lines.append("}")
        lines.append(f"{base_sel} .nav-files-container > div > .nav-folder:nth-child(8n+{n}) .tree-item-children {{")
        lines.append(f"  --nav-indentation-guide-color: {col};")
        lines.append(f"  border-left-color: {col} !important;")
        lines.append("}")

    # Level 2
    count = len(l2)
    for idx, col in enumerate(l2):
        n = idx + 1
        lines.append(f"{base_sel} .nav-files-container .nav-folder-children .nav-folder:nth-child({count}n+{n}) > .tree-item-self {{")
        lines.append(f"  border-left: 2px solid {col} !important;")
        lines.append("}")
        lines.append(f"{base_sel} .nav-files-container .nav-folder-children .nav-folder:nth-child({count}n+{n}) .tree-item-children {{")
        lines.append(f"  --nav-indentation-guide-color: {col};")
        lines.append(f"  border-left-color: {col} !important;")
        lines.append("}")

    # Level 3
    count = len(l3)
    for idx, col in enumerate(l3):
        n = idx + 1
        lines.append(f"{base_sel} .nav-files-container .nav-folder-children .nav-folder-children .nav-folder:nth-child({count}n+{n}) > .tree-item-self {{")
        lines.append(f"  border-left: 2px solid {col} !important;")
        lines.append("}")
        lines.append(f"{base_sel} .nav-files-container .nav-folder-children .nav-folder-children .nav-folder:nth-child({count}n+{n}) .tree-item-children {{")
        lines.append(f"  --nav-indentation-guide-color: {col};")
        lines.append(f"  border-left-color: {col} !important;")
        lines.append("}")

    # Level 4
    count = len(l4)
    for idx, col in enumerate(l4):
        n = idx + 1
        lines.append(f"{base_sel} .nav-files-container .nav-folder-children .nav-folder-children .nav-folder-children .nav-folder:nth-child({count}n+{n}) > .tree-item-self {{")
        lines.append(f"  border-left: 1px solid {col} !important;")
        lines.append("}")
        lines.append(f"{base_sel} .nav-files-container .nav-folder-children .nav-folder-children .nav-folder-children .nav-folder:nth-child({count}n+{n}) .tree-item-children {{")
        lines.append(f"  --nav-indentation-guide-color: {col};")
        lines.append(f"  border-left-color: {col} !important;")
        lines.append("}")

    # Level 5+
    count = len(l5)
    for idx, col in enumerate(l5):
        n = idx + 1
        lines.append(f"{base_sel} .nav-files-container .nav-folder-children .nav-folder-children .nav-folder-children .nav-folder-children .nav-folder:nth-child({count}n+{n}) > .tree-item-self {{")
        lines.append(f"  border-left: 1px solid {col} !important;")
        lines.append("}")
        lines.append(f"{base_sel} .nav-files-container .nav-folder-children .nav-folder-children .nav-folder-children .nav-folder-children .nav-folder:nth-child({count}n+{n}) .tree-item-children {{")
        lines.append(f"  --nav-indentation-guide-color: {col};")
        lines.append(f"  border-left-color: {col} !important;")
        lines.append("}")

    # Active file highlight
    lines.append("")
    lines.append(f"{base_sel} .nav-file-title.is-active {{")
    lines.append(f"  background-color: {alpha(accent, 0.18)} !important;")
    lines.append("}")

    return "\n".join(lines)


def derive_syntax_vars(scheme: dict) -> str:
    """Generate comprehensive token + code block overrides for one scheme."""
    c = scheme["colors"]
    bg = scheme["background"]
    fg = scheme["foreground"]
    sid = scheme["id"]
    light_mode = is_light(bg)
    mode_class = ".theme-light" if light_mode else ".theme-dark"
    base_sel = f"body.scheme-{sid}{mode_class}"
    plain_sel = f"body.scheme-{sid}"

    # Semantic colors
    keyword_col = c[5]     # color5 → purple/heading
    string_col = c[2]      # color2 → green/support (strings in code)
    number_col = c[4]      # color4 → accent (numbers)
    bool_col = c[6]        # color6 → cyan/info (booleans)
    prop_col = c[4]        # color4 → accent (properties)
    comment_col = mix(fg, bg, 0.55)
    accent = c[4]
    warm = c[3]
    support = c[2]
    heading = c[5]
    error_red = c[1]

    # Derived token colors
    tag_col = heading           # HTML tags like <div>, <h2>
    attr_col = support          # HTML attributes like className, href
    punctuation_col = mix(fg, bg, 0.45)  # brackets, parens
    operator_col = mix(fg, bg, 0.35)     # =, =>, etc.
    function_col = heading      # function names
    variable_col = fg           # variables
    builtin_col = support       # built-in objects
    type_col = heading          # types/classes
    bracket_col = mix(fg, bg, 0.45)  # < > { }
    meta_col = mix(fg, bg, 0.30)     # meta/doctype
    def_col = heading           # function definitions

    lines = [
        f"/* ── Syntax tokens for {scheme['name']} ── */",
        "",
        f"/* CM6 editor tokens */",
        f"{base_sel} .cm-keyword      {{ color: {keyword_col}; }}",
        f"{base_sel} .cm-string       {{ color: {string_col}; }}",
        f"{base_sel} .cm-string-2     {{ color: {string_col}; }}",
        f"{base_sel} .cm-number       {{ color: {number_col}; }}",
        f"{base_sel} .cm-atom,",
        f"{base_sel} .cm-bool         {{ color: {bool_col}; }}",
        f"{base_sel} .cm-property     {{ color: {prop_col}; }}",
        f"{base_sel} .cm-comment      {{ color: {comment_col}; }}",
        f"{base_sel} .cm-operator     {{ color: {operator_col}; }}",
        f"{base_sel} .cm-meta         {{ color: {meta_col}; }}",
        f"{base_sel} .cm-def          {{ color: {def_col}; }}",
        f"{base_sel} .cm-variable     {{ color: {variable_col}; }}",
        f"{base_sel} .cm-variable-2   {{ color: {mix(fg, bg, 0.20)}; }}",
        f"{base_sel} .cm-variable-3   {{ color: {mix(fg, bg, 0.35)}; }}",
        f"{base_sel} .cm-attribute    {{ color: {attr_col}; }}",
        f"{base_sel} .cm-tag          {{ color: {tag_col}; }}",
        f"{base_sel} .cm-bracket      {{ color: {bracket_col}; }}",
        f"{base_sel} .cm-builtin      {{ color: {builtin_col}; }}",
        f"{base_sel} .cm-type         {{ color: {type_col}; }}",
        f"{base_sel} .cm-qualifier    {{ color: {accent}; }}",
        f"{base_sel} .cm-error        {{ color: {error_red}; }}",
        "",
        f"/* Prism preview tokens */",
    ]

    # Prism token mapping
    prism_tokens = {
        "token.keyword": keyword_col,
        "token.string": string_col,
        "token.number": number_col,
        "token.boolean": bool_col,
        "token.property": prop_col,
        "token.comment": comment_col,
        "token.prolog": comment_col,
        "token.doctype": comment_col,
        "token.cdata": comment_col,
        "token.punctuation": punctuation_col,
        "token.tag": tag_col,
        "token.attr-name": attr_col,
        "token.attr-value": string_col,
        "token.selector": support,
        "token.char": string_col,
        "token.builtin": builtin_col,
        "token.operator": operator_col,
        "token.entity": operator_col,
        "token.url": string_col,
        "token.atrule": keyword_col,
        "token.function": function_col,
        "token.class-name": type_col,
        "token.regex": number_col,
        "token.important": error_red,
        "token.variable": variable_col,
        "token.constant": number_col,
        "token.symbol": number_col,
        "token.inserted": support,
        "token.deleted": error_red,
    }

    for token, color in prism_tokens.items():
        lines.append(f"{base_sel} .markdown-rendered code[class*=\"language-\"] .{token} {{ color: {color}; }}")

    # Generic code block backgrounds
    if light_mode:
        code_block_bg = mix(bg, accent, 0.04)
        code_inline_bg = mix(bg, accent, 0.06)
        code_border = mix(bg, accent, 0.12)
    else:
        code_block_bg = mix(bg, accent, 0.08)
        code_inline_bg = mix(bg, accent, 0.06)
        code_border = mix(bg, accent, 0.25)

    lines.extend([
        "",
        f"/* Code block backgrounds for {scheme['name']} */",
        f"{base_sel} .markdown-rendered pre,",
        f"{base_sel} .markdown-rendered pre code {{",
        f"  background: {code_block_bg} !important;",
        f"  color: {fg} !important;",
        f"  border: 1px solid {code_border} !important;",
        "}",
        "",
        f"{base_sel} .markdown-rendered code:not([class*=\"language-\"]) {{",
        f"  background: {code_inline_bg} !important;",
        f"  color: {fg} !important;",
        f"  border: 1px solid {code_border} !important;",
        "}",
    ])

    # Beat !important rules in base CSS for code/pre elements
    lines.append("")
    lines.append(f"{plain_sel} code {{")
    lines.append(f"  background-color: {code_inline_bg} !important;")
    lines.append(f"  border-color: {code_border} !important;")
    lines.append("}")
    lines.append("")
    lines.append(f"{plain_sel} pre {{")
    lines.append(f"  background-color: {code_block_bg} !important;")
    lines.append(f"  border-color: {code_border} !important;")
    lines.append("}")

    # Per-language code block tints
    lang_map = {
        "language-javascript": warm,
        "language-js": warm,
        "language-python": support,
        "language-py": support,
        "language-css": heading,
        "language-html": warm,
        "language-json": support,
        "language-markdown": heading,
        "language-md": heading,
        "language-bash": accent,
        "language-shell": accent,
        "language-sh": accent,
    }

    if light_mode:
        lang_opacity_bg = 0.06
        lang_opacity_bd = 0.18
    else:
        lang_opacity_bg = 0.12
        lang_opacity_bd = 0.35

    lines.append("")
    lines.append(f"/* Per-language code block tints for {scheme['name']} */")

    for lang, tint_color in lang_map.items():
        lines.append(f"{base_sel} .{lang} pre {{")
        lines.append(f"  background-color: {alpha(tint_color, lang_opacity_bg)} !important;")
        lines.append(f"  border-color: {alpha(tint_color, lang_opacity_bd)} !important;")
        lines.append("}")
        lines.append("")

    if lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines)


# ── Generate Style Settings block ────────────────────────────────

def generate_settings_block(schemes: list[dict]) -> str:
    x = next(s for s in schemes if s["id"] == "x")
    x_c = x["colors"]
    x_bg = x["background"]
    x_fg = x["foreground"]

    x_light = is_light(x_bg)
    accent_l = x_c[4]
    accent_d = x_c[4]
    h1_l = x_c[5]
    h1_d = x_c[5]
    h2_l = mix(x_c[3], x_c[4], 0.5)
    h2_d = mix(x_c[3], x_c[4], 0.5)
    h3_l = x_c[2]
    h3_d = x_c[2]
    italic_l = x_c[6]
    italic_d = x_c[6]

    options_lines = []
    for s in schemes:
        mode = "Light" if is_light(s["background"]) else "Dark"
        options_lines.append(
            f"            -\n"
            f"                label: '{s['name']} ({mode})'\n"
            f"                value: scheme-{s['id']}"
        )

    options_str = "\n".join(options_lines)

    return f"""/* @settings

name: Xscriptor Settings
id: xscriptor
settings:
    -
        id: scheme
        title: Esquema de color
        description: Cambia entre los 12 esquemas de color disponibles
        type: class-select
        allowEmpty: false
        default: scheme-x
        options:
{options_str}
    -
        id: transparency
        title: Transparencia
        type: heading
        level: 2
        collapsed: true
    -
        id: background-opacity
        title: Opacidad del fondo
        description: Controla la transparencia de la aplicación
        type: variable-number-slider
        default: 0.8
        min: 0.1
        max: 1
        step: 0.1
        format:
    -
        id: mica-effect
        title: Efecto Pseudo Mica
        description: Habilita el efecto de vidrio esmerilado (requiere fondo translúcido)
        type: variable-toggle
        default: true
    -
        id: blur-intensity
        title: Intensidad del desenfoque
        description: Controla la intensidad del efecto de desenfoque
        type: variable-number-slider
        default: 20
        min: 5
        max: 50
        step: 5
        format: px
    -
        id: colors
        title: Colores
        type: heading
        level: 2
        collapsed: true
    -
        id: accent-color
        title: Color de acento
        description: Color principal del tema
        type: variable-themed-color
        opacity: true
        format: hex
        default-light: '{accent_l.lstrip("#")}'
        default-dark: '{accent_d.lstrip("#")}'
    -
        id: h1-color
        title: Color de títulos H1
        type: variable-themed-color
        format: hex
        default-light: '{h1_l.lstrip("#")}'
        default-dark: '{h1_d.lstrip("#")}'
    -
        id: h2-color
        title: Color de títulos H2
        type: variable-themed-color
        format: hex
        default-light: '{h2_l.lstrip("#")}'
        default-dark: '{h2_d.lstrip("#")}'
    -
        id: h3-color
        title: Color de títulos H3
        type: variable-themed-color
        format: hex
        default-light: '{h3_l.lstrip("#")}'
        default-dark: '{h3_d.lstrip("#")}'
    -
        id: italic-color
        title: Color de texto en cursiva
        type: variable-themed-color
        format: hex
        default-light: '{italic_l.lstrip("#")}'
        default-dark: '{italic_d.lstrip("#")}'
    -
        id: typography
        title: Tipografía
        type: heading
        level: 2
        collapsed: true
    -
        id: font-size
        title: Tamaño de fuente
        description: Tamaño base de la fuente
        type: variable-number-slider
        default: 16
        min: 12
        max: 24
        step: 1
        format: px
    -
        id: line-height
        title: Altura de línea
        description: Espaciado entre líneas
        type: variable-number-slider
        default: 1.6
        min: 1.2
        max: 2.0
        step: 0.1
        format:
    -
        id: interface
        title: Interfaz
        type: heading
        level: 2
        collapsed: true
    -
        id: border-radius
        title: Radio de bordes
        description: Redondez de los elementos
        type: variable-number-slider
        default: 8
        min: 0
        max: 20
        step: 1
        format: px
    -
        id: folder-colors
        title: Colores de carpetas
        description: Habilitar colores en las carpetas
        type: class-toggle
        default: true

*/"""


# ── Main build ───────────────────────────────────────────────────

def build() -> None:
    colors_text = COLORS_MD.read_text(encoding="utf-8")
    schemes = parse_schemes(colors_text)
    print(f"Found {len(schemes)} schemes: {[s['name'] for s in schemes]}")

    css = THEME_CSS.read_text(encoding="utf-8")

    # Replace @settings block
    new_settings = generate_settings_block(schemes)
    css = re.sub(r'/\* @settings\n.*?\*/', new_settings, css, count=1, flags=re.S)

    # Append scheme overrides for all 12 schemes
    parts = [css.rstrip(), "",
             "/* ================================================================",
             "   SCHEME OVERRIDES",
             "   Each block activates when the corresponding scheme is selected",
             "   via Style Settings (class-select toggle on <body>).",
             "   ================================================================ */", ""]

    for scheme in schemes:
        print(f"  Generating: {scheme['name']} ({scheme['id']})")
        parts.append(f"/* ── {scheme['name']} ── */")
        parts.append(derive_scheme_vars(scheme))
        parts.append("")
        parts.append(derive_folder_colors(scheme))
        parts.append("")
        parts.append(derive_syntax_vars(scheme))
        parts.append("")

    output = "\n".join(parts)
    THEME_CSS.write_text(output, encoding="utf-8")
    total_size = len(output)
    line_count = output.count("\n") + 1
    print(f"\nDone! theme.css updated ({total_size} bytes, ~{line_count} lines)")


if __name__ == "__main__":
    build()
