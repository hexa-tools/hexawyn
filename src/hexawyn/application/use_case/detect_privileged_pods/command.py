from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DetectPrivilegedPodsCommand:
    namespaces: list[str] | None = None
