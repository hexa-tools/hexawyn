import pytest


class TestQuotaStorePortABC:
    def test_quota_store_port_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.quota_port import QuotaStorePort

        with pytest.raises(TypeError):
            QuotaStorePort()  # type: ignore[abstract]

    def test_concrete_implementation_works(self) -> None:
        from hexawyn.application.ports.driven.quota_port import QuotaStorePort
        from hexawyn.domain.models.quota import LicenseTier, SlackQuota, UsageQuota

        class InMemoryQuotaStore(QuotaStorePort):
            def get_investigation_quota(self, month: str) -> UsageQuota:
                return UsageQuota(month=month, count=0, limit=50)

            def get_slack_quota(self, month: str) -> SlackQuota:
                return SlackQuota(month=month, count=0, limit=5)

            def increment_investigation(self, month: str, tier: LicenseTier, limit: int) -> None:
                pass

            def increment_slack(self, month: str, tier: LicenseTier, limit: int) -> None:
                pass

        store = InMemoryQuotaStore()
        quota = store.get_investigation_quota("2026-06")
        assert quota.count == 0
        assert quota.limit == 50
