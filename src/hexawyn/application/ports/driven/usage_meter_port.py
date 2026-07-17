from abc import ABC, abstractmethod


class UsageMeterPort(ABC):
    """Current consumption — read-only for display purposes."""

    @abstractmethod
    def get_usage(self, resource: str) -> int:
        """Current month's consumption for this resource."""
