from dataclasses import dataclass, field


@dataclass
class KedaScaledobjectTriggersResponse:
    triggers: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
