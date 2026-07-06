from __future__ import annotations

from hexawyn.application.ports.driven.probe_audit_port import ProbeAuditPort
from hexawyn.application.ports.driving.detect_missing_probes.detect_missing_probes_command import (
    DetectMissingProbesCommand,
)
from hexawyn.application.ports.driving.detect_missing_probes.detect_missing_probes_response import (
    DetectMissingProbesResponse,
)
from hexawyn.application.ports.driving.detect_missing_probes.detect_missing_probes_service_port import (
    DetectMissingProbesServicePort,
)
from hexawyn.domain.services.probe_audit.probe_audit_engine import (
    ProbeAuditEngine,
)


class DetectMissingProbesService(DetectMissingProbesServicePort):
    def __init__(self, probe_audit_port: ProbeAuditPort) -> None:
        self._port = probe_audit_port
        self._engine = ProbeAuditEngine()

    def detect_missing_probes(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse:
        deployments_raw = self._port.get_probe_audit_data(command.namespace)
        deployments: list[dict[str, object]] = [dict(d) for d in deployments_raw]
        result = self._engine.detect(deployments)
        return DetectMissingProbesResponse(result=result)
