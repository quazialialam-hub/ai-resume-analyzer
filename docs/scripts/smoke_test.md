# `scripts/smoke_test.py`

**Path:** `scripts/smoke_test.py`
**Purpose:** End-to-end check of the whole analysis pipeline.

## What it does

Builds a resume in all three supported formats, runs each one through the
real extraction and analysis code and checks the results. It is the fastest
way to confirm that a change did not break the application.

## Usage

```
python scripts/smoke_test.py
```

## What it checks

| Check | Expectation |
| --- | --- |
| TXT extraction | The text of the file comes back |
| DOCX extraction | Paragraph and table text come back |
| PDF extraction | The text of the page comes back |
| Unsupported format | `ValueError` with a helpful message |
| Empty file | `ValueError` with a helpful message |
| Skill extraction | The expected skills are found, and the ambiguous ones are not |
| Alias resolution | "Amazon Web Services" resolves to "aws" |
| Match score | A number between 0 and 100 |
| Pipeline | A complete `Analysis` with all five fields filled in |
| Report | The report text contains the score |
| Code-line budget | Every file is within the 50 line limit |

## Notes

- The script writes its fixture files to a temporary directory and removes
  them again, so it leaves nothing behind.
- It exits with status 0 when everything passes and 1 otherwise, so it can
  be used as a CI step.
- It needs the dependencies from `requirements.txt` to be installed.
