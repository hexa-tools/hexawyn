from __future__ import annotations

from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class MTTRPerSeverity:
    severity: str
    mttr_minutes: float | None
    incident_count: int
    meets_benchmark: bool


@dataclass(frozen=True)
class SlowestIncident:
    incident_id: str
    service_name: str
    severity: str
    resolution_minutes: int
    root_cause: str
    month: str


@dataclass
class MTTRTrendReport:
    per_month: dict[str, dict[str, MTTRPerSeverity]] = field(default_factory=dict)
    slowest_incidents: list[SlowestIncident] = field(default_factory=list)
    trend: str = "stable"
    recommendation: str = ""
