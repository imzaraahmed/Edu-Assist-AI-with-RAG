from pdf_loader import load_pdf
from text_splitter import split_text
from embeddings import create_embeddings
from chroma_store import store_chunks


PDF_FILE = "ai_notes.pdf.pdf"


def build_rag():
    print("1. Loading PDF...")
    text = load_pdf(PDF_FILE)
    print(f"Extracted {len(text)} characters.")

    print("\n2. Splitting text...")
    chunks = split_text(text)
    print(f"Created {len(chunks)} chunks.")

    print("\n3. Creating embeddings...")
    embeddings = create_embeddings(chunks)
    print(f"Created {len(embeddings)} embeddings.")

    print("\n4. Storing in ChromaDB...")
    store_chunks(chunks, embeddings)

    print("\n✅ RAG knowledge base created successfully!")


if __name__ == "__main__":
    build_rag()