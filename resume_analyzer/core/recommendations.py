"""
Recommendation engine (part 1).

Turns the numeric match score and the detected skill gaps into short, concrete
actions that improve the chance of passing an ATS filter.
"""

from ..config import MAX_MISSING_SKILLS_SHOWN, SCORE_STRONG, SCORE_WEAK
from .style_advice import style_advice


def _score_advice(match_score: float) -> str:
    """Return overall-fit advice for the band the score falls into."""
    if match_score < SCORE_WEAK:
        return (
            "Your resume has low overlap with this job description. Tailor your summary "
            "and experience sections to mirror the language used in the posting."
        )
    if match_score < SCORE_STRONG:
        return (
            "Your resume partially matches this role. Strengthen alignment by weaving "
            "more of the job description's key terms into your bullet points."
        )
    return "Strong overall match! Fine-tune the remaining gaps below to maximize ATS scoring."


def _skill_advice(missing_skills: set) -> list:
    """Return advice about the skills the candidate is missing."""
    if not missing_skills:
        return []
    top = ", ".join(sorted(missing_skills)[:MAX_MISSING_SKILLS_SHOWN])
    return [
        f"Add these missing skills/keywords where genuinely applicable: {top}.",
        "If you have experience with these skills but didn't mention them, add a concrete "
        "example (a project or an achievement) rather than just listing the keyword.",
    ]


def generate_recommendations(match_score: float, missing_skills: set, resume_text: str) -> list:
    """Build the full, ordered list of recommendations for a resume."""
    recs = [_score_advice(match_score)]
    recs += _skill_advice(missing_skills)
    recs += style_advice(resume_text)
    return recs
