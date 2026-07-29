from dataclasses import dataclass, field


@dataclass
class ResourceYamlResponse:
    resource_name: str = ""
    namespace: str = ""
    kind: str = ""
    resource_found: bool = False
    yaml_data: str = ""
    image_tags: list[str] = field(default_factory=list)
    resource_limits: dict[str, object] = field(default_factory=dict)
    error: str | None = None
