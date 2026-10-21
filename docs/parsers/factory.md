# `resume_analyzer/parsers/factory.py`

**Path:** `resume_analyzer/parsers/factory.py`
**Purpose:** Chooses the right text extractor for an uploaded file.

## What it does

Takes the raw bytes of an upload plus its file name, picks the reader that
matches the extension, and normalises the result.

| Extension | Reader |
| --- | --- |
| `.pdf` | `pdf_reader.py` |
| `.docx` | `docx_reader.py` |
| `.txt` | `text_reader.py` |

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `extract_text(data, filename)` | function | Returns the resume text, raises `ValueError` on failure |

## Errors

| Situation | Message |
| --- | --- |
| Extension not in `SUPPORTED_EXTENSIONS` | "Unsupported file type. Please upload a PDF, DOCX or TXT file." |
| Extraction produced no text | "No readable text found in the file (it may be a scanned or image-based PDF)." |

Both are `ValueError`s, and `ui/inputs.py` catches them and shows the message
to the user instead of a traceback.

## Behaviour notes

- The extension is taken from the file name and lower-cased, so
  `Resume.PDF` works.
- The text is stripped of surrounding whitespace before it is returned.
- An empty result is treated as an error, because an empty resume would
  otherwise produce a meaningless score of zero.

## Used by

`ui/inputs.py`.
