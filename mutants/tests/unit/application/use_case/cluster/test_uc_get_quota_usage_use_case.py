from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cluster.get_quota_usage.command import (
    GetQuotaUsageCommand,
)
from hexawyn.application.use_case.cluster.get_quota_usage.get_quota_usage_use_case import (
    GetQuotaUsageUseCase,
)
from hexawyn.application.use_case.cluster.get_quota_usage.response import (
    GetQuotaUsageResponse,
)
from hexawyn.domain.models.quota import QuotaState


class TestGetQuotaUsageUseCase:
    def test_execute_returns_get_quota_usage_response(self) -> None:
        plan = MagicMock()
        plan.get_limit.return_value = 100
        plan.tier_required_for.return_value = None
        meter = MagicMock()
        meter.get_usage.return_value = 50

        use_case = GetQuotaUsageUseCase(plan_port=plan, usage_meter=meter)
        result = use_case.execute(GetQuotaUsageCommand())

        assert isinstance(result, GetQuotaUsageResponse)
        assert len(result.quotas) == 2  # noqa: PLR2004

    def test_execute_computes_quota_state(self) -> None:
        plan = MagicMock()
        plan.get_limit.return_value = 100
        plan.tier_required_for.return_value = None
        meter = MagicMock()
        meter.get_usage.return_value = 50

        use_case = GetQuotaUsageUseCase(plan_port=plan, usage_meter=meter)
        result = use_case.execute(GetQuotaUsageCommand())

        assert result.quotas[0].resource in ("investigations", "slack_alerts")
        assert result.quotas[0].used == 50  # noqa: PLR2004

    def test_execute_no_limit_shows_as_none(self) -> None:
        plan = MagicMock()
        plan.get_limit.return_value = -1
        plan.tier_required_for.return_value = None
        meter = MagicMock()
        meter.get_usage.return_value = 0

        use_case = GetQuotaUsageUseCase(plan_port=plan, usage_meter=meter)
        result = use_case.execute(GetQuotaUsageCommand())

        assert result.quotas[0].limit is None

    def test_execute_locked_state_triggers_tier_required(self) -> None:
        plan = MagicMock()
        plan.get_limit.return_value = 0
        plan.tier_required_for.return_value = "scale_up"
        meter = MagicMock()
        meter.get_usage.return_value = 0

        use_case = GetQuotaUsageUseCase(plan_port=plan, usage_meter=meter)
        result = use_case.execute(GetQuotaUsageCommand())

        assert result.quotas[0].state == QuotaState.LOCKED
        assert result.quotas[0].available_from_tier == "scale_up"
