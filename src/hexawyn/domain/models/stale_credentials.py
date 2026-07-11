from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class StaleCredential:
    name: str
    risk_level: str
    days_unrotated: int


@dataclass
class StaleCredentialsReport:
    period_label: str
    total_stale: int = 0
    critical_count: int = 0
    credentials: list[StaleCredential] = field(default_factory=list)
    has_data: bool = True
    warning: str = ""
