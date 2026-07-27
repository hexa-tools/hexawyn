from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.adaptive_namespace_investigation.command import (
    AdaptiveNamespaceInvestigationCommand,
)
from hexawyn.application.use_case.troubleshooting.adaptive_namespace_investigation.response import (
    AdaptiveNamespaceInvestigationResponse,
)


class AdaptiveNamespaceInvestigationServicePort(ABC):
    @abstractmethod
    def investigate(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse: ...
