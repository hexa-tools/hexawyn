from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.domain.models.pipeline_baseline import PipelineBaselineResult, StageStats


@dataclass
class PipelinePerformanceBaselineResponse:
    pipeline: str = ""
    runs_analyzed: int = 0
    requested_limit: int = 30
    stages: dict[str, StageStats] = field(default_factory=dict)
    total_duration: StageStats | None = None
    outliers: list[str] = field(default_factory=list)
    excluded_running: int = 0
    excluded_failed: int = 0
    trend: str = "insufficient_data"
    note: str = ""
    error: str | None = None

    @classmethod
    def from_result(
        cls, result: PipelineBaselineResult, error: str | None = None
    ) -> PipelinePerformanceBaselineResponse:
        return cls(
            pipeline=result.pipeline,
            runs_analyzed=result.runs_analyzed,
            requested_limit=result.requested_limit,
            stages=result.stages,
            total_duration=result.total_duration,
            outliers=result.outliers,
            excluded_running=result.excluded_running,
            excluded_failed=result.excluded_failed,
            trend=result.trend,
            note=result.note,
            error=error,
        )
