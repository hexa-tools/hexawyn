from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AnalyzeFailedPipelineCommand:
    pipeline_name: str
    namespace: str = "default"
