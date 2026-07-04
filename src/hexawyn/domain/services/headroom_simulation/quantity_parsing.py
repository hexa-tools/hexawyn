from __future__ import annotations

_BYTES_PER_GB = 1024.0**3


def parse_cpu_quantity(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def parse_memory_quantity(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def _float_prefix(value: str, suffix: str) -> float:
    return _safe_float(value[: -len(suffix)])


def _safe_float(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        return 0.0
