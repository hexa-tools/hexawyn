from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

DiffReason = Literal["never_promoted", "version_mismatch", "secret_manual", "crd_missing", "other"]
SyncStatus = Literal["in_sync", "out_of_sync"]
DiffPriority = Literal["blocking", "informational"]


@dataclass(frozen=True)
class ResourceDiff:
    resource: str
    namespace: str
    reason: str
    priority: str
    staging_value: str
    prod_value: str
    detail: str


@dataclass
class PromotionChecklist:
    ready_to_promote: list[str] = field(default_factory=list)
    requires_review: list[str] = field(default_factory=list)


@dataclass
class ClusterDiffReport:
    source_cluster: str
    target_cluster: str
    in_staging_not_prod: list[ResourceDiff] = field(default_factory=list)
    version_mismatches: list[ResourceDiff] = field(default_factory=list)
    prod_only: list[ResourceDiff] = field(default_factory=list)
    promotion_checklist: PromotionChecklist | None = None
    sync_status: str = "in_sync"
    total_differences: int = 0
    has_data: bool = True
    warning: str = ""
