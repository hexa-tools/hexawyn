from hexawyn.application.ports.driven.probe_audit_port import ProbeAuditPort
from hexawyn.application.use_case.detect_missing_probes.command import DetectMissingProbesCommand
from hexawyn.application.use_case.detect_missing_probes.response import DetectMissingProbesResponse


class DetectMissingProbesUseCase:
    def __init__(self, port: ProbeAuditPort) -> None:
        self._port = port

    def execute(self, command: DetectMissingProbesCommand) -> DetectMissingProbesResponse:
        return DetectMissingProbesResponse()
