from __future__ import annotations


class TestContainerImageDriftResponse:
    def test_defaults(self) -> None:
        from hexawyn.application.ports.driving.container_image_drift.container_image_drift_response import (
            ContainerImageDriftResponse,
        )

        response = ContainerImageDriftResponse()

        assert response.out_of_sync == []
        assert response.in_sync_count == 0
        assert response.excluded_count == 0
        assert response.total_checked == 0
        assert response.summary == ""
        assert response.error is None

    def test_accepts_explicit_values(self) -> None:
        from hexawyn.application.ports.driving.container_image_drift.container_image_drift_response import (
            ContainerImageDriftDict,
            ContainerImageDriftResponse,
        )

        drift: ContainerImageDriftDict = {
            "deployment": "payment-service",
            "namespace": "production",
            "container": "payment-app",
            "running_image": "payment:v1.3-hotfix",
            "declared_image": "payment:v1.2",
            "source_of_truth": "helm-release:payment-chart",
            "drift_type": "tag_mismatch",
            "severity": "critical",
        }
        response = ContainerImageDriftResponse(
            out_of_sync=[drift],
            in_sync_count=38,
            excluded_count=1,
            total_checked=39,
            summary="1 out of sync.",
            error=None,
        )

        assert response.out_of_sync == [drift]
        assert response.in_sync_count == 38
        assert response.excluded_count == 1
        assert response.total_checked == 39
        assert response.summary == "1 out of sync."
