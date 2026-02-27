from google import genai
import os
from dotenv import load_dotenv
from config import GEMINI_MODEL, GEMINI_PROMPT

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_screenshot(pil_image):
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=[GEMINI_PROMPT, pil_image]
        )
        raw = response.text.strip()

        # Clean up any markdown that slipped through
        if raw.startswith("```"):
            lines = raw.split("\n")
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            raw = "\n".join(lines)

        return raw.strip()

    except Exception as e:
        print(f"[Analyzer Error]: {e}")
        return None