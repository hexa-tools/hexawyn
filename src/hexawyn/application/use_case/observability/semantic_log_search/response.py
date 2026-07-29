from dataclasses import dataclass
from typing import TypedDict


@dataclass
class SemanticLogSearchResponse:
    time_window_minutes: str = ""
    summary: str = ""
    skipped_pods: str = ""
    skipped_namespaces: str = ""
    services_affected: str = ""
    scanned_namespaces: str = ""
    pods_affected: str = ""
    pattern: str = ""
    no_matches: str = ""
    namespaces_total: str = ""
    groups: str = ""
    error: str | None = None


class MatchedLogLineDict(TypedDict):
    line: str
    similarity: float


class PodLogMatchDict(TypedDict):
    pod_name: str
    namespace: str
    matches: list[MatchedLogLineDict]


class ServiceGroupDict(TypedDict):
    service_name: str
    pods: list[PodLogMatchDict]


class SkippedNamespaceDict(TypedDict):
    namespace: str
    reason: str


class SkippedPodDict(TypedDict):
    pod_name: str
    namespace: str
    reason: str
