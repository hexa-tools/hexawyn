from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class PolicyExplainDenialCommand:
    name: str = ""
    namespace: str = ""
    resource_kind: str = ""
    resource_name: str = ""
    name: str  # type: ignore
    namespace: str  # type: ignore
