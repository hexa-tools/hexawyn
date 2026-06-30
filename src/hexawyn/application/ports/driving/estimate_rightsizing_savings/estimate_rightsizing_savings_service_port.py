from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_command import (
    EstimateRightsizingSavingsCommand,
)
from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_response import (
    EstimateRightsizingSavingsResponse,
)


class EstimateRightsizingSavingsServicePort(ABC):
    @abstractmethod
    def estimate_rightsizing_savings(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse: ...
