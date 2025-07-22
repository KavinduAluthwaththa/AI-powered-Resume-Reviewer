from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
import openai
from .services.resume_parser import ResumeParser
from .services.ai_analyzer import AIAnalyzer
from .services.linkedin_optimizer import LinkedInOptimizer

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="AI-Powered Resume Reviewer",
    description="A smart web application for AI-powered resume analysis and optimization",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
resume_parser = ResumeParser()
ai_analyzer = AIAnalyzer()
linkedin_optimizer = LinkedInOptimizer()

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "AI-Powered Resume Reviewer API", "version": "1.0.0"}

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    """Upload and parse resume (PDF/DOCX)"""
    try:
        if not file.filename.lower().endswith(('.pdf', '.docx')):
            raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported")
        
        # Parse the resume
        content = await resume_parser.parse_resume(file)
        
        return JSONResponse(content={
            "status": "success",
            "filename": file.filename,
            "content": content,
            "message": "Resume uploaded and parsed successfully"
        })
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing resume: {str(e)}")

@app.post("/analyze")
async def analyze_resume(data: dict):
    """GPT-based resume analysis"""
    try:
        resume_content = data.get("resume_content")
        job_description = data.get("job_description", "")
        
        if not resume_content:
            raise HTTPException(status_code=400, detail="Resume content is required")
        
        # Analyze with AI
        analysis = await ai_analyzer.analyze_resume(resume_content, job_description)
        
        return JSONResponse(content={
            "status": "success",
            "analysis": analysis
        })
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing resume: {str(e)}")

@app.post("/linkedin")
async def optimize_linkedin(data: dict):
    """Optimize LinkedIn profile content"""
    try:
        resume_content = data.get("resume_content")
        current_profile = data.get("current_profile", {})
        
        if not resume_content:
            raise HTTPException(status_code=400, detail="Resume content is required")
        
        # Optimize LinkedIn profile
        optimized_profile = await linkedin_optimizer.optimize_profile(resume_content, current_profile)
        
        return JSONResponse(content={
            "status": "success",
            "optimized_profile": optimized_profile
        })
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error optimizing LinkedIn profile: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "API is running"}
