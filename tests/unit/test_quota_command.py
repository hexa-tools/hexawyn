from unittest.mock import patch

from click.testing import CliRunner
from hexawyn.cli.main import app
from hexawyn.domain.models.quota import UNLIMITED, LicenseTier, SlackQuota, UsageQuota


class TestQuotaCommand:
    def setup_method(self) -> None:
        self.runner = CliRunner()

    def _patch_quota(
        self,
        inv: UsageQuota,
        slack: SlackQuota,
        tier: LicenseTier,
        history: int = 7,
    ) -> list[object]:
        return [
            patch(
                "hexawyn.cli.commands.quota_command._get_current_investigation_quota",
                return_value=inv,
            ),
            patch(
                "hexawyn.cli.commands.quota_command._get_current_slack_quota",
                return_value=slack,
            ),
            patch(
                "hexawyn.cli.commands.quota_command.get_license_tier",
                return_value=tier,
            ),
            patch(
                "hexawyn.cli.commands.quota_command.get_history_days",
                return_value=history,
            ),
        ]

    def test_free_shows_investigation_count(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=23, limit=50),
            slack=SlackQuota(month="2026-06", count=2, limit=5),
            tier=LicenseTier.FREE,
        )
        with patches[0], patches[1], patches[2], patches[3]:
            result = self.runner.invoke(app, ["quota"])
            assert result.exit_code == 0
            assert "23" in result.output
            assert "50" in result.output

    def test_dev_shows_limits(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=45, limit=200),
            slack=SlackQuota(month="2026-06", count=10, limit=50),
            tier=LicenseTier.DEV,
            history=30,
        )
        with patches[0], patches[1], patches[2], patches[3]:
            result = self.runner.invoke(app, ["quota"])
            assert "Dev" in result.output
            assert "19" in result.output
            assert "45" in result.output
            assert "200" in result.output
            assert "30" in result.output

    def test_startup_shows_limits(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=300, limit=500),
            slack=SlackQuota(month="2026-06", count=9999, limit=UNLIMITED),
            tier=LicenseTier.STARTUP,
            history=90,
        )
        with patches[0], patches[1], patches[2], patches[3]:
            result = self.runner.invoke(app, ["quota"])
            assert "Startup" in result.output
            assert "99" in result.output
            assert "300" in result.output
            assert "500" in result.output
            assert "Unlimited" in result.output

    def test_scale_up_shows_unlimited(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=9999, limit=UNLIMITED),
            slack=SlackQuota(month="2026-06", count=9999, limit=UNLIMITED),
            tier=LicenseTier.SCALE_UP,
            history=UNLIMITED,
        )
        with patches[0], patches[1], patches[2], patches[3]:
            result = self.runner.invoke(app, ["quota"])
            assert "Scale-up" in result.output
            assert "199" in result.output
            assert "Unlimited" in result.output

    def test_enterprise_shows_unlimited(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=9999, limit=UNLIMITED),
            slack=SlackQuota(month="2026-06", count=9999, limit=UNLIMITED),
            tier=LicenseTier.ENTERPRISE,
            history=UNLIMITED,
        )
        with patches[0], patches[1], patches[2], patches[3]:
            result = self.runner.invoke(app, ["quota"])
            assert "Enterprise" in result.output

    def test_shows_remaining(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=23, limit=50),
            slack=SlackQuota(month="2026-06", count=2, limit=5),
            tier=LicenseTier.FREE,
        )
        with patches[0], patches[1], patches[2], patches[3]:
            result = self.runner.invoke(app, ["quota"])
            assert "remaining" in result.output.lower()

    def test_shows_upgrade_when_exceeded(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=50, limit=50),
            slack=SlackQuota(month="2026-06", count=0, limit=5),
            tier=LicenseTier.FREE,
        )
        with patches[0], patches[1], patches[2], patches[3]:
            result = self.runner.invoke(app, ["quota"])
            assert "hexawyn.com/pricing" in result.output

    def test_shows_warning_when_low(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=46, limit=50),
            slack=SlackQuota(month="2026-06", count=3, limit=5),
            tier=LicenseTier.FREE,
        )
        with patches[0], patches[1], patches[2], patches[3]:
            result = self.runner.invoke(app, ["quota"])
            assert "low" in result.output.lower()
