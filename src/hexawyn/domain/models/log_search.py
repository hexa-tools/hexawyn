from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

MatchType = Literal["exact", "semantic"]


@dataclass(frozen=True)
class MatchedLogLine:
    timestamp: str
    message: str
    match_type: MatchType


@dataclass(frozen=True)
class PodLogMatch:
    """One (pod, container) pair with its matching lines — a pod with matches
    in 2 containers produces 2 PodLogMatch entries, not 1."""

    pod_name: str
    namespace: str
    container: str
    matching_lines: list[MatchedLogLine] = field(default_factory=list)


@dataclass(frozen=True)
class ServiceGroup:
    service_name: str
    namespace: str
    pods: list[PodLogMatch] = field(default_factory=list)


@dataclass(frozen=True)
class SkippedPod:
    pod_name: str
    namespace: str
    reason: str


@dataclass(frozen=True)
class SkippedNamespace:
    namespace: str
    reason: str


@dataclass(frozen=True)
class LogSearchRequest:
    pattern: str
    is_regex: bool = False
    namespace: str | None = None
    time_window_minutes: int = 60


@dataclass(frozen=True)
class LogSearchResult:
    pattern: str
    time_window_minutes: int
    namespaces_total: int
    groups: list[ServiceGroup] = field(default_factory=list)
    pods_affected: int = 0
    services_affected: int = 0
    skipped_pods: list[SkippedPod] = field(default_factory=list)
    skipped_namespaces: list[SkippedNamespace] = field(default_factory=list)
    scanned_namespaces: list[str] = field(default_factory=list)
    no_matches: bool = False
    summary: str = ""
