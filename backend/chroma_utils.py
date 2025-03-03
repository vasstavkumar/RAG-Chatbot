from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, UnstructuredHTMLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from groq import Groq
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

textsplitter = RecursiveCharacterTextSplitter(
    chunk_size = 2000,
    chunk_overlap = 200
)

embedding_model = HuggingFaceInferenceAPIEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2',
    api_key= os.getenv('api_key')
)

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_model
)

def load_split_document(file_path : str)->list[Document]:
    if file_path.endswith('pdf'):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith('docx'):
        loader = Docx2txtLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")

    documents = loader.load()
    return textsplitter.split_documents(documents)

def index_document_to_chroma(file_path: str, file_id: int)->bool:
    try:
        splits = load_split_document(file_path)

        for split in splits:
            split.metadata['file_id'] = file_id

        vectorstore.add_documents(splits)
        return True

    except Exception as e:
        print(f"Error indexing document: {e}")
        return False

def delete_doc_from_chroma(file_id: int):
    try:
        docs = vectorstore.get(where = {'file_id': file_id})
        print(f"Found {len(docs['ids'])} document chunks for file_id {file_id}")

        vectorstore._collection.delete(where = {'file_id': file_id})
        print(f"Deleted all documents with file_id {file_id}")
        return True
        
    except Exception as e:
        print(f"Error deleting document with file_id {file_id} from Chroma: {str(e)}")
        return False

