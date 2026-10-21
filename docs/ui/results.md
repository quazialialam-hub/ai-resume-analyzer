# `resume_analyzer/ui/results.py`

**Path:** `resume_analyzer/ui/results.py`
**Purpose:** Composes the results view out of its individual sections.

## What it does

Renders the complete result page in the order a reader needs it:

1. The score card and the skill coverage chart (`score_view.py`)
2. A divider
3. The matched and missing skill pills (`skill_view.py`)
4. A divider
5. The personalised recommendations
6. The ATS compatibility notes

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `render(analysis)` | function | Renders every results section |
| `render_recommendations(analysis)` | function | The advice list |
| `render_ats_notes(analysis)` | function | The ATS warnings |

## Behaviour notes

- The module only composes; it holds no formatting logic of its own. That
  keeps each section independently changeable.
- The recommendations are rendered as a Markdown list, one line per item.
- The ATS notes use the word "Warning" as the marker for each issue, and the
  section shows a positive line when nothing was found.
- The `Analysis` object is passed straight through, so the view never
  recomputes a score or re-reads a skill set.

## Used by

`app.py`.
