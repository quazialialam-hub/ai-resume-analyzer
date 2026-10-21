"""
Plain-text extraction from PDF resumes.
"""

import io

from pypdf import PdfReader


def extract_text_from_pdf(data: bytes) -> str:
    """Return the text of every page of a PDF, joined by newlines."""
    reader = PdfReader(io.BytesIO(data))
    parts = [(page.extract_text() or "") for page in reader.pages]
    return "\n".join(parts)
