from __future__ import annotations

from hexawyn.application.ports.driving.version_regression.version_regression_command import (
    VersionRegressionCommand,
)
from hexawyn.application.ports.driving.version_regression.version_regression_response import (
    VersionRegressionResponse,
)
from hexawyn.application.ports.driving.version_regression.version_regression_service_port import (
    VersionRegressionServicePort,
)


class VersionRegressionUseCase:
    def __init__(self, service: VersionRegressionServicePort) -> None:
        self._svc = service

    def execute(self, cmd: VersionRegressionCommand) -> VersionRegressionResponse:
        return self._svc.detect(cmd)
