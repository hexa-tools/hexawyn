from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_command import (
    GenerateSlaReportCommand,
)
from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_response import (
    GenerateSlaReportResponse,
)


class GenerateSlaReportServicePort(ABC):
    @abstractmethod
    def generate(self, command: GenerateSlaReportCommand) -> GenerateSlaReportResponse: ...
