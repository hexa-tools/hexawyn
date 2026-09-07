from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ForecastCostCommand:
    historical_days: int = 7
    top_n_drivers: int = 3
