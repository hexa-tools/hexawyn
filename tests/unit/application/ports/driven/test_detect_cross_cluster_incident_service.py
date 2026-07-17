from unittest.mock import MagicMock

from hexawyn.application.ports.driven.cross_cluster_incident_port import CrossClusterIncidentPort
from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_command import (  # noqa: E501
    DetectCrossClusterIncidentCommand,
)


class TestDetectCrossClusterIncidentService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_service_port import (  # noqa: E501
            DetectCrossClusterIncidentServicePort,
        )
        from hexawyn.application.service.detect_cross_cluster_incident_service import (
            DetectCrossClusterIncidentService,
        )

        service = DetectCrossClusterIncidentService(
            incident_port=MagicMock(spec=CrossClusterIncidentPort)
        )
        assert isinstance(service, DetectCrossClusterIncidentServicePort)

    def test_detect_returns_result(self) -> None:
        from hexawyn.application.service.detect_cross_cluster_incident_service import (
            DetectCrossClusterIncidentService,
        )

        port = MagicMock(spec=CrossClusterIncidentPort)
        port.list_all_cluster_failures.return_value = []
        service = DetectCrossClusterIncidentService(incident_port=port)

        response = service.detect(DetectCrossClusterIncidentCommand())
        assert response.result.scope == "none"
