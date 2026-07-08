from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class MatchedResourceDict(TypedDict):
    name: str
    namespace: str
    kind: str
    node: str | None
    phase: str | None
    ready: bool | None
    is_healthy: bool | None
    labels: dict[str, str]


class NamespaceGroupDict(TypedDict):
    namespace: str
    resources: list[MatchedResourceDict]


@dataclass
class SearchResourcesByLabelsResponse:
    label_selector: str = ""
    total_matched: int = 0
    groups: list[NamespaceGroupDict] = field(default_factory=list)
    has_more: bool = False
    remaining_count: int = 0
    no_matches: bool = False
    summary: str = ""
    error: str | None = None
