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
        history: int = 30,
    ) -> list[object]:
        return [
            patch(
                "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
                return_value=inv,
            ),
            patch(
                "hexawyn.infrastructure.config.quota_manager._get_current_slack_quota",
                return_value=slack,
            ),
            patch(
                "hexawyn.adapters.secondary.pricing_plan_adapter._resolve_tier",
                return_value=tier,
            ),
            patch(
                "hexawyn.infrastructure.config.license_manager.get_license_tier",
                return_value=tier,
            ),
            patch(
                "hexawyn.infrastructure.config.quota_manager.get_history_days",
                return_value=history,
            ),
        ]

    def test_starter_shows_investigation_count(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=23, limit=50),
            slack=SlackQuota(month="2026-06", count=2, limit=5),
            tier=LicenseTier.STARTER,
        )
        with patches[0], patches[1], patches[2], patches[3], patches[4]:
            result = self.runner.invoke(app, ["quota"])
            assert result.exit_code == 0
            assert "23" in result.output
            assert "50" in result.output

    def test_team_shows_limits(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=300, limit=500),
            slack=SlackQuota(month="2026-06", count=10, limit=UNLIMITED),
            tier=LicenseTier.TEAM,
            history=90,
        )
        with patches[0], patches[1], patches[2], patches[3], patches[4]:
            result = self.runner.invoke(app, ["quota"])
            assert "Team" in result.output
            assert "99" in result.output
            assert "300" in result.output
            assert "500" in result.output
            assert "90 days" in result.output

    def test_scale_up_shows_unlimited(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=9999, limit=UNLIMITED),
            slack=SlackQuota(month="2026-06", count=9999, limit=UNLIMITED),
            tier=LicenseTier.SCALE_UP,
            history=UNLIMITED,
        )
        with patches[0], patches[1], patches[2], patches[3], patches[4]:
            result = self.runner.invoke(app, ["quota"])
            assert "Scale-up" in result.output
            assert "199" in result.output
            assert "Unlimited" in result.output

    def test_shows_remaining(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=23, limit=50),
            slack=SlackQuota(month="2026-06", count=2, limit=5),
            tier=LicenseTier.STARTER,
        )
        with patches[0], patches[1], patches[2], patches[3], patches[4]:
            result = self.runner.invoke(app, ["quota"])
            assert "remaining" in result.output.lower()

    def test_shows_upgrade_when_exceeded(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=200, limit=200),
            slack=SlackQuota(month="2026-06", count=0, limit=50),
            tier=LicenseTier.STARTER,
        )
        with patches[0], patches[1], patches[2], patches[3], patches[4]:
            result = self.runner.invoke(app, ["quota"])
            assert "hexawyn.com/pricing" in result.output

    def test_shows_all_resources(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=10, limit=50),
            slack=SlackQuota(month="2026-06", count=2, limit=5),
            tier=LicenseTier.STARTER,
        )
        with patches[0], patches[1], patches[2], patches[3], patches[4]:
            result = self.runner.invoke(app, ["quota"])
            assert "Investigations" in result.output
            assert "Slack alerts" in result.output

    def test_unlimited_renders_infinity_symbol(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=999, limit=UNLIMITED),
            slack=SlackQuota(month="2026-06", count=999, limit=UNLIMITED),
            tier=LicenseTier.SCALE_UP,
            history=UNLIMITED,
        )
        with patches[0], patches[1], patches[2], patches[3], patches[4]:
            result = self.runner.invoke(app, ["quota"])
            assert "\u221e" in result.output

    def test_shows_critical_warning_when_low(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=190, limit=200),
            slack=SlackQuota(month="2026-06", count=3, limit=50),
            tier=LicenseTier.STARTER,
            history=7,
        )
        with patches[0], patches[1], patches[2], patches[3], patches[4]:
            result = self.runner.invoke(app, ["quota"])
            assert "low" in result.output.lower()

    def test_tier_label_fallback_on_import_error(self) -> None:
        import sys

        saved = sys.modules.pop("hexawyn.infrastructure.config.license_manager", None)
        try:
            patches = self._patch_quota(
                inv=UsageQuota(month="2026-06", count=10, limit=50),
                slack=SlackQuota(month="2026-06", count=1, limit=5),
                tier=LicenseTier.STARTER,
            )
            with patches[0], patches[1], patches[2], patches[4]:
                result = self.runner.invoke(app, ["quota"])
                assert result.exit_code == 0
                assert "Starter" in result.output
        finally:
            if saved is not None:
                sys.modules["hexawyn.infrastructure.config.license_manager"] = saved

    def test_shows_critical_warning_when_above_90pc(self) -> None:
        patches = self._patch_quota(
            inv=UsageQuota(month="2026-06", count=190, limit=200),
            slack=SlackQuota(month="2026-06", count=0, limit=50),
            tier=LicenseTier.STARTER,
        )
        with patches[0], patches[1], patches[2], patches[3], patches[4]:
            result = self.runner.invoke(app, ["quota"])
            assert "low" in result.output.lower()
