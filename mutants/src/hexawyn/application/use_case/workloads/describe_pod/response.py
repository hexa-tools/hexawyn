from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class DescribePodResponse:
    pod_name: str = ""
    namespace: str = ""
    status: str = ""
    restarts: int = 0
    node: str = ""
    age: str = ""
    error: str | None = None
