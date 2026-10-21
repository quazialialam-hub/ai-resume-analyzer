# `scripts/pdf_fixture.py`

**Path:** `scripts/pdf_fixture.py`
**Purpose:** Builds a PDF resume for the smoke test.

## What it does

Writes a single-page PDF that contains a given block of text. The file is
assembled byte by byte, which means the smoke test needs no extra dependency
such as reportlab or fpdf.

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `write_pdf(directory, text)` | function | Writes `resume.pdf` and returns its path |
| `_pdf_bytes(text)` | private | Builds the PDF as a byte string |

## How the file is built

A PDF is a small text format. The builder writes:

1. A header, `%PDF-1.4`.
2. Five objects - the catalogue, the page tree, the page, the Helvetica font
   and the content stream that draws the text.
3. A cross-reference table with the byte offset of every object.
4. A trailer that points at the catalogue, and the start offset of the
   cross-reference table.

The text is drawn with the standard PDF text operators: `BT` starts the text
object, `Tj` shows a string, `T*` moves to the next line and `ET` ends the
text object. Parentheses inside a line would have to be escaped, which is why
the sample resume does not contain any.

## Notes

- The output is a valid, readable PDF: `pypdf` extracts the text from it
  again, which is what the smoke test asserts.
- The builder is only used by the tests. It is not part of the application.
