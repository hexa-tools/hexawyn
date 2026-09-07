from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.get_quota_usage.command import GetQuotaUsageCommand
from hexawyn.application.use_case.cluster.get_quota_usage.response import GetQuotaUsageResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GetQuotaUsageServicePort(ABC):
    @abstractmethod
    def execute(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse: ...
