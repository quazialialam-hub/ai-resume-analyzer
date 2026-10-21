"""
Results view.

Composes the individual result sections: the score, the skill breakdown, the
recommendations and the ATS compatibility notes.
"""

import streamlit as st

from .score_view import render_score_view
from .skill_view import render_skill_breakdown


def render_recommendations(analysis) -> None:
    """Render the personalised recommendations."""
    st.subheader("Personalized Recommendations")
    for recommendation in analysis.recommendations:
        st.write(f"- {recommendation}")


def render_ats_notes(analysis) -> None:
    """Render the ATS compatibility notes."""
    st.subheader("ATS Compatibility Check")
    if analysis.ats_issues:
        for issue in analysis.ats_issues:
            st.write(f"- Warning: {issue}")
    else:
        st.write("No obvious ATS formatting issues detected.")


def render(analysis) -> None:
    """Render every section of the results view."""
    render_score_view(analysis)
    st.divider()
    render_skill_breakdown(analysis)
    st.divider()
    render_recommendations(analysis)
    render_ats_notes(analysis)
