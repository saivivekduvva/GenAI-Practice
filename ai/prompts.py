import time
from ai.prompts import BASE_PROMPT, LEVEL_RULES

class GenAIError(Exception):
    pass

def _mock_slow_api(prompt: str) -> str:
    time.sleep(1)  # Simulating slow GenAI API

    if "error" in prompt.lower():
        raise GenAIError("GenAI API failed")

    return f"""
Explanation Generated Successfully

{prompt[:250]}

Real-life Example:
Example related to the topic.
"""

def generate_explanation(topic: str, level: int) -> str:
    if level not in LEVEL_RULES:
        raise ValueError("Invalid explanation level")

    prompt = f"""
{BASE_PROMPT}

Topic: {topic}
Level {level}: {LEVEL_RULES[level]}
"""

    return _mock_slow_api(prompt)