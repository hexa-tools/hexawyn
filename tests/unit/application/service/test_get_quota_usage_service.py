from unittest.mock import MagicMock

from hexawyn.application.ports.driving.get_quota_usage.get_quota_usage_command import (
    GetQuotaUsageCommand,
)
from hexawyn.application.ports.driving.get_quota_usage.get_quota_usage_service_port import (
    GetQuotaUsageServicePort,
)
from hexawyn.application.service.get_quota_usage_service import GetQuotaUsageService
from hexawyn.application.use_case.get_quota_usage.get_quota_usage_use_case import (
    GetQuotaUsageUseCase,
)
from hexawyn.domain.models.quota import UNLIMITED, LicenseTier, QuotaState, QuotaUsage


class TestGetQuotaUsageService:
    def _mock_plan_port(self, tier: LicenseTier = LicenseTier.STARTER) -> MagicMock:
        from hexawyn.domain.models.quota import (
            get_investigation_limit,
            get_slack_limit,
        )

        plan = MagicMock()
        plan.get_limit.side_effect = lambda resource: {
            "investigations": get_investigation_limit(tier),
            "slack_alerts": get_slack_limit(tier),
        }.get(resource)
        plan.is_available.return_value = True
        plan.tier_required_for.return_value = None
        return plan

    def _mock_usage_meter(self) -> MagicMock:
        meter = MagicMock()
        meter.get_usage.side_effect = lambda resource: {
            "investigations": 10,
            "slack_alerts": 2,
        }.get(resource, 0)
        return meter

    def test_implements_service_port(self) -> None:
        service = GetQuotaUsageService(
            plan_port=MagicMock(),
            usage_meter=MagicMock(),
        )
        assert isinstance(service, GetQuotaUsageServicePort)

    def test_execute_returns_quota_usage_list(self) -> None:
        service = GetQuotaUsageService(
            plan_port=self._mock_plan_port(),
            usage_meter=self._mock_usage_meter(),
        )
        result = service.execute(GetQuotaUsageCommand())

        assert len(result.quotas) == 2
        resources = [q.resource for q in result.quotas]
        assert "investigations" in resources
        assert "slack_alerts" in resources

    def test_starter_investigations_limit_50(self) -> None:
        service = GetQuotaUsageService(
            plan_port=self._mock_plan_port(LicenseTier.STARTER),
            usage_meter=self._mock_usage_meter(),
        )
        result = service.execute(GetQuotaUsageCommand())

        inv = next(q for q in result.quotas if q.resource == "investigations")
        assert inv.limit == 200
        assert inv.used == 10

    def test_scale_up_returns_unlimited_state(self) -> None:
        plan = self._mock_plan_port(LicenseTier.SCALE_UP)
        service = GetQuotaUsageService(
            plan_port=plan,
            usage_meter=self._mock_usage_meter(),
        )
        result = service.execute(GetQuotaUsageCommand())

        inv = next(q for q in result.quotas if q.resource == "investigations")
        assert inv.state == QuotaState.UNLIMITED
        assert inv.should_render_bar is False

    def test_usage_at_warning_threshold(self) -> None:
        plan = self._mock_plan_port(LicenseTier.TEAM)
        meter = MagicMock()
        meter.get_usage.side_effect = lambda resource: {
            "investigations": 400,
            "slack_alerts": 10,
        }.get(resource, 0)

        service = GetQuotaUsageService(plan_port=plan, usage_meter=meter)
        result = service.execute(GetQuotaUsageCommand())

        inv = next(q for q in result.quotas if q.resource == "investigations")
        assert inv.state == QuotaState.WARNING
        assert inv.limit == 500
        assert inv.used == 400

    def test_usage_at_critical_threshold(self) -> None:
        plan = self._mock_plan_port(LicenseTier.TEAM)
        meter = MagicMock()
        meter.get_usage.side_effect = lambda resource: {
            "investigations": 470,
            "slack_alerts": 10,
        }.get(resource, 0)

        service = GetQuotaUsageService(plan_port=plan, usage_meter=meter)
        result = service.execute(GetQuotaUsageCommand())

        inv = next(q for q in result.quotas if q.resource == "investigations")
        assert inv.state == QuotaState.CRITICAL

    def test_usage_exhausted_state(self) -> None:
        plan = self._mock_plan_port(LicenseTier.STARTER)
        meter = MagicMock()
        meter.get_usage.side_effect = lambda resource: {
            "investigations": 200,
            "slack_alerts": 0,
        }.get(resource, 0)

        service = GetQuotaUsageService(plan_port=plan, usage_meter=meter)
        result = service.execute(GetQuotaUsageCommand())

        inv = next(q for q in result.quotas if q.resource == "investigations")
        assert inv.state == QuotaState.EXHAUSTED

    def test_exhausted_state_from_compute_state(self) -> None:
        for used, limit, expected in [
            (0, 50, QuotaState.NORMAL),
            (35, 50, QuotaState.NORMAL),
            (40, 50, QuotaState.WARNING),
            (45, 50, QuotaState.CRITICAL),
            (50, 50, QuotaState.EXHAUSTED),
            (9999, UNLIMITED, QuotaState.UNLIMITED),
        ]:
            assert QuotaUsage.compute_state(used, limit) == expected

    def test_tier_required_for_called_when_limit_is_zero(self) -> None:
        plan = MagicMock()
        plan.get_limit.side_effect = lambda resource: {
            "investigations": 0,
            "slack_alerts": 5,
        }.get(resource, None)
        plan.is_available.return_value = True
        plan.tier_required_for.return_value = "Team"

        meter = self._mock_usage_meter()

        service = GetQuotaUsageService(plan_port=plan, usage_meter=meter)
        service.execute(GetQuotaUsageCommand())

        plan.tier_required_for.assert_called()


class TestGetQuotaUsageUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GetQuotaUsageServicePort)
        use_case = GetQuotaUsageUseCase(service=mock_service)

        command = GetQuotaUsageCommand()
        use_case.execute(command)

        mock_service.execute.assert_called_once_with(command)

    def test_command_is_frozen_dataclass(self) -> None:
        cmd = GetQuotaUsageCommand()
        assert cmd is not None
