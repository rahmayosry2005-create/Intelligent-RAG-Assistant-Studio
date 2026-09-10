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

```text
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
---
### 📊 Notebooks & Evaluation Pipeline

* **RAG Pipeline Notebook**: Located at `notebooks/rag_pipeline.ipynb`, this notebook runs top-to-bottom without errors, covering document parsing, chunking strategies, embedding generation, vector store retrieval testing, and a complete evaluation metrics table.
* **Corpus & Data**: The raw PDF files and source documents used for indexing and testing are organized under `backend/data/corpus/`.

---

## 👁️ Extended Track: Computer Vision & Multimodal Models

* **Multimodal Integration (BLIP)**: Integrated image-to-text capabilities to process and describe images uploaded alongside text queries.
* **Object Detection & Vision Architectures**: Leveraged advanced computer vision models including **YOLO** for real-time object detection and spatial analysis.
* **Attention Mechanisms**: Explored and utilized Transformer-based attention mechanisms (inspired by foundational NLP and vision papers like *Attention Is All You Need*) to capture deep contextual representations across text and visual data.

---

## 🔐 Environment Variables

Create a `.env` file in both the `backend/` and `frontend/` directories based on the following configurations:

* **OPENAI_API_KEY**: Your OpenAI API key for LLM generation *(Example: `sk-...`)*
* **API_BASE_URL**: Backend URL used by the frontend client *(Default: `http://localhost:8000`)*
* **CHROMA_PERSIST_DIRECTORY**: Directory path for the persistent vector database *(Default: `backend/data/chroma_db`)*

---

### 🌟 Key Features

* **Advanced PDF Processing**: Automated text extraction, cleaning, and smart chunking using PyMuPDF and LangChain.
* **Flexible Querying**: Search across all available knowledge base documents or target a specific file filter.
* **Modern Dark UI**: Carefully crafted high-contrast Streamlit interface for optimal readability and user experience.
* **Precise Citations**: Grounded responses accompanied by transparent source tracking.
