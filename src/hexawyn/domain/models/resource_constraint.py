from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum


class RiskLevel(str, Enum):
    CRITICAL = "CRITICAL"
    NO_LIMITS = "NO_LIMITS"
    OK = "OK"


@dataclass
class ContainerResourceEntry:
    container_name: str
    pod_name: str
    namespace: str
    cpu_usage_millicores: int
    cpu_limit_millicores: int | None
    memory_usage_bytes: int
    memory_limit_bytes: int | None
    cpu_pct: float | None
    memory_pct: float | None
    risk_level: RiskLevel
    is_init_container: bool = False
    tags: list[str] = field(default_factory=list)


@dataclass
class ResourceConstraintReport:
    namespace: str
    total_pods_scanned: int
    total_containers: int
    critical_count: int = 0
    no_limits_count: int = 0
    ok_count: int = 0
    containers: list[ContainerResourceEntry] = field(default_factory=list)
    generated_at: datetime = field(default_factory=lambda: datetime.now(UTC))
