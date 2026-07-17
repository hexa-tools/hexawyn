from hexawyn.domain.models.security_posture import SecurityPostureReport


class TestComputeSecurityPostureResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_response import (  # noqa: E501
            ComputeSecurityPostureResponse,
        )

        report = SecurityPostureReport(overall_score_pct=80.0)
        response = ComputeSecurityPostureResponse(result=report)

        assert response.result is report
        assert response.result.overall_score_pct == 80.0
