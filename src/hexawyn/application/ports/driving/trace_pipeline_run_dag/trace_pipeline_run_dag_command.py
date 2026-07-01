from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TracePipelineRunDAGCommand:
    pipeline_run_name: str
    namespace: str
