from unittest.mock import MagicMock

from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_command import (  # noqa: E501
    DetectCrossClusterIncidentCommand,
)
from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_response import (  # noqa: E501
    DetectCrossClusterIncidentResponse,
)
from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_service_port import (  # noqa: E501
    DetectCrossClusterIncidentServicePort,
)
from hexawyn.domain.models.cross_cluster_correlation import CrossClusterCorrelationReport


class TestDetectCrossClusterIncidentUseCase:
    def test_delegates(self) -> None:
        from hexawyn.application.use_case.detect_cross_cluster_incident.detect_cross_cluster_incident_use_case import (  # noqa: E501
            DetectCrossClusterIncidentUseCase,
        )

        service = MagicMock(spec=DetectCrossClusterIncidentServicePort)
        expected = DetectCrossClusterIncidentResponse(result=CrossClusterCorrelationReport())
        service.detect.return_value = expected
        use_case = DetectCrossClusterIncidentUseCase(service=service)

        response = use_case.execute(DetectCrossClusterIncidentCommand())
        assert response is expected
