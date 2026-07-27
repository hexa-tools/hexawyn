from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.generate_sla_report.command import (  # type: ignore
    GenerateSlaReportCommand,
)
from hexawyn.application.use_case.workloads.generate_sla_report.response import (  # type: ignore
    GenerateSlaReportResponse,
)


class GenerateSlaReportServicePort(ABC):
    @abstractmethod
    def generate(self, command: GenerateSlaReportCommand) -> GenerateSlaReportResponse: ...
