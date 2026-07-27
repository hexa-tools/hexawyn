from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.query_kubearchive.command import (  # type: ignore
    QueryKubeArchiveCommand,
)
from hexawyn.application.use_case.troubleshooting.query_kubearchive.response import (  # type: ignore
    QueryKubeArchiveResponse,
)


class QueryKubeArchiveServicePort(ABC):
    @abstractmethod
    def query(self, command: QueryKubeArchiveCommand) -> QueryKubeArchiveResponse: ...
