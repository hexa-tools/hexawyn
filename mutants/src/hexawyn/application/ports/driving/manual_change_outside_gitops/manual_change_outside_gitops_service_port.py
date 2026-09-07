# mypy: ignore-errors
from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.manual_change_outside_gitops.command import (  # noqa: E501  # type: ignore
    ManualChangeOutsideGitOpsCommand,
)
from hexawyn.application.use_case.gitops.manual_change_outside_gitops.response import (  # noqa: E501  # type: ignore
    ManualChangeOutsideGitOpsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ManualChangeOutsideGitOpsServicePort(ABC):
    @abstractmethod
    def detect_manual_changes(
        self, command: ManualChangeOutsideGitOpsCommand
    ) -> ManualChangeOutsideGitOpsResponse: ...
