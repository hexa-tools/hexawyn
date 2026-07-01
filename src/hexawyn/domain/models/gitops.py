from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class GitOpsEngine(Enum):
    FLUX = "flux"
    ARGOCD = "argocd"
    NONE = "none"


class SyncStatus(Enum):
    SYNCED = "synced"
    OUT_OF_SYNC = "out_of_sync"
    UNKNOWN = "unknown"
    FAILED = "failed"


class HealthStatus(Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    PROGRESSING = "progressing"
    SUSPENDED = "suspended"
    MISSING = "missing"


@dataclass(frozen=True)
class GitOpsApp:
    name: str
    namespace: str
    engine: GitOpsEngine
    kind: str
    sync_status: SyncStatus
    health_status: HealthStatus
    last_synced_at: str | None = None
    last_commit: str | None = None
    source_url: str | None = None
    revision: str | None = None
    message: str | None = None


@dataclass(frozen=True)
class GitOpsSource:
    name: str
    namespace: str
    kind: str
    url: str
    ready: bool
    last_updated_at: str | None = None
    message: str | None = None


@dataclass(frozen=True)
class GitOpsDetectionResult:
    engine: GitOpsEngine
    version: str | None
    namespace: str | None
    apps_count: int
    out_of_sync_count: int
    failed_count: int
