# Changelog

All notable changes to the "Vision Night" theme will be documented in this file.

## [0.2.0] - 2026-09-23

### Added
- **Vision Night Storm** theme variant calibrated for well-lit and daytime environments (`#222436` canvas).
- Automated theme generator (`scripts/build.py`) ensuring 100% token synchronization across all variants.
- Multi-theme validation suite (`tests/test_theme.py`) checking strict JSON, line highlight elevation, and WCAG AA contrast across all variants.
- Recommended setup and accessibility guidelines in `README.md` (Catppuccin Icons, typography, and ocular rhythm settings).
- Customization guide in `README.md` with examples for UI and token overrides.
- Relocated and consolidated design system documentation into `docs/`.

### Changed
- Refined accessibility language to distinguish WCAG AAA core text from WCAG AA syntax-token contrast.
- Expanded automated validation to cover all TextMate and semantic token foregrounds on both editor canvases.
- Removed outdated standalone palette visualizers so generated themes remain the source of truth.
- Improved accessibility for myopia: elevated comment contrast to `#828BAE` (>= 4.5:1 WCAG AA on all variants) and structural punctuation/operators to `#A9ADC1` (>= 6.87:1).
- Corrected UI layer hierarchy: set editor background to `#1A1A26` and active line highlight to `#212130` (eliminating inverted darker highlight).
- Streamlined theme files by removing redundant micro-scopes and aligning with the 15-color palette.
- Removed invalid comments and cleaned JSON formatting.

## [0.1.1] - 2026-03-07

### Added
- Extension icon included in the package.
- Visual assets for Marketplace preview.

## [0.1.0] - 2026-03-07

### Added
- Complete UI overhaul for Visual Studio Code.
- Multi-language syntax support (React, TS, Vue, Angular, PHP, etc.).
- Global design system based on the 60/30/10 rule.
- Palette visualizer (`palette.html`) for developers.

### Changed
- Refined background to `#151520` for better accessibility and eye strain reduction.
- Desaturated syntax colors to prevent the "halo effect" in myopia.
- Neutralized structural punctuation (brackets and tags) for improved focus.

### Fixed
- JSX/HTML attribute colors now correctly map to the variable palette.
- Cursor visibility improved with high-vis `#E6E6E6`.
