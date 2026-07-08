from __future__ import annotations


def resolves_to_root(container_level: bool | None, pod_level: bool | None) -> bool:
    effective = container_level if container_level is not None else pod_level
    return effective is not True


def allows_privilege_escalation(value: bool | None) -> bool:
    return value is not False


def is_privileged(value: bool | None) -> bool:
    return value is True
