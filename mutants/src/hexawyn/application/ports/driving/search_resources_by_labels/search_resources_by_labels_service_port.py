from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.search_resources_by_labels.command import (
    SearchResourcesByLabelsCommand,
)
from hexawyn.application.use_case.cluster.search_resources_by_labels.response import (
    SearchResourcesByLabelsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class SearchResourcesByLabelsServicePort(ABC):
    @abstractmethod
    def search(
        self, command: SearchResourcesByLabelsCommand
    ) -> SearchResourcesByLabelsResponse: ...
