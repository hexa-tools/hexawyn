from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ComputeSecurityPostureCommand:
    previous_score_pct: float | None = None
