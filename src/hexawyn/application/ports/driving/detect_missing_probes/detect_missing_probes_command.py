from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DetectMissingProbesCommand:
    namespace: str | None = None
