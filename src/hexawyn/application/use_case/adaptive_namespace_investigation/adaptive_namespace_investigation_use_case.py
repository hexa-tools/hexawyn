from __future__ import annotations

from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_command import (
    AdaptiveNamespaceInvestigationCommand,
)
from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_response import (
    AdaptiveNamespaceInvestigationResponse,
)
from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_service_port import (
    AdaptiveNamespaceInvestigationServicePort,
)


class AdaptiveNamespaceInvestigationUseCase:
    def __init__(self, service: AdaptiveNamespaceInvestigationServicePort) -> None:
        self._svc = service

    def execute(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        return self._svc.investigate(command)
