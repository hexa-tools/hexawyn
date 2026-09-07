from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class RunWhatIfSimulationCommand:
    target_service: str = ""
    namespace: str = ""
    current_replicas: int | None = None
    proposed_replicas: int = 1
    current_cpu_utilization: float | None = None
