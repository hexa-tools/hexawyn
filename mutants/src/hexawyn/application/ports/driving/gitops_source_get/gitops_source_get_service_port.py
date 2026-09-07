from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.gitops_source_get.command import (  # type: ignore
    GitOpsSourceGetCommand,
)
from hexawyn.application.use_case.gitops.gitops_source_get.response import (  # type: ignore
    GitOpsSourceGetResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GitOpsSourceGetServicePort(ABC):
    @abstractmethod
    def get_source(self, command: GitOpsSourceGetCommand) -> GitOpsSourceGetResponse: ...
