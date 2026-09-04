import chromadb


# Create a local ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")


# Create or load our collection
collection = client.get_or_create_collection(
    name="ai_notes"
)


def store_chunks(chunks: list[str], embeddings: list[list[float]]):
    """
    Store text chunks and their embeddings in ChromaDB.
    """

    if not chunks:
        return

    if len(chunks) != len(embeddings):
        raise ValueError(
            "The number of chunks must match the number of embeddings."
        )

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")


def search_chunks(query_embedding: list[float], n_results: int = 3):
    """
    Search ChromaDB for chunks similar to the query.
    """

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results


if __name__ == "__main__":
    print("ChromaDB is working!")
    print("Collection:", collection.name)
    print("Documents currently stored:", collection.count())