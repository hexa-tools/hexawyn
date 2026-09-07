from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.diff_cluster_resources.command import (  # noqa: E501
    DiffClusterResourcesCommand,
)
from hexawyn.application.use_case.cluster.diff_cluster_resources.response import (  # noqa: E501
    DiffClusterResourcesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DiffClusterResourcesServicePort(ABC):
    @abstractmethod
    def diff(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse: ...
