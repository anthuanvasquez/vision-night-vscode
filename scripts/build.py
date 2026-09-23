#!/usr/bin/env python3
"""
Vision Night Theme Generator
Builds both 'Vision Night' (Midnight) and 'Vision Night Storm' variants
from a single shared template to ensure 100% consistency and maintainability.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THEMES_DIR = ROOT / "themes"

SHARED_SYNTAX = {
    "fg": "#D5D6E1",
    "fg_secondary": "#A9ADC1",
    "comments": "#828BAE",
    "functions": "#6F9EF5",
    "keywords": "#B07CD6",
    "strings": "#A9D67A",
    "types": "#E8B463",
    "variables": "#74C9E8",
    "constants": "#C89A6A",
    "tags": "#D47D8A",
    "errors": "#FF6B7D",
    "cursor": "#E6E6E6",
}

PALETTES = {
    "Vision Night": {
        "filename": "Vision Night-color-theme.json",
        "bg_base": "#151520",
        "bg_editor": "#1A1A26",
        "bg_surface": "#1E1E28",
        "bg_line_hl": "#212130",
        "border": "#2A2F46",
        "border_subtle": "#2A2F4655",
        "selection": "#2F3C63",
        "selection_hover": "#222436",
        "shadow": "#101017",
        "line_number": "#656D8F",
    },
    "Vision Night Storm": {
        "filename": "Vision Night Storm-color-theme.json",
        "bg_base": "#1B1C2A",
        "bg_editor": "#222436",
        "bg_surface": "#272A3E",
        "bg_line_hl": "#292C42",
        "border": "#323753",
        "border_subtle": "#32375355",
        "selection": "#364470",
        "selection_hover": "#2B2E46",
        "shadow": "#141520",
        "line_number": "#737B9F",
    },
}

def generate_theme(name: str, palette: dict) -> dict:
    s = SHARED_SYNTAX
    p = palette

    return {
        "name": name,
        "type": "dark",
        "colors": {
            "focusBorder": s["functions"],
            "foreground": s["fg"],
            "widget.shadow": f"{p['shadow']}CC",
            "selection.background": p["selection"],
            "descriptionForeground": s["fg_secondary"],
            "errorForeground": s["errors"],
            "icon.foreground": s["fg_secondary"],
            "sash.hoverBorder": s["functions"],
            "window.activeBorder": p["bg_base"],
            "window.inactiveBorder": p["bg_base"],
            "textLink.foreground": s["functions"],
            "textLink.activeForeground": s["variables"],
            "textPreformat.foreground": s["constants"],
            "textBlockQuote.background": p["bg_surface"],
            "textBlockQuote.border": s["functions"],
            "textCodeBlock.background": p["bg_base"],
            "button.background": s["functions"],
            "button.foreground": p["bg_base"],
            "button.hoverBackground": s["variables"],
            "button.border": p["border"],
            "button.secondaryBackground": p["border"],
            "button.secondaryForeground": s["fg"],
            "button.secondaryHoverBackground": p["selection"],
            "checkbox.background": p["bg_surface"],
            "checkbox.border": p["border"],
            "dropdown.background": p["bg_surface"],
            "dropdown.border": p["border"],
            "dropdown.foreground": s["fg"],
            "input.background": p["bg_surface"],
            "input.border": p["border"],
            "input.foreground": s["fg"],
            "input.placeholderForeground": s["comments"],
            "inputOption.activeBackground": p["selection"],
            "inputOption.activeForeground": s["fg"],
            "inputOption.activeBorder": s["functions"],
            "inputOption.hoverBackground": p["border"],
            "inputValidation.errorBackground": f"{s['errors']}22",
            "inputValidation.errorBorder": s["errors"],
            "inputValidation.infoBackground": f"{s['functions']}22",
            "inputValidation.infoBorder": s["functions"],
            "inputValidation.warningBackground": f"{s['types']}22",
            "inputValidation.warningBorder": s["types"],
            "scrollbar.shadow": p["shadow"],
            "scrollbarSlider.background": f"{p['bg_surface']}AA",
            "scrollbarSlider.hoverBackground": p["border"],
            "scrollbarSlider.activeBackground": p["selection"],
            "badge.background": s["functions"],
            "badge.foreground": p["bg_base"],
            "progressBar.background": s["functions"],
            "list.activeSelectionBackground": p["selection"],
            "list.activeSelectionForeground": s["fg"],
            "list.dropBackground": p["selection"],
            "list.focusBackground": p["selection"],
            "list.hoverBackground": p["selection_hover"],
            "list.hoverForeground": s["fg"],
            "list.inactiveSelectionBackground": p["bg_surface"],
            "list.inactiveSelectionForeground": s["fg"],
            "list.errorForeground": s["errors"],
            "list.warningForeground": s["types"],
            "activityBar.background": p["bg_base"],
            "activityBar.foreground": s["fg"],
            "activityBar.inactiveForeground": s["comments"],
            "activityBar.border": p["border"],
            "activityBarBadge.background": s["functions"],
            "activityBarBadge.foreground": p["bg_base"],
            "sideBar.background": p["bg_base"],
            "sideBar.foreground": s["fg"],
            "sideBar.border": p["border"],
            "sideBarTitle.foreground": s["fg"],
            "sideBarSectionHeader.background": p["bg_base"],
            "sideBarSectionHeader.foreground": s["fg"],
            "sideBarSectionHeader.border": p["border"],
            "editorGroup.border": p["border"],
            "editorGroup.dropBackground": f"{p['selection']}88",
            "editorGroupHeader.tabsBackground": p["bg_base"],
            "editorGroupHeader.tabsBorder": p["border"],
            "tab.activeBackground": p["bg_editor"],
            "tab.activeForeground": s["fg"],
            "tab.border": p["border"],
            "tab.activeBorderTop": s["functions"],
            "tab.inactiveBackground": p["bg_base"],
            "tab.inactiveForeground": s["comments"],
            "tab.hoverBackground": p["selection_hover"],
            "tab.unfocusedActiveBackground": p["bg_editor"],
            "editor.background": p["bg_editor"],
            "editor.foreground": s["fg"],
            "editorLineNumber.foreground": p["line_number"],
            "editorLineNumber.activeForeground": s["fg"],
            "editorCursor.foreground": s["cursor"],
            "editor.selectionBackground": p["selection"],
            "editor.selectionHighlightBackground": f"{p['selection']}55",
            "editor.wordHighlightBackground": f"{p['selection']}44",
            "editor.wordHighlightStrongBackground": f"{p['selection']}66",
            "editor.findMatchBackground": p["selection"],
            "editor.findMatchHighlightBackground": f"{p['selection']}55",
            "editor.findRangeHighlightBackground": f"{p['selection']}33",
            "editor.lineHighlightBackground": p["bg_line_hl"],
            "editor.lineHighlightBorder": p["border_subtle"],
            "editorIndentGuide.background1": p["border"],
            "editorIndentGuide.activeBackground1": s["comments"],
            "editorRuler.foreground": p["border"],
            "editorCodeLens.foreground": s["comments"],
            "editorBracketMatch.background": f"{p['selection']}66",
            "editorBracketMatch.border": s["functions"],
            "editorOverviewRuler.border": p["border"],
            "editorError.foreground": s["errors"],
            "editorWarning.foreground": s["types"],
            "editorInfo.foreground": s["functions"],
            "editorHint.foreground": s["variables"],
            "editorGutter.modifiedBackground": s["functions"],
            "editorGutter.addedBackground": s["strings"],
            "editorGutter.deletedBackground": s["errors"],
            "editorGutter.commentRangeForeground": s["comments"],
            "editorSuggestWidget.background": p["bg_surface"],
            "editorSuggestWidget.border": p["border"],
            "editorSuggestWidget.foreground": s["fg"],
            "editorSuggestWidget.highlightForeground": s["functions"],
            "editorSuggestWidget.selectedBackground": p["selection"],
            "editorHoverWidget.background": p["bg_surface"],
            "editorHoverWidget.border": p["border"],
            "editorWidget.background": p["bg_surface"],
            "editorWidget.border": p["border"],
            "debugExceptionWidget.background": p["bg_surface"],
            "debugExceptionWidget.border": p["border"],
            "editorMarkerNavigation.background": p["bg_surface"],
            "panel.background": p["bg_editor"],
            "panel.border": p["border"],
            "panelTitle.activeBorder": s["functions"],
            "panelTitle.activeForeground": s["fg"],
            "panelTitle.inactiveForeground": s["comments"],
            "peekView.border": s["functions"],
            "peekViewEditor.background": p["bg_base"],
            "peekViewEditor.matchHighlightBackground": p["selection"],
            "peekViewResult.background": p["bg_surface"],
            "peekViewResult.fileForeground": s["fg"],
            "peekViewResult.lineForeground": s["fg_secondary"],
            "peekViewResult.matchHighlightBackground": p["selection"],
            "peekViewResult.selectionBackground": p["selection"],
            "peekViewResult.selectionForeground": s["fg"],
            "peekViewTitle.background": p["bg_surface"],
            "peekViewTitleDescription.foreground": s["fg_secondary"],
            "peekViewTitleLabel.foreground": s["fg"],
            "terminal.background": p["bg_editor"],
            "terminal.foreground": s["fg"],
            "terminal.ansiBlack": p["bg_base"],
            "terminal.ansiBlue": s["functions"],
            "terminal.ansiCyan": s["variables"],
            "terminal.ansiGreen": s["strings"],
            "terminal.ansiMagenta": s["keywords"],
            "terminal.ansiRed": s["errors"],
            "terminal.ansiWhite": s["fg"],
            "terminal.ansiYellow": s["constants"],
            "terminal.ansiBrightBlack": p["line_number"],
            "terminal.ansiBrightBlue": s["functions"],
            "terminal.ansiBrightCyan": s["variables"],
            "terminal.ansiBrightGreen": s["strings"],
            "terminal.ansiBrightMagenta": s["keywords"],
            "terminal.ansiBrightRed": s["errors"],
            "terminal.ansiBrightWhite": s["fg"],
            "terminal.ansiBrightYellow": s["types"],
            "statusBar.background": p["bg_base"],
            "statusBar.foreground": s["fg"],
            "statusBar.border": p["border"],
            "statusBar.debuggingBackground": s["constants"],
            "statusBar.debuggingForeground": p["bg_base"],
            "statusBar.noFolderBackground": p["bg_base"],
            "statusBarItem.activeBackground": p["selection"],
            "statusBarItem.hoverBackground": p["border"],
            "statusBarItem.prominentBackground": p["border"],
            "statusBarItem.prominentHoverBackground": p["selection"],
            "breadcrumb.foreground": s["comments"],
            "breadcrumb.focusForeground": s["fg"],
            "breadcrumb.activeSelectionForeground": s["functions"],
            "breadcrumbPicker.background": p["bg_surface"],
            "menubar.selectionForeground": s["fg"],
            "menubar.selectionBackground": p["border"],
            "menubar.selectionBorder": p["border"],
            "titleBar.activeBackground": p["bg_base"],
            "titleBar.activeForeground": s["fg"],
            "titleBar.inactiveBackground": p["bg_base"],
            "titleBar.inactiveForeground": s["comments"],
            "titleBar.border": p["border"],
            "settings.headerForeground": s["fg"],
            "settings.modifiedItemIndicator": s["functions"],
            "settings.dropdownBackground": p["bg_surface"],
            "settings.dropdownBorder": p["border"],
            "settings.checkboxBackground": p["bg_surface"],
            "settings.checkboxBorder": p["border"],
            "settings.textInputBackground": p["bg_surface"],
            "settings.textInputBorder": p["border"],
            "settings.numberInputBackground": p["bg_surface"],
            "settings.numberInputBorder": p["border"]
        },
        "tokenColors": [
            {
                "name": "Comments",
                "scope": ["comment", "punctuation.definition.comment"],
                "settings": {"foreground": s["comments"], "fontStyle": "italic"}
            },
            {
                "name": "Keywords & Control Flow",
                "scope": ["keyword", "storage.type", "storage.modifier", "keyword.control"],
                "settings": {"foreground": s["keywords"], "fontStyle": "italic"}
            },
            {
                "name": "Functions & Methods",
                "scope": ["entity.name.function", "meta.function-call", "support.function"],
                "settings": {"foreground": s["functions"]}
            },
            {
                "name": "Strings & Literals",
                "scope": ["string", "punctuation.definition.string", "string.template"],
                "settings": {"foreground": s["strings"]}
            },
            {
                "name": "Classes, Types & Interfaces",
                "scope": [
                    "entity.name.class",
                    "entity.name.type.class",
                    "support.type",
                    "support.class",
                    "entity.other.inherited-class",
                    "entity.name.type",
                    "support.class.component"
                ],
                "settings": {"foreground": s["types"]}
            },
            {
                "name": "Variables & Parameters",
                "scope": ["variable", "variable.parameter"],
                "settings": {"foreground": s["fg"]}
            },
            {
                "name": "Object Keys, Properties & Attributes",
                "scope": [
                    "meta.object-literal.key",
                    "support.variable.property",
                    "variable.other.property",
                    "entity.other.attribute-name"
                ],
                "settings": {"foreground": s["variables"]}
            },
            {
                "name": "HTML & JSX Tags",
                "scope": ["entity.name.tag"],
                "settings": {"foreground": s["tags"]}
            },
            {
                "name": "Constants, Numbers & Booleans",
                "scope": [
                    "constant.numeric",
                    "constant.language",
                    "constant.character",
                    "constant.other"
                ],
                "settings": {"foreground": s["constants"]}
            },
            {
                "name": "Operators & Punctuation",
                "scope": [
                    "keyword.operator",
                    "punctuation.separator",
                    "punctuation.terminator",
                    "punctuation.accessor",
                    "meta.brace",
                    "meta.delimiter",
                    "punctuation.definition.tag",
                    "punctuation.section"
                ],
                "settings": {"foreground": s["fg_secondary"]}
            },
            {
                "name": "Template Interpolation & Regex",
                "scope": [
                    "punctuation.definition.template-expression",
                    "meta.template.expression",
                    "string.regexp"
                ],
                "settings": {"foreground": s["variables"]}
            },
            {
                "name": "Markdown Headings",
                "scope": ["markup.heading"],
                "settings": {"foreground": s["functions"], "fontStyle": "bold"}
            },
            {
                "name": "Markdown Links",
                "scope": ["markup.underline.link", "string.other.link.title.markdown"],
                "settings": {"foreground": s["variables"], "fontStyle": "underline"}
            },
            {
                "name": "Markdown Code",
                "scope": ["markup.inline.raw", "markup.fenced_code.block"],
                "settings": {"foreground": s["constants"]}
            },
            {
                "name": "Markdown Quotes",
                "scope": ["markup.quote"],
                "settings": {"foreground": s["comments"], "fontStyle": "italic"}
            }
        ],
        "semanticHighlighting": True,
        "semanticTokenColors": {
            "class": s["types"],
            "interface": s["types"],
            "type": s["types"],
            "enum": s["constants"],
            "enumMember": s["constants"],
            "parameter": s["variables"],
            "variable": s["fg"],
            "property": s["variables"],
            "function": s["functions"],
            "method": s["functions"],
            "keyword": {"foreground": s["keywords"], "fontStyle": "italic"},
            "string": s["strings"],
            "number": s["constants"],
            "boolean": s["constants"],
            "comment": {"foreground": s["comments"], "fontStyle": "italic"},
            "operator": s["fg_secondary"],
            "decorator": s["types"]
        }
    }

def main():
    THEMES_DIR.mkdir(parents=True, exist_ok=True)
    for name, palette in PALETTES.items():
        theme_data = generate_theme(name, palette)
        out_file = THEMES_DIR / palette["filename"]
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(theme_data, f, indent=2)
            f.write("\n")
        print(f"Generated {name} -> {out_file.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
