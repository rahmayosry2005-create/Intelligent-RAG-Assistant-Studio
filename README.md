# 🚀 Intelligent RAG Assistant Studio

A production-ready Retrieval-Augmented Generation (RAG) system built with a microservices architecture, featuring a FastAPI backend, an interactive Streamlit frontend, and an extended multimodal vision track.

---

## 🛠️ Tech Stack

* **Backend**: FastAPI, LangChain, PyMuPDF (fitz), Chroma/Vector Store, Uvicorn
* **Frontend**: Streamlit, Custom CSS (Modern Dark Theme UI)
* **Processing & Evaluation**: Recursive Character Text Splitter, Custom Text Cleaning Pipelines, Jupyter Notebooks
* **Advanced AI & Vision Models (Extended Track)**: BLIP (Multimodal Image-to-Text), YOLO (Object Detection), Transformer Attention Mechanisms

---

## 📂 Project Architecture
<<<<<<< HEAD
```
=======

```text
>>>>>>> 5c99bf346c7be2a5a5b90121d34c78e9f2a4b54a
rag-assistant-project/
│
├── notebooks/
│   └── rag_pipeline.ipynb       # End-to-end RAG pipeline, chunking, embeddings & evaluation table
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
│   │   └── corpus/              # Raw PDF documents and dataset corpus
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py                   # Streamlit UI
│   ├── api_client.py            # HTTP requests handler for backend
│   └── requirements.txt
│
└── requirements.txt
```
---
<<<<<<< HEAD

## 📊 Notebooks & Evaluation Pipeline
=======
### 📊 Notebooks & Evaluation Pipeline
>>>>>>> 5c99bf346c7be2a5a5b90121d34c78e9f2a4b54a

* **RAG Pipeline Notebook**: Located at `notebooks/rag_pipeline.ipynb`, this notebook runs top-to-bottom without errors, covering document parsing, chunking strategies, embedding generation, vector store retrieval testing, and a complete evaluation metrics table.
* **Corpus & Data**: The raw PDF files and source documents used for indexing and testing are organized under `backend/data/corpus/`.

---
<<<<<<< HEAD

=======
>>>>>>> 5c99bf346c7be2a5a5b90121d34c78e9f2a4b54a
## 👁️ Extended Track: Computer Vision & Multimodal Models

* **Multimodal Integration (BLIP)**: Integrated image-to-text capabilities to process and describe images uploaded alongside text queries.
* **Object Detection & Vision Architectures**: Leveraged advanced computer vision models including **YOLO** for real-time object detection and spatial analysis.
* **Attention Mechanisms**: Explored and utilized Transformer-based attention mechanisms (inspired by foundational NLP and vision papers like *Attention Is All You Need*) to capture deep contextual representations across text and visual data.

---

## 🔐 Environment Variables

Create a `.env` file in both the `backend/` and `frontend/` directories based on the following configurations:

<<<<<<< HEAD
### 1. Prerequisites
Make sure you have Python (version 3.10 or higher) installed on your system along with pip.

### 2. Clone the Repository
```bash
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
=======
* **OPENAI_API_KEY**: Your OpenAI API key for LLM generation *(Example: `sk-...`)*
* **API_BASE_URL**: Backend URL used by the frontend client *(Default: `http://localhost:8000`)*
* **CHROMA_PERSIST_DIRECTORY**: Directory path for the persistent vector database *(Default: `backend/data/chroma_db`)*
>>>>>>> 5c99bf346c7be2a5a5b90121d34c78e9f2a4b54a

---
## 🔐 Environment Variables

<<<<<<< HEAD
Create a `.env` file in both the `backend/` and `frontend/` directories based on the following configurations:

* **OPENAI_API_KEY**: Your OpenAI API key for LLM generation *(Example: `sk-...`)*
* **API_BASE_URL**: Backend URL used by the frontend client *(Default: `http://localhost:8000`)*
* **CHROMA_PERSIST_DIRECTORY**: Directory path for the persistent vector database *(Default: `backend/data/chroma_db`)*
---
## 🌟 Key Features
=======
### 🌟 Key Features
>>>>>>> 5c99bf346c7be2a5a5b90121d34c78e9f2a4b54a

* **Advanced PDF Processing**: Automated text extraction, cleaning, and smart chunking using PyMuPDF and LangChain.
* **Flexible Querying**: Search across all available knowledge base documents or target a specific file filter.
* **Modern Dark UI**: Carefully crafted high-contrast Streamlit interface for optimal readability and user experience.
* **Precise Citations**: Grounded responses accompanied by transparent source tracking.
