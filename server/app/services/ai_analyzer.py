import os
import openai
from typing import Dict, List, Optional


class AIAnalyzer:
    """Service for AI-powered resume analysis using OpenAI GPT"""
    
    def __init__(self):
        self.client = openai.AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )
        self.model = "gpt-3.5-turbo"
    
    async def analyze_resume(self, resume_content: str, job_description: str = "") -> Dict:
        """Analyze resume content with AI and provide feedback"""
        
        prompt = self._build_analysis_prompt(resume_content, job_description)
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert resume reviewer and career counselor. Provide detailed, actionable feedback."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            analysis_text = response.choices[0].message.content
            
            # Parse the response into structured format
            return self._parse_analysis_response(analysis_text)
        
        except Exception as e:
            raise Exception(f"Error analyzing resume: {str(e)}")
    
    def _build_analysis_prompt(self, resume_content: str, job_description: str = "") -> str:
        """Build the prompt for AI analysis"""
        
        base_prompt = f"""
        Please analyze the following resume and provide comprehensive feedback:

        RESUME CONTENT:
        {resume_content}
        """
        
        if job_description:
            base_prompt += f"""
            
            JOB DESCRIPTION:
            {job_description}
            
            Please also provide specific feedback on how well this resume matches the job requirements.
            """
        
        base_prompt += """
        
        Please provide feedback in the following areas:

        1. **ATS Compatibility**: How well will this resume perform with Applicant Tracking Systems?
        2. **Content Quality**: Strength of experience descriptions, achievements, and skills
        3. **Keywords**: Missing keywords and optimization suggestions
        4. **Format & Structure**: Organization, readability, and professional presentation
        5. **Specific Improvements**: Detailed, actionable recommendations
        6. **Overall Score**: Rate the resume from 1-10 with justification
        
        Format your response clearly with headers and bullet points for easy reading.
        """
        
        return base_prompt
    
    def _parse_analysis_response(self, analysis_text: str) -> Dict:
        """Parse AI response into structured format"""
        
        return {
            "raw_analysis": analysis_text,
            "ats_score": self._extract_score(analysis_text),
            "key_recommendations": self._extract_recommendations(analysis_text),
            "missing_keywords": self._extract_keywords(analysis_text),
            "strengths": self._extract_strengths(analysis_text),
            "improvements": self._extract_improvements(analysis_text)
        }
    
    def _extract_score(self, text: str) -> int:
        """Extract numerical score from analysis"""
        # Simple extraction - look for patterns like "8/10" or "Score: 7"
        import re
        score_patterns = [
            r'(\d+)/10',
            r'Score:?\s*(\d+)',
            r'rate.*?(\d+)'
        ]
        
        for pattern in score_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return int(match.group(1))
        
        return 7  # Default score if not found
    
    def _extract_recommendations(self, text: str) -> List[str]:
        """Extract key recommendations from analysis"""
        # Simple extraction based on common patterns
        recommendations = []
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if any(keyword in line.lower() for keyword in ['recommend', 'suggest', 'should', 'improve']):
                if len(line) > 20 and not line.startswith('#'):
                    recommendations.append(line)
        
        return recommendations[:5]  # Return top 5 recommendations
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract missing keywords from analysis"""
        keywords = []
        lines = text.split('\n')
        
        for line in lines:
            if 'keyword' in line.lower() and ('missing' in line.lower() or 'add' in line.lower()):
                # Extract potential keywords from the line
                words = line.split()
                for word in words:
                    if len(word) > 3 and word.isalpha():
                        keywords.append(word)
        
        return list(set(keywords))[:10]  # Return unique keywords, max 10
    
    def _extract_strengths(self, text: str) -> List[str]:
        """Extract strengths from analysis"""
        strengths = []
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if any(keyword in line.lower() for keyword in ['strength', 'good', 'excellent', 'strong']):
                if len(line) > 20 and not line.startswith('#'):
                    strengths.append(line)
        
        return strengths[:3]  # Return top 3 strengths
    
    def _extract_improvements(self, text: str) -> List[str]:
        """Extract improvement suggestions from analysis"""
        improvements = []
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if any(keyword in line.lower() for keyword in ['improve', 'fix', 'change', 'update', 'add']):
                if len(line) > 20 and not line.startswith('#'):
                    improvements.append(line)
        
        return improvements[:5]  # Return top 5 improvements
