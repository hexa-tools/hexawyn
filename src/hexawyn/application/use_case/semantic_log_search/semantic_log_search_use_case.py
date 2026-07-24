from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.semantic_log_search.command import SemanticLogSearchCommand
from hexawyn.application.use_case.semantic_log_search.response import SemanticLogSearchResponse


class SemanticLogSearchUseCase:
    def __init__(self, port: K8sPort) -> None:
        self._port = port

    def execute(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
        return SemanticLogSearchResponse()
