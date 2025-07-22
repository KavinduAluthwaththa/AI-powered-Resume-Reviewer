import os
import openai
from typing import Dict, Optional


class LinkedInOptimizer:
    """Service for optimizing LinkedIn profile content"""
    
    def __init__(self):
        self.client = openai.AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )
        self.model = "gpt-3.5-turbo"
    
    async def optimize_profile(self, resume_content: str, current_profile: Dict = None) -> Dict:
        """Generate optimized LinkedIn profile content based on resume"""
        
        if current_profile is None:
            current_profile = {}
        
        # Generate optimized content for different profile sections
        optimized_sections = {}
        
        # Optimize headline
        optimized_sections["headline"] = await self._optimize_headline(resume_content, current_profile.get("headline", ""))
        
        # Optimize summary
        optimized_sections["summary"] = await self._optimize_summary(resume_content, current_profile.get("summary", ""))
        
        # Optimize skills
        optimized_sections["skills"] = await self._optimize_skills(resume_content, current_profile.get("skills", []))
        
        return {
            "optimized_profile": optimized_sections,
            "recommendations": await self._generate_profile_recommendations(resume_content, current_profile)
        }
    
    async def _optimize_headline(self, resume_content: str, current_headline: str = "") -> str:
        """Generate optimized LinkedIn headline"""
        
        prompt = f"""
        Based on the following resume content, create an optimized LinkedIn headline that is:
        - Professional and attention-grabbing
        - Keyword-rich for search optimization
        - Maximum 120 characters
        - Highlights key value proposition
        
        RESUME CONTENT:
        {resume_content}
        
        CURRENT HEADLINE (if any):
        {current_headline}
        
        Generate 3 headline options and provide the best one:
        """
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a LinkedIn optimization expert. Create compelling, keyword-rich headlines."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.8,
                max_tokens=500
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            return f"Error generating headline: {str(e)}"
    
    async def _optimize_summary(self, resume_content: str, current_summary: str = "") -> str:
        """Generate optimized LinkedIn summary"""
        
        prompt = f"""
        Based on the following resume content, create an optimized LinkedIn summary that:
        - Tells a compelling professional story
        - Includes relevant keywords
        - Is 3-4 paragraphs long
        - Uses first person
        - Includes a call to action
        - Shows personality while remaining professional
        
        RESUME CONTENT:
        {resume_content}
        
        CURRENT SUMMARY (if any):
        {current_summary}
        
        Generate an engaging and optimized summary:
        """
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a LinkedIn optimization expert. Create engaging, professional summaries."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=800
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            return f"Error generating summary: {str(e)}"
    
    async def _optimize_skills(self, resume_content: str, current_skills: list = None) -> list:
        """Generate optimized skills list"""
        
        if current_skills is None:
            current_skills = []
        
        prompt = f"""
        Based on the following resume content, suggest the top 20 most relevant skills for LinkedIn:
        - Include both technical and soft skills
        - Prioritize skills that are searchable on LinkedIn
        - Include industry-specific keywords
        - Mix of current skills and new relevant ones
        
        RESUME CONTENT:
        {resume_content}
        
        CURRENT SKILLS:
        {', '.join(current_skills) if current_skills else 'None listed'}
        
        Provide a comma-separated list of 20 optimized skills:
        """
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a LinkedIn optimization expert. Suggest relevant, searchable skills."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.6,
                max_tokens=400
            )
            
            skills_text = response.choices[0].message.content.strip()
            # Parse the comma-separated skills
            skills = [skill.strip() for skill in skills_text.split(',')]
            return skills[:20]  # Limit to 20 skills
        
        except Exception as e:
            return [f"Error generating skills: {str(e)}"]
    
    async def _generate_profile_recommendations(self, resume_content: str, current_profile: Dict) -> list:
        """Generate general LinkedIn profile improvement recommendations"""
        
        prompt = f"""
        Based on the resume content and current LinkedIn profile information, provide 5-7 specific recommendations for improving their LinkedIn presence:
        
        RESUME CONTENT:
        {resume_content}
        
        CURRENT PROFILE INFO:
        {current_profile}
        
        Focus on:
        - Profile completeness
        - Content optimization
        - Networking strategies
        - Engagement tips
        - Personal branding
        
        Provide actionable, specific recommendations:
        """
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a LinkedIn strategy expert. Provide actionable profile improvement advice."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=600
            )
            
            recommendations_text = response.choices[0].message.content.strip()
            # Split into individual recommendations
            recommendations = [rec.strip() for rec in recommendations_text.split('\n') if rec.strip() and len(rec.strip()) > 20]
            return recommendations[:7]  # Limit to 7 recommendations
        
        except Exception as e:
            return [f"Error generating recommendations: {str(e)}"]
