from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class FailureType(Enum):
    FLAKY_TEST = "flaky_test"
    REGRESSION = "regression"
    INFRASTRUCTURE = "infrastructure"
    DEPENDENCY = "dependency"
    CONFIG_ERROR = "config_error"


@dataclass(frozen=True)
class FailureAnalysis:
    task_name: str
    root_cause: str
    failure_type: FailureType
    confidence: float
    impact_score: float
    remediation: str


@dataclass(frozen=True)
class AnalyzeFailedPipelineRequest:
    pipeline_name: str
    namespace: str = "default"


@dataclass(frozen=True)
class AnalyzeFailedPipelineResult:
    pipeline_name: str
    namespace: str
    pipeline_run_found: bool
    failures: list[FailureAnalysis] = field(default_factory=list)
    aggregated_root_cause: str = ""
    summary: str = ""
