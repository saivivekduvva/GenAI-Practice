import os
from ai.ai_engine import generate_explanation
from nlp.nlp_engine import validate_request
from system.system_guard import rate_limit, retry_api, cache


# main.py
from ai.ai_engine import generate_explanation

def get_explanation(topic, level):
    return generate_explanation(topic, level)


# CLI test (optional)
if __name__ == "__main__":
    topic = input("Enter topic: ")
    level = int(input("Enter level (1-5): "))

    try:
        result = get_explanation(topic, level)
        print(result)
    except Exception as e:
        print("ERROR:", e)


