from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes.query import router as query_router
from app.api.routes.upload import router as upload_router

# 1. Define the FastAPI app first
app = FastAPI(title=settings.PROJECT_NAME)

# 2. Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Include all API routers safely after app initialization
app.include_router(query_router)
app.include_router(upload_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the RAG Assistant API. Visit /docs for Swagger documentation."}