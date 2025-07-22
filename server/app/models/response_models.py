"""
Pydantic models for API responses
"""
from pydantic import BaseModel
from typing import List, Optional

class ResumeAnalysisResponse(BaseModel):
    overall_score: int
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]
    ats_score: int
    keywords: List[str]
    linkedin_suggestions: Optional[List[str]] = None

class HealthCheckResponse(BaseModel):
    status: str
    service: str
