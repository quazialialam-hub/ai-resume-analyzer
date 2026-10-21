"""
Input controls.

Owns everything the user interacts with before the analysis runs: the resume
upload and the job-description box. Reading the upload is cached, so
re-running the Streamlit script does not re-parse the PDF on every
interaction.
"""

import streamlit as st

from ..config import MAX_UPLOAD_BYTES
from ..parsers.factory import extract_text


@st.cache_data(show_spinner=False, max_entries=32)
def parse_resume(data: bytes, filename: str) -> str:
    """Extract the text of an uploaded resume, cached per file."""
    return extract_text(data, filename)


def _read_upload(uploaded) -> str:
    """Read an uploaded resume and report any problem inline."""
    if uploaded is None:
        return ""
    if uploaded.size > MAX_UPLOAD_BYTES:
        st.error("That file is too large. Please upload a resume of 10 MB or less.")
        return ""
    try:
        return parse_resume(uploaded.getvalue(), uploaded.name)
    except Exception as exc:  # noqa: BLE001 - the message is shown to the user
        st.error(f"Could not read file: {exc}")
        return ""


def render_inputs() -> tuple:
    """Render the upload and job-description inputs and return their values."""
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Upload Resume")
        uploaded = st.file_uploader(
            "Upload your resume", type=["pdf", "docx", "txt"], label_visibility="collapsed"
        )
        resume_text = _read_upload(uploaded)
        if resume_text:
            with st.expander("Preview extracted resume text"):
                st.text_area(
                    "Resume text", resume_text, height=200, label_visibility="collapsed"
                )
    with col2:
        st.subheader("2. Paste Job Description")
        job_description = st.text_area(
            "Job description",
            height=280,
            label_visibility="collapsed",
            placeholder="Paste the full job description here...",
        )
    return resume_text, job_description
