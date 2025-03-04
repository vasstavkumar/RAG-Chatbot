# RAG-Chatbot

This project is a **Retrieval-Augmented Generation (RAG) Chatbot** built with **FastAPI, LangChain, ChromaDB, and Streamlit**. It enables users to upload multiple documents, process them, and query for relevant responses.

**Chunking** - Recursive Character Splitter
**Embedding** - sentence-transformers/all-MiniLM-L6-v2 model
**LLM** - Groq llama3-70b-8192 model

## 📁 Project Structure

```
RAG-Chatbot/
│── backend/
│   ├── chroma_utils.py
│   ├── db_utils.py
│   ├── pydantic_models.py
│   ├── main.py
│   ├── langchain_utils.py
│   ├── requirements.txt
│   ├── Dockerfile
│
│── frontend/
│   ├── api_utils.py
│   ├── streamlit_app.py
│   ├── chat_interface.py
│   ├── sidebar.py
│   ├── requirements.txt
│   ├── Dockerfile
│
│── docker-compose.yaml
│── .gitignore
│── README.md
```

## 🚀 Setup Instructions

### 1️⃣ Prerequisites
Ensure you have the following installed:
- **Docker & Docker Compose**
- **Python 3.11+** (if running locally)
- **Groq API Key** (for model inference)
- **Hugging Face API Key** (for embeddings)

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/vasstavkumar/RAG-Chatbot.git
cd RAG-Chatbot
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add the required API keys:
```env
groq_api_key=your_groq_api_key
api_key=your_huggingface_api_key
```

### 4️⃣ Run with Docker
```sh
docker-compose up --build
```
- FastAPI will run at **http://localhost:8000**
- Streamlit frontend will be available at **http://localhost:8501**