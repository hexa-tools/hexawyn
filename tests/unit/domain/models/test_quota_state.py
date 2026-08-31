from hexawyn.domain.models.quota import UNLIMITED, QuotaState, QuotaUsage


class TestQuotaState:
    def test_has_six_states(self) -> None:
        states = [
            QuotaState.NORMAL,
            QuotaState.WARNING,
            QuotaState.CRITICAL,
            QuotaState.EXHAUSTED,
            QuotaState.UNLIMITED,
            QuotaState.LOCKED,
        ]
        assert len(states) == 6  # noqa: PLR2004

    def test_state_values(self) -> None:
        assert QuotaState.NORMAL.value == "normal"
        assert QuotaState.WARNING.value == "warning"
        assert QuotaState.CRITICAL.value == "critical"
        assert QuotaState.EXHAUSTED.value == "exhausted"
        assert QuotaState.UNLIMITED.value == "unlimited"
        assert QuotaState.LOCKED.value == "locked"


class TestQuotaUsage:
    def test_percentage_under_limit(self) -> None:
        usage = QuotaUsage(resource="investigations", used=247, limit=500, state=QuotaState.NORMAL)
        assert usage.percentage == 49.4  # noqa: PLR2004

    def test_percentage_at_exhausted(self) -> None:
        usage = QuotaUsage(resource="investigations", used=50, limit=50, state=QuotaState.EXHAUSTED)
        assert usage.percentage == 100.0  # noqa: PLR2004

    def test_percentage_caps_at_100(self) -> None:
        usage = QuotaUsage(resource="investigations", used=60, limit=50, state=QuotaState.EXHAUSTED)
        assert usage.percentage == 100.0  # noqa: PLR2004

    def test_percentage_none_for_unlimited(self) -> None:
        usage = QuotaUsage(
            resource="investigations", used=1247, limit=None, state=QuotaState.UNLIMITED
        )
        assert usage.percentage is None

    def test_percentage_none_for_zero_limit(self) -> None:
        usage = QuotaUsage(resource="investigations", used=0, limit=0, state=QuotaState.LOCKED)
        assert usage.percentage is None

    def test_should_render_bar_for_normal(self) -> None:
        usage = QuotaUsage(resource="investigations", used=10, limit=50, state=QuotaState.NORMAL)
        assert usage.should_render_bar is True

    def test_should_render_bar_for_warning(self) -> None:
        usage = QuotaUsage(resource="investigations", used=40, limit=50, state=QuotaState.WARNING)
        assert usage.should_render_bar is True

    def test_should_render_bar_false_for_unlimited(self) -> None:
        usage = QuotaUsage(
            resource="investigations", used=999, limit=None, state=QuotaState.UNLIMITED
        )
        assert usage.should_render_bar is False

    def test_should_render_bar_false_for_locked(self) -> None:
        usage = QuotaUsage(
            resource="investigations",
            used=0,
            limit=0,
            state=QuotaState.LOCKED,
            available_from_tier="Team",
        )
        assert usage.should_render_bar is False

    def test_state_from_usage_below_80(self) -> None:
        assert QuotaUsage.compute_state(30, 50) == QuotaState.NORMAL

    def test_state_from_usage_warning_boundary(self) -> None:
        assert QuotaUsage.compute_state(40, 50) == QuotaState.WARNING

    def test_state_from_usage_critical_boundary(self) -> None:
        assert QuotaUsage.compute_state(45, 50) == QuotaState.CRITICAL

    def test_state_from_usage_exhausted(self) -> None:
        assert QuotaUsage.compute_state(50, 50) == QuotaState.EXHAUSTED

    def test_state_from_usage_unlimited(self) -> None:
        assert QuotaUsage.compute_state(9999, UNLIMITED) == QuotaState.UNLIMITED

    def test_state_from_usage_none_limit(self) -> None:
        assert QuotaUsage.compute_state(100, None) == QuotaState.UNLIMITED

    def test_available_from_tier_defaults_to_none(self) -> None:
        usage = QuotaUsage(resource="investigations", used=10, limit=50, state=QuotaState.NORMAL)
        assert usage.available_from_tier is None
