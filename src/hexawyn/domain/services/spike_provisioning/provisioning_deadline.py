from __future__ import annotations

import math
from datetime import date, datetime, timedelta

_HOURS_PER_DAY = 24


def compute_deadline(
    event_date: str,
    provider_lead_time_hours: int,
    safety_margin_days: int,
) -> str | None:
    """Compute the latest safe provisioning date.

    Deadline = event date minus the provider's node lead time (rounded up to
    whole days) minus a safety margin. Returns None when the event date is
    malformed.
    """
    event = _parse(event_date)
    if event is None:
        return None
    lead_time_days = math.ceil(provider_lead_time_hours / _HOURS_PER_DAY)
    deadline = event - timedelta(days=lead_time_days + safety_margin_days)
    return deadline.isoformat()


def _parse(event_date: str) -> date | None:
    try:
        return datetime.strptime(event_date, "%Y-%m-%d").date()
    except ValueError:
        return None
