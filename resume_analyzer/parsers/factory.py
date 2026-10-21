"""
Resume format dispatch.

Picks the right extractor for an uploaded file and normalises the result, so
the rest of the application only ever deals with plain text.
"""

from ..config import SUPPORTED_EXTENSIONS
from .docx_reader import extract_text_from_docx
from .pdf_reader import extract_text_from_pdf
from .text_reader import extract_text_from_txt

_EXTRACTORS = {
    "pdf": extract_text_from_pdf,
    "docx": extract_text_from_docx,
    "txt": extract_text_from_txt,
}


def extract_text(data: bytes, filename: str) -> str:
    """
    Extract the text of an uploaded resume.

    Raises ValueError for unsupported formats and for files that contain no
    readable text, so the caller can show a helpful message to the user.
    """
    extension = filename.rsplit(".", 1)[-1].lower()
    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError("Unsupported file type. Please upload a PDF, DOCX or TXT file.")
    text = _EXTRACTORS[extension](data).strip()
    if not text:
        raise ValueError(
            "No readable text found in the file (it may be a scanned or image-based PDF)."
        )
    return text
