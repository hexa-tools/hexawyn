from dataclasses import dataclass


@dataclass
class KedaTriggerauthGetResponse:
    name: str = ""
    namespace: str | None = None
    kind: str = ""
    error: str | None = None
