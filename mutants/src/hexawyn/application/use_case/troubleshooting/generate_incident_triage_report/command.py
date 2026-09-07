from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class GenerateIncidentTriageReportCommand:
    namespace: str = ""
    time_window_minutes: int = 60
    related_namespaces: list[str] = field(default_factory=list)
