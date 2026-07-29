from dataclasses import dataclass, field


@dataclass
class KedaScaledobjectsListResponse:
    scaled_objects: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
