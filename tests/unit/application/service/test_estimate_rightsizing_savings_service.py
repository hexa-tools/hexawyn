"""RED tests — application/service/estimate_rightsizing_savings_service.py"""

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort
from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_command import (
    EstimateRightsizingSavingsCommand,
)
from hexawyn.application.service.estimate_rightsizing_savings_service import (
    EstimateRightsizingSavingsService,
)
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.domain.models.rightsizing import RightsizingType


def _over_workload(name: str = "ml-worker") -> dict[str, object]:
    return {
        "resource_name": name,
        "namespace": "production",
        "kind": "Deployment",
        "cpu_requested_cores": 4.0,
        "memory_requested_mi": 8192.0,
        "cpu_actual_cores": 0.8,
        "memory_actual_mi": 2100.0,
    }


class TestEstimateRightsizingSavingsService:
    def test_returns_over_provisioned_recommendation(self) -> None:
        port = MagicMock(spec=RightsizingPort)
        port.get_workload_rightsizing_data.return_value = [_over_workload()]
        service = EstimateRightsizingSavingsService(rightsizing_port=port)

        response = service.estimate_rightsizing_savings(EstimateRightsizingSavingsCommand())

        assert len(response.report.recommendations) == 1
        assert (
            response.report.recommendations[0].rightsizing_type == RightsizingType.OVER_PROVISIONED
        )

    def test_metrics_server_available_true_when_data_has_actuals(self) -> None:
        port = MagicMock(spec=RightsizingPort)
        port.get_workload_rightsizing_data.return_value = [_over_workload()]
        service = EstimateRightsizingSavingsService(rightsizing_port=port)

        response = service.estimate_rightsizing_savings(EstimateRightsizingSavingsCommand())

        assert response.metrics_server_available is True

    def test_metrics_server_available_false_when_all_actuals_none(self) -> None:
        port = MagicMock(spec=RightsizingPort)
        port.get_workload_rightsizing_data.return_value = [
            {
                "resource_name": "svc",
                "namespace": "ns",
                "kind": "Deployment",
                "cpu_requested_cores": 2.0,
                "memory_requested_mi": 4096.0,
                "cpu_actual_cores": None,
                "memory_actual_mi": None,
            }
        ]
        service = EstimateRightsizingSavingsService(rightsizing_port=port)

        response = service.estimate_rightsizing_savings(EstimateRightsizingSavingsCommand())

        assert response.metrics_server_available is False

    def test_cluster_unreachable_propagates(self) -> None:
        port = MagicMock(spec=RightsizingPort)
        port.get_workload_rightsizing_data.side_effect = ClusterUnreachableError("timeout")
        service = EstimateRightsizingSavingsService(rightsizing_port=port)

        with pytest.raises(ClusterUnreachableError):
            service.estimate_rightsizing_savings(EstimateRightsizingSavingsCommand())

    def test_top_n_passed_to_domain_service(self) -> None:
        port = MagicMock(spec=RightsizingPort)
        port.get_workload_rightsizing_data.return_value = [
            _over_workload(f"svc-{i}") for i in range(10)
        ]
        service = EstimateRightsizingSavingsService(rightsizing_port=port)

        response = service.estimate_rightsizing_savings(EstimateRightsizingSavingsCommand(top_n=2))

        assert len(response.report.recommendations) <= 2

    def test_empty_workloads_returns_empty_recommendations(self) -> None:
        """Real scenario: new cluster with no workloads or Prometheus not scraping yet."""
        port = MagicMock(spec=RightsizingPort)
        port.get_workload_rightsizing_data.return_value = []
        service = EstimateRightsizingSavingsService(rightsizing_port=port)

        response = service.estimate_rightsizing_savings(EstimateRightsizingSavingsCommand())
        assert len(response.report.recommendations) == 0
        assert response.metrics_server_available is False


class TestEstimateRightsizingSavingsServiceEdgeCases:
    def test_top_n_zero_returns_all(self) -> None:
        port = MagicMock(spec=RightsizingPort)
        port.get_workload_rightsizing_data.return_value = [
            _over_workload(f"svc-{i}") for i in range(5)
        ]
        service = EstimateRightsizingSavingsService(rightsizing_port=port)

        response = service.estimate_rightsizing_savings(EstimateRightsizingSavingsCommand(top_n=0))

        assert response.metrics_server_available is True

    def test_runtime_error_propagates(self) -> None:
        port = MagicMock(spec=RightsizingPort)
        port.get_workload_rightsizing_data.side_effect = RuntimeError("Prometheus down")
        service = EstimateRightsizingSavingsService(rightsizing_port=port)

        with pytest.raises(RuntimeError, match="Prometheus down"):
            service.estimate_rightsizing_savings(EstimateRightsizingSavingsCommand())
