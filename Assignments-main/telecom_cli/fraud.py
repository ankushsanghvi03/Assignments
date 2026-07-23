from config import DEFAULT_FRAUD_THRESHOLD_SEC

def is_suspicious(duration_sec: int) -> bool:
    return duration_sec > DEFAULT_FRAUD_THRESHOLD_SEC