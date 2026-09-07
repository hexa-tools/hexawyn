from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.report_unauthorized_access.command import (  # noqa: E501
    ReportUnauthorizedAccessCommand,
)
from hexawyn.application.use_case.security.report_unauthorized_access.response import (  # noqa: E501
    ReportUnauthorizedAccessResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ReportUnauthorizedAccessServicePort(ABC):
    @abstractmethod
    def report(
        self, command: ReportUnauthorizedAccessCommand
    ) -> ReportUnauthorizedAccessResponse: ...
