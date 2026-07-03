from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class MatchedLogLineDict(TypedDict):
    timestamp: str
    message: str
    match_type: str


class PodLogMatchDict(TypedDict):
    pod_name: str
    namespace: str
    container: str
    matching_lines: list[MatchedLogLineDict]


class ServiceGroupDict(TypedDict):
    service_name: str
    namespace: str
    pods: list[PodLogMatchDict]


class SkippedPodDict(TypedDict):
    pod_name: str
    namespace: str
    reason: str


class SkippedNamespaceDict(TypedDict):
    namespace: str
    reason: str


@dataclass
class SemanticLogSearchResponse:
    pattern: str = ""
    time_window_minutes: int = 0
    groups: list[ServiceGroupDict] = field(default_factory=list)
    pods_affected: int = 0
    services_affected: int = 0
    skipped_pods: list[SkippedPodDict] = field(default_factory=list)
    skipped_namespaces: list[SkippedNamespaceDict] = field(default_factory=list)
    scanned_namespaces: list[str] = field(default_factory=list)
    namespaces_total: int = 0
    no_matches: bool = False
    summary: str = ""
    error: str | None = None
