from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_command import (  # noqa: E501
    ReportNightInterventionsCommand,
)
from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_response import (  # noqa: E501
    ReportNightInterventionsResponse,
)


class ReportNightInterventionsServicePort(ABC):
    @abstractmethod
    def report(
        self, command: ReportNightInterventionsCommand
    ) -> ReportNightInterventionsResponse: ...
