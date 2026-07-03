from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class FailureAnalysisDict(TypedDict):
    task_name: str
    root_cause: str
    failure_type: str
    confidence: float
    impact_score: float
    remediation: str


@dataclass
class AnalyzeFailedPipelineResponse:
    pipeline_name: str = ""
    namespace: str = "default"
    pipeline_run_found: bool = False
    failures: list[FailureAnalysisDict] = field(default_factory=list)
    aggregated_root_cause: str = ""
    summary: str = ""
    error: str | None = None
