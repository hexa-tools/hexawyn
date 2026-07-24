from hexawyn.application.ports.driven.adaptive_investigation_port import AdaptiveInvestigationPort
from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_overview_port import NamespaceOverviewPort
from hexawyn.application.use_case.adaptive_namespace_investigation.command import (
    AdaptiveNamespaceInvestigationCommand,
)
from hexawyn.application.use_case.adaptive_namespace_investigation.response import (
    AdaptiveNamespaceInvestigationResponse,
)


class AdaptiveNamespaceInvestigationUseCase:
    def __init__(
        self,
        investigation_port: AdaptiveInvestigationPort,
        k8s_port: K8sPort,
        overview_port: NamespaceOverviewPort,
    ) -> None:
        self._investigation = investigation_port
        self._k8s = k8s_port
        self._overview = overview_port

    def execute(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        return AdaptiveNamespaceInvestigationResponse()
