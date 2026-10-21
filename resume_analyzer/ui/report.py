"""
Downloadable analysis report.

Turns an :class:`~resume_analyzer.core.pipeline.Analysis` into a readable
plain-text report that the user can download.
"""

import streamlit as st


def build_report(analysis) -> str:
    """Render the analysis as a plain-text report."""
    lines = [
        "AI RESUME ANALYZER REPORT",
        "=" * 30,
        f"Overall Match Score: {analysis.match_score:.0f}%",
        "",
        "Matched Skills:",
        ", ".join(sorted(analysis.matched_skills)) or "None",
        "",
        "Missing Skills:",
        ", ".join(sorted(analysis.missing_skills)) or "None",
        "",
        "Recommendations:",
    ]
    lines += [f"- {recommendation}" for recommendation in analysis.recommendations]
    lines += ["", "ATS Formatting Notes:"]
    lines += [f"- {issue}" for issue in analysis.ats_issues] or ["- None"]
    return "\n".join(lines)


def render(analysis) -> None:
    """Render the report download button."""
    st.download_button(
        "Download Report (TXT)",
        data=build_report(analysis),
        file_name="resume_analysis_report.txt",
        mime="text/plain",
    )
