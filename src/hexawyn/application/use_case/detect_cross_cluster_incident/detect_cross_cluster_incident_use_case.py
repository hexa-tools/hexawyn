from hexawyn.application.ports.driven.cross_cluster_incident_port import CrossClusterIncidentPort
from hexawyn.application.use_case.detect_cross_cluster_incident.command import (
    DetectCrossClusterIncidentCommand,
)
from hexawyn.application.use_case.detect_cross_cluster_incident.response import (
    DetectCrossClusterIncidentResponse,
)
from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (
    correlate,
)


class DetectCrossClusterIncidentUseCase:
    def __init__(self, incident_port: CrossClusterIncidentPort) -> None:
        self._port = incident_port

    def execute(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse:
        failures = self._port.list_all_cluster_failures()
        result = correlate(failures, window_minutes=command.window_minutes)
        return DetectCrossClusterIncidentResponse(result=result)
