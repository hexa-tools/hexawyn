from dataclasses import dataclass, field


@dataclass(frozen=True)
class SensitiveDataAuditCommand:
    pattern: str = ""
    time_window_minutes: int = 30
    allowlist: list[str] = field(default_factory=list)
