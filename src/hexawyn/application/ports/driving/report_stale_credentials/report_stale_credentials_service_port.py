from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.report_stale_credentials.command import (  # noqa: E501
    ReportStaleCredentialsCommand,
)
from hexawyn.application.use_case.security.report_stale_credentials.response import (  # noqa: E501
    ReportStaleCredentialsResponse,
)


class ReportStaleCredentialsServicePort(ABC):
    @abstractmethod
    def report(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse: ...
