"""
ATS-compatibility heuristics.

Runs plain-text checks for the resume problems that most often break Applicant
Tracking Systems: exotic symbols, no standard section headers, a missing
contact e-mail and layouts that collapse when converted to text.
"""

import re

from ..config import ATS_MIN_LINES

# Symbols that commonly break ATS parsers: dashes, bullet glyphs, tick marks.
_RISKY_SYMBOLS = re.compile(r"[\u2013\u2014\u2022\u25cf\u25aa\u2713\u2714\u00a0\u00ae\u2122]")

_EMAIL = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

_SECTIONS = {
    "Experience": r"experience|employment|work history|professional background",
    "Education": r"education|academic background|qualifications",
    "Skills": r"skills|technical skills|competencies",
}


def _check_symbols(resume_text: str) -> list:
    """Flag symbols that some ATS parsers mis-read."""
    if _RISKY_SYMBOLS.search(resume_text):
        return [
            "Unusual symbols (dashes, bullet glyphs, tick marks) detected - some ATS "
            "systems misread these. Stick to standard characters and simple hyphens."
        ]
    return []


def _check_structure(resume_text: str) -> list:
    """Flag resumes whose layout cannot be reconstructed from text alone."""
    if len(resume_text.splitlines()) < ATS_MIN_LINES:
        return [
            "Very little line structure was detected. If your resume uses text boxes, "
            "columns or graphics, ATS systems may fail to parse it - use a single-column "
            "standard format."
        ]
    return []


def _check_sections(resume_text: str) -> list:
    """Flag missing standard section headers."""
    lowered = resume_text.lower()
    issues = []
    for label, pattern in _SECTIONS.items():
        if not re.search(pattern, lowered):
            issues.append(
                f"No clear '{label}' section header detected - use standard section titles."
            )
    return issues


def _check_contact(resume_text: str) -> list:
    """Flag a missing contact e-mail address."""
    if not _EMAIL.search(resume_text):
        return [
            "No email address detected - make sure your contact info is plain text, not an image."
        ]
    return []


def check_ats_formatting(resume_text: str) -> list:
    """Return every ATS issue detected in the given resume text."""
    issues = []
    issues += _check_symbols(resume_text)
    issues += _check_structure(resume_text)
    issues += _check_sections(resume_text)
    issues += _check_contact(resume_text)
    return issues
