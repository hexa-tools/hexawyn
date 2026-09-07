from abc import ABC, abstractmethod
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class LogEntry(TypedDict):
    timestamp: str
    message: str
    severity: str


class LogsPort(ABC):
    """Port for log search — CloudWatch, Log Analytics, Cloud Logging, Datadog."""

    @abstractmethod
    def search_logs(
        self,
        pattern: str,
        time_window_minutes: int,
        namespace: str | None = None,
    ) -> list[LogEntry]:
        """Search logs matching pattern in the given time window."""
