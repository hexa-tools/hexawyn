from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.estimate_rightsizing_savings.command import (
    EstimateRightsizingSavingsCommand,
)
from hexawyn.application.use_case.finops.estimate_rightsizing_savings.response import (
    EstimateRightsizingSavingsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class EstimateRightsizingSavingsServicePort(ABC):
    @abstractmethod
    def estimate_rightsizing_savings(
        self, command: EstimateRightsizingSavingsCommand
    ) -> EstimateRightsizingSavingsResponse: ...
