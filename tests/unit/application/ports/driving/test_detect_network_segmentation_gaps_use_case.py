from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_command import (
    DetectNetworkSegmentationGapsCommand,
)
from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_response import (
    DetectNetworkSegmentationGapsResponse,
)
from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_service_port import (
    DetectNetworkSegmentationGapsServicePort,
)
from hexawyn.application.use_case.detect_network_segmentation_gaps.detect_network_segmentation_gaps_use_case import (
    DetectNetworkSegmentationGapsUseCase,
)


class TestDetectNetworkSegmentationGapsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=DetectNetworkSegmentationGapsServicePort)
        expected = DetectNetworkSegmentationGapsResponse()
        service.detect_segmentation_gaps.return_value = expected
        use_case = DetectNetworkSegmentationGapsUseCase(service=service)
        command = DetectNetworkSegmentationGapsCommand()

        result = use_case.execute(command)

        service.detect_segmentation_gaps.assert_called_once_with(command)
        assert result is expected
