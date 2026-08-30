# Hebrew Text Summarizer

An AI-powered web application for summarizing Hebrew texts, built with Python and FastAPI.

The application provides full RTL support, three configurable summary lengths, asynchronous AI requests, input validation, and safe error handling.

## Features

- AI-powered Hebrew text summarization
- Three summary lengths: short, medium, and detailed
- Full RTL user interface
- Asynchronous OpenRouter API calls
- Input validation and maximum text length enforcement
- Safe error handling without exposing internal exception details
- Explicit rate-limit handling
- Basic logging
- Automated tests

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn
- **AI Provider:** OpenRouter
- **Model:** Google Gemini 2.5 Flash
- **Frontend:** HTML, CSS, Jinja2
- **Testing:** Pytest, Pytest-Asyncio

## Design Decisions

### English instructions, Hebrew output

The model receives system instructions in English while being required to answer in Hebrew.

This keeps system instructions separate from user content and provides a clear contract for the model.

### System and user messages are separated

Application instructions are sent as a `system` message, while the source text is sent as user content.

The source text is explicitly delimited and treated as data rather than instructions, which reduces prompt-injection risk.

### Asynchronous API access

FastAPI routes are asynchronous, so the OpenRouter request also uses `AsyncOpenAI`.

This avoids blocking the event loop while waiting for the upstream AI provider.

### Backend validation

The backend validates:

- Summary length using an enum
- Empty input
- Maximum input size

The server does not rely on frontend controls for correctness.

### Safe error handling

Internal exception details are logged but are never returned directly to the user.

Rate-limit failures are handled separately from general API failures.

## Project Structure

```text
hebrew-text-summarizer/
├── main.py
├── summarizer.py
├── templates/
│   └── index.html
├── tests/
│   └── test_summarizer.py
├── requirements.txt
├── pytest.ini
├── .env.example
└── README.md
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/rafael-mishayev/hebrew-text-summarizer.git
cd hebrew-text-summarizer
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and add your OpenRouter API key:

```env
OPENROUTER_API_KEY=your_api_key_here
```

5. Run the application:

```bash
uvicorn main:app --reload
```

6. Open:

```text
http://127.0.0.1:8000
```

## Running Tests

```bash
pytest
```
