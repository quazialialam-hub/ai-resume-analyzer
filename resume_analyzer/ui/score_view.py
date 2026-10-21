"""
Match score view.

Renders the headline match score and the skill coverage chart.
"""

import streamlit as st

from ..config import SCORE_STRONG, SCORE_WEAK


def _score_card(analysis) -> None:
    """Render the large match-score card."""
    score = analysis.match_score
    color = "#28a745" if score >= SCORE_STRONG else "#ffc107" if score >= SCORE_WEAK else "#dc3545"
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    st.markdown("**Overall Match Score**")
    st.markdown(
        f'<div class="big-score" style="color:{color}">{score:.0f}%</div>',
        unsafe_allow_html=True,
    )
    if score >= SCORE_STRONG:
        st.write("Strong match")
    elif score >= SCORE_WEAK:
        st.write("Moderate match")
    else:
        st.write("Weak match")
    st.markdown("</div>", unsafe_allow_html=True)


def _skill_chart(analysis) -> None:
    """Render the matched/missing skill coverage bar chart."""
    st.markdown("**Skill Coverage**")
    coverage = {
        "Matched": len(analysis.matched_skills),
        "Missing": len(analysis.missing_skills),
    }
    st.bar_chart(coverage)


def render_score_view(analysis) -> None:
    """Render the score card next to the skill coverage chart."""
    score_col, chart_col = st.columns([1, 2])
    with score_col:
        _score_card(analysis)
    with chart_col:
        _skill_chart(analysis)
