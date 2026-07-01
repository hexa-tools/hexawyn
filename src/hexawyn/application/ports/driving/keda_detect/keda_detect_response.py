from __future__ import annotations

from dataclasses import dataclass


@dataclass
class KedaDetectResponse:
    installed: bool = False
    version: str | None = None
    namespace: str | None = None
    total_scaledobjects: int = 0
    ready_scaledobjects: int = 0
    error_scaledobjects: int = 0
    scaled_to_zero_count: int = 0
    total_scaledjobs: int = 0
    managed_namespaces: list[str] | None = None
    error: str | None = None
