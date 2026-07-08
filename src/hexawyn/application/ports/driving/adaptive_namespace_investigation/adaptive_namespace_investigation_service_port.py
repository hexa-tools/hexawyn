from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_command import (
    AdaptiveNamespaceInvestigationCommand,
)
from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_response import (
    AdaptiveNamespaceInvestigationResponse,
)


class AdaptiveNamespaceInvestigationServicePort(ABC):
    @abstractmethod
    def investigate(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse: ...
