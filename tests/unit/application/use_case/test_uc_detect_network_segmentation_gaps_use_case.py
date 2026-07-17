"""Unit tests for DetectNetworkSegmentationGapsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_service_port import (
    DetectNetworkSegmentationGapsServicePort,
)
from hexawyn.application.use_case.detect_network_segmentation_gaps.detect_network_segmentation_gaps_use_case import (
    DetectNetworkSegmentationGapsUseCase,
)


class TestDetectNetworkSegmentationGapsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DetectNetworkSegmentationGapsServicePort)
        use_case = DetectNetworkSegmentationGapsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect_segmentation_gaps.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DetectNetworkSegmentationGapsServicePort)
        mock_service.detect_segmentation_gaps.side_effect = RuntimeError("test error")
        use_case = DetectNetworkSegmentationGapsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
