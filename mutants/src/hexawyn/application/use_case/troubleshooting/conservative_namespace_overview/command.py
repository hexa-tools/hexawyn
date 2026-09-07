from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ConservativeNamespaceOverviewCommand:
    namespace: str = ""
    max_tokens: int = 2000
