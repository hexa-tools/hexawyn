from dataclasses import dataclass, field


@dataclass
class TracePipelineRunDagResponse:
    tasks: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
