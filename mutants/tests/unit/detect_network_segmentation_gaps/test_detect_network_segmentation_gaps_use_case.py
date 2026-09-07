from __future__ import annotations

from unittest.mock import MagicMock


class TestDetectNetworkSegmentationGapsUseCase:
    def test_execute_returns_response(self) -> None:
        from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.command import (  # noqa: E501
            DetectNetworkSegmentationGapsCommand,
        )
        from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.detect_network_segmentation_gaps_use_case import (  # noqa: E501
            DetectNetworkSegmentationGapsUseCase,
        )
        from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.response import (  # noqa: E501
            DetectNetworkSegmentationGapsResponse,
        )

        port = MagicMock()
        port.list_namespaces_with_pod_counts.return_value = []
        port.list_network_policies.return_value = []
        port.has_calico_global_network_policies.return_value = False
        port.has_istio_strict_peer_authentication.return_value = False
        use_case = DetectNetworkSegmentationGapsUseCase(port=port)
        result = use_case.execute(DetectNetworkSegmentationGapsCommand())
        assert isinstance(result, DetectNetworkSegmentationGapsResponse)
