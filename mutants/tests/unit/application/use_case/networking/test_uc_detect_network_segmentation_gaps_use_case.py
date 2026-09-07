from __future__ import annotations

from dataclasses import asdict
from unittest.mock import MagicMock

from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.command import (
    DetectNetworkSegmentationGapsCommand,
)
from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.detect_network_segmentation_gaps_use_case import (  # noqa: E501
    DetectNetworkSegmentationGapsUseCase,
)
from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.response import (
    DetectNetworkSegmentationGapsResponse,
)


class TestDetectNetworkSegmentationGapsUseCase:
    def test_execute_returns_response_type(self) -> None:
        port = MagicMock()
        use_case = DetectNetworkSegmentationGapsUseCase(port=port)
        result = use_case.execute(DetectNetworkSegmentationGapsCommand())
        assert isinstance(result, DetectNetworkSegmentationGapsResponse)
        assert result.error is None

    def test_response_defaults_are_empty_not_none(self) -> None:
        response = DetectNetworkSegmentationGapsResponse()
        assert response.findings == []
        assert response.excluded_namespaces == []
        assert response.total_namespaces_checked == 0
        assert response.fully_open_count == 0
        assert response.partially_restricted_count == 0
        assert response.restricted_count == 0
        assert response.summary == ""
        assert response.error is None

    def test_response_with_data(self) -> None:
        response = DetectNetworkSegmentationGapsResponse(
            total_namespaces_checked=10,
            fully_open_count=3,
            partially_restricted_count=5,
            restricted_count=2,
            summary="3 namespaces need NetworkPolicies",
        )
        assert response.total_namespaces_checked == 10  # noqa: PLR2004
        assert response.fully_open_count == 3  # noqa: PLR2004

    def test_response_findings_are_serializable(self) -> None:
        response = DetectNetworkSegmentationGapsResponse(
            findings=[{"namespace": "default", "risk": "high"}],
            excluded_namespaces=["kube-system"],
            total_namespaces_checked=5,
            restricted_count=1,
            partially_restricted_count=3,
            fully_open_count=1,
            summary="1 namespace at risk",
        )
        result = asdict(response)
        assert result["total_namespaces_checked"] == 5  # noqa: PLR2004
        assert "kube-system" in result["excluded_namespaces"]
        assert len(result["findings"]) == 1

    def test_command_is_frozen(self) -> None:
        cmd = DetectNetworkSegmentationGapsCommand()
        assert isinstance(cmd, DetectNetworkSegmentationGapsCommand)

    def test_response_with_explicit_error_none(self) -> None:
        response = DetectNetworkSegmentationGapsResponse(error=None)
        assert response.error is None

    def test_response_edge_case_zero_counts(self) -> None:
        response = DetectNetworkSegmentationGapsResponse(
            total_namespaces_checked=0,
            fully_open_count=0,
            partially_restricted_count=0,
            restricted_count=0,
        )
        assert response.total_namespaces_checked == 0
        assert response.fully_open_count == 0
        assert response.findings == []
