import time
from functools import lru_cache

REQUEST_TIMES = []
WINDOW = 60

def rate_limit(max_requests: int):
    global REQUEST_TIMES
    now = time.time()

    REQUEST_TIMES = [t for t in REQUEST_TIMES if now - t < WINDOW]

    if len(REQUEST_TIMES) >= max_requests:
        raise Exception("Rate limit exceeded. Try again later.")

    REQUEST_TIMES.append(now)

def retry_api(call, retries=2):
    for attempt in range(retries + 1):
        try:
            return call()
        except Exception as e:
            if attempt == retries:
                raise Exception(f"GenAI failed after retries: {str(e)}")
            time.sleep(2)

@lru_cache(maxsize=100)
def cache(topic: str, level: int):
    return None