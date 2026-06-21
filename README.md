# 📝 Hebrew Text Summarizer

An AI-powered web application for summarizing Hebrew texts, built with Python and FastAPI.
Includes full RTL (right-to-left) support and three configurable summary lengths.

## ✨ Features

- AI-powered text summarization with full Hebrew support
- Three summary lengths: short, medium, detailed
- Clean and intuitive RTL user interface
- Graceful handling of API rate limits

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, Uvicorn
- **AI:** OpenRouter API (Google Gemini 2.0 Flash)
- **Frontend:** HTML, CSS, Jinja2

## 📂 Project Structure

```
hebrew-text-summarizer/
├── main.py            # FastAPI app and routes
├── summarizer.py      # Summarization logic (OpenRouter API call)
├── templates/
│   └── index.html     # RTL web interface
├── requirements.txt   # Python dependencies
└── .env.example       # Example environment configuration
```

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/rafaelmishayev-maker/hebrew-text-summarizer.git
   cd hebrew-text-summarizer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS / Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file (copy from `.env.example`) and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

5. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

6. Open your browser at http://127.0.0.1:8000
