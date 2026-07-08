from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_command import (
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_response import (
    ConservativeNamespaceOverviewResponse,
)


class ConservativeNamespaceOverviewServicePort(ABC):
    @abstractmethod
    def get_overview(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse: ...
