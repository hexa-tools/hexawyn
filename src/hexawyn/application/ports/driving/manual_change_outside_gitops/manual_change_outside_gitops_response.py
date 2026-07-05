from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, TypedDict


class ManualChangeDict(TypedDict):
    kind: str
    name: str
    namespace: str
    timestamp: str
    actor: str
    actor_type: Literal["human", "service_account", "gitops_controller"]
    changed_fields: list[str]
    severity: Literal["critical", "warning"]
    is_limited_actor_info: bool


@dataclass
class ManualChangeOutsideGitOpsResponse:
    manual_changes: list[ManualChangeDict] = field(default_factory=list)
    total_manual_changes: int = 0
    excluded_gitops_change_count: int = 0
    used_managed_fields_fallback: bool = False
    partial_window: bool = False
    notes: list[str] = field(default_factory=list)
    error: str | None = None
