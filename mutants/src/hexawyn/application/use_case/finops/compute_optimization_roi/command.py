from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ComputeOptimizationRoiCommand:
    sprint_id: str
    traffic_growth_pct: float = 0.0
