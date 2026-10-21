# `resume_analyzer/skills/aliases.py`

**Path:** `resume_analyzer/skills/aliases.py`
**Purpose:** Maps alternative skill spellings onto canonical skill names.

## What it does

A resume says "Amazon Web Services" and a job advert says "AWS". Without an
alias table those are two different strings, the skill is reported as
missing, and the match score is wrong. This table closes that gap.

| Surface form in the text | Canonical skill |
| --- | --- |
| amazon web services, amazon aws | aws |
| google cloud platform | gcp |
| apache spark, apache kafka, apache airflow, apache hadoop | spark, kafka, airflow, hadoop |
| postgres | postgresql |
| k8s | kubernetes |
| powerbi | power bi |
| node js, nodejs | node.js |
| sklearn | scikit-learn |
| containerization, containers | docker |
| ml | machine learning |
| gen ai | generative ai |
| large language model | llm |
| bash scripting | shell scripting |
| unit tests | unit testing |
| continuous integration, continuous delivery | ci/cd |

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `ALIASES` | constant | `dict` of surface form to canonical skill name |

## Rules

- The key is the text that may appear in a resume. It is matched with the
  same boundary rules as a database entry.
- The value must be a name that exists in `SKILL_DB`. The extractor only ever
  returns canonical names, so a typo in the value would silently drop the
  skill.
- An alias never introduces a new skill on its own. "postgres" is only
  reported as "postgresql".

## Extending the table

Add the alternative spelling as a key and the canonical name as the value.
This is the place to add industry-specific jargon, for example
"power bi" and "powerbi" for a data analyst role.
