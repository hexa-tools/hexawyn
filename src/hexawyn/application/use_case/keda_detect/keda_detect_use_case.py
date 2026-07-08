from __future__ import annotations

from hexawyn.application.ports.driving.keda_detect.keda_detect_command import KedaDetectCommand
from hexawyn.application.ports.driving.keda_detect.keda_detect_response import KedaDetectResponse
from hexawyn.application.ports.driving.keda_detect.keda_detect_service_port import (
    KedaDetectServicePort,
)


class KedaDetectUseCase:
    def __init__(self, service: KedaDetectServicePort) -> None:
        self._svc = service

    def execute(self, cmd: KedaDetectCommand) -> KedaDetectResponse:
        return self._svc.detect(cmd)
