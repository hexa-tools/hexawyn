from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

DriftSeverity = Literal["critical", "warning", "info"]
ManagedBy = Literal["helm", "kustomize"]


@dataclass(frozen=True)
class DriftedField:
    field_path: str
    desired_value: str
    live_value: str
    severity: DriftSeverity


@dataclass(frozen=True)
class ResourceManifest:
    kind: str
    name: str
    namespace: str
    data: dict[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class DriftResult:
    kind: str
    name: str
    namespace: str
    managed_by: ManagedBy
    release_or_source: str
    drifted_fields: list[DriftedField]
    has_critical_drift: bool
    is_orphaned: bool


@dataclass(frozen=True)
class ConfigurationDriftRequest:
    namespace: str
    kustomize_paths: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ConfigurationDriftReport:
    drifted_resources: list[DriftResult]
    drifted_by_namespace: dict[str, list[DriftResult]]
    in_sync_count: int
    excluded_resources: list[str]
    total_checked: int
    summary: str
