from pathlib import Path
from pypdf import PdfReader


def load_pdf(pdf_path: str) -> str:
    """Extract text from all pages of a PDF."""

    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    reader = PdfReader(str(path))

    pages_text = []

    for page in reader.pages:
        text = page.extract_text() or ""
        pages_text.append(text)

    return "\n\n".join(pages_text)


if __name__ == "__main__":
    pdf_file = "ai_notes.pdf.pdf"

    text = load_pdf(pdf_file)

    print(f"Extracted characters: {len(text)}")
    print("\nFirst 2000 characters:\n")
    print(text[:2000])