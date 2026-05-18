#!/usr/bin/env python3
import argparse
import base64
import json
import re
from pathlib import Path


ROOT_START = ":root {"
ROOT_END = "\n}\n\n/* ================================================================="
LIGHT_START = ".theme-light {"
LIGHT_END = "\n}\n\n/* Estilos específicos para modo claro */"
DARK_START = ".theme-dark {"
DARK_END = "\n}\n\n/* Estilos específicos para modo oscuro */"


def replace_decl(text: str, selector: str, prop: str, value: str, count: int = 1) -> str:
    pattern = re.compile(
        rf"({re.escape(selector)}\s*\{{[^}}]*?{re.escape(prop)}:\s*)[^;]+(;)",
        re.S,
    )
    new_text, replacements = pattern.subn(lambda m: f"{m.group(1)}{value}{m.group(2)}", text, count=count)
    if replacements == 0:
        raise ValueError(f"No se pudo actualizar `{prop}` en el selector `{selector}`")
    return new_text


def replace_region_var(
    text: str,
    start_marker: str,
    end_marker: str,
    var_name: str,
    first_value: str,
    rest_value: str | None = None,
) -> str:
    start = text.find(start_marker)
    if start == -1:
        raise ValueError(f"No se encontro el bloque que empieza con: {start_marker}")
    end = text.find(end_marker, start)
    if end == -1:
        raise ValueError(f"No se encontro el final del bloque: {end_marker}")

    region = text[start:end]
    pattern = re.compile(rf"(^\s*{re.escape(var_name)}:\s*)[^;]+;", re.M)
    matches = list(pattern.finditer(region))
    if not matches:
        raise ValueError(f"No se encontro la variable `{var_name}` dentro del bloque esperado")

    replacement_values = [first_value]
    if rest_value is None:
        replacement_values.extend([first_value] * (len(matches) - 1))
    else:
        replacement_values.extend([rest_value] * (len(matches) - 1))

    replacement_iter = iter(replacement_values)
    region = pattern.sub(lambda m: f"{m.group(1)}{next(replacement_iter)};", region)
    return text[:start] + region + text[end:]


def replace_setting_defaults(text: str, setting_id: str, light_value: str, dark_value: str) -> str:
    lines = text.splitlines(keepends=True)
    start_idx = None

    for index, line in enumerate(lines):
        if line.strip() == f"id: {setting_id}":
            start_idx = index
            break

    if start_idx is None:
        raise ValueError(f"No se pudieron actualizar los defaults de Style Settings para `{setting_id}`")

    end_idx = len(lines)
    for index in range(start_idx + 1, len(lines)):
        stripped = lines[index].strip()
        if stripped == "-" or stripped == "*/":
            end_idx = index
            break

    light_count = 0
    dark_count = 0
    for index in range(start_idx, end_idx):
        stripped = lines[index].strip()
        if stripped.startswith("default-light:"):
            indent = lines[index][: len(lines[index]) - len(lines[index].lstrip())]
            lines[index] = f"{indent}default-light: '{light_value}'\n"
            light_count += 1
        elif stripped.startswith("default-dark:"):
            indent = lines[index][: len(lines[index]) - len(lines[index].lstrip())]
            lines[index] = f"{indent}default-dark: '{dark_value}'\n"
            dark_count += 1

    if light_count == 0 or dark_count == 0:
        raise ValueError(f"No se pudieron actualizar los defaults de Style Settings para `{setting_id}`")

    return "".join(lines)


def list_to_value_map(items: list[dict], name_key: str = "name") -> dict[str, str]:
    return {item[name_key]: item["value"] for item in items}


def apply_core_palette(css: str, core_colors: list[dict]) -> str:
    for item in core_colors:
        css_var = item["css_var"]
        light = item["light"]
        dark = item["dark"]

        css = replace_setting_defaults(css, item["setting_id"], light, dark)
        css = replace_region_var(css, ROOT_START, ROOT_END, css_var, light)
        css = replace_region_var(css, LIGHT_START, LIGHT_END, css_var, f"var({css_var}, {light})", light)
        css = replace_region_var(css, DARK_START, DARK_END, css_var, f"var({css_var}, {dark})", dark)

    return css


def apply_mode_palette(css: str, start_marker: str, end_marker: str, items: list[dict]) -> str:
    for item in items:
        css = replace_region_var(css, start_marker, end_marker, item["var"], item["value"])
    return css


def apply_replacements(css: str, replacements: list[dict]) -> str:
    for item in replacements:
        css = css.replace(item["from"], item["to"])
    return css


def update_font_face_block(css: str, font_cfg: dict, face: dict) -> str:
    pattern = re.compile(
        rf"@font-face\s*\{{(?:(?!@font-face)[\s\S])*?font-style:\s*{re.escape(face['style'])};"
        rf"(?:(?!@font-face)[\s\S])*?font-weight:\s*{re.escape(face['weight'])};"
        rf"(?:(?!@font-face)[\s\S])*?\}}",
        re.S,
    )

    def repl(match: re.Match[str]) -> str:
        block = match.group(0)
        block = re.sub(
            r"(font-family:\s*')[^']+(';)",
            rf"\1{font_cfg['family_name']}\2",
            block,
            count=1,
        )

        encoded = ""
        source_path = face.get("source_path", "").strip()
        source_base64 = face.get("source_base64", "").strip()
        keep_existing = face.get("keep_existing_base64", False)

        if source_path:
            font_bytes = Path(source_path).read_bytes()
            encoded = base64.b64encode(font_bytes).decode("ascii")
        elif source_base64:
            encoded = source_base64
        elif keep_existing:
            return block
        else:
            raise ValueError(
                f"La cara de fuente `{face['label']}` necesita `source_path`, `source_base64` o `keep_existing_base64: true`"
            )

        src_value = f'src: url("data:font/{face["format"]};base64,{encoded}");'
        block, count = re.subn(r'src:\s*url\("data:font/[^"]+"\);', src_value, block, count=1)
        if count == 0:
            raise ValueError(f"No se pudo actualizar el bloque `@font-face` para `{face['label']}`")
        return block

    new_css, count = pattern.subn(repl, css, count=1)
    if count == 0:
        raise ValueError(f"No se encontro el bloque `@font-face` para `{face['label']}`")
    return new_css


def apply_font_config(css: str, font_cfg: dict) -> str:
    for face in font_cfg.get("faces", []):
        css = update_font_face_block(css, font_cfg, face)

    text_stack = font_cfg["text_stack"]
    interface_stack = font_cfg["interface_stack"]
    monospace_stack = font_cfg["monospace_stack"]

    css = replace_decl(css, "body", "font-family", f"{text_stack} !important")
    css = replace_decl(css, "body", "--font-text", text_stack)
    css = replace_decl(css, "body", "--font-interface", interface_stack)
    css = replace_decl(css, "body", "--font-monospace", monospace_stack)

    font_selectors = [
        "h1, h2, h3, h4, h5, h6",
        ".markdown-source-view,\n.markdown-preview-view",
        ".nav-folder-title,\n.nav-file-title",
        ".workspace-tab-header-inner",
        ".status-bar",
        "button",
        "input, textarea, select",
        ".menu-item",
        "table",
    ]
    for selector in font_selectors:
        css = replace_decl(css, selector, "font-family", f"{text_stack} !important", count=0)

    return css


def apply_code_palette(css: str, code: dict[str, str]) -> str:
    css = replace_decl(
        css,
        ".theme-dark .markdown-rendered pre,\n.theme-dark .markdown-rendered pre code",
        "background",
        code["dark_block_background"],
    )
    css = replace_decl(
        css,
        ".theme-dark .markdown-rendered pre,\n.theme-dark .markdown-rendered pre code",
        "color",
        code["dark_code_text"],
    )
    css = replace_decl(
        css,
        ".theme-dark .markdown-rendered pre,\n.theme-dark .markdown-rendered pre code",
        "border",
        f"1px solid {code['dark_code_border']}",
    )
    css = replace_decl(
        css,
        ".theme-dark .markdown-rendered code:not([class*=\"language-\"])",
        "background",
        code["dark_inline_background"],
    )
    css = replace_decl(
        css,
        ".theme-dark .markdown-rendered code:not([class*=\"language-\"])",
        "color",
        code["dark_code_text"],
    )
    css = replace_decl(
        css,
        ".theme-dark .markdown-rendered code:not([class*=\"language-\"])",
        "border",
        f"1px solid {code['dark_code_border']}",
    )

    css = replace_decl(
        css,
        ".theme-light .markdown-rendered pre,\n.theme-light .markdown-rendered pre code",
        "background",
        code["light_block_background"],
    )
    css = replace_decl(
        css,
        ".theme-light .markdown-rendered pre,\n.theme-light .markdown-rendered pre code",
        "color",
        code["light_code_text"],
    )
    css = replace_decl(
        css,
        ".theme-light .markdown-rendered pre,\n.theme-light .markdown-rendered pre code",
        "border",
        f"1px solid {code['light_code_border']}",
    )
    css = replace_decl(
        css,
        ".theme-light .markdown-rendered code:not([class*=\"language-\"])",
        "background",
        code["light_inline_background"],
    )
    css = replace_decl(
        css,
        ".theme-light .markdown-rendered code:not([class*=\"language-\"])",
        "color",
        code["light_code_text"],
    )
    css = replace_decl(
        css,
        ".theme-light .markdown-rendered code:not([class*=\"language-\"])",
        "border",
        f"1px solid {code['light_code_border']}",
    )

    css = replace_decl(css, ".theme-dark .cm-keyword", "color", code["dark_cm_keyword"])
    css = replace_decl(css, ".theme-dark .cm-string", "color", code["dark_cm_string"])
    css = replace_decl(css, ".theme-dark .cm-number", "color", code["dark_cm_number"])
    css = replace_decl(css, ".theme-dark .cm-atom,\n.theme-dark .cm-bool", "color", code["dark_cm_bool"])
    css = replace_decl(css, ".theme-dark .cm-property", "color", code["dark_cm_property"])
    css = replace_decl(css, ".theme-dark .cm-comment", "color", code["dark_cm_comment"])

    css = replace_decl(css, ".theme-light .cm-keyword", "color", code["light_cm_keyword"])
    css = replace_decl(css, ".theme-light .cm-string", "color", code["light_cm_string"])
    css = replace_decl(css, ".theme-light .cm-number", "color", code["light_cm_number"])
    css = replace_decl(css, ".theme-light .cm-atom,\n.theme-light .cm-bool", "color", code["light_cm_bool"])
    css = replace_decl(css, ".theme-light .cm-property", "color", code["light_cm_property"])
    css = replace_decl(css, ".theme-light .cm-comment", "color", code["light_cm_comment"])

    css = replace_decl(
        css,
        ".theme-dark .markdown-rendered code[class*=\"language-\"] .token.keyword",
        "color",
        code["dark_cm_keyword"],
    )
    css = replace_decl(
        css,
        ".theme-dark .markdown-rendered code[class*=\"language-\"] .token.string",
        "color",
        code["dark_cm_string"],
    )
    css = replace_decl(
        css,
        ".theme-dark .markdown-rendered code[class*=\"language-\"] .token.number",
        "color",
        code["dark_cm_number"],
    )
    css = replace_decl(
        css,
        ".theme-dark .markdown-rendered code[class*=\"language-\"] .token.boolean",
        "color",
        code["dark_cm_bool"],
    )
    css = replace_decl(
        css,
        ".theme-dark .markdown-rendered code[class*=\"language-\"] .token.property",
        "color",
        code["dark_cm_property"],
    )
    css = replace_decl(
        css,
        ".theme-dark .markdown-rendered code[class*=\"language-\"] .token.comment",
        "color",
        code["dark_cm_comment"],
    )

    css = replace_decl(
        css,
        ".theme-light .markdown-rendered code[class*=\"language-\"] .token.keyword",
        "color",
        code["light_cm_keyword"],
    )
    css = replace_decl(
        css,
        ".theme-light .markdown-rendered code[class*=\"language-\"] .token.string",
        "color",
        code["light_cm_string"],
    )
    css = replace_decl(
        css,
        ".theme-light .markdown-rendered code[class*=\"language-\"] .token.number",
        "color",
        code["light_cm_number"],
    )
    css = replace_decl(
        css,
        ".theme-light .markdown-rendered code[class*=\"language-\"] .token.boolean",
        "color",
        code["light_cm_bool"],
    )
    css = replace_decl(
        css,
        ".theme-light .markdown-rendered code[class*=\"language-\"] .token.property",
        "color",
        code["light_cm_property"],
    )
    css = replace_decl(
        css,
        ".theme-light .markdown-rendered code[class*=\"language-\"] .token.comment",
        "color",
        code["light_cm_comment"],
    )

    css = replace_decl(css, "code", "background-color", code["dark_inline_background"])
    css = replace_decl(css, "code", "border-color", code["dark_code_border"])
    css = replace_decl(css, "pre", "background-color", code["dark_block_background"])
    css = replace_decl(css, "pre", "border-color", code["dark_code_border"])

    css = re.sub(
        r"^code \{ background-color: [^;]+; border-color: [^;]+; text-shadow: none !important; \}$",
        f"code {{ background-color: {code['dark_inline_background']} !important; border-color: {code['dark_code_border']} !important; text-shadow: none !important; }}",
        css,
        flags=re.M,
    )
    css = re.sub(
        r"^pre  \{ background-color: [^;]+; border-color: [^;]+; \}$",
        f"pre  {{ background-color: {code['dark_block_background']} !important; border-color: {code['dark_code_border']} !important; }}",
        css,
        flags=re.M,
    )

    css = replace_decl(css, ".markdown-rendered pre code.language-javascript", "--code-bg", code["javascript_code_bg"])
    css = replace_decl(css, ".markdown-rendered pre code.language-javascript", "--code-bd", code["javascript_code_border"])
    css = replace_decl(css, ".markdown-rendered pre code.language-python", "--code-bg", code["python_code_bg"])
    css = replace_decl(css, ".markdown-rendered pre code.language-python", "--code-bd", code["python_code_border"])
    css = replace_decl(css, ".markdown-rendered pre code.language-css", "--code-bg", code["css_code_bg"])
    css = replace_decl(css, ".markdown-rendered pre code.language-css", "--code-bd", code["css_code_border"])
    css = replace_decl(css, ".markdown-rendered pre code.language-html", "--code-bg", code["html_code_bg"])
    css = replace_decl(css, ".markdown-rendered pre code.language-html", "--code-bd", code["html_code_border"])

    return css


def apply_focus_shadows(css: str, focus_items: list[dict]) -> str:
    for item in focus_items:
        css = re.sub(item["from"], item["to"], css)
    return css


def apply_config(css: str, config: dict) -> str:
    palette = config["palette"]
    css = apply_core_palette(css, palette["core_colors"])
    css = apply_mode_palette(css, LIGHT_START, LIGHT_END, palette["light_mode"])
    css = apply_mode_palette(css, DARK_START, DARK_END, palette["dark_mode"])
    css = apply_replacements(css, palette["replacements"])
    css = apply_font_config(css, config["font"])
    css = apply_code_palette(css, list_to_value_map(palette["code"]))
    css = apply_focus_shadows(css, palette["focus_shadows"])
    return css


def main() -> None:
    parser = argparse.ArgumentParser(description="Aplica una configuracion simple de paleta y fuentes a theme.css")
    parser.add_argument("--config", default="theme-palette.json", help="Ruta al JSON editable")
    parser.add_argument("--input", default="theme.css", help="Archivo CSS de entrada")
    parser.add_argument("--output", default="theme.css", help="Archivo CSS de salida")
    args = parser.parse_args()

    config_path = Path(args.config)
    input_path = Path(args.input)
    output_path = Path(args.output)

    config = json.loads(config_path.read_text(encoding="utf-8"))
    css = input_path.read_text(encoding="utf-8")
    css = apply_config(css, config)
    output_path.write_text(css, encoding="utf-8")


if __name__ == "__main__":
    main()
