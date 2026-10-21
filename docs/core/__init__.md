# `resume_analyzer/core/__init__.py`

**Path:** `resume_analyzer/core/__init__.py`
**Purpose:** Public API of the core analysis package.

## What it does

Re-exports every public function of the `core` sub-package so that callers
can write `from resume_analyzer.core import run_analysis` instead of knowing
which module inside the package a function lives in.

## Public API

| Name | Source | Description |
| --- | --- | --- |
| `Analysis` | `pipeline.py` | Result object of a completed analysis |
| `run_analysis` | `pipeline.py` | Runs the whole pipeline |
| `compute_match_score` | `scoring.py` | TF-IDF / cosine similarity score |
| `get_matched_skills` | `skill_gap.py` | Skills in both documents |
| `get_missing_skills` | `skill_gap.py` | Skills only in the job description |
| `generate_recommendations` | `recommendations.py` | Full advice list |
| `style_advice` | `style_advice.py` | Wording and length advice only |
| `check_ats_formatting` | `ats_check.py` | ATS issues found in a resume |

## Notes

Nothing in this package imports Streamlit. Every function is a pure function
of its arguments, which is what makes the analysis layer testable and
reusable from a script or an API.
