from __future__ import annotations


class TestScanContainerVulnerabilitiesResponse:
    def test_defaults(self) -> None:
        from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_response import (
            ScanContainerVulnerabilitiesResponse,
        )

        response = ScanContainerVulnerabilitiesResponse()

        assert response.findings == []
        assert response.total_images_scanned == 0
        assert response.images_with_critical_cves == 0
        assert response.eol_image_count == 0
        assert response.summary == ""
        assert response.error is None

    def test_accepts_explicit_values(self) -> None:
        from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_response import (
            CVEDict,
            ImageVulnerabilityFindingDict,
            ScanContainerVulnerabilitiesResponse,
        )

        cve: CVEDict = {
            "cve_id": "CVE-2024-5535",
            "severity": "critical",
            "package": "openssl",
            "fix_version": "3.0.14",
        }
        finding: ImageVulnerabilityFindingDict = {
            "image": "payment:v1.2",
            "namespaces": ["production"],
            "pods_using": ["payment-pod-abc", "payment-pod-def"],
            "cves": [cve],
            "eol_base": True,
            "is_mutable_tag": False,
            "scan_status": "scanned",
            "scanned_at": "2026-07-05T12:00:00+00:00",
            "priority_score": 8,
        }

        response = ScanContainerVulnerabilitiesResponse(
            findings=[finding],
            total_images_scanned=10,
            images_with_critical_cves=2,
            eol_image_count=3,
            summary="3/10 images affected by known CVEs.",
            error=None,
        )

        assert response.findings == [finding]
        assert response.total_images_scanned == 10
        assert response.images_with_critical_cves == 2
        assert response.eol_image_count == 3
        assert "3/10" in response.summary
