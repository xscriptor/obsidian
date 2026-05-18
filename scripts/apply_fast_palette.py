#!/usr/bin/env python3
import argparse
import copy
import json
from pathlib import Path

from apply_palette import apply_config
from apply_quick_palette import build_font_config, hex_to_rgb, mix, rgb_to_hex, set_core, set_var


TITLE_STRENGTHS = {
    "h1": 1.00,
    "h2": 0.86,
    "h3": 0.72,
    "h4": 0.58,
    "h5": 0.44,
    "h6": 0.30,
    "italic": 0.52,
}

MUTED_RATIO = 0.28
FAINT_RATIO = 0.52


def get_var(items: list[dict], var_name: str) -> str:
    for item in items:
        if item["var"] == var_name:
            return item["value"]
    raise ValueError(f"Could not find variable `{var_name}`")


def invert_rgb_string(rgb_value: str) -> str:
    red, green, blue = [int(part.strip()) for part in rgb_value.split(",")]
    return rgb_to_hex((255 - red, 255 - green, 255 - blue))


def apply_fast_typography(base_config: dict, fast_config: dict) -> dict:
    config = copy.deepcopy(base_config)
    palette = config["palette"]
    light_mode = palette["light_mode"]
    dark_mode = palette["dark_mode"]

    light_background = invert_rgb_string(get_var(light_mode, "--background-primary-rgb"))
    dark_background = invert_rgb_string(get_var(dark_mode, "--background-primary-rgb"))

    light_emphasis = fast_config["typography"]["light_emphasis"]
    dark_emphasis = fast_config["typography"]["dark_emphasis"]

    light_normal = light_background
    dark_normal = dark_background

    light_base = get_var(light_mode, "--background-primary")
    dark_base_rgb = get_var(dark_mode, "--background-primary-rgb")
    dark_base = rgb_to_hex(tuple(int(part.strip()) for part in dark_base_rgb.split(",")))

    light_muted = mix(light_normal, light_base, MUTED_RATIO)
    dark_muted = mix(dark_normal, dark_base, MUTED_RATIO)
    light_faint = mix(light_normal, light_base, FAINT_RATIO)
    dark_faint = mix(dark_normal, dark_base, FAINT_RATIO)

    light_h1 = mix(light_normal, light_emphasis, TITLE_STRENGTHS["h1"])
    light_h2 = mix(light_normal, light_emphasis, TITLE_STRENGTHS["h2"])
    light_h3 = mix(light_normal, light_emphasis, TITLE_STRENGTHS["h3"])
    light_h4 = mix(light_normal, light_emphasis, TITLE_STRENGTHS["h4"])
    light_h5 = mix(light_normal, light_emphasis, TITLE_STRENGTHS["h5"])
    light_h6 = mix(light_normal, light_emphasis, TITLE_STRENGTHS["h6"])
    light_italic = mix(light_normal, light_emphasis, TITLE_STRENGTHS["italic"])

    dark_h1 = mix(dark_normal, dark_emphasis, TITLE_STRENGTHS["h1"])
    dark_h2 = mix(dark_normal, dark_emphasis, TITLE_STRENGTHS["h2"])
    dark_h3 = mix(dark_normal, dark_emphasis, TITLE_STRENGTHS["h3"])
    dark_h4 = mix(dark_normal, dark_emphasis, TITLE_STRENGTHS["h4"])
    dark_h5 = mix(dark_normal, dark_emphasis, TITLE_STRENGTHS["h5"])
    dark_h6 = mix(dark_normal, dark_emphasis, TITLE_STRENGTHS["h6"])
    dark_italic = mix(dark_normal, dark_emphasis, TITLE_STRENGTHS["italic"])

    set_var(light_mode, "--text-normal", light_normal)
    set_var(light_mode, "--text-muted", light_muted)
    set_var(light_mode, "--text-faint", light_faint)
    set_var(light_mode, "--text-accent", light_h2)
    set_var(light_mode, "--text-accent-hover", mix(light_h2, light_normal, 0.12))
    set_var(light_mode, "--interactive-accent", light_h2)
    set_var(light_mode, "--interactive-accent-hover", mix(light_h2, light_normal, 0.12))
    set_var(light_mode, "--h4-color", light_h4)
    set_var(light_mode, "--h5-color", light_h5)
    set_var(light_mode, "--h6-color", light_h6)
    set_var(light_mode, "--tag-text", light_h2)

    set_var(dark_mode, "--text-normal", dark_normal)
    set_var(dark_mode, "--text-muted", dark_muted)
    set_var(dark_mode, "--text-faint", dark_faint)
    set_var(dark_mode, "--text-accent", dark_h2)
    set_var(dark_mode, "--text-accent-hover", mix(dark_h2, dark_normal, 0.12))
    set_var(dark_mode, "--interactive-accent", dark_h2)
    set_var(dark_mode, "--interactive-accent-hover", mix(dark_h2, dark_normal, 0.12))
    set_var(dark_mode, "--h4-color", dark_h4)
    set_var(dark_mode, "--h5-color", dark_h5)
    set_var(dark_mode, "--h6-color", dark_h6)
    set_var(dark_mode, "--tag-text", dark_h2)

    set_core(palette["core_colors"], "accent", light_h2, dark_h2)
    set_core(palette["core_colors"], "heading_1", light_h1, dark_h1)
    set_core(palette["core_colors"], "heading_2", light_h2, dark_h2)
    set_core(palette["core_colors"], "heading_3", light_h3, dark_h3)
    set_core(palette["core_colors"], "italic", light_italic, dark_italic)

    config["font"] = build_font_config(fast_config["font"], config["font"])
    return config


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Aplica una jerarquia tipografica rapida usando solo dos colores de enfasis"
    )
    parser.add_argument("--fast-config", default="fast-palette.json", help="JSON corto de tipografia y fuente")
    parser.add_argument("--full-config", default="theme-palette.json", help="JSON completo que se reescribira")
    parser.add_argument("--input", default="theme.css", help="Archivo CSS de entrada")
    parser.add_argument("--output", default="theme.css", help="Archivo CSS de salida")
    parser.add_argument("--light-emphasis", help="Override directo del color tipografico de enfasis para modo claro")
    parser.add_argument("--dark-emphasis", help="Override directo del color tipografico de enfasis para modo oscuro")
    args = parser.parse_args()

    fast_path = Path(args.fast_config)
    full_path = Path(args.full_config)
    input_path = Path(args.input)
    output_path = Path(args.output)

    fast_config = json.loads(fast_path.read_text(encoding="utf-8"))
    if args.light_emphasis:
        fast_config["typography"]["light_emphasis"] = args.light_emphasis
    if args.dark_emphasis:
        fast_config["typography"]["dark_emphasis"] = args.dark_emphasis
    base_config = json.loads(full_path.read_text(encoding="utf-8"))
    full_config = apply_fast_typography(base_config, fast_config)

    full_path.write_text(json.dumps(full_config, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")

    css = input_path.read_text(encoding="utf-8")
    css = apply_config(css, full_config)
    output_path.write_text(css, encoding="utf-8")


if __name__ == "__main__":
    main()
