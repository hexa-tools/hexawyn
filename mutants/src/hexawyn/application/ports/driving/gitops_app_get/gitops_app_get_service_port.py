from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.gitops_app_get.command import (  # type: ignore
    GitOpsAppGetCommand,
)
from hexawyn.application.use_case.gitops.gitops_app_get.response import (  # type: ignore
    GitOpsAppGetResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GitOpsAppGetServicePort(ABC):
    @abstractmethod
    def get_app(self, command: GitOpsAppGetCommand) -> GitOpsAppGetResponse: ...
