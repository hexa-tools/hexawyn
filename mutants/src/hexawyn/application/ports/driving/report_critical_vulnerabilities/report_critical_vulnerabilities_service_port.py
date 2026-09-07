from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.report_critical_vulnerabilities.command import (  # noqa: E501
    ReportCriticalVulnerabilitiesCommand,
)
from hexawyn.application.use_case.security.report_critical_vulnerabilities.response import (  # noqa: E501
    ReportCriticalVulnerabilitiesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ReportCriticalVulnerabilitiesServicePort(ABC):
    @abstractmethod
    def report(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse: ...
