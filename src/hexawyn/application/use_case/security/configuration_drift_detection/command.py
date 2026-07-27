from dataclasses import dataclass, field


@dataclass(frozen=True)
class ConfigurationDriftDetectionCommand:
    namespace: str
    kustomize_paths: list[str] = field(default_factory=list)
