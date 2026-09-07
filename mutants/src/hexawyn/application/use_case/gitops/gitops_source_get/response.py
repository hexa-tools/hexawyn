from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class GitopsSourceGetResponse:
    name: str = ""
    namespace: str = ""
    kind: str = ""
    url: str = ""
    ready: bool = False
    last_updated_at: str = ""
    message: str = ""
    error: str | None = None
