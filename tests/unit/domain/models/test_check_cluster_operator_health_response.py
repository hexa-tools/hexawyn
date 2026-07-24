from hexawyn.domain.models.cluster_operator_health import ClusterOperatorHealthReport


class TestCheckClusterOperatorHealthResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.use_case.check_cluster_operator_health.response import (  # noqa: E501
            CheckClusterOperatorHealthResponse,
        )

        report = ClusterOperatorHealthReport(total=1, healthy=1)
        response = CheckClusterOperatorHealthResponse(result=report)

        assert response.result is report
        assert response.result.total == 1
