# `resume_analyzer/ui/inputs.py`

**Path:** `resume_analyzer/ui/inputs.py`
**Purpose:** Renders the resume upload and the job description box.

## What it does

Builds the two-column input area and returns the two raw values the rest of
the app works with.

| Column | Control | Returned value |
| --- | --- | --- |
| 1. Upload Resume | File uploader, plus an expander with the extracted text | `resume_text` |
| 2. Paste Job Description | Text area | `job_description` |

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `render_inputs()` | function | Returns `(resume_text, job_description)` |
| `parse_resume(data, filename)` | function | Cached text extraction |
| `_read_upload(uploaded)` | private | Reads the upload and reports errors inline |

## Behaviour notes

- **The parse is cached.** `parse_resume` is wrapped in `st.cache_data` and
  keyed on the file bytes, so the PDF is decoded once instead of on every
  Streamlit re-run. Re-running the script is the default behaviour of
  Streamlit, and it happens on every keystroke in the job description box.
- **The size is checked** against `MAX_UPLOAD_BYTES` before the file is
  read, so an oversized upload is rejected without being parsed.
- **Errors are shown inline.** A file that cannot be parsed produces a
  readable message in the column instead of a traceback, and the app
  continues with an empty resume.
- **The preview is optional.** The extracted text is shown inside a collapsed
  expander, so the user can confirm the text was read correctly without the
  preview taking up the page.

## Used by

`app.py`.
