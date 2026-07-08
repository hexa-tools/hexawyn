from __future__ import annotations

from datetime import datetime, timedelta

from hexawyn.domain.models.manual_change import ActorType


def is_within_window(timestamp: str, window_days: int, now: datetime) -> bool:
    parsed = _parse_timestamp(timestamp)
    window_start = now - timedelta(days=window_days)
    return parsed >= window_start


def is_manual_change(actor_type: ActorType) -> bool:
    return actor_type != "gitops_controller"


def is_partial_window(earliest_timestamp: str | None, window_days: int, now: datetime) -> bool:
    if earliest_timestamp is None:
        return False
    window_start = now - timedelta(days=window_days)
    return _parse_timestamp(earliest_timestamp) > window_start


def _parse_timestamp(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))
