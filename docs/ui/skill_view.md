# `resume_analyzer/ui/skill_view.py`

**Path:** `resume_analyzer/ui/skill_view.py`
**Purpose:** Renders the matched and missing skills as coloured pills.

## What it does

Shows the skill breakdown as two columns of labels - green for the skills the
candidate already has, red for the ones the job wants and the resume does
not mention.

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `render_skill_breakdown(analysis)` | function | Renders both columns |
| `_skill_pills(title, skills, css_class, empty_message)` | private | Renders one column |

## Behaviour notes

- The skills are sorted alphabetically, so the same analysis always produces
  the same layout.
- Each pill is an HTML `span` with the `.skill-pill` class from
  `styles.py`, plus `.matched` or `.missing` for the colour.
- An empty column shows a short positive message instead of an empty area:
  "No overlapping skills found." for matched, and "Great - no missing skills
  detected!" for missing.
- The skill names come from the curated database and from the alias table, so
  they are developer-controlled strings. They are still inserted as HTML, so
  the database must not be filled with untrusted content.

## Used by

`ui/results.py`.
