from __future__ import annotations


def is_unused(referenced_by: list[str]) -> bool:
    return len(referenced_by) == 0


def deduplicate_references(referenced_by: list[str]) -> list[str]:
    return sorted(set(referenced_by))
