from dataclasses import dataclass


@dataclass
class KedaTriggerauthGetResponse:
    name: str = ""
    namespace: str = ""
    kind: str = ""
    auth_type: str = ""
    secret_names: list[str] | None = None
    environment_names: list[str] | None = None
    pod_identity_provider: str = ""
    ready: bool = False
    message: str = ""
    error: str | None = None
