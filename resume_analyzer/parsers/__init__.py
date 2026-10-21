"""
Resume text extraction.

Each reader works on raw bytes so that the parsers stay independent of
Streamlit and can be reused by a CLI or an API.
"""

from .docx_reader import extract_text_from_docx
from .factory import extract_text
from .pdf_reader import extract_text_from_pdf
from .text_reader import extract_text_from_txt

__all__ = [
    "extract_text",
    "extract_text_from_docx",
    "extract_text_from_pdf",
    "extract_text_from_txt",
]
