from abc import ABC, abstractmethod


class DatadogMonitoringPort(ABC):
    """Port for Datadog-specific monitoring operations."""

    @abstractmethod
    def get_triggered_monitors(self) -> list[dict[str, str | int | float]]:
        """Get currently triggered Datadog monitors."""

    @abstractmethod
    def get_apm_services(self) -> list[dict[str, str | int | float]]:
        """Get APM service metrics (p99 latency, error rate)."""
