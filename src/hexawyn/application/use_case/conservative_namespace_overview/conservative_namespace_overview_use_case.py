from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_overview_port import NamespaceOverviewPort
from hexawyn.application.use_case.conservative_namespace_overview.command import (
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.use_case.conservative_namespace_overview.response import (
    ConservativeNamespaceOverviewResponse,
)


class ConservativeNamespaceOverviewUseCase:
    def __init__(self, port: NamespaceOverviewPort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s = k8s_port

    def execute(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        return ConservativeNamespaceOverviewResponse()
