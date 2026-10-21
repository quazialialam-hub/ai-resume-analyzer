# `resume_analyzer/core/skill_gap.py`

**Path:** `resume_analyzer/core/skill_gap.py`
**Purpose:** Compares the skills of a resume with the skills a job asks for.

## What it does

Two plain set operations over the skill sets produced by the extractor. This
is the step that turns "the candidate knows X, Y and Z" and "the job needs X
and W" into "matched: X" and "missing: W".

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `get_matched_skills(resume_skills, jd_skills)` | function | Intersection of the two sets |
| `get_missing_skills(resume_skills, jd_skills)` | function | Skills of the job minus skills of the resume |

## Behaviour notes

- Both functions copy their arguments, so the caller's sets are never
  modified.
- The extractor only ever returns canonical skill names, which is what makes
  the comparison meaningful: "sklearn" in a resume and "scikit-learn" in the
  job description resolve to the same name and are counted as a match.
- The result is a set, so the order is not defined. The UI sorts the skills
  before it displays them.

## Used by

`core/pipeline.py`.
