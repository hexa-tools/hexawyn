from dataclasses import dataclass


@dataclass(frozen=True)
class KedaTriggerauthListCommand:
    namespace: str | None = None
