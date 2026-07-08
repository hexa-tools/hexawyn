from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class GenerateIncidentTriageReportCommand:
    namespace: str
    time_window_minutes: int = 120
    related_namespaces: list[str] = field(default_factory=list)
