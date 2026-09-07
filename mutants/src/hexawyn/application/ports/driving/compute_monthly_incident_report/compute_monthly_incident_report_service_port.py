from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.compute_monthly_incident_report.command import (  # noqa: E501
    ComputeMonthlyIncidentReportCommand,
)
from hexawyn.application.use_case.finops.compute_monthly_incident_report.response import (  # noqa: E501
    ComputeMonthlyIncidentReportResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ComputeMonthlyIncidentReportServicePort(ABC):
    @abstractmethod
    def compute(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse: ...
