# 🚀 Intelligent RAG Assistant Studio

A production-ready Retrieval-Augmented Generation (RAG) system built with a microservices architecture, featuring a FastAPI backend and an interactive, dark-themed Streamlit frontend.

---

## 🛠️ Tech Stack

* **Backend**: FastAPI, LangChain, PyMuPDF (fitz), Chroma/Vector Store, Uvicorn
* **Frontend**: Streamlit, Custom CSS (Modern Dark Theme UI)
* **Processing**: Recursive Character Text Splitter, Custom Text Cleaning Pipelines

---

## 📂 Project Architecture

rag-assistant-project/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── query.py
│   │   │       └── upload.py
│   │   ├── core/
│   │   │   └── config.py
│   │   └── services/
│   │       └── retrieval.py
│   ├── data/
│   │   └── corpus/          # Stores uploaded PDF documents
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py               # Streamlit UI
│   ├── api_client.py        # HTTP requests handler for backend
│   └── requirements.txt
│
└── requirements.txt

---

## ⚙️ Setup & Installation Guide

Follow these steps to set up and run the RAG Assistant project locally.

### 1. Prerequisites
Make sure you have Python (version 3.10 or higher) installed on your system along with pip.

### 2. Clone the Repository
git clone <repository-url>
cd rag-assistant-project

### 3. Backend Setup (FastAPI)
1. Navigate to the backend directory:
   cd backend

2. Install the required dependencies:
   pip install -r requirements.txt

3. Run the FastAPI server:
   uvicorn main:app --reload

* The API will be active at: http://127.0.0.1:8000
* Swagger Documentation: http://127.0.0.1:8000/docs

### 4. Frontend Setup (Streamlit)
1. Open a new terminal window and navigate to the frontend directory:
   cd frontend

2. Install the required dependencies:
   pip install -r requirements.txt

3. Run the Streamlit application:
   streamlit run app.py

* The user interface will automatically open in your browser at: http://localhost:8501

---

## 🌟 Key Features

* **Advanced PDF Processing**: Automated text extraction, cleaning, and smart chunking using PyMuPDF and LangChain.
* **Flexible Querying**: Search across all available knowledge base documents or target a specific file filter.
* **Modern Dark UI**: Carefully crafted high-contrast Streamlit interface for optimal readability and user experience.
* **Precise Citations**: Grounded responses accompanied by transparent source tracking.