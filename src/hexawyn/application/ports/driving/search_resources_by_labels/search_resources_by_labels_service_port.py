from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_command import (
    SearchResourcesByLabelsCommand,
)
from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_response import (
    SearchResourcesByLabelsResponse,
)


class SearchResourcesByLabelsServicePort(ABC):
    @abstractmethod
    def search(
        self, command: SearchResourcesByLabelsCommand
    ) -> SearchResourcesByLabelsResponse: ...
