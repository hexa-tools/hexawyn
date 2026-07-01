from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RolloutsDetectResponse:
    installed: bool = False
    version: str | None = None
    namespace: str | None = None
    total_rollouts: int = 0
    healthy: int = 0
    progressing: int = 0
    degraded: int = 0
    paused: int = 0
    error: str | None = None
