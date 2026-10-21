# `resume_analyzer/skills/database.py`

**Path:** `resume_analyzer/skills/database.py`
**Purpose:** The curated list of skills the app can detect.

## What it does

Holds `SKILL_DB`, a dictionary of every skill the extractor knows about,
grouped by category:

| Category | Examples |
| --- | --- |
| Programming languages | python, java, c++, typescript, rust, matlab |
| Web and frameworks | react, angular, django, fastapi, node.js, html |
| Data, ML and AI | machine learning, pytorch, scikit-learn, llm, prompt engineering |
| Data engineering and cloud | aws, azure, docker, kubernetes, spark, snowflake |
| Databases | mysql, postgresql, mongodb, oracle, nosql |
| Tools and practices | git, jira, agile, ci/cd, unit testing, linux |
| Soft skills | communication, leadership, project management, problem solving |
| Cybersecurity | cybersecurity, penetration testing, encryption |

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `SKILL_DB` | constant | `set` of canonical skill names |
| `CASE_SENSITIVE_SKILLS` | constant | `{"go", "r"}` - see below |

## The case-sensitivity exception

`go` and `r` are also ordinary English words and single letters. Matched
case-insensitively, "go to market" would be reported as the Go language and
"R&D" as the R language. Both are therefore matched only when they are
written in their canonical form - "Go" and "R" - so "Go" counts as the
language and "go" does not.

Add any further ambiguous skill to `CASE_SENSITIVE_SKILLS` to give it the
same treatment.

## Extending the database

Add the canonical name to `SKILL_DB`. The extractor matches it
automatically - no other change is needed. If the same skill is commonly
written in another way, add that spelling to `skills/aliases.md` so it
resolves to the same canonical name.

## Notes

- The names are lower case, because the matcher lower-cases the text before
  it matches.
- Multi-word entries such as "machine learning" are matched as a phrase, and
  the boundary check makes sure they are not found inside a longer word.
