from __future__ import annotations

from datetime import UTC, datetime, timedelta


def within_window(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)
