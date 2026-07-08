from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GetPipelineRunStatusCommand:
    namespace: str
    hours_window: int = 24
    limit: int = 500
