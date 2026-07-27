from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.diff_helm_values.command import (
    DiffHelmValuesCommand,
)
from hexawyn.application.use_case.gitops.diff_helm_values.response import (
    DiffHelmValuesResponse,
)


class DiffHelmValuesServicePort(ABC):
    @abstractmethod
    def diff(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse: ...
