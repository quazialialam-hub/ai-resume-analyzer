# `resume_analyzer/ui/score_view.py`

**Path:** `resume_analyzer/ui/score_view.py`
**Purpose:** Renders the match score and the skill coverage chart.

## What it does

Draws the headline result: a card with the big percentage on the left and a
bar chart of the skill coverage on the right.

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `render_score_view(analysis)` | function | Renders the card and the chart |
| `_score_card(analysis)` | private | The score card |
| `_skill_chart(analysis)` | private | The coverage bar chart |

## Behaviour notes

- **The colour follows the band.** Green at or above `SCORE_STRONG`, amber
  at or above `SCORE_WEAK`, red below that. The thresholds come from
  `config.py`, so the colour and the written verdict can never disagree.
- **The verdict is written out** as well - "Strong match", "Moderate match"
  or "Weak match" - so the meaning does not depend on the colour alone.
- **The chart uses a plain dictionary.** `st.bar_chart` accepts a
  `{"Matched": n, "Missing": n}` mapping directly, which removed the need
  for `pandas` in this project.

## Used by

`ui/results.py`.
