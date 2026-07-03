from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

ResourceType = Literal["pods", "deployments", "services", "configmaps"]
ResourceKind = Literal["pod", "deployment", "service", "configmap"]

_ALL_RESOURCE_TYPES: list[ResourceType] = ["pods", "deployments", "services", "configmaps"]


@dataclass(frozen=True)
class MatchedResourceResult:
    """One resource matched by a label selector — node/phase/ready are pod-only."""

    name: str
    namespace: str
    kind: ResourceKind
    node: str | None
    phase: str | None
    ready: bool | None
    is_healthy: bool | None
    labels: dict[str, str]


@dataclass(frozen=True)
class NamespaceGroup:
    namespace: str
    resources: list[MatchedResourceResult] = field(default_factory=list)


@dataclass(frozen=True)
class LabelSearchRequest:
    label_selector: str
    resource_types: list[ResourceType] = field(default_factory=lambda: list(_ALL_RESOURCE_TYPES))
    namespace: str | None = None


@dataclass(frozen=True)
class LabelSearchResult:
    label_selector: str
    total_matched: int
    groups: list[NamespaceGroup] = field(default_factory=list)
    has_more: bool = False
    remaining_count: int = 0
    no_matches: bool = False
    summary: str = ""
