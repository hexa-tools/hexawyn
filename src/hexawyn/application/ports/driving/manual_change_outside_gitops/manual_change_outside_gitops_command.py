from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ManualChangeOutsideGitOpsCommand:
    namespace: str
    window_days: int = 7
