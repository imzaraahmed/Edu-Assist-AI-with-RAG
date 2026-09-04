import os

from dotenv import load_dotenv
from crewai import Agent, Crew, Task, LLM

from src.tools.rag_tool import RAGTool


load_dotenv()


# Load OpenRouter settings from .env
api_key = os.getenv("OPENROUTER_API_KEY")
model = os.getenv("MODEL")


# Configure CrewAI to use OpenRouter
llm = LLM(
    model=f"openrouter/{model}",
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


# Create the RAG tool
rag_tool = RAGTool()


# Create the Edu-Assist AI agent
edu_assistant = Agent(
    role="AI Course Assistant",
    goal="Answer students' questions using the provided Artificial Intelligence course notes.",
    backstory=(
        "You are an educational AI assistant. "
        "You help students understand Artificial Intelligence concepts "
        "using their course notes."
    ),
    tools=[rag_tool],
    llm=llm,
    verbose=True
)


# Create the question-answering task
answer_task = Task(
    description=(
        "Answer the student's question using the AI course notes. "
        "Always use the AI Notes RAG Search tool before answering. "
        "Do not invent information that is not supported by the notes.\n\n"
        "Student question: {question}"
    ),
    expected_output=(
        "A clear, accurate and easy-to-understand answer "
        "based on the provided AI course notes."
    ),
    agent=edu_assistant
)


# Create the Crew
edu_crew = Crew(
    agents=[edu_assistant],
    tasks=[answer_task],
    verbose=True
)


if __name__ == "__main__":
    question = input("Enter your question: ")

    result = edu_crew.kickoff(
        inputs={"question": question}
    )

    print("\n🤖 Edu-Assist AI:\n")
    print(result)