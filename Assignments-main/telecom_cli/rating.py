from config import RATES

def compute_cost(call_type: str, duration_sec: int) -> float:
    minutes = duration_sec / 60
    rate = RATES.get(call_type, RATES["domestic"])
    return round(minutes * rate, 2)