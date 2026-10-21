"""
Recommendation engine (part 2).

Checks the writing quality of a resume: whether achievements are quantified,
whether bullet points start with passive filler, and whether the resume is a
sensible length.
"""

import re

from ..config import MAX_RESUME_WORDS, MIN_RESUME_WORDS

_QUANTIFIED = re.compile(r"\d+%|\$\d+|\d+\+|\bincreased\b|\bimproved\b|\breduced\b", re.I)
_WEAK_PHRASES = ("responsible for", "worked on", "helped with", "duties included")


def _style_advice(resume_text: str) -> list:
    """Return advice about impact statements and bullet-point phrasing."""
    advice = []
    if not _QUANTIFIED.search(resume_text):
        advice.append(
            "Quantify your achievements with numbers or percentages (e.g. 'improved "
            "processing speed by 30%') so impact is obvious to recruiters and ATS parsers."
        )
    if any(phrase in resume_text.lower() for phrase in _WEAK_PHRASES):
        advice.append(
            "Replace passive phrases like 'responsible for' or 'worked on' with strong "
            "action verbs such as 'led', 'built', 'optimized' or 'delivered'."
        )
    return advice


def _length_advice(resume_text: str) -> list:
    """Return advice about resume length."""
    words = len(resume_text.split())
    if words < MIN_RESUME_WORDS:
        return ["Your resume seems short - add detail on relevant projects and achievements."]
    if words > MAX_RESUME_WORDS:
        return ["Your resume is quite long - trim it to 1-2 pages of the most relevant content."]
    return []


def style_advice(resume_text: str) -> list:
    """Return every writing-quality recommendation for the given resume."""
    return _style_advice(resume_text) + _length_advice(resume_text)
