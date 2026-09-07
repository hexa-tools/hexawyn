from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class TraceK8sEventsCommand:
    namespace: str | None = None
    trace_id: str = ""
