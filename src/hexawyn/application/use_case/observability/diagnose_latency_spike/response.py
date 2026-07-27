from dataclasses import dataclass, field


@dataclass
class DiagnoseLatencySpikeUseCaseResponse:
    namespace: str = ""
    pods: list[dict[str, object]] = field(default_factory=list)
    total_pods: int = 0
    error: str | None = None
