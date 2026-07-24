from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.search_resources_by_labels.command import (
    SearchResourcesByLabelsCommand,
)
from hexawyn.application.use_case.search_resources_by_labels.response import (
    SearchResourcesByLabelsResponse,
)


class SearchResourcesByLabelsUseCase:
    def __init__(self, port: K8sPort) -> None:
        self._port = port

    def execute(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        return SearchResourcesByLabelsResponse()
