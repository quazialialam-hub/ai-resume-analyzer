# `resume_analyzer/core/ats_check.py`

**Path:** `resume_analyzer/core/ats_check.py`
**Purpose:** Detects resume formatting that commonly breaks ATS parsers.

## What it does

Runs four independent checks over the extracted resume text and returns one
message per problem found.

| Check | Looks for | Why it matters |
| --- | --- | --- |
| Symbols | Bullet glyphs, tick marks, em/en dashes, non-breaking spaces, trademark symbols | Some parsers read them as noise or drop the line |
| Structure | Fewer than `ATS_MIN_LINES` lines of text | A layout built from text boxes or columns collapses into an unreadable blob |
| Sections | No "Experience", "Education" or "Skills" heading | ATS keyword matching relies on standard section titles |
| Contact | No e-mail address | Contact details in an image are invisible to a parser |

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `check_ats_formatting(resume_text)` | function | Returns a list of issue strings |
| `_check_symbols(resume_text)` | private | Risky glyph check |
| `_check_structure(resume_text)` | private | Line-structure check |
| `_check_sections(resume_text)` | private | Section-heading check |
| `_check_contact(resume_text)` | private | E-mail check |

## Behaviour notes

- The symbol check is deliberately narrow. An earlier version 
