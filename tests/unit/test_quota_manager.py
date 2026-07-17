import sys
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.domain.errors import QuotaExceededError, SlackQuotaExceededError
from hexawyn.domain.models.quota import UNLIMITED, LicenseTier, SlackQuota, UsageQuota


class TestCheckQuota:
    def test_passes_when_under_limit(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=UsageQuota(month="2026-06", count=10, limit=50),
        ):
            from hexawyn.infrastructure.config.quota_manager import check_quota

            check_quota()

    def test_raises_when_starter_limit_reached(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=UsageQuota(month="2026-06", count=50, limit=50),
        ):
            from hexawyn.infrastructure.config.quota_manager import check_quota

            with pytest.raises(QuotaExceededError) as exc_info:
                check_quota()
            assert exc_info.value.used == 50
            assert exc_info.value.limit == 50

    def test_raises_when_team_limit_reached(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=UsageQuota(month="2026-06", count=500, limit=500),
        ):
            from hexawyn.infrastructure.config.quota_manager import check_quota

            with pytest.raises(QuotaExceededError) as exc_info:
                check_quota()
            assert exc_info.value.limit == 500

    def test_passes_when_scale_up_unlimited(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=UsageQuota(month="2026-06", count=99999, limit=UNLIMITED),
        ):
            from hexawyn.infrastructure.config.quota_manager import check_quota

            check_quota()


class TestCheckSlackQuota:
    def test_raises_when_starter_slack_limit_reached(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_slack_quota",
            return_value=SlackQuota(month="2026-06", count=5, limit=5),
        ):
            from hexawyn.infrastructure.config.quota_manager import check_slack_quota

            with pytest.raises(SlackQuotaExceededError):
                check_slack_quota()

    def test_raises_when_team_slack_limit_reached(self) -> None:
        """Team has unlimited Slack — but test with a custom limit."""
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_slack_quota",
            return_value=SlackQuota(month="2026-06", count=50, limit=50),
        ):
            from hexawyn.infrastructure.config.quota_manager import check_slack_quota

            with pytest.raises(SlackQuotaExceededError) as exc_info:
                check_slack_quota()
            assert exc_info.value.limit == 50

    def test_passes_when_team_unlimited(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_slack_quota",
            return_value=SlackQuota(month="2026-06", count=9999, limit=UNLIMITED),
        ):
            from hexawyn.infrastructure.config.quota_manager import check_slack_quota

            check_slack_quota()


class TestIncrementQuota:
    def test_increment_investigation_called(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._increment_investigation"
        ) as mock_inc:
            from hexawyn.infrastructure.config.quota_manager import increment_quota

            increment_quota()
            mock_inc.assert_called_once()

    def test_increment_slack_called(self) -> None:
        with patch("hexawyn.infrastructure.config.quota_manager._increment_slack") as mock_inc:
            from hexawyn.infrastructure.config.quota_manager import increment_slack_quota

            increment_slack_quota()
            mock_inc.assert_called_once()


class TestGetHistoryDays:
    def test_starter_returns_7(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_tier",
            return_value=LicenseTier.STARTER,
        ):
            from hexawyn.infrastructure.config.quota_manager import get_history_days

            assert get_history_days() == 7

    def test_team_returns_90(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_tier",
            return_value=LicenseTier.TEAM,
        ):
            from hexawyn.infrastructure.config.quota_manager import get_history_days

            assert get_history_days() == 90

    def test_scale_up_returns_unlimited(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_tier",
            return_value=LicenseTier.SCALE_UP,
        ):
            from hexawyn.infrastructure.config.quota_manager import get_history_days

            assert get_history_days() == UNLIMITED


class TestGetQuotaDisplay:
    def test_starter_shows_count(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=UsageQuota(month="2026-06", count=23, limit=50),
        ):
            with patch(
                "hexawyn.infrastructure.config.quota_manager._get_current_tier",
                return_value=LicenseTier.STARTER,
            ):
                from hexawyn.infrastructure.config.quota_manager import get_quota_display

                display = get_quota_display()
                assert "23" in display
                assert "50" in display
                assert "27" in display

    def test_team_shows_team_limits(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=UsageQuota(month="2026-06", count=300, limit=500),
        ):
            with patch(
                "hexawyn.infrastructure.config.quota_manager._get_current_tier",
                return_value=LicenseTier.TEAM,
            ):
                from hexawyn.infrastructure.config.quota_manager import get_quota_display

                display = get_quota_display()
                assert "300" in display
                assert "500" in display

    def test_scale_up_shows_unlimited(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=UsageQuota(month="2026-06", count=9999, limit=UNLIMITED),
        ):
            with patch(
                "hexawyn.infrastructure.config.quota_manager._get_current_tier",
                return_value=LicenseTier.SCALE_UP,
            ):
                from hexawyn.infrastructure.config.quota_manager import get_quota_display

                display = get_quota_display()
                assert "unlimited" in display.lower()

    def test_low_remaining_shows_warning(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=UsageQuota(month="2026-06", count=46, limit=50),
        ):
            with patch(
                "hexawyn.infrastructure.config.quota_manager._get_current_tier",
                return_value=LicenseTier.STARTER,
            ):
                from hexawyn.infrastructure.config.quota_manager import get_quota_display

                display = get_quota_display()
                assert "4" in display


class TestGetCurrentTier:
    def test_returns_license_tier_when_manager_available(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.license_manager.get_license_tier",
            return_value=LicenseTier.TEAM,
        ):
            from hexawyn.infrastructure.config.quota_manager import _get_current_tier

            assert _get_current_tier() == LicenseTier.TEAM

    def test_falls_back_to_starter_on_import_error(self) -> None:
        saved = sys.modules.pop("hexawyn.infrastructure.config.license_manager", None)
        try:
            import builtins

            original_import = builtins.__import__

            def selective_import(name, *args, **kwargs):
                if name == "hexawyn.infrastructure.config.license_manager":
                    raise ImportError("Mocked import failure")
                return original_import(name, *args, **kwargs)

            with patch("builtins.__import__", side_effect=selective_import):
                from hexawyn.infrastructure.config.quota_manager import _get_current_tier

                assert _get_current_tier() == LicenseTier.STARTER
        finally:
            if saved is not None:
                sys.modules["hexawyn.infrastructure.config.license_manager"] = saved


class TestGetCurrentQuotaViaDb:
    def test_get_current_investigation_quota_via_db(self) -> None:
        mock_store = MagicMock()
        mock_store.get_investigation_quota.return_value = UsageQuota(
            month="2026-06", count=0, limit=50
        )
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_store",
            return_value=mock_store,
        ):
            from hexawyn.infrastructure.config.quota_manager import (
                _get_current_investigation_quota,
            )

            quota = _get_current_investigation_quota()
            assert isinstance(quota, UsageQuota)
            assert quota.count == 0
            mock_store.get_investigation_quota.assert_called_once()

    def test_get_current_slack_quota_via_db(self) -> None:
        mock_store = MagicMock()
        mock_store.get_slack_quota.return_value = SlackQuota(month="2026-06", count=0, limit=5)
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_store",
            return_value=mock_store,
        ):
            from hexawyn.infrastructure.config.quota_manager import (
                _get_current_slack_quota,
            )

            quota = _get_current_slack_quota()
            assert isinstance(quota, SlackQuota)
            assert quota.count == 0


class TestIncrementQuotaViaDb:
    def test_increment_investigation_via_db(self) -> None:
        mock_store = MagicMock()
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_store",
            return_value=mock_store,
        ):
            with patch(
                "hexawyn.infrastructure.config.quota_manager._get_current_tier",
                return_value=LicenseTier.STARTER,
            ):
                from hexawyn.infrastructure.config.quota_manager import (
                    _increment_investigation,
                )

                _increment_investigation()
                mock_store.increment_investigation.assert_called_once()

    def test_increment_slack_via_db(self) -> None:
        mock_store = MagicMock()
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_store",
            return_value=mock_store,
        ):
            with patch(
                "hexawyn.infrastructure.config.quota_manager._get_current_tier",
                return_value=LicenseTier.STARTER,
            ):
                from hexawyn.infrastructure.config.quota_manager import (
                    _increment_slack,
                )

                _increment_slack()
                mock_store.increment_slack.assert_called_once()


class TestQuotaStoreInjection:
    def test_inject_quota_store_overrides_default(self) -> None:
        from hexawyn.infrastructure.config.quota_manager import _get_store, inject_quota_store

        mock_store = MagicMock()
        inject_quota_store(mock_store)
        assert _get_store() is mock_store
        inject_quota_store(None)  # type: ignore[arg-type] — reset for other tests


class TestGetCurrentMonth:
    def test_returns_yyyy_mm_format(self) -> None:
        from hexawyn.infrastructure.config.quota_manager import _get_current_month

        month = _get_current_month()
        assert len(month) == 7
        assert month[4] == "-"
        assert month[:4].isdigit()
        assert month[5:].isdigit()
