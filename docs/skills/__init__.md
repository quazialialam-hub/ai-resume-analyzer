# `resume_analyzer/skills/__init__.py`

**Path:** `resume_analyzer/skills/__init__.py`
**Purpose:** Public API of the skill detection package.

## What it does

Re-exports the skill database, the alias table and the extraction function.

## Public API

| Name | Source | Description |
| --- | --- | --- |
| `SKILL_DB` | `database.py` | The curated dictionary of skills |
| `ALIASES` | `aliases.py` | Alternative spellings mapped to canonical names |
| `extract_skills(text)` | `extractor.py` | Returns the canonical skills found in a text |

## Usage

```python
from resume_analyzer.skills import extract_skills

extract_skills("Built ETL pipelines on AWS with Python and PostgreSQL.")
# {'aws', 'etl', 'python', 'postgresql'}
```

## Notes

The database and the alias table are plain dictionaries, so extending the
coverage for a specific industry needs no code changes - add the skill to
`database.py`, add any alternative spelling to `aliases.py`, and the matcher
picks it up immediately.
