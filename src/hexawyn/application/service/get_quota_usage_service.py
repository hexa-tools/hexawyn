from hexawyn.application.ports.driven.plan_port import PlanPort
from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort
from hexawyn.application.ports.driving.get_quota_usage.get_quota_usage_command import (
    GetQuotaUsageCommand,
)
from hexawyn.application.ports.driving.get_quota_usage.get_quota_usage_response import (
    GetQuotaUsageResponse,
)
from hexawyn.application.ports.driving.get_quota_usage.get_quota_usage_service_port import (
    GetQuotaUsageServicePort,
)
from hexawyn.domain.models.quota import QuotaUsage

_RESOURCES = [
    "investigations",
    "slack_alerts",
]


class GetQuotaUsageService(GetQuotaUsageServicePort):
    def __init__(self, plan_port: PlanPort, usage_meter: UsageMeterPort) -> None:
        self._plan = plan_port
        self._meter = usage_meter

    def execute(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)
