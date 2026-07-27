from __future__ import annotations

from hexawyn.application.ports.driven.probe_audit_port import ProbeAuditPort
from hexawyn.application.use_case.security.detect_missing_probes.command import (
    DetectMissingProbesCommand,
)
from hexawyn.application.use_case.security.detect_missing_probes.response import (
    DetectMissingProbesResponse,
)
from hexawyn.domain.services.probe_audit.probe_audit_engine import (
    ProbeAuditEngine,
)


class DetectMissingProbesUseCase:
    def __init__(self, probe_audit_port: ProbeAuditPort) -> None:
        self._port = probe_audit_port
        self._engine = ProbeAuditEngine()

    def detect_missing_probes(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse:
        deployments_raw = self._port.get_probe_audit_data(command.namespace)
        deployments: list[dict[str, object]] = [dict(d) for d in deployments_raw]
        result = self._engine.detect(deployments)
        return DetectMissingProbesResponse(result=result)  # type: ignore
