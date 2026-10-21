"""
Skill detection.

A curated, easily extensible database of skills plus the matching algorithm
that finds them in free text.
"""

from .aliases import ALIASES
from .database import SKILL_DB
from .extractor import extract_skills

__all__ = ["ALIASES", "SKILL_DB", "extract_skills"]
