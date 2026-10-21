"""
AI Resume Analyzer - Streamlit application.

Uploads a resume and a job description, scores the match, lists the skill gaps
and returns ATS-friendly improvement advice.

Run with:

    streamlit run app.py
"""

import streamlit as st

from resume_analyzer.core.pipeline import run_analysis
from resume_analyzer.ui import header, inputs, report, results


def main() -> None:
    """Render the page and run the analysis when the user asks for it."""
    header.render_header()
    resume_text, job_description = inputs.render_inputs()

    st.divider()
    if not st.button("Analyze Resume", type="primary"):
        return
    if not resume_text.strip():
        st.warning("Please upload a resume first.")
        return
    if not job_description.strip():
        st.warning("Please paste a job description first.")
        return

    with st.spinner("Analyzing resume against job description..."):
        analysis = run_analysis(resume_text, job_description)

    st.success("Analysis complete!")
    results.render(analysis)
    report.render(analysis)


if __name__ == "__main__":
    main()
