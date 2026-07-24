from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class KedaScaledobjectGetResponse:
    name: str = ""
    namespace: str = ""
    triggers: list[dict[str, object]] = field(default_factory=list)
    min_replicas: int | None = None
    max_replicas: int = 0
    cooldown_period: int | None = None
    polling_interval: int | None = None
    status: str = "unknown"
    error: str | None = None
