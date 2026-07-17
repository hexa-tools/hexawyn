from hexawyn.domain.models.helm_values_diff import HelmValuesDiffReport


class TestDiffHelmValuesResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_response import (
            DiffHelmValuesResponse,
        )

        report = HelmValuesDiffReport(
            release="payment-service", source_env="staging", target_env="production"
        )
        response = DiffHelmValuesResponse(result=report)

        assert response.result is report
        assert response.result.release == "payment-service"
