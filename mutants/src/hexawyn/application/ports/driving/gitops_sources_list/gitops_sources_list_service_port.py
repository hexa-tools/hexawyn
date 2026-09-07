from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.gitops_sources_list.command import (  # type: ignore
    GitOpsSourcesListCommand,
)
from hexawyn.application.use_case.gitops.gitops_sources_list.response import (  # type: ignore
    GitOpsSourcesListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GitOpsSourcesListServicePort(ABC):
    @abstractmethod
    def list_sources(self, command: GitOpsSourcesListCommand) -> GitOpsSourcesListResponse: ...
