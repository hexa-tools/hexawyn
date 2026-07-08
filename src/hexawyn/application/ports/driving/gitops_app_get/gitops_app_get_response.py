from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GitOpsAppGetResponse:
    name: str = ""
    namespace: str = ""
    engine: str = "unknown"
    kind: str = ""
    sync_status: str = "unknown"
    health_status: str = "unknown"
    last_synced_at: str | None = None
    last_commit: str | None = None
    source_url: str | None = None
    revision: str | None = None
    message: str | None = None
    error: str | None = None
