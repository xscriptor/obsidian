#!/usr/bin/env python3
import argparse
import copy
import json
from pathlib import Path

from apply_palette import apply_config


def clamp(value: float, minimum: float = 0, maximum: float = 255) -> int:
    return min(max(int(round(value)), int(minimum)), int(maximum))


def hex_to_rgb(color: str) -> tuple[int, int, int]:
    value = color.lstrip("#")
    if len(value) != 6:
        raise ValueError(f"Expected a 6-digit hex color, got `{color}`")
    return tuple(int(value[index:index + 2], 16) for index in (0, 2, 4))


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#" + "".join(f"{channel:02x}" for channel in rgb)


def rgb_to_string(rgb: tuple[int, int, int]) -> str:
    return f"{rgb[0]}, {rgb[1]}, {rgb[2]}"


def mix(color_a: str, color_b: str, ratio: float) -> str:
    rgb_a = hex_to_rgb(color_a)
    rgb_b = hex_to_rgb(color_b)
    mixed = tuple(
        clamp((rgb_a[index] * (1 - ratio)) + (rgb_b[index] * ratio))
        for index in range(3)
    )
    return rgb_to_hex(mixed)


def rgba(color: str, alpha: float) -> str:
    red, green, blue = hex_to_rgb(color)
    return f"rgba({red}, {green}, {blue}, {alpha})"


def update_item(items: list[dict], key_name: str, key_value: str, field_name: str, new_value: str) -> None:
    for item in items:
        if item[key_name] == key_value:
            item[field_name] = new_value
            return
    raise ValueError(f"Could not find `{key_value}` in `{key_name}`")


def set_var(items: list[dict], var_name: str, value: str) -> None:
    update_item(items, "var", var_name, "value", value)


def set_code(items: list[dict], code_name: str, value: str) -> None:
    update_item(items, "name", code_name, "value", value)


def set_core(core_colors: list[dict], name: str, light: str, dark: str) -> None:
    for item in core_colors:
        if item["name"] == name:
            item["light"] = light
            item["dark"] = dark
            return
    raise ValueError(f"Could not find core color `{name}`")


def build_font_config(short_font: dict, full_font: dict) -> dict:
    font = copy.deepcopy(full_font)
    font["family_name"] = short_font["family_name"]
    font["text_stack"] = short_font["text_stack"]
    font["interface_stack"] = short_font["interface_stack"]
    font["monospace_stack"] = short_font["monospace_stack"]

    keep_existing = short_font.get("keep_existing_base64", True)
    regular_path = short_font.get("regular_path", "").strip()
    italic_path = short_font.get("italic_path", "").strip()
    regular_base64 = short_font.get("regular_base64", "").strip()
    italic_base64 = short_font.get("italic_base64", "").strip()

    for face in font["faces"]:
        if face["label"] == "regular":
            face["source_path"] = regular_path
            face["source_base64"] = regular_base64
            face["keep_existing_base64"] = keep_existing and not regular_path and not regular_base64
        elif face["label"] == "italic":
            face["source_path"] = italic_path
            face["source_base64"] = italic_base64
            face["keep_existing_base64"] = keep_existing and not italic_path and not italic_base64

    return font


def apply_short_palette(base_config: dict, quick_config: dict) -> dict:
    config = copy.deepcopy(base_config)
    palette = config["palette"]
    light_mode = palette["light_mode"]
    dark_mode = palette["dark_mode"]
    code = palette["code"]
    core_colors = palette["core_colors"]

    colors = quick_config["colors"]
    backgrounds = quick_config["backgrounds"]

    accent_light = colors["accent_light"]
    accent_dark = colors["accent_dark"]
    heading_light = colors["heading_light"]
    heading_dark = colors["heading_dark"]
    support_light = colors["support_light"]
    support_dark = colors["support_dark"]
    warm_light = colors["warm_light"]
    warm_dark = colors["warm_dark"]

    light_base = backgrounds["light_base"]
    light_surface = backgrounds["light_surface"]
    dark_base = backgrounds["dark_base"]
    dark_surface = backgrounds["dark_surface"]

    light_alt = mix(light_base, light_surface, 0.35)
    light_secondary = mix(light_base, light_surface, 0.65)
    light_secondary_alt = mix(light_base, light_surface, 0.9)
    light_border = mix(light_base, accent_light, 0.08)
    light_border_hover = mix(light_base, accent_light, 0.12)
    light_border_focus = mix(light_base, accent_light, 0.18)
    light_divider = mix(light_base, accent_light, 0.06)
    light_hover = mix(light_base, accent_light, 0.03)
    light_note = mix(light_base, accent_light, 0.015)
    light_code_bg = mix(light_base, accent_light, 0.04)
    light_inline_bg = mix(light_surface, accent_light, 0.06)
    light_code_border = mix(light_base, accent_light, 0.12)

    dark_alt = mix(dark_base, dark_surface, 0.35)
    dark_secondary = mix(dark_base, dark_surface, 0.65)
    dark_secondary_alt = mix(dark_base, dark_surface, 0.9)
    dark_border = mix(dark_surface, accent_dark, 0.16)
    dark_border_hover = mix(dark_surface, accent_dark, 0.24)
    dark_border_focus = mix(dark_surface, accent_dark, 0.32)
    dark_divider = mix(dark_base, dark_surface, 0.8)
    dark_hover = mix(dark_surface, accent_dark, 0.08)
    dark_code_bg = mix(dark_base, accent_dark, 0.08)
    dark_inline_bg = mix(dark_surface, accent_dark, 0.06)
    dark_code_border = mix(dark_surface, accent_dark, 0.25)

    set_core(core_colors, "accent", accent_light, accent_dark)
    set_core(core_colors, "heading_1", heading_light, heading_dark)
    set_core(core_colors, "heading_2", accent_light, accent_dark)
    set_core(core_colors, "heading_3", support_light, support_dark)
    set_core(core_colors, "italic", warm_light, warm_dark)

    set_var(light_mode, "--background-opacity", "1")
    set_var(light_mode, "--background-primary-rgb", rgb_to_string(hex_to_rgb(light_base)))
    set_var(light_mode, "--background-secondary-rgb", rgb_to_string(hex_to_rgb(light_surface)))
    set_var(light_mode, "--background-primary", light_base)
    set_var(light_mode, "--background-primary-alt", light_alt)
    set_var(light_mode, "--background-secondary", light_secondary)
    set_var(light_mode, "--background-secondary-alt", light_secondary_alt)
    set_var(light_mode, "--background-accent", light_base)
    set_var(light_mode, "--background-modifier-border", light_border)
    set_var(light_mode, "--background-modifier-form-field", light_base)
    set_var(light_mode, "--background-modifier-form-field-highlighted", light_note)
    set_var(light_mode, "--text-accent", accent_light)
    set_var(light_mode, "--text-accent-hover", mix(accent_light, "#000000", 0.12))
    set_var(light_mode, "--h4-color", mix(heading_light, accent_light, 0.45))
    set_var(light_mode, "--h5-color", mix("#1f2937", accent_light, 0.18))
    set_var(light_mode, "--h6-color", mix("#64748b", accent_light, 0.12))
    set_var(light_mode, "--border-color", light_border)
    set_var(light_mode, "--border-color-hover", light_border_hover)
    set_var(light_mode, "--border-color-focus", light_border_focus)
    set_var(light_mode, "--divider-color", light_divider)
    set_var(light_mode, "--divider-color-hover", light_border_hover)
    set_var(light_mode, "--interactive-normal", light_base)
    set_var(light_mode, "--interactive-hover", light_hover)
    set_var(light_mode, "--interactive-accent", accent_light)
    set_var(light_mode, "--interactive-accent-hover", mix(accent_light, "#000000", 0.12))
    set_var(light_mode, "--callout-info", mix(light_base, accent_light, 0.08))
    set_var(light_mode, "--callout-info-border", accent_light)
    set_var(light_mode, "--callout-warning", mix(light_base, warm_light, 0.08))
    set_var(light_mode, "--callout-warning-border", warm_light)
    set_var(light_mode, "--callout-success", mix(light_base, support_light, 0.08))
    set_var(light_mode, "--callout-success-border", support_light)
    set_var(light_mode, "--callout-tip", mix(light_base, heading_light, 0.08))
    set_var(light_mode, "--callout-tip-border", heading_light)
    set_var(light_mode, "--callout-note", light_note)
    set_var(light_mode, "--tag-background", mix(light_base, accent_light, 0.08))
    set_var(light_mode, "--tag-text", mix(accent_light, "#000000", 0.06))
    set_var(light_mode, "--tag-border", mix(light_base, accent_light, 0.18))
    set_var(light_mode, "--table-header-background", light_note)
    set_var(light_mode, "--table-row-even", light_note)
    set_var(light_mode, "--table-border-color", light_border)
    set_var(light_mode, "--card-color", light_base)
    set_var(light_mode, "--select-color", light_base)
    set_var(light_mode, "--input-color", light_note)

    set_var(dark_mode, "--background-primary-rgb", rgb_to_string(hex_to_rgb(dark_base)))
    set_var(dark_mode, "--background-secondary-rgb", rgb_to_string(hex_to_rgb(dark_surface)))
    set_var(dark_mode, "--background-primary", rgba(dark_base, 0.8))
    set_var(dark_mode, "--background-primary-alt", rgba(dark_alt, 0.8))
    set_var(dark_mode, "--background-secondary", rgba(dark_secondary, 0.8))
    set_var(dark_mode, "--background-secondary-alt", rgba(dark_secondary_alt, 0.8))
    set_var(dark_mode, "--background-accent", rgba(dark_base, 0.8))
    set_var(dark_mode, "--background-modifier-border", dark_border)
    set_var(dark_mode, "--background-modifier-form-field", rgba(dark_base, 0.8))
    set_var(dark_mode, "--background-modifier-form-field-highlighted", rgba(dark_base, 0.8))
    set_var(dark_mode, "--text-accent", accent_dark)
    set_var(dark_mode, "--text-accent-hover", mix(accent_dark, "#ffffff", 0.22))
    set_var(dark_mode, "--h4-color", mix(accent_dark, support_dark, 0.35))
    set_var(dark_mode, "--h5-color", mix(heading_dark, warm_dark, 0.3))
    set_var(dark_mode, "--h6-color", mix("#94a3b8", accent_dark, 0.12))
    set_var(dark_mode, "--color-orange-rgb", rgb_to_string(hex_to_rgb(warm_dark)))
    set_var(dark_mode, "--color-yellow-rgb", rgb_to_string(hex_to_rgb(mix(warm_dark, "#facc15", 0.5))))
    set_var(dark_mode, "--color-green-rgb", rgb_to_string(hex_to_rgb(support_dark)))
    set_var(dark_mode, "--color-cyan-rgb", rgb_to_string(hex_to_rgb(mix(accent_dark, support_dark, 0.55))))
    set_var(dark_mode, "--color-blue-rgb", rgb_to_string(hex_to_rgb(accent_dark)))
    set_var(dark_mode, "--color-purple-rgb", rgb_to_string(hex_to_rgb(heading_dark)))
    set_var(dark_mode, "--table-border-color", dark_border)
    set_var(dark_mode, "--border-color", dark_border)
    set_var(dark_mode, "--border-color-hover", dark_border_hover)
    set_var(dark_mode, "--border-color-focus", dark_border_focus)
    set_var(dark_mode, "--divider-color", dark_divider)
    set_var(dark_mode, "--divider-color-hover", dark_border_hover)
    set_var(dark_mode, "--interactive-normal", rgba(dark_secondary, 0.88))
    set_var(dark_mode, "--interactive-hover", rgba(dark_hover, 0.92))
    set_var(dark_mode, "--interactive-accent", accent_dark)
    set_var(dark_mode, "--interactive-accent-hover", mix(accent_dark, "#ffffff", 0.22))
    set_var(dark_mode, "--callout-info", mix(dark_base, accent_dark, 0.12))
    set_var(dark_mode, "--callout-info-border", accent_dark)
    set_var(dark_mode, "--callout-warning", mix(dark_base, warm_dark, 0.12))
    set_var(dark_mode, "--callout-warning-border", warm_dark)
    set_var(dark_mode, "--callout-success", mix(dark_base, support_dark, 0.12))
    set_var(dark_mode, "--callout-success-border", support_dark)
    set_var(dark_mode, "--callout-tip", mix(dark_base, heading_dark, 0.15))
    set_var(dark_mode, "--callout-tip-border", heading_dark)
    set_var(dark_mode, "--tag-background", mix(dark_base, accent_dark, 0.16))
    set_var(dark_mode, "--tag-text", mix(accent_dark, "#ffffff", 0.2))
    set_var(dark_mode, "--tag-border", mix(dark_surface, accent_dark, 0.3))
    set_var(dark_mode, "--table-header-background", mix(dark_base, accent_dark, 0.08))
    set_var(dark_mode, "--table-row-even", mix(dark_base, dark_surface, 0.55))
    set_var(dark_mode, "--table-row-odd", dark_base)
    set_var(dark_mode, "--card-color", rgba(dark_base, 0.8))
    set_var(dark_mode, "--select-color", rgba(dark_base, 0.8))
    set_var(dark_mode, "--input-color", rgba(dark_alt, 0.8))

    set_code(code, "dark_block_background", dark_code_bg)
    set_code(code, "dark_inline_background", dark_inline_bg)
    set_code(code, "dark_code_text", "#e6edf3")
    set_code(code, "dark_code_border", dark_code_border)
    set_code(code, "light_block_background", light_code_bg)
    set_code(code, "light_inline_background", light_inline_bg)
    set_code(code, "light_code_text", "#1f2937")
    set_code(code, "light_code_border", light_code_border)
    set_code(code, "dark_cm_keyword", heading_dark)
    set_code(code, "dark_cm_string", mix(support_dark, "#ffffff", 0.15))
    set_code(code, "dark_cm_number", warm_dark)
    set_code(code, "dark_cm_bool", mix(accent_dark, "#ffffff", 0.12))
    set_code(code, "dark_cm_property", mix(accent_dark, "#ffffff", 0.2))
    set_code(code, "dark_cm_comment", "#6b7280")
    set_code(code, "light_cm_keyword", heading_light)
    set_code(code, "light_cm_string", support_light)
    set_code(code, "light_cm_number", warm_light)
    set_code(code, "light_cm_bool", accent_light)
    set_code(code, "light_cm_property", mix(support_light, accent_light, 0.4))
    set_code(code, "light_cm_comment", "#64748b")
    set_code(code, "javascript_code_bg", mix(dark_base, accent_dark, 0.12))
    set_code(code, "javascript_code_border", mix(dark_surface, accent_dark, 0.35))
    set_code(code, "python_code_bg", mix(dark_base, support_dark, 0.12))
    set_code(code, "python_code_border", mix(dark_surface, support_dark, 0.35))
    set_code(code, "css_code_bg", mix(dark_base, heading_dark, 0.14))
    set_code(code, "css_code_border", mix(dark_surface, heading_dark, 0.35))
    set_code(code, "html_code_bg", mix(dark_base, warm_dark, 0.14))
    set_code(code, "html_code_border", mix(dark_surface, warm_dark, 0.35))

    focus_shadows = palette["focus_shadows"]
    focus_shadows[0]["to"] = f"box-shadow: 0 0 0 2px {rgba(accent_dark, 0.25)};"
    focus_shadows[1]["to"] = f"box-shadow: 0 0 0 2px {rgba(accent_dark, 0.18)};"
    focus_shadows[2]["to"] = f"box-shadow: 0 0 0 2px {rgba(accent_light, 0.22)};"
    focus_shadows[3]["to"] = f"box-shadow: 0 0 0 2px {rgba(accent_light, 0.12)};"

    config["font"] = build_font_config(quick_config["font"], config["font"])
    return config


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Aplica una paleta corta y genera automaticamente la configuracion completa del tema"
    )
    parser.add_argument("--quick-config", default="quick-palette.json", help="JSON corto de colores y fuente")
    parser.add_argument("--full-config", default="theme-palette.json", help="JSON completo que se reescribira")
    parser.add_argument("--input", default="theme.css", help="Archivo CSS de entrada")
    parser.add_argument("--output", default="theme.css", help="Archivo CSS de salida")
    args = parser.parse_args()

    quick_path = Path(args.quick_config)
    full_path = Path(args.full_config)
    input_path = Path(args.input)
    output_path = Path(args.output)

    quick_config = json.loads(quick_path.read_text(encoding="utf-8"))
    base_config = json.loads(full_path.read_text(encoding="utf-8"))
    full_config = apply_short_palette(base_config, quick_config)

    full_path.write_text(json.dumps(full_config, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")

    css = input_path.read_text(encoding="utf-8")
    css = apply_config(css, full_config)
    output_path.write_text(css, encoding="utf-8")


if __name__ == "__main__":
    main()
