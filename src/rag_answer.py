import os

from dotenv import load_dotenv
from openai import OpenAI

from rag_search import search_knowledge_base


load_dotenv()


# Load API settings from .env
api_key = os.getenv("OPENROUTER_API_KEY")
model = os.getenv("MODEL")


# Create OpenRouter client
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


def build_context(results) -> str:
    """Combine retrieved documents into one context string."""

    documents = results.get("documents", [[]])[0]

    return "\n\n".join(
        f"Source {i}: {document}"
        for i, document in enumerate(documents, start=1)
    )


def answer_question(question: str, n_results: int = 3) -> str:
    """
    Retrieve relevant information from the AI notes
    and generate an answer using the LLM.
    """

    # Retrieve relevant chunks from ChromaDB
    results = search_knowledge_base(
        question,
        n_results=n_results
    )

    context = build_context(results)

    # Ask the LLM to answer using only the retrieved context
    prompt = f"""
You are Edu-Assist AI, an educational assistant.

Answer the student's question using ONLY the information
provided in the context below.

If the answer cannot be found in the context, say:
"I could not find this information in the provided notes."

Context:
{context}

Student Question:
{question}

Give a clear and easy-to-understand answer.
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=500,
        temperature=0.2
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    question = "What is Artificial Intelligence?"

    answer = answer_question(question)

    print("\n🤖 Edu-Assist AI Answer:\n")
    print(answer)