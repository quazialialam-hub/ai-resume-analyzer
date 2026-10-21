# `resume_analyzer/skills/extractor.py`

**Path:** `resume_analyzer/skills/extractor.py`
**Purpose:** Finds the skills mentioned in a block of text.

## What it does

Normalises the text, then looks for every known skill name and every known
alias in it.

```
"Built ETL pipelines on AWS with Python and PostgreSQL."
   |
   v
 normalize -> "built etl pipelines on aws with python and postgresql"
   |
   v
 match every surface form, boundary aware
   |
   v
 {'aws', 'etl', 'python', 'postgresql'}
```

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `extract_skills(text)` | function | Returns the set of canonical skills found |
| `_normalize(text)` | private | Lower-cases and strips punctuation |
| `_pattern_for(surface)` | private | Returns the cached matcher for a surface form |
| `_exact_case_match(surface, text)` | private | Exact-case match for ambiguous skills |

## Matching rules

- **Normalisation** lower-cases the text and replaces everything that is not
  a letter, a digit or one of `+ # . /` with a space. The symbols are kept so
  that "c++", "c#", "node.js" and "ci/cd" survive.
- **Boundaries** - a skill is only found when it is not glued to another word.
  "react" is not found inside "reactive", and "go" is not found inside
  "going".
- **Phrases** are matched as a whole, with any amount of whitespace between
  the words, so "machine  learning" across a line break still matches.
- **Aliases** resolve to the canonical name, so a skill is never reported
  twice under two spellings.
- **Ambiguous skills** - the entries in `CASE_SENSITIVE_SKILLS` ("go" and "r")
  are matched against the original text instead, and only in their canonical
  written form: "Go" and "R". A lowercase "go" in "go to market" is not
  reported as the Go language, and the "&" is excluded from the boundary so
  that "R&D" is not read as the R language.

## Performance

The matcher for each surface form is compiled once and kept in a
module-level cache, so repeated analyses do not recompile roughly 130
regular expressions. The cache is keyed on the surface form and is safe to
share between calls.

## Used by

`core/pipeline.py`.
