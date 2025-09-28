# src/utils.py
import datetime

def log_event(event: str):
    """
    Logs an event with timestamp for debugging and record-keeping.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {event}")
