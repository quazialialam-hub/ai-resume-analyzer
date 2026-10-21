# `resume_analyzer/core/pipeline.py`

**Path:** `resume_analyzer/core/pipeline.py`
**Purpose:** Runs the whole analysis and returns one result object.

## What it does

This is the seam between the analysis logic and the UI. It calls each step
once, in order, and collects the results into an `Analysis`.

```
resume text + job description
        |
        v
  compute_match_score        -> match score (0-100)
  extract_skills (x2)        -> resume skills, job skills
  get_matched_skills         -> matched skills
  get_missing_skills         -> missing skills
  generate_recommendations   -> advice list
  check_ats_formatting       -> ATS issue list
        |
        v
     Analysis
```

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `Analysis` | dataclass | The result of a completed analysis |
| `run_analysis(resume_text, job_description)` | function | Runs the pipeline |

### `Analysis` fields

| Field | Type | Description |
| --- | --- | --- |
| `match_score` | `float` | Match percentage, 0-100 |
| `matched_skills` | `set` | Skills found in both documents |
| `missing_skills` | `set` | Skills the job wants that the resume lacks |
| `recommendations` | `list` | Ordered advice strings |
| `ats_issues` | `list` | ATS compatibility warnings |

## Behaviour notes

- The score is computed exactly once and passed to everything that needs it.
- `Analysis` is a plain dataclass with defaults, so it can be constructed
  directly in a test without running the pipeline.
- The pipeline has no Streamlit dependency, so it can be driven from a script,
  a notebook or a test.

## Used by

`app.py`.
