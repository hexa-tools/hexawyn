from dataclasses import dataclass


@dataclass
class GitopsAppSyncResponse:
    name: str = ""
    namespace: str = ""
    sync_status: str = ""
    last_synced_at: str = ""
    revision: str = ""
    message: str = ""
    error: str | None = None
