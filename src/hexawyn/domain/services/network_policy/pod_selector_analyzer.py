from __future__ import annotations


def has_empty_pod_selector(match_labels: dict[str, str], match_expressions: list[object]) -> bool:
    return not match_labels and not match_expressions
