from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.get_quota_usage.get_quota_usage_command import (
    GetQuotaUsageCommand,
)
from hexawyn.application.ports.driving.get_quota_usage.get_quota_usage_response import (
    GetQuotaUsageResponse,
)


class GetQuotaUsageServicePort(ABC):
    @abstractmethod
    def execute(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse: ...
