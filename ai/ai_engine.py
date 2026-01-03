import os
import google.generativeai as genai
from ai.prompts import LEVEL_PROMPTS

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_explanation(topic: str, level: int) -> str:
    prompt = LEVEL_PROMPTS[level].format(topic=topic)

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.4,
            "max_output_tokens": 400
        }
    )

    return response.text.strip()
