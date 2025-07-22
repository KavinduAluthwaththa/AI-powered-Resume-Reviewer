import React from 'react';

const AnalysisResults = ({ analysis }) => {
  if (!analysis) return null;

  const { ats_score, key_recommendations, strengths, improvements, raw_analysis } = analysis;

  return (
    <div className="max-w-4xl mx-auto p-6 space-y-6">
      {/* Score Section */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="flex items-center justify-between">
          <h3 className="text-xl font-semibold text-gray-800">ATS Score</h3>
          <div className="flex items-center">
            <span className="text-3xl font-bold text-blue-600">{ats_score}/10</span>
          </div>
        </div>
        <div className="mt-2">
          <div className="bg-gray-200 rounded-full h-2">
            <div
              className="bg-blue-600 h-2 rounded-full transition-all duration-300"
              style={{ width: `${(ats_score / 10) * 100}%` }}
            ></div>
          </div>
        </div>
      </div>

      {/* Strengths */}
      {strengths && strengths.length > 0 && (
        <div className="bg-green-50 rounded-lg shadow-md p-6">
          <h3 className="text-xl font-semibold text-green-800 mb-4">✅ Strengths</h3>
          <ul className="space-y-2">
            {strengths.map((strength, index) => (
              <li key={index} className="text-green-700 flex items-start">
                <span className="text-green-500 mr-2">•</span>
                {strength}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Key Recommendations */}
      {key_recommendations && key_recommendations.length > 0 && (
        <div className="bg-blue-50 rounded-lg shadow-md p-6">
          <h3 className="text-xl font-semibold text-blue-800 mb-4">🎯 Key Recommendations</h3>
          <ul className="space-y-3">
            {key_recommendations.map((recommendation, index) => (
              <li key={index} className="text-blue-700 flex items-start">
                <span className="text-blue-500 mr-2 font-bold">{index + 1}.</span>
                {recommendation}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Improvements */}
      {improvements && improvements.length > 0 && (
        <div className="bg-orange-50 rounded-lg shadow-md p-6">
          <h3 className="text-xl font-semibold text-orange-800 mb-4">🔧 Areas for Improvement</h3>
          <ul className="space-y-2">
            {improvements.map((improvement, index) => (
              <li key={index} className="text-orange-700 flex items-start">
                <span className="text-orange-500 mr-2">•</span>
                {improvement}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Raw Analysis */}
      {raw_analysis && (
        <div className="bg-gray-50 rounded-lg shadow-md p-6">
          <h3 className="text-xl font-semibold text-gray-800 mb-4">📄 Detailed Analysis</h3>
          <div className="text-gray-700 whitespace-pre-wrap text-sm leading-relaxed">
            {raw_analysis}
          </div>
        </div>
      )}
    </div>
  );
};

export default AnalysisResults;
