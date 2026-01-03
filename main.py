import os
from ai.ai_engine import generate_explanation
from nlp.nlp_engine import validate_request
from system.system_guard import rate_limit, retry_api, cache

MAX_REQ = int(os.getenv("MAX_REQUESTS_PER_MIN", 20))

def get_explanation(topic: str, level: int):
    validate_request(topic, level)
    rate_limit(MAX_REQ)

    cached = cache(topic, level)
    if cached:
        return cached

    return retry_api(lambda: generate_explanation(topic, level))

# CLI test (optional)
if __name__ == "__main__":
    topic = input("Enter topic: ")
    level = int(input("Enter level (1-5): "))

    try:
        result = get_explanation(topic, level)
        print(result)
    except Exception as e:
        print("ERROR:", e)
