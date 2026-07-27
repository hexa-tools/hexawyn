from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.report_night_interventions.command import (  # noqa: E501
    ReportNightInterventionsCommand,
)
from hexawyn.application.use_case.workloads.report_night_interventions.response import (  # noqa: E501
    ReportNightInterventionsResponse,
)


class ReportNightInterventionsServicePort(ABC):
    @abstractmethod
    def report(
        self, command: ReportNightInterventionsCommand
    ) -> ReportNightInterventionsResponse: ...
