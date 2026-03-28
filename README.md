📝 Hebrew Text Summarizer

An AI-powered web application for summarizing Hebrew texts, built with Python and FastAPI.

✨ Features
- AI-powered text summarization with full Hebrew support
- Three summary lengths: short, medium, detailed
- Clean and intuitive user interface
- Full RTL (Right-to-Left) support

🛠️ Tech Stack
- Backend: Python, FastAPI
- AI: OpenRouter API (Gemini)
- Frontend: HTML, CSS, Jinja2
- Server: Uvicorn

🚀 Getting Started

1. Clone the repository:
```
git clone https://github.com/rafaelmishayev-maker/hebrew-text-summarizer.git
cd hebrew-text-summarizer
```

2. Create and activate a virtual environment:
```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```
pip install fastapi uvicorn openai python-dotenv jinja2 python-multipart
```

4. Create a `.env` file with your API key:
```
GEMINI_API_KEY=your_api_key_here
```

5. Run the server:
```
uvicorn main:app --reload
```

6. Open your browser at: http://127.0.0.1:8000