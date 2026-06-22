from unittest.mock import patch

from click.testing import CliRunner
from hexawyn.cli.main import app
from hexawyn.domain.models.quota import UNLIMITED, SlackQuota, UsageQuota


class TestQuotaCommand:
    def setup_method(self):
        self.runner = CliRunner()

    def test_shows_investigation_count(self):
        with patch(
            "hexawyn.cli.commands.quota_command._get_current_investigation_quota",
            return_value=UsageQuota(month="2026-06", count=23, limit=50),
        ):
            with patch(
                "hexawyn.cli.commands.quota_command._get_current_slack_quota",
                return_value=SlackQuota(month="2026-06", count=2, limit=5),
            ):
                result = self.runner.invoke(app, ["quota"])
                assert result.exit_code == 0
                assert "23" in result.output
                assert "50" in result.output

    def test_shows_slack_count(self):
        with patch(
            "hexawyn.cli.commands.quota_command._get_current_investigation_quota",
            return_value=UsageQuota(month="2026-06", count=10, limit=50),
        ):
            with patch(
                "hexawyn.cli.commands.quota_command._get_current_slack_quota",
                return_value=SlackQuota(month="2026-06", count=3, limit=5),
            ):
                result = self.runner.invoke(app, ["quota"])
                assert "3" in result.output
                assert "5" in result.output

    def test_shows_history_days(self):
        with patch(
            "hexawyn.cli.commands.quota_command._get_current_investigation_quota",
            return_value=UsageQuota(month="2026-06", count=10, limit=50),
        ):
            with patch(
                "hexawyn.cli.commands.quota_command._get_current_slack_quota",
                return_value=SlackQuota(month="2026-06", count=0, limit=5),
            ):
                with patch(
                    "hexawyn.cli.commands.quota_command.get_history_days",
                    return_value=7,
                ):
                    result = self.runner.invoke(app, ["quota"])
                    assert "7" in result.output

    def test_shows_upgrade_link_when_exceeded(self):
        with patch(
            "hexawyn.cli.commands.quota_command._get_current_investigation_quota",
            return_value=UsageQuota(month="2026-06", count=50, limit=50),
        ):
            with patch(
                "hexawyn.cli.commands.quota_command._get_current_slack_quota",
                return_value=SlackQuota(month="2026-06", count=0, limit=5),
            ):
                result = self.runner.invoke(app, ["quota"])
                assert "hexawyn.com/pro" in result.output

    def test_shows_unlimited_for_pro(self):
        with patch(
            "hexawyn.cli.commands.quota_command._get_current_investigation_quota",
            return_value=UsageQuota(month="2026-06", count=9999, limit=UNLIMITED),
        ):
            with patch(
                "hexawyn.cli.commands.quota_command._get_current_slack_quota",
                return_value=SlackQuota(month="2026-06", count=9999, limit=UNLIMITED),
            ):
                result = self.runner.invoke(app, ["quota"])
                assert "unlimited" in result.output.lower()
