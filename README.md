📝 מסכם טקסט חכם בעברית

כלי ווב לסיכום טקסטים בעברית באמצעות AI, בנוי עם Python ו-FastAPI.

✨ תכונות
- סיכום טקסט בעברית באמצעות AI
- שלושה אורכי סיכום: קצר, בינוני, מפורט
- ממשק משתמש נוח ונקי
- תמיכה מלאה בעברית (RTL)

🛠️ טכנולוגיות
- **Backend:** Python, FastAPI
- **AI:** OpenRouter API (Gemini)
- **Frontend:** HTML, CSS, Jinja2
- **Server:** Uvicorn

🚀 התקנה והרצה

1. שכפל את הפרויקט:
git clone https://github.com/rafaelmishayev-maker/hebrew-text-summarizer.git
cd hebrew-text-summarizer

2. צור סביבה וירטואלית:
python -m venv venv
venv\Scripts\activate

3. התקן תלויות:
pip install fastapi uvicorn openai python-dotenv jinja2 python-multipart

4. צור קובץ `.env` עם ה-API key:
GEMINI_API_KEY=your_api_key_here

5. הרץ את השרת:
uvicorn main:app --reload

6. פתח בדפדפן: http://127.0.0.1:8000