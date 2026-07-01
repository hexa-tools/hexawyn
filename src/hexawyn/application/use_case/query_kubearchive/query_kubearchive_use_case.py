from __future__ import annotations

from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_command import (
    QueryKubeArchiveCommand,
)
from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_response import (
    QueryKubeArchiveResponse,
)
from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_service_port import (
    QueryKubeArchiveServicePort,
)


class QueryKubeArchiveUseCase:
    def __init__(self, service: QueryKubeArchiveServicePort) -> None:
        self._service = service

    def execute(self, command: QueryKubeArchiveCommand) -> QueryKubeArchiveResponse:
        return self._service.query(command)
