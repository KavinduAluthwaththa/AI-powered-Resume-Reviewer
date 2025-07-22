import io
import os
from typing import Union
from fastapi import UploadFile
import pdfplumber
from docx import Document


class ResumeParser:
    """Service for parsing resume files (PDF and DOCX)"""
    
    def __init__(self):
        self.supported_formats = ['.pdf', '.docx']
    
    async def parse_resume(self, file: UploadFile) -> str:
        """Parse resume content from uploaded file"""
        
        # Read file content
        content = await file.read()
        filename = file.filename.lower()
        
        if filename.endswith('.pdf'):
            return self._parse_pdf(content)
        elif filename.endswith('.docx'):
            return self._parse_docx(content)
        else:
            raise ValueError("Unsupported file format")
    
    def _parse_pdf(self, content: bytes) -> str:
        """Extract text from PDF using pdfplumber"""
        try:
            text = ""
            pdf_file = io.BytesIO(content)
            
            with pdfplumber.open(pdf_file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            
            return text.strip()
        
        except Exception as e:
            raise Exception(f"Error parsing PDF: {str(e)}")
    
    def _parse_docx(self, content: bytes) -> str:
        """Extract text from DOCX using python-docx"""
        try:
            text = ""
            docx_file = io.BytesIO(content)
            
            doc = Document(docx_file)
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            
            return text.strip()
        
        except Exception as e:
            raise Exception(f"Error parsing DOCX: {str(e)}")
    
    def validate_file_format(self, filename: str) -> bool:
        """Validate if file format is supported"""
        return any(filename.lower().endswith(fmt) for fmt in self.supported_formats)
