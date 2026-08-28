from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DetectCiliumDenialsCommand:
    namespace: str | None = None
    window_minutes: int = 5
    limit: int = 100
