from crewai.tools import BaseTool
from pydantic import BaseModel, Field

from src.rag_search import search_knowledge_base


class RAGToolInput(BaseModel):
    question: str = Field(
        ...,
        description="The student's question about Artificial Intelligence."
    )


class RAGTool(BaseTool):
    name: str = "AI Notes RAG Search"
    description: str = (
        "Searches the Artificial Intelligence course notes "
        "stored in the RAG knowledge base and returns relevant information."
    )
    args_schema: type[BaseModel] = RAGToolInput

    def _run(self, question: str) -> str:
        results = search_knowledge_base(
            question,
            n_results=3
        )

        documents = results.get("documents", [[]])[0]

        if not documents:
            return "No relevant information was found in the AI notes."

        return "\n\n".join(
            f"Source {i}: {document}"
            for i, document in enumerate(documents, start=1)
        )