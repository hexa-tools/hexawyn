from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.detect_cross_cluster_incident.command import (  # noqa: E501
    DetectCrossClusterIncidentCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_cross_cluster_incident.detect_cross_cluster_incident_use_case import (  # noqa: E501
    DetectCrossClusterIncidentUseCase,
)
from hexawyn.application.use_case.troubleshooting.detect_cross_cluster_incident.response import (  # noqa: E501
    DetectCrossClusterIncidentResponse,
)


class TestDetectCrossClusterIncidentUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_cross_cluster_failures.return_value = []

        use_case = DetectCrossClusterIncidentUseCase(
            incident_port=port,
        )
        result = use_case.execute(DetectCrossClusterIncidentCommand())

        assert isinstance(result, DetectCrossClusterIncidentResponse)

    def test_execute_short_window_no_data(self) -> None:
        port = MagicMock()
        port.fetch_cross_cluster_failures.return_value = []

        use_case = DetectCrossClusterIncidentUseCase(
            incident_port=port,
        )
        result = use_case.execute(DetectCrossClusterIncidentCommand(window_minutes=5))

        assert result.result is not None
