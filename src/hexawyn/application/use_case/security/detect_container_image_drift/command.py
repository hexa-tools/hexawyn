from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class DetectContainerImageDriftCommand:
    namespace: str
    kustomize_paths: list[str] = field(default_factory=list)
