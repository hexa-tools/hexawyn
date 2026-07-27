from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.estimate_rightsizing_savings.command import (
    EstimateRightsizingSavingsCommand,
)
from hexawyn.application.use_case.finops.estimate_rightsizing_savings.response import (
    EstimateRightsizingSavingsResponse,
)


class EstimateRightsizingSavingsServicePort(ABC):
    @abstractmethod
    def estimate_rightsizing_savings(
        self, command: EstimateRightsizingSavingsCommand
    ) -> EstimateRightsizingSavingsResponse: ...
