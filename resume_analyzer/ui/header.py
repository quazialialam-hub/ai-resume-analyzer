"""
Page header.

Owns the page configuration, the custom styling and the "how it works"
sidebar, so the rest of the UI can focus on the analysis itself.
"""

import streamlit as st

from .styles import CSS


def render_header() -> None:
    """Render the page title, the styling and the "how it works" sidebar."""
    st.set_page_config(page_title="AI Resume Analyzer", page_icon=":page_facing_up:", layout="wide")
    st.markdown(CSS, unsafe_allow_html=True)
    st.title("AI Resume Analyzer")
    st.caption(
        "Match your resume against a job description, find missing skills, "
        "and get ATS-friendly recommendations."
    )
    with st.sidebar:
        st.header("How it works")
        st.write(
            "1. Upload your resume (PDF, DOCX or TXT)\n"
            "2. Paste the job description\n"
            "3. Click **Analyze** to get your match score, skill gaps and tips"
        )
        st.divider()
        st.write("Built with Python, Streamlit, NLP & Scikit-learn")
