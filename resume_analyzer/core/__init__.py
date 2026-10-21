"""
Core analysis logic.

Pure functions only - no Streamlit imports - so every step can be unit tested
without a browser session.
"""

from .ats_check import check_ats_formatting
from .pipeline import Analysis, run_analysis
from .recommendations import generate_recommendations
from .scoring import compute_match_score
from .skill_gap import get_matched_skills, get_missing_skills
from .style_advice import style_advice

__all__ = [
    "Analysis",
    "check_ats_formatting",
    "compute_match_score",
    "generate_recommendations",
    "get_matched_skills",
    "get_missing_skills",
    "run_analysis",
    "style_advice",
]
