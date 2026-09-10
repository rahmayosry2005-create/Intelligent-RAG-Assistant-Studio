import os
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

env_path = r"D:\rag-assistant-project\.env"



class Settings(BaseSettings):
    PROJECT_NAME: str = "RAG Assistant API"
    VECTOR_DB_PATH: str = r"D:\rag-assistant-project\backend\data\vector_db"
    EMBEDDING_MODEL_PATH: str = r"D:\rag-assistant-project\backend\data\models\all-MiniLM-L6-v2"
    OPENROUTER_API_KEY: str = ""
    
    model_config = ConfigDict(env_file=env_path, extra="ignore")

settings = Settings()

