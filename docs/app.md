# `app.py`

**Path:** `app.py` (project root)
**Purpose:** Streamlit entry point.

## What it does

`app.py` is the only executable script in the project. It is the file
Streamlit loads, and it does exactly four things:

1. Renders the page header and sidebar (`ui/header.py`).
2. Renders the upload and job-description controls (`ui/inputs.py`).
3. On a click of the "Analyze Resume" button, validates the input and calls
   the analysis pipeline (`core/pipeline.py`).
4. Renders the results and the download button (`ui/results.py`,
   `ui/report.py`).

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `main()` | function | Renders the page and runs the analysis when requested. |

## Flow

```
header -> inputs -> validate input -> run_analysis() -> results.render() -> report.render()
```

The button check happens before the validation checks, so an empty form
produces no warnings until the user actually asks for an analysis. A missing
resume shows "Please upload a resume first."; a missing job description shows
"Please paste a job description first."

## Notes

- `main()` is called under `if __name__ == "__main__":`. Streamlit executes
  the script with `__name__` set to `"__main__"`, so the guard does not
  interfere with `streamlit run app.py`.
- The file is intentionally thin. Every piece of behaviour lives in the
  package so it can be tested without a browser.
