from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GitOpsSourceGetResponse:
    name: str = ""
    namespace: str = ""
    kind: str = ""
    url: str = ""
    ready: bool = False
    last_updated_at: str | None = None
    message: str | None = None
    error: str | None = None
