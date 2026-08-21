from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.plan_port import PlanPort
from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort


def _runtime_with_quota(used: int, limit: int) -> MagicMock:
    runtime = MagicMock()
    runtime.check_quota.return_value = {
        "allowed": True,
        "used": used,
        "limit": limit,
        "remaining": limit - used,
    }
    return runtime


class TestRuntimeQuotaSourceImplementsPorts:
    def test_implements_usage_meter_port(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=MagicMock())
        assert isinstance(source, UsageMeterPort)

    def test_implements_plan_port(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=MagicMock())
        assert isinstance(source, PlanPort)


class TestInvestigationsUsageFromControlPlane:
    def test_uses_cp_used_when_available(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=_runtime_with_quota(used=42, limit=500))

        assert source.get_usage("investigations") == 42  # noqa: PLR2004

    def test_uses_cp_limit_when_available(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=_runtime_with_quota(used=42, limit=500))

        assert source.get_limit("investigations") == 500  # noqa: PLR2004

    def test_falls_back_to_local_when_cp_unavailable(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        runtime = MagicMock()
        runtime.check_quota.return_value = {
            "allowed": True,
            "used": 0,
            "limit": -1,
            "remaining": -1,
        }
        source = RuntimeQuotaSource(runtime=runtime)

        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source._get_current_investigation_quota",
            return_value=MagicMock(count=7, limit=200),
        ):
            assert source.get_usage("investigations") == 7  # noqa: PLR2004
            assert source.get_limit("investigations") == 200  # noqa: PLR2004

    def test_falls_back_to_local_when_cp_raises(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        runtime = MagicMock()
        runtime.check_quota.side_effect = RuntimeError("cp down")
        source = RuntimeQuotaSource(runtime=runtime)

        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source._get_current_investigation_quota",
            return_value=MagicMock(count=3, limit=200),
        ):
            assert source.get_usage("investigations") == 3  # noqa: PLR2004

    def test_falls_back_to_local_via_real_lazy_import(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        runtime = MagicMock()
        runtime.check_quota.return_value = {
            "allowed": True,
            "used": 0,
            "limit": -1,
            "remaining": -1,
        }
        source = RuntimeQuotaSource(runtime=runtime)

        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
            return_value=MagicMock(count=9, limit=200),
        ):
            assert source.get_usage("investigations") == 9  # noqa: PLR2004
            assert source.get_limit("investigations") == 200  # noqa: PLR2004

    def test_falls_back_to_local_when_cp_returns_non_dict(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        runtime = MagicMock()
        runtime.check_quota.return_value = "unexpected"
        source = RuntimeQuotaSource(runtime=runtime)

        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source._get_current_investigation_quota",
            return_value=MagicMock(count=5, limit=200),
        ):
            assert source.get_usage("investigations") == 5  # noqa: PLR2004


class TestSlackAlertsLocalOnly:
    def test_slack_usage_comes_from_local_store(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=MagicMock())

        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source._get_current_slack_quota",
            return_value=MagicMock(count=4, limit=50),
        ):
            assert source.get_usage("slack_alerts") == 4  # noqa: PLR2004

    def test_slack_limit_comes_from_local_plan(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=MagicMock())

        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source._get_current_slack_quota",
            return_value=MagicMock(count=4, limit=50),
        ):
            assert source.get_limit("slack_alerts") == 50  # noqa: PLR2004

    def test_slack_ignores_cp_even_when_available(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=_runtime_with_quota(used=99, limit=500))

        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source._get_current_slack_quota",
            return_value=MagicMock(count=2, limit=50),
        ):
            assert source.get_usage("slack_alerts") == 2  # noqa: PLR2004

    def test_slack_usage_via_real_lazy_import(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=MagicMock())

        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_slack_quota",
            return_value=MagicMock(count=6, limit=50),
        ):
            assert source.get_usage("slack_alerts") == 6  # noqa: PLR2004

    def test_slack_limit_via_real_lazy_import(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=MagicMock())

        with patch(
            "hexawyn.infrastructure.config.quota_manager._get_current_slack_quota",
            return_value=MagicMock(count=6, limit=50),
        ):
            assert source.get_limit("slack_alerts") == 50  # noqa: PLR2004


class TestOtherResources:
    def test_usage_of_unknown_resource_is_zero(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=_runtime_with_quota(used=10, limit=100))

        assert source.get_usage("clusters") == 0

    def test_limit_of_unknown_resource_uses_local_plan(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=MagicMock())
        source._plan = MagicMock()
        source._plan.get_limit.return_value = 3

        assert source.get_limit("clusters") == 3  # noqa: PLR2004
        source._plan.get_limit.assert_called_once_with("clusters")

    def test_local_plan_created_lazily(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=MagicMock())

        plan = source._local_plan()

        assert source._plan is plan
        assert isinstance(plan, MagicMock) is False


class TestPlanDelegation:
    def test_is_available_delegates_to_local_plan(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        runtime = MagicMock()
        source = RuntimeQuotaSource(runtime=runtime)
        source._plan = MagicMock()
        source._plan.is_available.return_value = True

        assert source.is_available("investigations") is True
        source._plan.is_available.assert_called_once_with("investigations")

    def test_tier_required_for_delegates_to_local_plan(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        runtime = MagicMock()
        source = RuntimeQuotaSource(runtime=runtime)
        source._plan = MagicMock()
        source._plan.tier_required_for.return_value = "team"

        assert source.tier_required_for("clusters") == "team"
        source._plan.tier_required_for.assert_called_once_with("clusters")
