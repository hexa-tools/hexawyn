from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.report_stale_credentials.command import (  # noqa: E501
    ReportStaleCredentialsCommand,
)
from hexawyn.application.use_case.security.report_stale_credentials.response import (  # noqa: E501
    ReportStaleCredentialsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ReportStaleCredentialsServicePort(ABC):
    @abstractmethod
    def report(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse: ...
