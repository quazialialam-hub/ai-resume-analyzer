# `resume_analyzer/core/recommendations.py`

**Path:** `resume_analyzer/core/recommendations.py`
**Purpose:** Produces the overall-fit and skill-gap part of the advice.

## What it does

Builds the first part of the recommendation list:

1. **Score advice** - one sentence chosen from the band the match score falls
   into, using `SCORE_WEAK` and `SCORE_STRONG` from `config.py`.
2. **Skill advice** - names up to `MAX_MISSING_SKILLS_SHOWN` of the missing
   skills, plus a reminder to back them up with a concrete example.

The wording, impact and length checks live in `core/style_advice.py`, and
this module simply concatenates the two lists.

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `generate_recommendations(match_score, missing_skills, resume_text)` | function | Returns a list of advice strings |
| `_score_advice(match_score)` | private | Overall-fit sentence for the score band |
| `_skill_advice(missing_skills)` | private | Advice about the missing skills |

## Behaviour notes

- The order of the returned list is the order the advice should be shown in.
- When there are no missing skills, no skill advice is produced at all - the
  list stays short and relevant instead of padding itself out.
- The function never raises on an empty skill set or a zero score.

## Used by

`core/pipeline.py`.
