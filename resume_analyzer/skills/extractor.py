"""
Skill extraction.

Normalises free text and matches it against the curated skill database and its
alias table. Matching is boundary aware, so "react" is not found inside
"reactive", and every pattern is compiled once and cached.
"""

import re

from .aliases import ALIASES
from .database import CASE_SENSITIVE_SKILLS, SKILL_DB

# Every surface form we can match, mapped onto the canonical skill name.
_SURFACE_FORMS = {form: ALIASES.get(form, form) for form in set(SKILL_DB) | set(ALIASES)}

_PATTERN_CACHE: dict = {}


def _normalize(text: str) -> str:
    """Lower-case text and drop punctuation, keeping the symbols skills use."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\s/]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _pattern_for(surface: str) -> re.Pattern:
    """Return the cached, boundary-aware matcher for a skill surface form."""
    if surface not in _PATTERN_CACHE:
        body = r"\s+".join(re.escape(token) for token in surface.split())
        _PATTERN_CACHE[surface] = re.compile(rf"(?<![a-z0-9]){body}(?![a-z0-9])")
    return _PATTERN_CACHE[surface]


def _exact_case_match(surface: str, text: str) -> bool:
    """
    Match an ambiguous surface form only in its canonical written form.

    "go" and "r" are ordinary English words, so they are only counted when
    they are written as "Go" and "R". The "&" is excluded from the boundary
    so that "R&D" is not read as the R language.
    """
    body = r"\s+".join(re.escape(token) for token in surface.capitalize().split())
    return bool(re.search(rf"(?<![A-Za-z0-9&]){body}(?![A-Za-z0-9&])", text))


def extract_skills(text: str) -> set:
    """Return the canonical skills mentioned in the given text."""
    normalized = _normalize(text)
    found = set()
    for surface, canonical in _SURFACE_FORMS.items():
        if surface in CASE_SENSITIVE_SKILLS:
            hit = _exact_case_match(surface, text)
        else:
            hit = _pattern_for(surface).search(normalized) is not None
        if hit:
            found.add(canonical)
    return found & set(SKILL_DB)
