import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

def upload_pdf_to_backend(uploaded_file):
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
    try:
        response = requests.post(f"{BASE_URL}/upload/", files=files)
        print("Upload Response Status:", response.status_code)
        return response
    except Exception as e:
        print("Upload Error:", e)
        return None

def get_available_files():
    """Fetches the list of uploaded/available PDF files from the backend with detailed logging."""
    try:
        url = f"{BASE_URL}/upload/files/"
        print(f"Fetching files from: {url}")
        response = requests.get(url)
        print("Get Files Response Status:", response.status_code)
        
        if response.status_code == 200:
            data = response.json()
            print("Files Data Received:", data)
            return data.get("files", [])
        else:
            print("Failed to fetch files, response:", response.text)
    except Exception as e:
        print(f"Connection Exception in get_available_files: {e}")
    return []

def query_backend(question, filename=None):
    payload = {
        "question": question,
        "filename": filename if filename and filename != "All Files (No Filter)" else None
    }
    try:
        response = requests.post(f"{BASE_URL}/query/", json=payload)
        return response
    except Exception as e:
        print("Query Error:", e)
        return None