from ai.ai_engine import generate_explanation
from nlp.nlp_engine import clean_topic
from system.system_guard import allow_request

def get_explanation(topic: str, level: int) -> str:
    if not allow_request():
        return "⚠️ Too many requests. Please wait."

    topic = clean_topic(topic)

    if not topic:
        return "❌ Invalid topic."

    return generate_explanation(topic, level)
