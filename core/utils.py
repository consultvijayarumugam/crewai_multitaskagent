"""
Common utility helpers.
"""

from datetime import datetime


def current_timestamp() -> str:
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")