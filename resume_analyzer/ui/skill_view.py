"""
Skill breakdown view.

Renders the matched and missing skills as coloured pills, side by side.
"""

import streamlit as st


def _skill_pills(title: str, skills: set, css_class: str, empty_message: str) -> None:
    """Render one column of skill pills."""
    st.markdown(f"**{title}**")
    if not skills:
        st.write(empty_message)
        return
    pills = "".join(
        f'<span class="skill-pill {css_class}">{skill}</span>' for skill in sorted(skills)
    )
    st.markdown(pills, unsafe_allow_html=True)


def render_skill_breakdown(analysis) -> None:
    """Render the matched and missing skill columns."""
    st.subheader("Skill Breakdown")
    matched_col, missing_col = st.columns(2)
    with matched_col:
        _skill_pills(
            "Matched Skills", analysis.matched_skills, "matched", "No overlapping skills found."
        )
    with missing_col:
        _skill_pills(
            "Missing Skills",
            analysis.missing_skills,
            "missing",
            "Great - no missing skills detected!",
        )
