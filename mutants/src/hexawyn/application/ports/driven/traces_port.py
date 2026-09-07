from abc import ABC, abstractmethod
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class SlowTrace(TypedDict):
    trace_id: str
    service: str
    duration_ms: int
    is_error: bool


class TracesPort(ABC):
    """Port for distributed traces — OTel, Datadog APM, Cloud Trace."""

    @abstractmethod
    def get_slow_traces(
        self,
        service: str,
        threshold_ms: int,
        time_window_minutes: int,
    ) -> list[SlowTrace]:
        """Get traces slower than threshold_ms for a given service."""
