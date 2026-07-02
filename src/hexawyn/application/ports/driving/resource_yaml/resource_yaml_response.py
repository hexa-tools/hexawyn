from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ResourceYAMLResponse:
    resource_name: str = ""
    namespace: str = ""
    kind: str = ""
    resource_found: bool = False
    yaml_data: dict[str, object] = field(default_factory=dict)
    image_tags: list[str] = field(default_factory=list)
    resource_limits: dict[str, str] | None = None
    error: str | None = None
