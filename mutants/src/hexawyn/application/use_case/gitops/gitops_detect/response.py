from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class GitopsDetectResponse:
    engine: str = ""
    version: str = ""
    namespace: str = ""
    apps_count: int = 0
    out_of_sync_count: int = 0
    failed_count: int = 0
    error: str | None = None
