from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class GitopsAppSyncResponse:
    name: str = ""
    namespace: str = ""
    sync_status: str = ""
    last_synced_at: str = ""
    revision: str = ""
    message: str = ""
    error: str | None = None
