import time

_last_call = 0

def allow_request(min_gap=2):
    global _last_call
    now = time.time()

    if now - _last_call < min_gap:
        return False

    _last_call = now
    return True
