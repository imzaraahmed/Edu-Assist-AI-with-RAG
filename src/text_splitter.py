from typing import List


def split_text(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> List[str]:
    """
    Split extracted PDF text into overlapping chunks.
    """

    if not text.strip():
        return []

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - chunk_overlap

    return chunks


if __name__ == "__main__":
    from pdf_loader import load_pdf

    text = load_pdf("ai_notes.pdf.pdf")
    chunks = split_text(text)

    print(f"Total characters: {len(text)}")
    print(f"Total chunks: {len(chunks)}")

    print("\nFirst chunk:\n")
    print(chunks[0])