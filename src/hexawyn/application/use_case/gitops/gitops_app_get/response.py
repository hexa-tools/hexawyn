from dataclasses import dataclass


@dataclass
class GitopsAppGetResponse:
    name: str = ""
    namespace: str = ""
    engine: str = ""
    kind: str = ""
    sync_status: str = ""
    health_status: str = ""
    last_synced_at: str | None = None
    last_commit: str = ""
    source_url: str = ""
    revision: str | None = None
    message: str | None = None
    error: str | None = None
