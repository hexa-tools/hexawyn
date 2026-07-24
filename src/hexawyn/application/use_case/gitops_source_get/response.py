from dataclasses import dataclass


@dataclass
class GitopsSourceGetResponse:
    name: str = ""
    namespace: str | None = None
    kind: str = ""
    url: str | None = None
    ready: bool = False
    last_updated_at: str | None = None
    message: str | None = None
    error: str | None = None
