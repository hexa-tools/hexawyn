from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class CveSummary:
    business_service_name: str
    severity: str
    count: int
    oldest_unresolved_days: int


@dataclass
class CriticalCveReport:
    period_label: str
    total_critical_cves: int = 0
    affected_service_count: int = 0
    oldest_unresolved_days: int = 0
    cves: list[CveSummary] = field(default_factory=list)
    total_images_scanned: int = 0
    has_data: bool = True
    warning: str = ""
