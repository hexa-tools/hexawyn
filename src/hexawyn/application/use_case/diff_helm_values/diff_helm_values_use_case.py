from __future__ import annotations

from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_command import (
    DiffHelmValuesCommand,
)
from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_response import (
    DiffHelmValuesResponse,
)
from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_service_port import (
    DiffHelmValuesServicePort,
)


class DiffHelmValuesUseCase:
    def __init__(self, service: DiffHelmValuesServicePort) -> None:
        self._service = service

    def execute(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        return self._service.diff(command)
