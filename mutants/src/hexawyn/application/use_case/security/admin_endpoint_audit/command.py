from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class AdminEndpointAuditCommand:
    endpoint_pattern: str = "/admin"
    time_window_minutes: int = 30
    flag_threshold: int = 5
