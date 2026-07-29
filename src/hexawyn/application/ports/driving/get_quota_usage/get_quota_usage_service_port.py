from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.get_quota_usage.command import GetQuotaUsageCommand
from hexawyn.application.use_case.cluster.get_quota_usage.response import GetQuotaUsageResponse


class GetQuotaUsageServicePort(ABC):
    @abstractmethod
    def execute(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse: ...
