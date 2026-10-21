# `resume_analyzer/core/style_advice.py`

**Path:** `resume_analyzer/core/style_advice.py`
**Purpose:** Checks how well the resume is written.

## What it does

Runs three writing-quality checks over the resume text and returns advice for
the ones that fail.

| Check | Trigger | Advice |
| --- | --- | --- |
| Quantified impact | No percentage, currency amount, "+N" or improvement verb | Quantify achievements with numbers |
| Bullet-point phrasing | Contains "responsible for", "worked on", "helped with" or "duties included" | Replace passive phrases with strong action verbs |
| Length | Fewer than 150 words, or more than 1200 | Add detail, or trim to 1-2 pages |

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `style_advice(resume_text)` | function | Returns a list of advice strings |
| `_style_advice(resume_text)` | private | Impact and phrasing checks |
| `_length_advice(resume_text)` | private | Length check |

## Behaviour notes

- The word count is a simple whitespace split, so it counts tokens rather
  than true words. It is a rough indicator, not a linguistic measurement.
- The quantification pattern is case-insensitive and also accepts the verbs
  "increased", "improved" and "reduced" without a number, because a resume
  that mentions improvement at all is doing better than one that never does.
- The checks are advisory. The application never rewrites the resume.

## Used by

`core/recommendations.py`.
