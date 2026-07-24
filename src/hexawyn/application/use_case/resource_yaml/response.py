from dataclasses import dataclass


@dataclass
class ResourceYamlResponse:
    yaml_content: str = ""
    error: str | None = None
