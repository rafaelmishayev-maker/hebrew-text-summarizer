from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def summarize_text(text: str, length: str = "medium") -> str:
    length_instructions = {
        "short": "Summarize in 2-3 sentences only.",
        "medium": "Summarize in 5-7 sentences.",
        "detailed": "Summarize in detail, in 10-15 sentences."
    }

    prompt = f"""You are a professional assistant for summarizing Hebrew texts.
{length_instructions[length]}
You MUST respond in Hebrew only, in natural and fluent Hebrew.

Text to summarize:
{text}"""

    try:
        response = client.chat.completions.create(
            model="google/gemini-2.5-flash",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2048
        )
        return response.choices[0].message.content
    except Exception as e:
        if "429" in str(e):
            return "השרת עמוס כרגע — אנא המתן כדקה ונסה שוב."
        return f"שגיאה: {str(e)}"