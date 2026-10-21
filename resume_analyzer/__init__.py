"""
AI Resume Analyzer.

A Streamlit application that scores a resume against a job description,
highlights missing skills and returns ATS-compatibility advice.

The package is split by responsibility:

* ``core``      - pure analysis logic (scoring, gaps, advice, ATS checks)
* ``parsers``   - text extraction from PDF / DOCX / TXT uploads
* ``skills``    - the curated skill database and the extraction algorithm
* ``ui``        - Streamlit rendering helpers
"""

__version__ = "2.0.0"
