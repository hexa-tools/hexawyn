from dataclasses import dataclass, field

from hexawyn.application.ports.driven.tekton_port import PipelineRunInfo


@dataclass
class PipelineRunStats:
    total_runs: int = 0
    succeeded_runs: int = 0
    failed_runs: int = 0
    cancelled_runs: int = 0
    success_rate: float = 0.0
    average_duration_seconds: float | None = None
    fastest_run_name: str | None = None
    slowest_run_name: str | None = None


@dataclass
class ListPipelineRunsResponse:
    runs: list[PipelineRunInfo] = field(default_factory=list)
    stats: PipelineRunStats = field(default_factory=PipelineRunStats)
    outliers: list[str] = field(default_factory=list)
    note: str | None = None
