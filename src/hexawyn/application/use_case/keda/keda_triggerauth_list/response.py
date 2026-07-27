from dataclasses import dataclass, field


@dataclass
class KedaTriggerauthListResponse:
    trigger_auths: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
