# `resume_analyzer/ui/header.py`

**Path:** `resume_analyzer/ui/header.py`
**Purpose:** Renders the page title, the custom styling and the sidebar.

## What it does

Draws the fixed part of the page:

- the page configuration - title, icon and wide layout
- the custom CSS from `styles.py`
- the page title and the caption
- the "How it works" sidebar

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `render_header()` | function | Renders the header and the sidebar |

## Behaviour notes

- `st.set_page_config` must be the first Streamlit command of the session, so
  `render_header()` is called before anything else in `app.py`.
- The page icon is given as the shortcode `:page_facing_up:` rather than an
  emoji, so the project stays free of emoji characters.
- The sidebar explains the three steps - upload, paste, analyse - and names
  the technology stack, so a first-time user knows what to do without
  reading the README.

## Used by

`app.py`.
