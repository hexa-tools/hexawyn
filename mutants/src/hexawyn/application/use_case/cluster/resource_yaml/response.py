from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
