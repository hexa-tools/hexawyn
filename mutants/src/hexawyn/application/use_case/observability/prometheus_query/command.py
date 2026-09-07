from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class PrometheusQueryCommand:
    end: str = ""
    query_type: str = ""
    start: str = ""
    step: str = ""
    timeout_seconds: str = ""
    unit_hint: str = ""
