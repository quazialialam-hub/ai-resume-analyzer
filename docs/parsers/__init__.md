# `resume_analyzer/parsers/__init__.py`

**Path:** `resume_analyzer/parsers/__init__.py`
**Purpose:** Public API of the resume parsing package.

## What it does

Re-exports the text extractors so callers can write
`from resume_analyzer.parsers import extract_text` without knowing which
module implements a given format.

## Public API

| Name | Source | Description |
| --- | --- | --- |
| `extract_text` | `factory.py` | Dispatch on the file extension |
| `extract_text_from_pdf` | `pdf_reader.py` | PDF text extraction |
| `extract_text_from_docx` | `docx_reader.py` | DOCX text extraction |
| `extract_text_from_txt` | `text_reader.py` | TXT text extraction |

## Notes

Every reader in this package works on raw bytes rather than on a file
object. That keeps the parsers independent of Streamlit, so the same code
can be driven from a command-line script or an HTTP API, and it makes them
straightforward to test.
