def clean_topic(topic: str) -> str:
    topic = topic.strip()
    topic = topic.replace("\n", " ")
    return topic
