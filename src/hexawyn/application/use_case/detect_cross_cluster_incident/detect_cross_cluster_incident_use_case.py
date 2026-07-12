from __future__ import annotations

from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_command import (  # noqa: E501
    DetectCrossClusterIncidentCommand,
)
from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_response import (  # noqa: E501
    DetectCrossClusterIncidentResponse,
)
from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_service_port import (  # noqa: E501
    DetectCrossClusterIncidentServicePort,
)


class DetectCrossClusterIncidentUseCase:
    def __init__(self, service: DetectCrossClusterIncidentServicePort) -> None:
        self._service = service

    def execute(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse:
        return self._service.detect(command)
