from hexawyn.domain.models.quota import UsageQuota


class TestUsageQuota:
    def test_is_dataclass(self):
        q = UsageQuota(month="2026-06", count=0)
        assert q.month == "2026-06"
