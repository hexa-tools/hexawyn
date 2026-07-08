from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_command import (
    QueryKubeArchiveCommand,
)
from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_response import (
    QueryKubeArchiveResponse,
)


class QueryKubeArchiveServicePort(ABC):
    @abstractmethod
    def query(self, command: QueryKubeArchiveCommand) -> QueryKubeArchiveResponse:
        """Query historical resource state and optionally compare with current state."""
