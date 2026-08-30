import logging

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from summarizer import (
    MAX_INPUT_CHARACTERS,
    SummarizationError,
    SummarizationRateLimitError,
    SummaryLength,
    summarize_text,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

app = FastAPI(title="Hebrew Text Summarizer")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "selected_length": SummaryLength.MEDIUM.value,
            "max_input_characters": MAX_INPUT_CHARACTERS,
        },
    )


@app.post("/summarize", response_class=HTMLResponse)
async def summarize(
    request: Request,
    text: str = Form(...),
    length: SummaryLength = Form(SummaryLength.MEDIUM),
):
    cleaned_text = text.strip()
    summary = None
    error = None

    try:
        summary = await summarize_text(cleaned_text, length)
    except ValueError as exc:
        error = str(exc)
    except SummarizationRateLimitError:
        error = "The summarization service is temporarily busy. Please try again shortly."
    except SummarizationError:
        error = "The summarization service is currently unavailable. Please try again later."

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "summary": summary,
            "error": error,
            "original_text": cleaned_text,
            "selected_length": length.value,
            "max_input_characters": MAX_INPUT_CHARACTERS,
        },
    )
