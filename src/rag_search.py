#from embeddings import create_embeddings
#from chroma_store import search_chunks
from src.embeddings import create_embeddings
from src.chroma_store import search_chunks


def search_knowledge_base(query: str, n_results: int = 3):
    """
    Search the AI notes for information relevant to a question.
    """

    query_embedding = create_embeddings([query])[0]

    results = search_chunks(
        query_embedding=query_embedding,
        n_results=n_results
    )

    return results


if __name__ == "__main__":
    question = "What is Artificial Intelligence?"

    results = search_knowledge_base(question)

    print("\n🔎 Search results:\n")

    for i, document in enumerate(results["documents"][0], start=1):
        print(f"--- Result {i} ---")
        print(document[:1000])
        print()