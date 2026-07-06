from __future__ import annotations

_EXTERNALLY_EXPOSED_TYPES = frozenset({"LoadBalancer", "NodePort"})


def is_externally_exposed_type(service_type: str) -> bool:
    return service_type in _EXTERNALLY_EXPOSED_TYPES
