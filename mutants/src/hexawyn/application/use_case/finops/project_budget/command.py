from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ProjectBudgetCommand:
    history_months: int = 6
    horizon_months: int = 3
    budget_threshold_usd: float = 1000.0
    exclude_months: list[str] = field(default_factory=list)
