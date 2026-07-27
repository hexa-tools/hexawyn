from dataclasses import dataclass, field


@dataclass(frozen=True)
class GenerateIncidentTriageReportCommand:
    namespace: str = ""
    time_window_minutes: int = 60
    related_namespaces: list[str] = field(default_factory=list)
