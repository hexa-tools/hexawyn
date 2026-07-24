from hexawyn.application.ports.driven.plan_port import PlanPort
from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort
from hexawyn.application.use_case.get_quota_usage.command import GetQuotaUsageCommand
from hexawyn.application.use_case.get_quota_usage.response import GetQuotaUsageResponse
from hexawyn.domain.models.quota import QuotaUsage

_RESOURCES = [
    "investigations",
    "slack_alerts",
    "slack_channels",
    "clusters",
    "users",
    "billing_api",
]


class GetQuotaUsageUseCase:
    def __init__(
        self, plan_port: PlanPort | None = None, usage_meter: UsageMeterPort | None = None
    ) -> None:
        self._plan = plan_port
        self._meter = usage_meter

    def execute(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        investigations_used = 0
        investigations_limit = 0

        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource) if self._plan else None
            used = self._meter.get_usage(resource) if self._meter else 0
            state = QuotaUsage.compute_state(used, limit)
            quotas.append(QuotaUsage(resource=resource, used=used, limit=limit, state=state))
            if resource == "investigations":
                investigations_used = used
                investigations_limit = limit or 0

        return GetQuotaUsageResponse(
            quotas=quotas,
            investigations_used=investigations_used,
            investigations_limit=investigations_limit,
        )
