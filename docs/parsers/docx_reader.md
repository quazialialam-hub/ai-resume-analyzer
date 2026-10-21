# `resume_analyzer/parsers/docx_reader.py`

**Path:** `resume_analyzer/parsers/docx_reader.py`
**Purpose:** Extracts plain text from a DOCX resume.

## What it does

Opens the uploaded bytes with `python-docx` and collects the text of every
paragraph. Resumes are often built with tables - especially for the header
block with name, contact details and dates - so the text of every table cell
is collected as well.

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `extract_text_from_docx(data)` | function | Takes the raw bytes of a DOCX and returns its text |

## Behaviour notes

- Paragraph text is collected first, then table cell text, so the order of
  the result is the body of the document followed by the tables.
- A cell that is merged across several columns is returned once per column
  it spans, so its text can appear more than once. This slightly inflates the
  word count used by the length advice, but it never removes content.
- Headers, footers and text inside text boxes are not extracted.

## Dependency

`python-docx`.

## Used by

`parsers/factory.py`.
