from dataclasses import dataclass, field


@dataclass
class DiffHelmValuesResponse:
    release: str = ""
    source_namespace: str = ""
    target_namespace: str = ""
    diff_count: int = 0
    result: dict[str, object] = field(default_factory=dict)
    error: str | None = None
