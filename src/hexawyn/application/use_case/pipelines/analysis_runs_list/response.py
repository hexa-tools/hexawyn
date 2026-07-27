from dataclasses import dataclass, field


@dataclass
class AnalysisRunsListResponse:
    analysis_runs: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
