# `resume_analyzer/config.py`

**Path:** `resume_analyzer/config.py`
**Purpose:** Single source of truth for every tunable value.

## What it does

Holds the thresholds, limits and label sets that more than one module needs.
Centralising them means a change to, say, the "strong match" boundary only has
to be made in one place.

## Constants

| Name | Value | Meaning |
| --- | --- | --- |
| `SCORE_WEAK` | `40.0` | Below this score the match is reported as weak |
| `SCORE_STRONG` | `70.0` | At or above this score the match is reported as strong |
| `MAX_UPLOAD_BYTES` | `10 MB` | Largest resume the app will read |
| `SUPPORTED_EXTENSIONS` | `("pdf", "docx", "txt")` | Accepted upload formats |
| `SUPPORTED_ENCODINGS` | `("utf-8", "utf-16", "cp1252", "latin-1")` | Encodings tried for TXT files |
| `MIN_RESUME_WORDS` | `150` | Below this, a resume is reported as short |
| `MAX_RESUME_WORDS` | `1200` | Above this, a resume is reported as long |
| `MAX_MISSING_SKILLS_SHOWN` | `8` | How many missing skills one advice line names |
| `ATS_MIN_LINES` | `5` | Minimum text lines before a resume counts as structured |

## Used by

- `core/ats_check.py` - `ATS_MIN_LINES`
- `core/recommendations.py` - `SCORE_WEAK`, `SCORE_STRONG`,
  `MAX_MISSING_SKILLS_SHOWN`
- `core/style_advice.py` - `MIN_RESUME_WORDS`, `MAX_RESUME_WORDS`
- `parsers/factory.py` - `SUPPORTED_EXTENSIONS`
- `parsers/text_reader.py` - `SUPPORTED_ENCODINGS`
- `ui/inputs.py` - `MAX_UPLOAD_BYTES`
- `ui/score_view.py` - `SCORE_WEAK`, `SCORE_STRONG`
