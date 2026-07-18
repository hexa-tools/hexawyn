class TestQuotaRenderer:
    def test_state_icons_are_consistent(self) -> None:
        from hexawyn.cli.presentation.quota_renderer import QUOTA_STATE_ICONS
        from hexawyn.domain.models.quota import QuotaState

        assert "\u26a0" in QUOTA_STATE_ICONS[QuotaState.WARNING]
        assert "\U0001f534" in QUOTA_STATE_ICONS[QuotaState.CRITICAL]
        assert "\u274c" in QUOTA_STATE_ICONS[QuotaState.EXHAUSTED]
        assert QUOTA_STATE_ICONS[QuotaState.NORMAL] == ""

    def test_resource_labels_are_consistent(self) -> None:
        from hexawyn.cli.presentation.quota_renderer import QUOTA_RESOURCE_LABELS

        assert QUOTA_RESOURCE_LABELS["investigations"] == "Investigations"
        assert QUOTA_RESOURCE_LABELS["slack_alerts"] == "Slack alerts"

    def test_compute_bar_fill(self) -> None:
        from hexawyn.cli.presentation.quota_renderer import compute_bar_fill

        filled, pct = compute_bar_fill(5, 10, 20)
        assert filled == 10
        assert pct == 50.0

        filled, pct = compute_bar_fill(10, 10, 20)
        assert filled == 20
        assert pct == 100.0

        filled, pct = compute_bar_fill(0, 10, 20)
        assert filled == 0
        assert pct == 0.0
