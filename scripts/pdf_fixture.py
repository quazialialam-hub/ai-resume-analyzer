"""
Minimal PDF fixture builder for the smoke test.

Writes a single-page PDF that contains a given block of text. The file is
built by hand so the smoke test needs no extra dependency such as reportlab.
"""

from pathlib import Path


def _pdf_bytes(text: str) -> bytes:
    """Build a minimal single-page PDF that renders the given text."""
    body = "BT /F1 11 Tf 40 760 Td 13 TL " + " ".join(
        f"({line}) Tj T*" for line in text.splitlines()
    ) + " ET"
    parts = [
        "<< /Type /Catalog /Pages 2 0 R >>",
        "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        f"<< /Length {len(body)} >>\nstream\n{body}\nendstream",
    ]
    out = "%PDF-1.4\n"
    offsets = []
    for index, part in enumerate(parts, start=1):
        offsets.append(len(out))
        out += f"{index} 0 obj\n{part}\nendobj\n"
    start = len(out)
    out += f"xref\n0 {len(parts) + 1}\n0000000000 65535 f \n"
    out += "".join(f"{offset:010d} 00000 n \n" for offset in offsets)
    out += f"trailer\n<< /Size {len(parts) + 1} /Root 1 0 R >>\nstartxref\n{start}\n%%EOF\n"
    return out.encode("latin-1")


def write_pdf(directory: Path, text: str) -> Path:
    """Write the given text as a single-page PDF inside the directory."""
    path = directory / "resume.pdf"
    path.write_bytes(_pdf_bytes(text))
    return path
