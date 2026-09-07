from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.gitops_apps_list.command import (  # type: ignore
    GitOpsAppsListCommand,
)
from hexawyn.application.use_case.gitops.gitops_apps_list.response import (  # type: ignore
    GitOpsAppsListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GitOpsAppsListServicePort(ABC):
    @abstractmethod
    def list_apps(self, command: GitOpsAppsListCommand) -> GitOpsAppsListResponse: ...
