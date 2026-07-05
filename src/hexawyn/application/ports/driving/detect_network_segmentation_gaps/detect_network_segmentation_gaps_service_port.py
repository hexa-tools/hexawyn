from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_command import (
    DetectNetworkSegmentationGapsCommand,
)
from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_response import (
    DetectNetworkSegmentationGapsResponse,
)


class DetectNetworkSegmentationGapsServicePort(ABC):
    @abstractmethod
    def detect_segmentation_gaps(
        self, command: DetectNetworkSegmentationGapsCommand
    ) -> DetectNetworkSegmentationGapsResponse: ...
