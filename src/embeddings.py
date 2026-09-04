from sentence_transformers import SentenceTransformer


# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks: list[str]):
    """
    Convert text chunks into numerical embeddings.
    """
    if not chunks:
        return []

    embeddings = model.encode(
        chunks,
        show_progress_bar=True
    )

    return embeddings.tolist()


if __name__ == "__main__":
    test_chunks = [
        "Artificial Intelligence is the study of intelligent machines.",
        "Machine learning is a part of Artificial Intelligence."
    ]

    embeddings = create_embeddings(test_chunks)

    print("Number of embeddings:", len(embeddings))
    print("Embedding dimensions:", len(embeddings[0]))