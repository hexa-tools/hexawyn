from abc import ABC, abstractmethod

from hexawyn.domain.models.quota import LicenseTier, SlackQuota, UsageQuota


class QuotaStorePort(ABC):
    """Port for quota storage — abstracts DuckDB away from quota_manager."""

    @abstractmethod
    def get_investigation_quota(self, month: str) -> UsageQuota:
        """Get investigation quota for a given month."""

    @abstractmethod
    def get_slack_quota(self, month: str) -> SlackQuota:
        """Get Slack alert quota for a given month."""

    @abstractmethod
    def increment_investigation(self, month: str, tier: LicenseTier, limit: int) -> None:
        """Increment investigation counter for a given month."""

    @abstractmethod
    def increment_slack(self, month: str, tier: LicenseTier, limit: int) -> None:
        """Increment Slack alert counter for a given month."""
