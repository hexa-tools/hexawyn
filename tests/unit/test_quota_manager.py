from unittest.mock import patch

import pytest
from hexawyn.domain.errors import QuotaExceededError, SlackQuotaExceededError
from hexawyn.domain.models.quota import (
    FREE_HISTORY_DAYS,
    PRO_HISTORY_DAYS,
    UNLIMITED,
    SlackQuota,
    UsageQuota,
)


class TestCheckQuota:
    def test_passes_when_under_limit(self):
        mock_quota = UsageQuota(month="2026-06", count=10, limit=50)
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=mock_quota,
        ):
            from hexawyn.infrastructure.config.quota_manager import check_quota

            check_quota()

    def test_raises_when_limit_reached(self):
        mock_quota = UsageQuota(month="2026-06", count=50, limit=50)
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=mock_quota,
        ):
            from hexawyn.infrastructure.config.quota_manager import check_quota

            with pytest.raises(QuotaExceededError) as exc_info:
                check_quota()
            assert exc_info.value.used == 50
            assert exc_info.value.limit == 50

    def test_passes_when_unlimited(self):
        mock_quota = UsageQuota(month="2026-06", count=99999, limit=UNLIMITED)
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=mock_quota,
        ):
            from hexawyn.infrastructure.config.quota_manager import check_quota

            check_quota()


class TestCheckSlackQuota:
    def test_passes_when_under_slack_limit(self):
        mock_quota = SlackQuota(month="2026-06", count=3, limit=5)
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_slack_quota",
            return_value=mock_quota,
        ):
            from hexawyn.infrastructure.config.quota_manager import check_slack_quota

            check_slack_quota()

    def test_raises_when_slack_limit_reached(self):
        mock_quota = SlackQuota(month="2026-06", count=5, limit=5)
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_slack_quota",
            return_value=mock_quota,
        ):
            from hexawyn.infrastructure.config.quota_manager import check_slack_quota

            with pytest.raises(SlackQuotaExceededError):
                check_slack_quota()


class TestIncrementQuota:
    def test_increment_investigation_called(self):
        with patch(
            "hexawyn.infrastructure.config.quota_manager._increment_investigation"
        ) as mock_inc:
            from hexawyn.infrastructure.config.quota_manager import increment_quota

            increment_quota()
            mock_inc.assert_called_once()

    def test_increment_slack_called(self):
        with patch("hexawyn.infrastructure.config.quota_manager._increment_slack") as mock_inc:
            from hexawyn.infrastructure.config.quota_manager import increment_slack_quota

            increment_slack_quota()
            mock_inc.assert_called_once()


class TestGetHistoryDays:
    def test_returns_7_for_free(self):
        with patch(
            "hexawyn.infrastructure.config.quota_manager.is_pro",
            return_value=False,
        ):
            from hexawyn.infrastructure.config.quota_manager import get_history_days

            assert get_history_days() == FREE_HISTORY_DAYS

    def test_returns_90_for_pro(self):
        with patch(
            "hexawyn.infrastructure.config.quota_manager.is_pro",
            return_value=True,
        ):
            from hexawyn.infrastructure.config.quota_manager import get_history_days

            assert get_history_days() == PRO_HISTORY_DAYS


class TestGetQuotaDisplay:
    def test_free_tier_shows_count_and_remaining(self):
        mock_quota = UsageQuota(month="2026-06", count=23, limit=50)
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=mock_quota,
        ):
            from hexawyn.infrastructure.config.quota_manager import get_quota_display

            display = get_quota_display()
            assert "23" in display
            assert "50" in display
            assert "27" in display

    def test_pro_tier_shows_unlimited(self):
        mock_quota = UsageQuota(month="2026-06", count=9999, limit=UNLIMITED)
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=mock_quota,
        ):
            from hexawyn.infrastructure.config.quota_manager import get_quota_display

            display = get_quota_display()
            assert "unlimited" in display.lower()
            assert "Pro" in display

    def test_low_remaining_shows_warning(self):
        mock_quota = UsageQuota(month="2026-06", count=46, limit=50)
        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=mock_quota,
        ):
            from hexawyn.infrastructure.config.quota_manager import get_quota_display

            display = get_quota_display()
            assert "4" in display


class TestGetCurrentMonth:
    def test_returns_yyyy_mm_format(self):
        from hexawyn.infrastructure.config.quota_manager import _get_current_month

        month = _get_current_month()
        assert len(month) == 7
        assert month[4] == "-"
        assert month[:4].isdigit()
        assert month[5:].isdigit()
