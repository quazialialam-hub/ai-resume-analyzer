"""
Central configuration for the AI Resume Analyzer.

Every tunable threshold, limit and label used across the package lives here so
behaviour can be adjusted in one place instead of being hard-coded in several
modules.
"""

# Match-score bands, in percentage points.
SCORE_WEAK = 40.0
SCORE_STRONG = 70.0

# Upload guard rails.
MAX_UPLOAD_BYTES = 10 * 1024 * 1024  # 10 MB
SUPPORTED_EXTENSIONS = ("pdf", "docx", "txt")

# Text encodings tried, in order, when decoding a plain-text resume.
SUPPORTED_ENCODINGS = ("utf-8", "utf-16", "cp1252", "latin-1")

# Resume length guidance, measured in words.
MIN_RESUME_WORDS = 150
MAX_RESUME_WORDS = 1200

# How many missing skills are named in a single recommendation.
MAX_MISSING_SKILLS_SHOWN = 8

# Minimum number of text lines before a resume is considered "structured".
ATS_MIN_LINES = 5
