# `resume_analyzer/parsers/pdf_reader.py`

**Path:** `resume_analyzer/parsers/pdf_reader.py`
**Purpose:** Extracts plain text from a PDF resume.

## What it does

Opens the uploaded bytes with `pypdf`, pulls the text out of every page and
joins the pages with newlines.

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `extract_text_from_pdf(data)` | function | Takes the raw bytes of a PDF and returns its text |

## Behaviour notes

- The bytes are wrapped in a `BytesIO` buffer, so the reader needs no file
  on disk and works the same in a test as in the app.
- `page.extract_text()` returns `None` for a page that holds only an image.
  That case is turned into an empty string, so one image page does not break
  the whole extraction.
- Page text is joined with a newline. This keeps the line structure of the
  document, which the ATS structure check depends on.
- A scanned PDF produces no text at all. The factory turns that into a
  readable error message rather than an empty analysis.

## Dependency

`pypdf` - the actively maintained successor to `PyPDF2`, which has not been
updated since 2022.

## Used by

`parsers/factory.py`.
