from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GitOpsAppStatusResponse:
    name: str = ""
    namespace: str = ""
    sync_status: str = "unknown"
    health_status: str = "unknown"
    last_synced_at: str | None = None
    last_commit: str | None = None
    revision: str | None = None
    message: str | None = None
    error: str | None = None
