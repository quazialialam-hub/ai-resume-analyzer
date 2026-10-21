# `resume_analyzer/ui/report.py`

**Path:** `resume_analyzer/ui/report.py`
**Purpose:** Builds the downloadable plain-text analysis report.

## What it does

Turns an `Analysis` into a readable text report and offers it as a download.

The report contains the overall score, the matched skills, the missing skills,
the recommendations and the ATS notes, in that order, with a heading and a
rule of `=` characters at the top.

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `build_report(analysis)` | function | Returns the report as a string |
| `render(analysis)` | function | Renders the download button |

## Behaviour notes

- `build_report` is a pure function and can be tested without Streamlit.
- Empty sections are written as "None" rather than being left blank, so the
  report always reads as a complete document.
- The file is offered as `resume_analysis_report.txt` with the
  `text/plain` MIME type, so it opens in any text editor.
- The report is a snapshot of the analysis that is on screen; it is not
  regenerated when the download is clicked.

## Used by

`app.py`.
