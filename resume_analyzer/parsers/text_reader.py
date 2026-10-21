"""
Plain-text extraction from TXT resumes.
"""

from ..config import SUPPORTED_ENCODINGS


def extract_text_from_txt(data: bytes) -> str:
    """
    Decode a TXT resume, trying the supported encodings in order.

    Falls back to a lossy UTF-8 decode so that a slightly corrupt file still
    produces usable text instead of an error.
    """
    for encoding in SUPPORTED_ENCODINGS:
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="ignore")
