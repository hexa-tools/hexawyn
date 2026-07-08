from __future__ import annotations

from dataclasses import dataclass


@dataclass
class KedaTriggerAuthGetResponse:
    name: str = ""
    namespace: str = ""
    kind: str = ""
    auth_type: str = "unknown"
    secret_names: list[str] | None = None
    environment_names: list[str] | None = None
    pod_identity_provider: str | None = None
    ready: bool = False
    message: str | None = None
    error: str | None = None
