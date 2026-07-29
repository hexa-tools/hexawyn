from dataclasses import dataclass


@dataclass
class GitopsDetectResponse:
    engine: str = ""
    version: str = ""
    namespace: str = ""
    apps_count: int = 0
    out_of_sync_count: int = 0
    failed_count: int = 0
    error: str | None = None
