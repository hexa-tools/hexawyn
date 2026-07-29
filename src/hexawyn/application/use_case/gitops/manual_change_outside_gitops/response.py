from dataclasses import dataclass, field
from typing import TypedDict


class ManualChangeDict(TypedDict):
    kind: str
    name: str
    namespace: str
    timestamp: str
    actor: str
    actor_type: str
    changed_fields: list[str]
    severity: str
    is_limited_actor_info: bool


@dataclass
class ManualChangeOutsideGitopsResponse:
    manual_changes: list[ManualChangeDict] = field(default_factory=list)
    total_manual_changes: int = 0
    excluded_gitops_change_count: int = 0
    used_managed_fields_fallback: bool = False
    partial_window: bool = False
    notes: list[str] = field(default_factory=list)
    error: str | None = None
