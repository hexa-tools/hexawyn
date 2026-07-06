from __future__ import annotations

from hexawyn.application.ports.driving.detect_missing_probes.detect_missing_probes_command import (
    DetectMissingProbesCommand,
)
from hexawyn.application.ports.driving.detect_missing_probes.detect_missing_probes_response import (
    DetectMissingProbesResponse,
)
from hexawyn.application.ports.driving.detect_missing_probes.detect_missing_probes_service_port import (
    DetectMissingProbesServicePort,
)


class DetectMissingProbesUseCase:
    def __init__(self, service: DetectMissingProbesServicePort) -> None:
        self._service = service

    def execute(self, command: DetectMissingProbesCommand) -> DetectMissingProbesResponse:
        return self._service.detect_missing_probes(command)
