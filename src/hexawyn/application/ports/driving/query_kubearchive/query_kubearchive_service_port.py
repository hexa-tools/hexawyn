from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.query_kubearchive.command import (
    QueryKubearchiveCommand,
)
from hexawyn.application.use_case.troubleshooting.query_kubearchive.response import (
    QueryKubearchiveResponse,
)


class QueryKubeArchiveServicePort(ABC):
    @abstractmethod
    def query(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse: ...
