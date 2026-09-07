from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ChatSlackCommand:
    query: str
    cluster_name: str
    channel_id: str
    thread_ts: str | None = None
