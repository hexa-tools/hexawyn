from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

DriftType = Literal["tag_mismatch", "digest_mismatch"]
ImageDriftSeverity = Literal["critical"]


@dataclass(frozen=True)
class ImageReference:
    repository: str
    tag: str | None
    digest: str | None


@dataclass(frozen=True)
class ContainerImageDrift:
    deployment: str
    namespace: str
    container: str
    running_image: str
    declared_image: str
    source_of_truth: str
    drift_type: DriftType
    severity: ImageDriftSeverity


@dataclass(frozen=True)
class ContainerImageDriftRequest:
    namespace: str
    kustomize_paths: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ContainerImageDriftReport:
    out_of_sync: list[ContainerImageDrift]
    in_sync_count: int
    excluded_count: int
    total_checked: int
    summary: str
