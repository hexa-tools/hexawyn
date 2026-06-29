from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, TypedDict

from hexawyn.domain.models.cluster import ClusterContext

# ── Types ───────────────────────────────────────────────────


@dataclass
class StartupScanResult:
    health_score: int = 0
    narrative_summary: str = ""
    provider_badge: str = ""
    top_issues: list[str] = field(default_factory=list)
    suggestions: list[dict[str, str]] = field(default_factory=list)
    provider: str = ""
    provider_display: str = ""
    cluster_summary: dict[str, int | str] = field(default_factory=dict)
    findings: list[dict[str, str]] = field(default_factory=list)


class InvestigationOutput(TypedDict):
    answer: str
    cause: str
    solution: str
    status: str
    suggestions: list[str]
    error: str | None


class QuotaCheckResult(TypedDict):
    allowed: bool
    used: int
    limit: int
    remaining: int


# ── Port ────────────────────────────────────────────────────


class RuntimePort(ABC):
    @abstractmethod
    def set_adapter(self, adapter: Any) -> None: ...

    @abstractmethod
    def run_investigation(
        self, query: str, cluster_context: ClusterContext
    ) -> InvestigationOutput: ...

    @abstractmethod
    def run_startup_scan(self, cluster_name: str) -> StartupScanResult: ...

    @abstractmethod
    def check_quota(self) -> QuotaCheckResult: ...

    @abstractmethod
    def increment_quota(self) -> None: ...
