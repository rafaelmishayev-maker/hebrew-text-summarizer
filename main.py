from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from summarizer import summarize_text

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {})

@app.post("/summarize", response_class=HTMLResponse)
async def summarize(
    request: Request,
    text: str = Form(...),
    length: str = Form("medium")
):
    summary = summarize_text(text, length)
    return templates.TemplateResponse(request, "index.html", {
        "summary": summary,
        "original_text": text,
        "selected_length": length
    })