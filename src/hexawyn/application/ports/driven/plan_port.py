from abc import ABC, abstractmethod


class PlanPort(ABC):
    """Source of quotas — reflects the Pricing Matrix (Notion)."""

    @abstractmethod
    def get_limit(self, resource: str) -> int | None:
        """Return the limit for a resource. None = unlimited."""

    @abstractmethod
    def is_available(self, feature: str) -> bool:
        """Is the feature available in the current plan?"""

    @abstractmethod
    def tier_required_for(self, feature: str) -> str | None:
        """Minimum tier required to unlock this feature."""
