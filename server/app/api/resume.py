"""
Resume upload and processing endpoints
"""
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.services.resume_analyzer import ResumeAnalyzer
from app.services.file_processor import FileProcessor
from app.models.response_models import ResumeAnalysisResponse
import logging

router = APIRouter(prefix="/api/v1/resume", tags=["resume"])
resume_analyzer = ResumeAnalyzer()
file_processor = FileProcessor()

logger = logging.getLogger(__name__)

@router.post("/upload", response_model=ResumeAnalysisResponse)
async def upload_resume(file: UploadFile = File(...)):
    """
    Upload and analyze a resume file
    """
    try:
        # Validate file type
        if not file.filename.lower().endswith(('.pdf', '.docx', '.doc')):
            raise HTTPException(
                status_code=400, 
                detail="Only PDF and Word documents are supported"
            )
        
        # Process the file
        content = await file_processor.extract_text(file)
        
        # Analyze the resume
        analysis = await resume_analyzer.analyze(content)
        
        return ResumeAnalysisResponse(**analysis)
        
    except Exception as e:
        logger.error(f"Error processing resume: {str(e)}")
        raise HTTPException(status_code=500, detail="Error processing resume")

@router.get("/sample-analysis")
async def get_sample_analysis():
    """
    Get a sample analysis for demo purposes
    """
    return {
        "overall_score": 75,
        "strengths": [
            "Strong technical skills section",
            "Clear work experience descriptions",
            "Relevant educational background"
        ],
        "weaknesses": [
            "Missing contact information",
            "No action verbs in experience",
            "Lacks quantified achievements"
        ],
        "suggestions": [
            "Add LinkedIn profile URL",
            "Include specific metrics and numbers",
            "Use stronger action verbs"
        ],
        "ats_score": 68,
        "keywords": ["Python", "JavaScript", "React", "API"]
    }
