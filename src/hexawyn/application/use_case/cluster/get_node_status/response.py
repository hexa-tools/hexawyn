from dataclasses import dataclass, field


@dataclass
class GetNodeStatusResponse:
    node_name: str = ""
    status: str = ""
    pods: list[dict[str, object]] = field(default_factory=list)
    total_pods: int = 0
    error: str | None = None
