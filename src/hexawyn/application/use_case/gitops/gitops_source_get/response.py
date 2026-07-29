from dataclasses import dataclass


@dataclass
class GitopsSourceGetResponse:
    name: str = ""
    namespace: str = ""
    kind: str = ""
    url: str = ""
    ready: bool = False
    last_updated_at: str = ""
    message: str = ""
    error: str | None = None
