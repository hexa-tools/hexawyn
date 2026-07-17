from __future__ import annotations


class TestDetectPrivilegedPodsResponse:
    def test_defaults(self) -> None:
        from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_response import (
            DetectPrivilegedPodsResponse,
        )

        response = DetectPrivilegedPodsResponse()

        assert response.findings == []
        assert response.compliant_pod_count == 0
        assert response.total_pods_checked == 0
        assert response.summary == ""
        assert response.error is None

    def test_accepts_explicit_values(self) -> None:
        from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_response import (
            DetectPrivilegedPodsResponse,
            PodSecurityFindingDict,
            SecurityViolationDict,
        )

        violation: SecurityViolationDict = {
            "violation_type": "privileged",
            "severity": "critical",
            "pss_level": "Baseline",
            "container_name": "app",
            "recommendation": "Set privileged: false in the container's securityContext.",
        }
        finding: PodSecurityFindingDict = {
            "pod_name": "data-processor-abc",
            "namespace": "production",
            "violations": [violation],
            "note": None,
            "namespace_psa_enforce_level": None,
        }

        response = DetectPrivilegedPodsResponse(
            findings=[finding],
            compliant_pod_count=8,
            total_pods_checked=9,
            summary="1 pod violating Pod Security Standards across 1 namespace, 1 critical.",
            error=None,
        )

        assert response.findings == [finding]
        assert response.compliant_pod_count == 8
        assert response.total_pods_checked == 9
        assert "1 pod violating" in response.summary
