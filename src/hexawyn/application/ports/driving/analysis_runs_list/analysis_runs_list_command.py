from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AnalysisRunsListCommand:
    namespace: str | None = None
    rollout_name: str | None = None
