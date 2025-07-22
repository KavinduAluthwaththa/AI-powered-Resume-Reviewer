const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

class ApiService {
  async uploadResume(file) {
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch(`${API_BASE_URL}/upload-resume`, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error('Failed to upload resume');
    }

    return response.json();
  }

  async analyzeResume(resumeContent, jobDescription = '') {
    const response = await fetch(`${API_BASE_URL}/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        resume_content: resumeContent,
        job_description: jobDescription,
      }),
    });

    if (!response.ok) {
      throw new Error('Failed to analyze resume');
    }

    return response.json();
  }

  async optimizeLinkedIn(resumeContent, currentProfile = {}) {
    const response = await fetch(`${API_BASE_URL}/linkedin`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        resume_content: resumeContent,
        current_profile: currentProfile,
      }),
    });

    if (!response.ok) {
      throw new Error('Failed to optimize LinkedIn profile');
    }

    return response.json();
  }
}

export default new ApiService();
