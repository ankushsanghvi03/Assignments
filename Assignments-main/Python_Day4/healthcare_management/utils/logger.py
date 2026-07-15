def log_event(message, details=None):
    print(f"[LOG] {message}")
    if details:
        print(details)
