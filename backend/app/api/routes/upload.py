import os
import shutil
import re
import pymupdf as fitz  # PyMuPDF
from fastapi import APIRouter, UploadFile, File, HTTPException
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.services.retrieval import load_vector_store
from app.core.config import settings

router = APIRouter(prefix="/upload", tags=["Upload"])

def clean_extracted_text(text: str) -> str:
    """Clean extracted PDF text by removing excessive newlines, spaces, and artifacts."""
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    lines = [line.strip() for line in text.split('\n') if len(line.strip()) > 2]
    return "\n".join(lines)

@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    # Validate if the uploaded file is a PDF
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    
    # Define the corpus directory path for saving uploaded files
    corpus_dir = r"D:\rag-assistant-project\backend\data\corpus"
    os.makedirs(corpus_dir, exist_ok=True)
    file_path = os.path.join(corpus_dir, file.filename)
    
    # Save the uploaded file locally
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        # Load and clean the PDF text using PyMuPDF (similar to the notebook approach)
        doc = fitz.open(file_path)
        full_text = ""
        total_pages = len(doc)
        
        for page_index in range(total_pages):
            page = doc[page_index]
            extracted = page.get_text()
            if extracted:
                cleaned_page_text = clean_extracted_text(extracted)
                full_text += cleaned_page_text + "\n"
        
        # Split text into chunks using LangChain
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200,
            length_function=len,
            is_separator_regex=False
        )
        
        # Create chunks manually and attach comprehensive metadata
        texts = text_splitter.split_text(full_text)
        chunks = [
            Document(
                page_content=chunk,
                metadata={
                    "filename": file.filename,
                    "file_name": file.filename,
                    "total_pages": total_pages
                }
            )
            for chunk in texts
            if len(chunk.strip()) > 100  # Filter out very short chunks
        ]
        
        # Load the vector database and add the new document chunks
        vector_db = load_vector_store()
        vector_db.add_documents(chunks)
        vector_db.persist()
        
        return {
            "message": "File uploaded, cleaned, and processed successfully!",
            "filename": file.filename,
            "pages": total_pages,
            "chunks_added": len(chunks)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

    import os

@router.get("/files/")
async def list_corpus_files():
    corpus_dir = r"D:\rag-assistant-project\backend\data\corpus"
    if not os.path.exists(corpus_dir):
        return {"files": []}
    
    files = [f for f in os.listdir(corpus_dir) if f.endswith(".pdf") and "Graduation_Project" not in f]
    return {"files": files}