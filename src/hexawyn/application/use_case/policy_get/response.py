from dataclasses import dataclass


@dataclass
class PolicyGetResponse:
    name: str = ""
    kind: str = ""
    action: str = ""
    status: str = ""
    error: str | None = None
