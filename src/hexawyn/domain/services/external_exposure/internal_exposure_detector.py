from __future__ import annotations


def is_internal_load_balancer(
    annotations: dict[str, str], internal_annotations: tuple[tuple[str, str], ...]
) -> bool:
    return any(annotations.get(key) == value for key, value in internal_annotations)
