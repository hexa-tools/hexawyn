from __future__ import annotations

from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class NightInterventionReport:
    period_label: str
    avg_interventions_per_night: float = 0.0
    previous_avg_per_night: float | None = None
    delta_pct: float = 0.0
    trend: str = "stable"
    summary: str = ""
