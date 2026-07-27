from dataclasses import dataclass, field
from typing import TypedDict


class MatchedResourceDict(TypedDict):
    name: str
    namespace: str
    kind: str
    node: str
    phase: str
    ready: bool


class NamespaceGroupDict(TypedDict):
    namespace: str
    resources: list[MatchedResourceDict]


@dataclass
class SearchResourcesByLabelsResponse:
    label_selector: str = ""
    total_matched: int = 0
    groups: list[NamespaceGroupDict] = field(default_factory=list)
    total_resources: int = 0
    has_more: bool = False
    remaining_count: int = 0
    no_matches: bool = True
    summary: str = ""
    error: str | None = None
