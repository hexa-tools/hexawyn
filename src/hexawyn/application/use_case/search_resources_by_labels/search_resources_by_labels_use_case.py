from __future__ import annotations

from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_command import (
    SearchResourcesByLabelsCommand,
)
from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_response import (
    SearchResourcesByLabelsResponse,
)
from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_service_port import (
    SearchResourcesByLabelsServicePort,
)


class SearchResourcesByLabelsUseCase:
    def __init__(self, service: SearchResourcesByLabelsServicePort) -> None:
        self._svc = service

    def execute(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        return self._svc.search(command)
