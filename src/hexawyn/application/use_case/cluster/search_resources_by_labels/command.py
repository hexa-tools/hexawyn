from dataclasses import dataclass, field


@dataclass(frozen=True)
class SearchResourcesByLabelsCommand:
    namespace: str | None = None
    label_selector: str = ""
    resource_types: list[str] = field(default_factory=list)
