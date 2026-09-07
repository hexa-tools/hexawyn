from __future__ import annotations

from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class UnauthorizedAccessReport:
    period_label: str
    attempt_count: int = 0
    window_minutes: int = 30
    source_type: str = "unknown"
    alert_level: str = "low"
    has_data: bool = True
    warning: str = ""
