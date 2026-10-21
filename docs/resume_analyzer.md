# `resume_analyzer/__init__.py`

**Path:** `resume_analyzer/__init__.py`
**Purpose:** Package root.

## What it does

Marks `resume_analyzer` as a package, documents the layout of the four
sub-packages and exposes the package version.

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `__version__` | constant | `"2.0.0"` |

## Layout

| Sub-package | Responsibility |
| --- | --- |
| `core` | Pure analysis logic, no Streamlit imports |
| `parsers` | Text extraction from PDF, DOCX and TXT |
| `skills` | Skill database, aliases and matching algorithm |
| `ui` | Streamlit rendering helpers |

## Notes

The package root deliberately re-exports nothing. Import from the specific
sub-package instead, for example
`from resume_analyzer.core.pipeline import run_analysis`, so that it stays
obvious which layer a call belongs to.
