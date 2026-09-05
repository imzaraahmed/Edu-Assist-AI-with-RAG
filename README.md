🎓 Edu-Assist AI

Learn smarter. Understand deeper.

Edu-Assist AI is an AI-powered study companion that helps students understand concepts from their Artificial Intelligence course notes.

The application uses Retrieval-Augmented Generation (RAG) to search relevant information from the provided course notes and then generate clear, easy-to-understand answers using an LLM.

✨ Features
🧠 Understand Concepts — Get simple explanations of AI concepts from the notes.
🔎 Search My Notes — Ask questions about topics covered in the course material.
📚 Lecture Help — Get explanations of difficult lecture topics.
💡 Study Examples — Ask for examples related to concepts in the notes.
💬 Custom Questions — Ask your own questions about the study material.
📖 RAG-based Answers — Retrieves relevant information from the knowledge base before generating an answer.
🚫 Out-of-Notes Protection — If the requested information cannot be found in the provided notes, the application tells the user instead of inventing an answer.
🌙 Modern Dark UI — Built with an interactive Streamlit interface.
🏗️ How It Works

The application follows a Retrieval-Augmented Generation pipeline:

Student Question
       ↓
Streamlit Interface
       ↓
Question Embedding
       ↓
ChromaDB Vector Search
       ↓
Relevant Course Note Chunks
       ↓
Context + Student Question
       ↓
OpenRouter LLM
       ↓
AI Generated Answer
RAG Pipeline
The student's question is received by the Streamlit application.
The question is converted into an embedding using Sentence Transformers.
ChromaDB searches the vector database for the most relevant note chunks.
The retrieved information is combined into a context.
The context and question are sent to the configured LLM through OpenRouter.
The AI generates an answer using the retrieved course material.
🛠️ Technologies Used
Technology	Purpose
Python	Application development
Streamlit	Web interface
ChromaDB	Vector database
Sentence Transformers	Text embeddings
OpenRouter	LLM API
OpenAI Python SDK	API communication
PyPDF	PDF text extraction
python-dotenv	Environment variable management
📁 Project Structure
Edu-Assist-AI-with-rag/
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
├── .env
│
├── config/
│
├── data/
│
├── knowledge_base/
│
├── chroma_db/
│
├── output/
│
└── src/
    ├── build_rag.py
    ├── chroma_store.py
    ├── embeddings.py
    ├── pdf_loader.py
    ├── rag_answer.py
    ├── rag_search.py
    ├── text_splitter.py
    ├── crew.py
    └── tools/

.env, chroma_db/, generated files, and other ignored files should not be committed to GitHub.

⚙️ Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd Edu-Assist-AI-with-rag
2. Create a virtual environment

Windows:

py -m venv .venv

Activate it:

.venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
🔐 Environment Variables

Create a .env file in the project root:

OPENROUTER_API_KEY=your_api_key_here
MODEL=your_model_name

The project already includes .env in .gitignore.

📚 Knowledge Base

The application uses Artificial Intelligence course notes as its knowledge source.

The notes are:

Loaded from PDF.
Converted into text.
Split into smaller chunks.
Converted into vector embeddings.
Stored in ChromaDB.
Retrieved when a student asks a question.
▶️ Running the Application

Activate your virtual environment:

.venv\Scripts\activate

Run Streamlit:

streamlit run app.py

The application will open in your browser.

💬 Example Questions

You can ask questions such as:

What is Artificial Intelligence?
Explain machine learning in simple words.
What are the main topics covered in my notes?

You can also ask questions that are not covered by the notes. In that case, Edu-Assist AI is designed to respond that the information could not be found in the provided notes.

🎯 Project Goal

The goal of Edu-Assist AI is to demonstrate how Retrieval-Augmented Generation (RAG) can be used to build an educational AI assistant that answers questions based on a specific knowledge source rather than relying only on general model knowledge.

This project combines:

PDF Processing → Embeddings → Vector Search → Retrieval → LLM → Student-Friendly Answer

👩‍💻 Author

Zara Ahmed

Aspiring AI & Data Science Engineer | Student at SMIT

Skills demonstrated

Python RAG ChromaDB Streamlit AI LLMs Embeddings Vector Search

⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
