from dataclasses import dataclass, field


@dataclass
class DetectMissingProbesResponse:
    result: dict[str, object] = field(default_factory=dict)
