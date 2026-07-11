from __future__ import annotations


def compute_financial_impact(
    total_downtime_minutes: int, cost_per_minute: float | None
) -> float | None:
    """Estimate the financial impact of downtime.

    Returns None when pricing is not configured (``cost_per_minute is None``),
    so no financial figure is ever fabricated. A configured cost of 0.0 yields
    0.0 — a real, meaningful figure — not None.
    """
    if cost_per_minute is None:
        return None
    return round(total_downtime_minutes * cost_per_minute, 2)
