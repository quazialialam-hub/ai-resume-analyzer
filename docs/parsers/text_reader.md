# `resume_analyzer/parsers/text_reader.py`

**Path:** `resume_analyzer/parsers/text_reader.py`
**Purpose:** Decodes a plain-text resume.

## What it does

Turns the raw bytes of a `.txt` upload into a string. The encodings listed in
`SUPPORTED_ENCODINGS` are tried in order, and the first one that decodes
without an error is used.

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `extract_text_from_txt(data)` | function | Takes the raw bytes of a text file and returns its content |

## Behaviour notes

- The fallback chain is `utf-8`, `utf-16`, `cp1252`, `latin-1`. The last one
  never fails, so the loop always terminates.
- If every strict decode fails, the file is decoded as UTF-8 with errors
  ignored. A slightly corrupt file therefore still produces usable text
  instead of an error.
- Earlier versions of this reader always used a lossy UTF-8 decode, which
  silently dropped every character outside UTF-8. That is now the explicit
  last resort rather than the default.

## Used by

`parsers/factory.py`.
