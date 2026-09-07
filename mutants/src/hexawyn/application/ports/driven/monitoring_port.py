from abc import ABC, abstractmethod


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class MonitoringPort(ABC):
    """Port for monitoring observability — Datadog, Prometheus, CloudWatch, Azure Monitor."""

    @abstractmethod
    def get_triggered_monitors(self) -> list[dict[str, str | int | float]]:
        """Get currently triggered monitors/alerts."""

    @abstractmethod
    def get_apm_services(self) -> list[dict[str, str | int | float]]:
        """Get APM service metrics (p99 latency, error rate)."""
