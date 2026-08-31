"""RuntimeQuotaSource — Option A neutral matrix.

Rows under test (the three the Option C decision asked to cover explicitly):
  1. control plane reachable -> used/limit from CP (and cached).
  2. control plane down + encrypted cache -> cached last-known values.
  3. control plane down, no cache -> NEUTRAL (get_limit None, get_usage 0,
     never a fabricated number, never blocks).
"""

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


class TestImplementsPorts:
    def test_implements_usage_meter_port(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        assert isinstance(RuntimeQuotaSource(runtime=MagicMock()), UsageMeterPort)

    def test_implements_plan_port(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        assert isinstance(RuntimeQuotaSource(runtime=MagicMock()), PlanPort)


class TestRowOneControlPlaneReachable:
    def test_get_usage_from_cp(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=_runtime_with_quota(used=42, limit=500))
        assert source.get_usage("investigations") == 42  # noqa: PLR2004

    def test_get_limit_from_cp(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=_runtime_with_quota(used=42, limit=500))
        assert source.get_limit("investigations") == 500  # noqa: PLR2004

    def test_quota_is_cached_when_cp_reachable(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=_runtime_with_quota(used=7, limit=300))
        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source.quota_cache.save_quota"
        ) as save:
            source.get_limit("investigations")
            save.assert_called_once()
            assert save.call_args[0][0]["used"] == 7  # noqa: PLR2004
            assert save.call_args[0][0]["limit"] == 300  # noqa: PLR2004


class TestRowTwoCpDownWithCache:
    def test_uses_cached_quota_when_cp_unreachable_and_cache_present(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        runtime = MagicMock()
        runtime.check_quota.side_effect = RuntimeError("cp down")

        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source.quota_cache.load_quota",
            return_value={"allowed": True, "used": 11, "limit": 200, "remaining": 189},
        ):
            source = RuntimeQuotaSource(runtime=runtime)
            assert source.get_usage("investigations") == 11  # noqa: PLR2004
            assert source.get_limit("investigations") == 200  # noqa: PLR2004


class TestRowThreeCpDownNoCache:
    def test_get_limit_returns_none_when_cp_down_and_no_cache(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        runtime = MagicMock()
        runtime.check_quota.side_effect = RuntimeError("cp down")

        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source.quota_cache.load_quota",
            return_value=None,
        ):
            source = RuntimeQuotaSource(runtime=runtime)
            assert source.get_limit("investigations") is None

    def test_get_usage_returns_zero_when_neutral(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        runtime = MagicMock()
        runtime.check_quota.side_effect = RuntimeError("cp down")

        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source.quota_cache.load_quota",
            return_value=None,
        ):
            source = RuntimeQuotaSource(runtime=runtime)
            assert source.get_usage("investigations") == 0

    def test_neutral_does_not_block_availability(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        runtime = MagicMock()
        runtime.check_quota.side_effect = RuntimeError("cp down")

        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source.quota_cache.load_quota",
            return_value=None,
        ):
            source = RuntimeQuotaSource(runtime=runtime)
            # Neutral plan: unknown limit -> feature is available, not blocked.
            assert source.is_available("investigations") is True

    def test_cp_with_unverifiable_limit_is_treated_as_neutral(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        runtime = MagicMock()
        runtime.check_quota.return_value = {
            "allowed": True,
            "used": 0,
            "limit": -1,
            "remaining": -1,
        }

        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source.quota_cache.load_quota",
            return_value=None,
        ):
            source = RuntimeQuotaSource(runtime=runtime)
            assert source.get_limit("investigations") is None


class TestSlackCountedButUnlimited:
    def test_slack_usage_from_local_store(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=MagicMock())
        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source._get_current_slack_quota",
            return_value=MagicMock(count=4, limit=50),
        ):
            assert source.get_usage("slack_alerts") == 4  # noqa: PLR2004

    def test_slack_limit_is_unlimited_locally(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=MagicMock())
        with patch(
            "hexawyn.adapters.secondary.runtime_quota_source._get_current_slack_quota",
            return_value=MagicMock(count=4, limit=50),
        ):
            # (ii) counted-but-unlimited: no hardcoded number, -1 == unlimited.
            assert source.get_limit("slack_alerts") == -1  # noqa: PLR2004


class TestPlanDelegation:
    def test_is_available_delegates_to_local_plan(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=MagicMock())
        source._plan = MagicMock()
        source._plan.is_available.return_value = True
        assert source.is_available("investigations") is True
        source._plan.is_available.assert_called_once_with("investigations")

    def test_tier_required_for_delegates_to_local_plan(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=MagicMock())
        source._plan = MagicMock()
        source._plan.tier_required_for.return_value = "team"
        assert source.tier_required_for("clusters") == "team"
        source._plan.tier_required_for.assert_called_once_with("clusters")

    def test_other_resource_limit_uses_local_plan(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        source = RuntimeQuotaSource(runtime=MagicMock())
        source._plan = MagicMock()
        source._plan.get_limit.return_value = 3
        assert source.get_limit("clusters") == 3  # noqa: PLR2004
        source._plan.get_limit.assert_called_once_with("clusters")

    def test_usage_of_unknown_resource_is_zero(self) -> None:
        from hexawyn.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

        # Category: absence / unknown resource — no fabricated usage figure.
        source = RuntimeQuotaSource(runtime=MagicMock())
        assert source.get_usage("clusters") == 0
