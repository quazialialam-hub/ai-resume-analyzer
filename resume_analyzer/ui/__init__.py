"""
Streamlit presentation layer.

Every module in this package renders part of the page and nothing else, so the
analysis logic stays completely independent of the UI framework.
"""

from . import header, inputs, report, results, score_view, skill_view, styles

__all__ = [
    "header",
    "inputs",
    "report",
    "results",
    "score_view",
    "skill_view",
    "styles",
]
