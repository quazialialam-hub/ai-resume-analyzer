# `requirements.txt`

**Path:** `requirements.txt` (project root)
**Purpose:** The third-party dependencies of the project.

## What it does

Pins the minimum version of every package the application needs. The
installed launcher (`run.bat`) reads this file to set up the environment.

## Dependencies

| Package | Minimum | Why it is needed |
| --- | --- | --- |
| `streamlit` | 1.30.0 | The web interface |
| `scikit-learn` | 1.3.0 | TF-IDF vectorisation and cosine similarity |
| `pypdf` | 4.0.0 | Text extraction from PDF resumes |
| `python-docx` | 1.0.0 | Text extraction from DOCX resumes |

## Changes in this version

- **`pandas` was removed.** It was used for a single two-row bar chart, and
  `st.bar_chart` accepts a plain dictionary instead. This removes roughly
  60 MB of install weight, NumPy included.
- **`PyPDF2` was replaced by `pypdf`.** `PyPDF2` has not been updated since
  2022; `pypdf` is its actively maintained successor and is a drop-in
  replacement for the way the project uses it.

## Notes

- Only the direct dependencies are listed. Their own dependencies are
  resolved by pip.
- The versions are lower bounds, not exact pins, so a fresh install gets the
  latest compatible release of each package.
