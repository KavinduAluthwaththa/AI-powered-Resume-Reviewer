# 🧠 AI-Powered Resume Reviewer

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![React](https://img.shields.io/badge/React-18.2.0-blue.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)

A comprehensive web application that leverages AI to provide intelligent resume analysis, ATS optimization, and LinkedIn profile enhancement. Built with modern technologies for scalable performance and intuitive user experience.

## ✨ Key Features

### 📄 Resume Analysis
- **Multi-format Support**: Upload PDF and DOCX files
- **AI-Powered Feedback**: GPT-based comprehensive analysis
- **ATS Compatibility**: Optimization for Applicant Tracking Systems
- **Keyword Matching**: Job description alignment analysis

### 💼 LinkedIn Optimization
- **Profile Enhancement**: Headline and summary optimization
- **Skills Recommendation**: Industry-relevant skill suggestions
- **Professional Branding**: Personal brand strengthening tips

### 🎯 Smart Features
- **Real-time Analysis**: Instant feedback generation
- **Responsive Design**: Works on all device sizes
- **Export Options**: Download optimized content
- **Progress Tracking**: Resume improvement scoring

## 🛠️ Technology Stack

### Frontend
- **React 18.2** - Modern UI framework
- **TailwindCSS** - Utility-first styling
- **Vite** - Lightning-fast build tool
- **JavaScript ES6+** - Modern language features

### Backend
- **FastAPI** - High-performance Python web framework
- **OpenAI API** - GPT-powered AI analysis
- **pdfplumber** - PDF text extraction
- **python-docx** - DOCX document processing
- **uvicorn** - ASGI server implementation

### Development Tools
- **ESLint** - Code quality and consistency
- **Git** - Version control
- **Environment Variables** - Secure configuration management

## 📁 Project Structure

```
AI-powered-Resume-Reviewer/
├── 📁 client/                    # React Frontend Application
│   ├── 📁 public/               # Static assets
│   ├── 📁 src/
│   │   ├── 📁 components/       # Reusable UI components
│   │   ├── 📁 pages/           # Application pages/views
│   │   ├── 📁 services/        # API integration layer
│   │   ├── 📁 hooks/           # Custom React hooks
│   │   ├── 📁 utils/           # Utility functions
│   │   ├── 📁 styles/          # CSS and styling files
│   │   └── 📁 assets/          # Images, icons, etc.
│   ├── package.json
│   └── vite.config.js
├── 📁 server/                   # FastAPI Backend Application
│   ├── 📁 app/
│   │   ├── 📁 services/        # Business logic services
│   │   │   ├── resume_parser.py    # PDF/DOCX parsing
│   │   │   ├── ai_analyzer.py      # AI analysis engine
│   │   │   └── linkedin_optimizer.py # LinkedIn optimization
│   │   ├── main.py             # FastAPI application entry
│   │   └── __init__.py
│   ├── requirements.txt        # Python dependencies
│   └── .env                    # Environment variables
├── README.md                   # Project documentation
├── LICENSE                     # MIT license
└── .gitignore                 # Git ignore rules
```

## 🚀 Quick Start

### Prerequisites
- **Node.js** 16+ and npm
- **Python** 3.8+
- **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))

### 1️⃣ Clone Repository
```bash
git clone https://github.com/KavinduAluthwaththa/AI-powered-Resume-Reviewer.git
cd AI-powered-Resume-Reviewer
```

### 2️⃣ Backend Setup
```bash
# Navigate to server directory
cd server

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
# Add your OpenAI API key to .env file

# Start the server
uvicorn app.main:app --reload
```

Server will be available at `http://localhost:8000`

### 3️⃣ Frontend Setup
```bash
# Navigate to client directory (new terminal)
cd client

# Install dependencies
npm install

# Create environment file
cp .env.example .env
# Configure API base URL if needed

# Start development server
npm run dev
```

Client will be available at `http://localhost:5173`

## ⚙️ Configuration

### Environment Variables

#### Backend (`server/.env`)
```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
MAX_FILE_SIZE=10485760  # 10MB in bytes
```

#### Frontend (`client/.env`)
```env
VITE_API_BASE_URL=http://localhost:8000
VITE_MAX_FILE_SIZE=10485760
```

## 📚 API Documentation

### Core Endpoints

| Method | Endpoint | Description | Request Format |
|--------|----------|-------------|----------------|
| `GET` | `/` | API health check | - |
| `POST` | `/upload-resume` | Upload and parse resume | `multipart/form-data` |
| `POST` | `/analyze` | AI-powered analysis | `application/json` |
| `POST` | `/linkedin` | LinkedIn optimization | `application/json` |

### Example API Usage

#### Resume Upload
```javascript
const formData = new FormData();
formData.append('file', resumeFile);

const response = await fetch('/upload-resume', {
  method: 'POST',
  body: formData
});
```

#### Resume Analysis
```javascript
const analysis = await fetch('/analyze', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    resume_content: "...",
    job_description: "..."
  })
});
```

## 🧪 Development

### Running Tests
```bash
# Backend tests
cd server
python -m pytest

# Frontend tests
cd client
npm test
```

### Code Quality
```bash
# Backend linting
cd server
flake8 app/

# Frontend linting
cd client
npm run lint
```

## 🚢 Deployment

### Production Build
```bash
# Frontend build
cd client
npm run build

# Backend production server
cd server
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Deployment Platforms
- **Frontend**: Vercel, Netlify, GitHub Pages
- **Backend**: Railway, Render, Heroku, AWS EC2

## 🗺️ Roadmap

- [ ] **Authentication System** - User accounts and session management
- [ ] **Resume Templates** - AI-generated professional templates
- [ ] **Batch Processing** - Multiple resume analysis
- [ ] **Advanced Analytics** - Detailed performance metrics
- [ ] **Industry-Specific Analysis** - Tailored feedback by field
- [ ] **Mobile Application** - React Native implementation
- [ ] **API Rate Limiting** - Enhanced security and fair usage
- [ ] **Resume History** - Track improvements over time

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Process
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **[@KavinduAluthwaththa](https://github.com/KavinduAluthwaththa)** - Project Creator & Lead Developer

## 🙏 Acknowledgments

- OpenAI for providing the GPT API
- FastAPI team for the excellent web framework
- React team for the powerful UI library
- The open-source community for invaluable tools and libraries

## 📞 Support

- 📧 **Email**: support@resumereviewer.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/KavinduAluthwaththa/AI-powered-Resume-Reviewer/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/KavinduAluthwaththa/AI-powered-Resume-Reviewer/discussions)

---

<div align="center">
  <p>Made with ❤️ and ☕ by developers, for developers</p>
  <p>⭐ Star this repository if you found it helpful!</p>
</div>bsolutely! Here’s a **professional and complete `README.md`** tailored for your **AI-Powered Resume Reviewer** project using React, FastAPI, and GPT-based analysis.

---

```markdown
# 🧠 AI-Powered Resume Reviewer

A smart web application that allows users to upload their resumes (PDF/DOCX), receive AI-powered feedback for ATS compatibility, keyword optimization, and LinkedIn profile improvement. Built with **React**, **FastAPI**, and **OpenAI's GPT API**.

---

## 🚀 Features

- ✅ Upload Resume (PDF / DOCX)
- 🤖 GPT-based Resume Review & Feedback
- 🔍 Job Description Keyword Matching
- 💼 LinkedIn Profile Optimizer (Headline, Summary, Skills)
- 📄 Export suggestions or updated resume content
- 🎨 Responsive UI with React + TailwindCSS

---

## 🛠️ Tech Stack

| Layer       | Technology                  |
|-------------|------------------------------|
| Frontend    | React.js + TailwindCSS       |
| Backend     | FastAPI (Python)             |
| AI Engine   | OpenAI GPT / Claude API      |
| Parsing     | `pdfplumber`, `python-docx`  |
| Styling     | TailwindCSS                  |
| Hosting     | Vercel (Frontend), Render/Railway (Backend)

---

## 📁 Project Structure

```

AI-powered-Resume-Reviewer/
├── client/           # React Frontend
│   └── src/
│       ├── components/
│       ├── pages/
│       └── styles/
├── server/           # FastAPI Backend
│   ├── app/
│   ├── venv/
│   └── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

````

---

## 🔧 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-powered-Resume-Reviewer.git
cd AI-powered-Resume-Reviewer
````

---

### 2. 🌐 Frontend Setup (React)

```bash
cd client
npm install
npm run dev
```

* Starts the React app on `http://localhost:5173/` (or `http://localhost:3000/`)

---

### 3. ⚙️ Backend Setup (FastAPI)

```bash
cd ../server
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

* Starts the FastAPI backend on `http://localhost:8000/`

---

## 🔑 Environment Variables

### 📁 `client/.env`

```
VITE_API_BASE_URL=http://localhost:8000
```

### 📁 `server/.env`

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 📄 API Endpoints (FastAPI)

| Method | Endpoint         | Description               |
| ------ | ---------------- | ------------------------- |
| POST   | `/upload-resume` | Upload and parse resume   |
| POST   | `/analyze`       | GPT-based analysis        |
| POST   | `/linkedin`      | Optimize LinkedIn content |

---

## 🧪 Future Features

* AI-generated resume templates
* User authentication (Google OAuth, Firebase)
* Resume scoring system
* PDF export with styled suggestions
* Saved history of past reviews

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## 🤝 Contributing

Pull requests are welcome! If you have ideas to improve performance, features, or UX, feel free to fork and contribute.

---

## 👨‍💻 Author

Developed by [@cloudwalk3r](https://github.com/cloudwalk3r)
Crafted with 💡, ☕, and a little help from GPT.

```

---

Let me know if you'd like badge icons (`react`, `fastapi`, `openai`, etc.) or if you want this exported as a file.
```
