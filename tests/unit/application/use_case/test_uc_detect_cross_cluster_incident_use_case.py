"""Unit tests for DetectCrossClusterIncidentUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_service_port import (
    DetectCrossClusterIncidentServicePort,
)
from hexawyn.application.use_case.detect_cross_cluster_incident.detect_cross_cluster_incident_use_case import (
    DetectCrossClusterIncidentUseCase,
)


class TestDetectCrossClusterIncidentUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DetectCrossClusterIncidentServicePort)
        use_case = DetectCrossClusterIncidentUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DetectCrossClusterIncidentServicePort)
        mock_service.detect.side_effect = RuntimeError("test error")
        use_case = DetectCrossClusterIncidentUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
