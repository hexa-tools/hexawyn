from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.command import (
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.response import (
    ConservativeNamespaceOverviewResponse,
)


class ConservativeNamespaceOverviewServicePort(ABC):
    @abstractmethod
    def get_overview(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse: ...
