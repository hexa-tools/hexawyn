from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.ports.driving.keda_detect.keda_detect_command import KedaDetectCommand
from hexawyn.application.ports.driving.keda_detect.keda_detect_response import KedaDetectResponse
from hexawyn.application.ports.driving.keda_detect.keda_detect_service_port import (
    KedaDetectServicePort,
)


class KedaDetectService(KedaDetectServicePort):
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def detect(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )
