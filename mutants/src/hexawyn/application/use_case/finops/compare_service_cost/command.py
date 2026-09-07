from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class CompareServiceCostCommand:
    service_name: str
    cpu_price_per_core_hour: float = 0.03
    memory_price_per_gb_hour: float = 0.01
