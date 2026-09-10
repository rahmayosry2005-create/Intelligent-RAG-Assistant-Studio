import os
import streamlit as st
from api_client import upload_pdf_to_backend, get_available_files, query_backend

# Page Configuration & Modern Styling
st.set_page_config(
    page_title="RAG Assistant Studio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Professional Dark Theme & Clean Layout
st.markdown("""
    <style>
    /* Main App Background */
    .stApp {
        background-color: #0b0f19;
        color: #ffffff !important;
    }
    
    /* Sidebar Clean Structure & Fix Overflow */
    [data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #1f2937;
        padding-top: 1rem;
    }
    [data-testid="stSidebar"] > div:first-child {
        padding: 1rem;
    }
    
    /* File Uploader Box Customization */
    [data-testid="stFileUploader"] {
        background-color: #1f2937 !important;
        border: 2px dashed #6366f1 !important;
        border-radius: 10px;
        padding: 10px;
        width: 100% !important;
    }
    [data-testid="stFileUploader"] label, 
    [data-testid="stFileUploader"] small, 
    [data-testid="stFileUploader"] span,
    [data-testid="stFileUploader"] div {
        color: #ffffff !important;
    }
    [data-testid="stFileUploader"] button {
        background-color: #374151 !important;
        color: #ffffff !important;
        border: 1px solid #4b5563 !important;
        border-radius: 6px !important;
    }
    
    /* General Labels and Headings */
    label, .stTextInput label, .stSelectbox label {
        color: #f3f4f6 !important;
        font-weight: 500 !important;
    }
    
    /* Text Input Styling (Question Bar) */
    .stTextInput input {
        background-color: #1f2937 !important;
        color: #ffffff !important;
        border: 1px solid #4b5563 !important;
        border-radius: 8px !important;
    }
    .stTextInput input::placeholder {
        color: #9ca3af !important;
        opacity: 1 !important;
    }
    
    /* Selectboxes */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #1f2937 !important;
        color: #ffffff !important;
        border: 1px solid #374151;
        border-radius: 8px;
    }
    div[data-baseweb="select"] span {
        color: #ffffff !important;
    }
    
    /* Action Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white !important;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        opacity: 0.9;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
    }
    
    /* Alerts and Containers */
    div.stAlert {
        border-radius: 8px;
        background-color: #1f2937;
        color: #ffffff !important;
        border: 1px solid #374151;
    }
    
    /* General Typography */
    h1, h2, h3, h4, h5, h6, p {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar: Upload & Document Management ---
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/artificial-intelligence.png", width=80)
    st.title("RAG Studio")
    st.markdown("---")
    
    st.subheader("📁 Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        if st.button("🚀 Upload & Process"):
            with st.spinner("Processing document..."):
                response = upload_pdf_to_backend(uploaded_file)
                if response and response.status_code == 200:
                    st.success(f"Uploaded: {uploaded_file.name}")
                    st.rerun()  
                else:
                    detail = response.json().get('detail', 'Error') if response else 'Connection failed'
                    st.error(f"Error: {detail}")
                    
    st.markdown("---")
    st.markdown("<p style='font-size: 0.85rem; color: #cbd5e1;'>💡 <b>Tip:</b> Select a specific file to restrict your queries, or search across all documents.</p>", unsafe_allow_html=True)

# --- Main Interface ---
st.title("💬 Intelligent Document Q&A")
st.markdown("Ask questions grounded in your knowledge base with precise source attribution.")

# Fetch available files dynamically from backend
available_files = get_available_files()

# Filter options
filtered_files = [f for f in available_files if "Graduation_Project" not in f] 
dropdown_options = ["All Files (No Filter)"] + filtered_files

col1, col2 = st.columns([2, 1])
with col1:
    question = st.text_input("✨ What would you like to know?", placeholder="e.g., What are the main components of this system?")
with col2:
    selected_file = st.selectbox("🎯 Target Document Filter", options=dropdown_options)

# Handle search execution
if st.button("🔍 Generate Answer", type="primary"):
    if not question.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Synthesizing answer from vector database..."):
            target_file = None if selected_file == "All Files (No Filter)" else selected_file
            response = query_backend(question, target_file)
            
            if response is not None and response.status_code == 200:
                data = response.json()
                
                # Answer Section
                st.markdown("### 📝 Answer")
                st.markdown(f"> {data.get('answer', 'No answer returned.')}")
                
                # Sources Section
                st.markdown("### 📚 Cited Sources")
                sources = data.get("sources", [])
                if sources:
                    cols = st.columns(len(sources) if len(sources) <= 3 else 3)
                    for idx, src in enumerate(sources):
                        with cols[idx % len(cols)]:
                            st.metric(label=f"Source {idx+1}", value=src)
                else:
                    st.info("No sources explicitly cited for this query.")
            else:
                detail = response.json().get('detail', 'Unknown error') if response else 'Connection failed'
                st.error(f"Server Error: {detail}")