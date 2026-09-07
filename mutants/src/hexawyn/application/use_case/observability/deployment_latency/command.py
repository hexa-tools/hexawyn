from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class DeploymentLatencyCommand:
    service_name: str
    regression_threshold_pct: float = 20.0
