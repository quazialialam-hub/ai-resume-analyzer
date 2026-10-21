# `resume_analyzer/ui/styles.py`

**Path:** `resume_analyzer/ui/styles.py`
**Purpose:** The custom CSS used by the results view.

## What it does

Holds a single CSS string that Streamlit injects into the page. Keeping it in
one module means the look of the app can be changed without touching any
logic.

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `CSS` | constant | The stylesheet, as a string |

## Classes

| Class | Applied to | Style |
| --- | --- | --- |
| `.big-score` | The match percentage | 3rem, bold |
| `.score-card` | The card around the score | Padded panel with a light border |
| `.skill-pill` | Every skill pill | Rounded, inline label |
| `.matched` | A matched skill pill | Green background |
| `.missing` | A missing skill pill | Red background |

## Notes

- The stylesheet uses `unsafe_allow_html=True` when it is injected, which is
  why it is applied through `st.markdown` rather than through a Streamlit
  theme file. The content is a static, developer-controlled string - no user
  input is ever interpolated into it.
- The classes are used by `score_view.py` and `skill_view.py`.

## Used by

`ui/header.py`.
