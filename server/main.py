"""
Main FastAPI application for AI-powered Resume Reviewer
"""
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI(
    title="AI-powered Resume Reviewer API",
    description="Backend API for resume review and analysis",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI-powered Resume Reviewer API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "resume-reviewer-api"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
