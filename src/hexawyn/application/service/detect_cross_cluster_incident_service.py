from __future__ import annotations

from hexawyn.application.ports.driven.cross_cluster_incident_port import (
    CrossClusterIncidentPort,
)
from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_command import (  # noqa: E501
    DetectCrossClusterIncidentCommand,
)
from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_response import (  # noqa: E501
    DetectCrossClusterIncidentResponse,
)
from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_service_port import (  # noqa: E501
    DetectCrossClusterIncidentServicePort,
)
from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
    correlate,
)


class DetectCrossClusterIncidentService(DetectCrossClusterIncidentServicePort):
    def __init__(self, incident_port: CrossClusterIncidentPort) -> None:
        self._port = incident_port

    def detect(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse:
        failures = self._port.list_all_cluster_failures()
        result = correlate(failures, window_minutes=command.window_minutes)
        return DetectCrossClusterIncidentResponse(result=result)
