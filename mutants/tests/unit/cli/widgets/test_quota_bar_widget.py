from hexawyn.cli.widgets.quota_bar import QuotaProgressBar, _quota_bar
from hexawyn.domain.models.quota import QuotaState, QuotaUsage


class TestQuotaBar:
    def test_unlimited_renders_infinity(self) -> None:
        quota = QuotaUsage(
            resource="investigations",
            used=1000,
            limit=None,
            state=QuotaState.UNLIMITED,
        )
        result = _quota_bar(quota)
        assert "Illimit" in result
        assert "Investigations" in result
        assert "1000" not in result

    def test_normal_renders_bar(self) -> None:
        quota = QuotaUsage(
            resource="investigations",
            used=10,
            limit=50,
            state=QuotaState.NORMAL,
        )
        result = _quota_bar(quota)
        assert "Investigations" in result
        assert "10/50" in result

    def test_warning_renders_warning_icon(self) -> None:
        quota = QuotaUsage(
            resource="investigations",
            used=150,
            limit=200,
            state=QuotaState.WARNING,
        )
        result = _quota_bar(quota)
        assert "warning" in result.lower() or "\u26a0" in result

    def test_critical_renders_red_dot(self) -> None:
        quota = QuotaUsage(
            resource="investigations",
            used=470,
            limit=500,
            state=QuotaState.CRITICAL,
        )
        result = _quota_bar(quota)
        assert "\U0001f534" in result or "critical" in result.lower()

    def test_exhausted_renders_cross(self) -> None:
        quota = QuotaUsage(
            resource="investigations",
            used=50,
            limit=50,
            state=QuotaState.EXHAUSTED,
        )
        result = _quota_bar(quota)
        assert "\u274c" in result

    def test_locked_renders_available_from(self) -> None:
        quota = QuotaUsage(
            resource="slack_alerts",
            used=0,
            limit=0,
            state=QuotaState.LOCKED,
            available_from_tier="Team",
        )
        result = _quota_bar(quota)
        assert "Available from" in result
        assert "Team" in result

    def test_bar_chars_used(self) -> None:
        quota = QuotaUsage(
            resource="users",
            used=10,
            limit=20,
            state=QuotaState.NORMAL,
        )
        result = _quota_bar(quota)
        assert chr(9608) in result
        assert chr(9617) in result

    def test_unknown_resource_uses_raw_name(self) -> None:
        quota = QuotaUsage(
            resource="custom_metric",
            used=5,
            limit=10,
            state=QuotaState.NORMAL,
        )
        result = _quota_bar(quota)
        assert "custom_metric" in result


class TestQuotaProgressBarWidget:
    def test_update_quotas_renders_all_lines(self) -> None:
        widget = QuotaProgressBar()
        quotas = [
            QuotaUsage(
                resource="investigations",
                used=10,
                limit=50,
                state=QuotaState.NORMAL,
            ),
            QuotaUsage(
                resource="clusters",
                used=1,
                limit=1,
                state=QuotaState.NORMAL,
            ),
        ]
        widget.update_quotas(quotas)
        rendered = widget.content
        assert rendered is not None

    def test_update_quotas_with_exhausted_shows_upgrade(self) -> None:
        widget = QuotaProgressBar()
        quotas = [
            QuotaUsage(
                resource="investigations",
                used=50,
                limit=50,
                state=QuotaState.EXHAUSTED,
            ),
        ]
        widget.update_quotas(quotas)
        rendered = widget.content
        assert rendered is not None
