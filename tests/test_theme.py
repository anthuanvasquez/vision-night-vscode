#!/usr/bin/env python3
import json
from pathlib import Path

def lum(hex_str):
    hex_str = hex_str.lstrip('#')[:6]
    r, g, b = [int(hex_str[i:i+2], 16) / 255.0 for i in (0, 2, 4)]
    adj = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * adj(r) + 0.7152 * adj(g) + 0.0722 * adj(b)

def contrast(c1, c2):
    l1, l2 = lum(c1), lum(c2)
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)

def validate_theme(theme_file: Path):
    print(f"\nValidating {theme_file.name}...")
    with open(theme_file, "r", encoding="utf-8") as f:
        theme = json.load(f)

    colors = theme["colors"]
    editor_bg = colors["editor.background"]
    line_hl = colors["editor.lineHighlightBackground"]

    # 1. Line highlight must not be darker than editor
    assert lum(line_hl) >= lum(editor_bg), (
        f"Line highlight ({line_hl}) is darker than editor ({editor_bg})!"
    )

    # 2. Text and comments contrast on editor canvas
    fg = colors["foreground"]
    fg_contrast = contrast(fg, editor_bg)
    assert fg_contrast >= 4.5, f"Foreground contrast {fg_contrast:.2f}:1 fails WCAG AA!"

    comment_token = next(
        t for t in theme["tokenColors"] if "comment" in t.get("scope", [])
    )
    comment_color = comment_token["settings"]["foreground"]
    comment_contrast = contrast(comment_color, editor_bg)
    assert comment_contrast >= 4.5, (
        f"Comment contrast {comment_contrast:.2f}:1 ({comment_color}) fails WCAG AA on {editor_bg}!"
    )

    print(f"  ✓ Valid strict JSON")
    print(f"  ✓ Editor BG: {editor_bg} (lum: {lum(editor_bg):.5f})")
    print(f"  ✓ Line Highlight: {line_hl} (lum: {lum(line_hl):.5f})")
    print(f"  ✓ Foreground contrast: {fg_contrast:.2f}:1 (WCAG AA pass)")
    print(f"  ✓ Comment contrast: {comment_contrast:.2f}:1 (WCAG AA pass)")

def main():
    root = Path(__file__).resolve().parent.parent
    themes_dir = root / "themes"
    theme_files = sorted(themes_dir.glob("*.json"))
    assert len(theme_files) >= 2, f"Expected at least 2 themes, found {len(theme_files)}"

    for tf in theme_files:
        validate_theme(tf)

    print(f"\nAll {len(theme_files)} themes passed all accessibility and validity checks!")

if __name__ == "__main__":
    main()
