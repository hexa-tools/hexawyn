from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.gitops_app_sync.command import (  # type: ignore
    GitOpsAppSyncCommand,
)
from hexawyn.application.use_case.gitops.gitops_app_sync.response import (  # type: ignore
    GitOpsAppSyncResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GitOpsAppSyncServicePort(ABC):
    @abstractmethod
    def get_sync_status(self, command: GitOpsAppSyncCommand) -> GitOpsAppSyncResponse: ...
