from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("GEMINI_API_KEY")
)

def summarize_text(text: str, length: str = "medium") -> str:
    length_instructions = {
        "short": "סכם ב-2-3 משפטים בלבד",
        "medium": "סכם ב-5-7 משפטים",
        "detailed": "סכם בפירוט ב-10-15 משפטים"
    }

    prompt = f"""אתה עוזר מקצועי לסיכום טקסטים בעברית.
{length_instructions[length]}.
חובה לענות בעברית בלבד.

הטקסט לסיכום:
{text}"""

    try:
        response = client.chat.completions.create(
            model="google/gemini-2.0-flash-001",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        if "429" in str(e):
            return "השרת עמוס כרגע — אנא המתן כדקה ונסה שוב."
        return f"שגיאה: {str(e)}"