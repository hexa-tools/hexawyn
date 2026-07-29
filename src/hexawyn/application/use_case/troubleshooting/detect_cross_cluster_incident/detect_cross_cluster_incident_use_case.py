from __future__ import annotations

from hexawyn.application.ports.driven.cross_cluster_incident_port import (
    CrossClusterIncidentPort,
)
from hexawyn.application.use_case.troubleshooting.detect_cross_cluster_incident.command import (  # noqa: E501
    DetectCrossClusterIncidentCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_cross_cluster_incident.response import (  # noqa: E501
    DetectCrossClusterIncidentResponse,
)
from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
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
