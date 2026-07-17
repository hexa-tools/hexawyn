from __future__ import annotations


class TestDetectNetworkSegmentationGapsResponse:
    def test_defaults(self) -> None:
        from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_response import (
            DetectNetworkSegmentationGapsResponse,
        )

        response = DetectNetworkSegmentationGapsResponse()

        assert response.findings == []
        assert response.excluded_namespaces == []
        assert response.total_namespaces_checked == 0
        assert response.fully_open_count == 0
        assert response.partially_restricted_count == 0
        assert response.restricted_count == 0
        assert response.summary == ""
        assert response.error is None

    def test_accepts_explicit_values(self) -> None:
        from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_response import (
            DetectNetworkSegmentationGapsResponse,
            ExcludedNamespaceDict,
            NamespaceNetworkFindingDict,
        )

        finding: NamespaceNetworkFindingDict = {
            "namespace": "dev",
            "ingress_policies": 0,
            "egress_policies": 0,
            "pod_count": 8,
            "network_status": "open",
            "risk_level": "critical",
            "recommendation": "Apply default-deny NetworkPolicy for both ingress and egress",
            "note": None,
        }
        excluded: ExcludedNamespaceDict = {
            "namespace": "kube-system",
            "reason": "system namespace",
        }

        response = DetectNetworkSegmentationGapsResponse(
            findings=[finding],
            excluded_namespaces=[excluded],
            total_namespaces_checked=8,
            fully_open_count=2,
            partially_restricted_count=3,
            restricted_count=3,
            summary="2 namespace(s) fully open to east-west traffic out of 8 checked.",
            error=None,
        )

        assert response.findings == [finding]
        assert response.excluded_namespaces == [excluded]
        assert response.total_namespaces_checked == 8
        assert response.fully_open_count == 2
        assert response.partially_restricted_count == 3
        assert response.restricted_count == 3
        assert "fully open" in response.summary
