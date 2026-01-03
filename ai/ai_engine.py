def validate_request(topic: str, level: int):
    if not topic or not isinstance(topic, str):
        raise ValueError("Topic must be a valid string")

    if level not in [1, 2, 3, 4, 5]:
        raise ValueError("Level must be between 1 and 5")

def ensure_same_concept(responses: list):
    base_keywords = responses[0].split()[:5]

    for response in responses[1:]:
        if not any(word in response for word in base_keywords):
            raise Exception("Concept drift detected between levels")

# ai/ai_engine.py

def generate_explanation(topic, level):
    return f"Explanation of {topic} at level {level}"
