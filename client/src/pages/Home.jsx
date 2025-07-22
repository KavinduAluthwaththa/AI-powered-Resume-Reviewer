import React from 'react';

const Home = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-12">
        {/* Hero Section */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-gray-800 mb-4">
            🧠 AI-Powered Resume Reviewer
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Get instant AI-powered feedback on your resume. Optimize for ATS compatibility, 
            improve keyword matching, and enhance your LinkedIn profile.
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid md:grid-cols-3 gap-8 mb-12">
          <div className="bg-white rounded-lg shadow-md p-6 text-center">
            <div className="text-4xl mb-4">🤖</div>
            <h3 className="text-xl font-semibold mb-2">AI-Powered Analysis</h3>
            <p className="text-gray-600">
              Advanced GPT-based analysis provides detailed feedback on your resume content and structure.
            </p>
          </div>
          
          <div className="bg-white rounded-lg shadow-md p-6 text-center">
            <div className="text-4xl mb-4">🔍</div>
            <h3 className="text-xl font-semibold mb-2">ATS Optimization</h3>
            <p className="text-gray-600">
              Ensure your resume passes Applicant Tracking Systems with keyword optimization and formatting tips.
            </p>
          </div>
          
          <div className="bg-white rounded-lg shadow-md p-6 text-center">
            <div className="text-4xl mb-4">💼</div>
            <h3 className="text-xl font-semibold mb-2">LinkedIn Enhancement</h3>
            <p className="text-gray-600">
              Get personalized suggestions to optimize your LinkedIn profile headline, summary, and skills.
            </p>
          </div>
        </div>

        {/* CTA Section */}
        <div className="text-center">
          <div className="bg-white rounded-lg shadow-lg p-8 max-w-2xl mx-auto">
            <h2 className="text-2xl font-semibold mb-4">Ready to improve your resume?</h2>
            <p className="text-gray-600 mb-6">
              Upload your resume in PDF or DOCX format and get instant AI-powered feedback.
            </p>
            <button 
              className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-8 rounded-lg transition-colors"
              onClick={() => {/* Navigate to upload */}}
            >
              Get Started Now
            </button>
          </div>
        </div>

        {/* Stats Section */}
        <div className="mt-16 grid md:grid-cols-4 gap-8 text-center">
          <div>
            <div className="text-3xl font-bold text-blue-600">10k+</div>
            <div className="text-gray-600">Resumes Analyzed</div>
          </div>
          <div>
            <div className="text-3xl font-bold text-blue-600">95%</div>
            <div className="text-gray-600">ATS Compatibility</div>
          </div>
          <div>
            <div className="text-3xl font-bold text-blue-600">50+</div>
            <div className="text-gray-600">Industries Covered</div>
          </div>
          <div>
            <div className="text-3xl font-bold text-blue-600">24/7</div>
            <div className="text-gray-600">AI Analysis</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
