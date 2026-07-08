from __future__ import annotations

from hexawyn.domain.models.metrics_query import UnitHint

_BYTES_IN_KB = 1_000
_BYTES_IN_MB = 1_000_000
_BYTES_IN_GB = 1_000_000_000


def format_metric_value(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "cores":
        return _format_cores(value)
    if unit_hint == "bytes":
        return _format_bytes(value)
    if unit_hint == "percent":
        return f"{value:.1f}%"
    return _format_raw(value)


def _format_cores(value: float) -> str:
    if abs(value) < 1:
        millicores = round(value * 1000, 6)
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"


def _format_bytes(value: float) -> str:
    if abs(value) >= _BYTES_IN_GB:
        return f"{value / _BYTES_IN_GB:.2f} GB"
    if abs(value) >= _BYTES_IN_MB:
        return f"{value / _BYTES_IN_MB:.2f} MB"
    if abs(value) >= _BYTES_IN_KB:
        return f"{value / _BYTES_IN_KB:.2f} KB"
    return f"{value:g} B"


def _format_raw(value: float) -> str:
    return f"{value:g}"
