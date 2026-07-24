from dataclasses import dataclass


@dataclass
class GitopsAppStatusResponse:
    name: str = ""
    namespace: str | None = None
    sync_status: str = ""
    health_status: str = ""
    last_synced_at: str | None = None
    last_commit: str | None = None
    revision: str | None = None
    message: str | None = None
    error: str | None = None
