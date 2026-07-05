from __future__ import annotations

from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_command import (
    DetectNetworkSegmentationGapsCommand,
)
from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_response import (
    DetectNetworkSegmentationGapsResponse,
)
from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_service_port import (
    DetectNetworkSegmentationGapsServicePort,
)


class DetectNetworkSegmentationGapsUseCase:
    def __init__(self, service: DetectNetworkSegmentationGapsServicePort) -> None:
        self._svc = service

    def execute(
        self, command: DetectNetworkSegmentationGapsCommand
    ) -> DetectNetworkSegmentationGapsResponse:
        return self._svc.detect_segmentation_gaps(command)
