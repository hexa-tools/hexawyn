from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import cast


def items_from(item_list: object) -> list[object]:
    items = getattr(item_list, "items", [])
    return _object_sequence(items)


def _object_sequence(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


def text_attr(source: object, attr_name: str, default: str) -> str:
    value = optional_text_attr(source, attr_name)
    return value if value is not None else default


def optional_text_attr(source: object, attr_name: str) -> str | None:
    value = getattr(source, attr_name, None)
    if isinstance(value, str) and value:
        return value
    return None


def integer_attr(source: object, attr_name: str) -> int:
    value = getattr(source, attr_name, 0)
    return value if isinstance(value, int) else 0


def conditions(status: object) -> list[object]:
    conditions_list = getattr(status, "conditions", [])
    return _object_sequence(conditions_list)


def container_statuses(status: object) -> list[object]:
    cs = getattr(status, "container_statuses", [])
    return _object_sequence(cs)


def waiting_reason(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def restart_count(status: object) -> int:
    return sum(integer_attr(cs, "restart_count") for cs in container_statuses(status))


def parse_cpu(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("m"):
        return int(float(cpu_str[:-1]))
    return int(float(cpu_str) * 1000)


def parse_memory(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def namespace_age(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def mapping_from(value: object) -> Mapping[object, object] | None:
    return value if isinstance(value, Mapping) else None


def mapping_text(mapping: Mapping[object, object], key: str) -> str:
    value = mapping.get(key, "")
    return value if isinstance(value, str) else ""


def metric_items(metrics: object) -> list[Mapping[object, object]]:
    m = mapping_from(metrics)
    if m is None:
        return []
    items = m.get("items", [])
    return [item for item in _object_sequence(items) if isinstance(item, Mapping)]


def cpu_to_cores(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def memory_to_bytes(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def _float_prefix(value: str, suffix: str) -> float:
    return _safe_float(value[: -len(suffix)])


def _safe_float(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        return 0.0


def percentage(used: float, capacity: float) -> float:
    if capacity <= 0:
        return 0.0
    return round((used / capacity) * 100, 2)
