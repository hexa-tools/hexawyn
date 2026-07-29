from dataclasses import dataclass


@dataclass
class GitopsAppStatusResponse:
    name: str = ""
    namespace: str = ""
    sync_status: str = ""
    health_status: str = ""
    last_synced_at: str = ""
    last_commit: str = ""
    revision: str = ""
    message: str = ""
    error: str | None = None
