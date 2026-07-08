from __future__ import annotations


class TestDetectUnintendedExternalExposureResponse:
    def test_defaults(self) -> None:
        from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_response import (
            DetectUnintendedExternalExposureResponse,
        )

        response = DetectUnintendedExternalExposureResponse()

        assert response.findings == []
        assert response.excluded_exposures == []
        assert response.total_external_services_checked == 0
        assert response.summary == ""
        assert response.error is None

    def test_accepts_explicit_values(self) -> None:
        from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_response import (
            DetectUnintendedExternalExposureResponse,
            ExcludedExposureDict,
            ExternalExposureFindingDict,
        )

        finding: ExternalExposureFindingDict = {
            "name": "postgres-svc",
            "namespace": "production",
            "service_type": "LoadBalancer",
            "ports": [5432],
            "external_ip": "34.120.45.12",
            "external_hostname": None,
            "node_port": None,
            "is_pending": False,
            "risk_level": "critical",
            "note": None,
        }
        excluded: ExcludedExposureDict = {
            "name": "api-gateway",
            "namespace": "production",
            "reason": "allowlisted",
        }

        response = DetectUnintendedExternalExposureResponse(
            findings=[finding],
            excluded_exposures=[excluded],
            total_external_services_checked=5,
            summary="1 unintended external service(s) found out of 5 checked.",
            error=None,
        )

        assert response.findings == [finding]
        assert response.excluded_exposures == [excluded]
        assert response.total_external_services_checked == 5
        assert "1 unintended" in response.summary
