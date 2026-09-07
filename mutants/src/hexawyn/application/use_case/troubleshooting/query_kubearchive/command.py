from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class QueryKubearchiveCommand:
    namespace: str
    resource_type: str = "pods"
    timestamp: str = ""
    compare_with_current: bool = False
