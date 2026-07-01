from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class QueryKubeArchiveCommand:
    namespace: str
    resource_type: str
    timestamp: str
    compare_with_current: bool = False
