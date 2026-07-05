from __future__ import annotations

from datetime import date


def calculate_age_days(last_modified: date, today: date) -> int:
    return (today - last_modified).days


def is_stale(age_days: int, threshold_days: int) -> bool:
    return age_days > threshold_days
