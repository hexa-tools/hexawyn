from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.search_resources_by_labels.command import (
    SearchResourcesByLabelsCommand,
)
from hexawyn.application.use_case.cluster.search_resources_by_labels.response import (
    SearchResourcesByLabelsResponse,
)


class SearchResourcesByLabelsServicePort(ABC):
    @abstractmethod
    def search(
        self, command: SearchResourcesByLabelsCommand
    ) -> SearchResourcesByLabelsResponse: ...
