from hexawyn.application.ports.driving.get_quota_usage.get_quota_usage_command import (
    GetQuotaUsageCommand,
)
from hexawyn.application.ports.driving.get_quota_usage.get_quota_usage_response import (
    GetQuotaUsageResponse,
)
from hexawyn.application.ports.driving.get_quota_usage.get_quota_usage_service_port import (
    GetQuotaUsageServicePort,
)


class GetQuotaUsageUseCase:
    def __init__(self, service: GetQuotaUsageServicePort) -> None:
        self._service = service

    def execute(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        return self._service.execute(command)
