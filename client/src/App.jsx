import React, { useState } from 'react';
import './App.css';

function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [jobDescription, setJobDescription] = useState('');
  const [analysisResult, setAnalysisResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleFileChange = (e) => {
    setResumeFile(e.target.files[0]);
  };

  const handleAnalyze = async () => {
    if (!resumeFile) return;
    
    setIsLoading(true);
    try {
      const formData = new FormData();
      formData.append('file', resumeFile);
      formData.append('job_description', jobDescription);

      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      setAnalysisResult(data);
    } catch (error) {
      console.error('Error analyzing resume:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const getScoreColor = (score) => {
    if (score >= 80) return 'score-excellent';
    if (score >= 60) return 'score-good';
    if (score >= 40) return 'score-average';
    return 'score-poor';
  };

  return (
    <div className="app-container">

      <div className="main-content">
        <div className="hero-section">
          <h1 className="heading">🧠 AI-Powered Resume Reviewer</h1>
          <p className="subtitle">Get instant AI feedback to optimize your resume for ATS and improve your job prospects</p>
        </div>
        <div className="upload-section">
          <div className="section-header">
            <h2>📄 Upload Your Resume</h2>
            <p>Upload your resume in PDF or DOCX format</p>
          </div>
          
          <div className="file-upload-container">
            <input 
              type="file" 
              id="resume-file"
              onChange={handleFileChange}
              accept=".pdf,.doc,.docx"
              className="file-input"
            />
            <label htmlFor="resume-file" className="file-label">
              <span className="file-icon">📎</span>
              {resumeFile ? resumeFile.name : 'Choose Resume File'}
            </label>
          </div>

          <div className="job-description-container">
            <label className="label">💼 Job Description (Optional)</label>
            <textarea
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              placeholder="Paste the job description here to get more targeted feedback..."
              className="job-textarea"
            />
          </div>

          <button 
            className={`analyze-button ${!resumeFile ? 'disabled' : ''}`} 
            onClick={handleAnalyze}
            disabled={!resumeFile || isLoading}
          >
            {isLoading ? (
              <>
                <span className="loading-spinner"></span>
                Analyzing...
              </>
            ) : (
              <>
                <span className="button-icon">🔍</span>
                Analyze Resume
              </>
            )}
          </button>
        </div>

        {analysisResult && (
          <div className="result-section">
            <div className="result-header">
              <h2>📊 Analysis Results</h2>
            </div>
            
            <div className="results-grid">
              <div className="score-card">
                <div className="score-label">ATS Compatibility Score</div>
                <div className={`score-value ${getScoreColor(analysisResult.ats_score)}`}>
                  {analysisResult.ats_score}%
                </div>
                <div className="score-description">
                  {analysisResult.ats_score >= 80 ? 'Excellent!' : 
                   analysisResult.ats_score >= 60 ? 'Good' :
                   analysisResult.ats_score >= 40 ? 'Needs Improvement' : 'Poor'}
                </div>
              </div>

              {analysisResult.missing_keywords && analysisResult.missing_keywords.length > 0 && (
                <div className="keywords-card">
                  <h3>🔑 Missing Keywords</h3>
                  <div className="keywords-list">
                    {analysisResult.missing_keywords.map((keyword, index) => (
                      <span key={index} className="keyword-tag">{keyword}</span>
                    ))}
                  </div>
                </div>
              )}

              {analysisResult.suggestions && analysisResult.suggestions.length > 0 && (
                <div className="suggestions-card">
                  <h3>💡 Improvement Suggestions</h3>
                  <ul className="suggestions-list">
                    {analysisResult.suggestions.map((tip, index) => (
                      <li key={index} className="suggestion-item">{tip}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;