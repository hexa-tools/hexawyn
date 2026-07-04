from __future__ import annotations

from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_command import (
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_response import (
    ConservativeNamespaceOverviewResponse,
)
from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_service_port import (
    ConservativeNamespaceOverviewServicePort,
)


class ConservativeNamespaceOverviewUseCase:
    def __init__(self, service: ConservativeNamespaceOverviewServicePort) -> None:
        self._svc = service

    def execute(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        return self._svc.get_overview(command)
