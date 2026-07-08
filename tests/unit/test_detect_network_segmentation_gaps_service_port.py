from __future__ import annotations

from abc import ABC

import pytest


class TestDetectNetworkSegmentationGapsServicePort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_service_port import (
            DetectNetworkSegmentationGapsServicePort,
        )

        assert issubclass(DetectNetworkSegmentationGapsServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_service_port import (
            DetectNetworkSegmentationGapsServicePort,
        )

        with pytest.raises(TypeError):
            DetectNetworkSegmentationGapsServicePort()  # type: ignore[abstract]
