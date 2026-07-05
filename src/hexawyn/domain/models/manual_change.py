from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

ActorType = Literal["human", "service_account", "gitops_controller"]
ManualChangeSeverity = Literal["critical", "warning"]


@dataclass(frozen=True)
class ManualChange:
    kind: str
    name: str
    namespace: str
    timestamp: str
    actor: str
    actor_type: ActorType
    changed_fields: list[str]
    severity: ManualChangeSeverity
    is_limited_actor_info: bool


@dataclass(frozen=True)
class ManualChangeOutsideGitOpsRequest:
    namespace: str
    window_days: int = 7


@dataclass(frozen=True)
class ManualChangeOutsideGitOpsReport:
    manual_changes: list[ManualChange]
    total_manual_changes: int
    excluded_gitops_change_count: int
    used_managed_fields_fallback: bool
    partial_window: bool
    notes: list[str] = field(default_factory=list)
