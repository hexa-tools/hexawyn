from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class PipelineForServiceResponse:
    service_name: str = ""
    pipelines_found: int = 0
    pipelines: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
