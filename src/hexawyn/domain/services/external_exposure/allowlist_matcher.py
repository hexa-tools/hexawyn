from __future__ import annotations


def is_allowlisted(name: str, allowlist: tuple[str, ...]) -> bool:
    return name in allowlist
