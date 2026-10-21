# `resume_analyzer/ui/__init__.py`

**Path:** `resume_analyzer/ui/__init__.py`
**Purpose:** Public API of the Streamlit presentation layer.

## What it does

Re-exports the UI modules so a caller can write
`from resume_analyzer.ui import header, results`.

## Public API

| Name | Source | Description |
| --- | --- | --- |
| `header` | `header.py` | Page title, styling and sidebar |
| `inputs` | `inputs.py` | Upload and job description controls |
| `styles` | `styles.py` | The custom CSS |
| `score_view` | `score_view.py` | Score card and coverage chart |
| `skill_view` | `skill_view.py` | Matched and missing skill pills |
| `results` | `results.py` | Composition of the results view |
| `report` | `report.py` | Downloadable text report |

## Notes

This is the only part of the package that imports Streamlit. Everything
under `core`, `parsers` and `skills` stays free of it, so the analysis can be
run, tested and reused without a browser session.

Every rendering function takes an `Analysis` object and returns nothing, so
the UI never has to know how a score or a skill set was produced.
