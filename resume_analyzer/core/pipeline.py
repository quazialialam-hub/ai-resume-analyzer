"""
End-to-end analysis pipeline.

Ties the individual analysis steps together and returns a single result object,
so the UI layer can render a completed analysis without knowing how any of the
individual scores were computed.
"""

from dataclasses import dataclass, field

from ..skills.extractor import extract_skills
from . import ats_check, recommendations, scoring, skill_gap


@dataclass
class Analysis:
    """Everything the UI needs in order to render a completed analysis."""

    match_score: float = 0.0
    matched_skills: set = field(default_factory=set)
    missing_skills: set = field(default_factory=set)
    recommendations: list = field(default_factory=list)
    ats_issues: list = field(default_factory=list)


def run_analysis(resume_text: str, job_description: str) -> Analysis:
    """Score a resume against a job description and collect all findings."""
    match_score = scoring.compute_match_score(resume_text, job_description)
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)
    missing = skill_gap.get_missing_skills(resume_skills, jd_skills)
    return Analysis(
        match_score=match_score,
        matched_skills=skill_gap.get_matched_skills(resume_skills, jd_skills),
        missing_skills=missing,
        recommendations=recommendations.generate_recommendations(
            match_score, missing, resume_text
        ),
        ats_issues=ats_check.check_ats_formatting(resume_text),
    )
