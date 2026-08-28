from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GetCiliumFlowsCommand:
    namespace: str | None = None
    pod: str | None = None
    direction: str | None = None
    verdict: str | None = None
    window_minutes: int = 15
    limit: int = 100
