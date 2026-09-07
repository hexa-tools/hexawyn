from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class PolicyGetResponse:
    name: str = ""
    namespace: str = ""
    engine: str = ""
    kind: str = ""
    action: str = ""
    description: str = ""
    rules_count: int = 0
    violations_count: int = 0
    ready: bool = False
    error: str | None = None
