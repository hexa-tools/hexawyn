from __future__ import annotations

from unittest.mock import Mock, patch

import pytest
from hexawyn.adapters.secondary.fleet_health_adapter import FleetHealthAdapter
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.domain.models.fleet_health import ClusterRawMetrics


class TestFleetHealthAdapter:
    def test_list_contexts(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.fleet_health_adapter.list_available_contexts",
            return_value=[{"name": "ctx1"}, {"name": "ctx2"}],
        ):
            adapter = FleetHealthAdapter()
            result = adapter.list_contexts()
            assert result == ["ctx1", "ctx2"]

    def test_list_contexts_empty(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.fleet_health_adapter.list_available_contexts",
            return_value=[],
        ):
            adapter = FleetHealthAdapter()
            assert adapter.list_contexts() == []

    def test_get_cluster_raw_metrics_unreachable_kubeconfig(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.fleet_health_adapter.load_kubeconfig",
            side_effect=Exception("no such context"),
        ):
            adapter = FleetHealthAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.get_cluster_raw_metrics("bad-ctx")

    def test_get_cluster_raw_metrics_unreachable_validation(self) -> None:
        mock_api = Mock()
        with (
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter.load_kubeconfig",
                return_value=mock_api,
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter.validate_connection",
                return_value={"status": "disconnected", "error": "timeout"},
            ),
        ):
            adapter = FleetHealthAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.get_cluster_raw_metrics("ctx")

    def test_get_cluster_raw_metrics_connected(self) -> None:
        mock_api = Mock()
        with (
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter.load_kubeconfig",
                return_value=mock_api,
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter.validate_connection",
                return_value={"status": "connected"},
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter._get_node_counts",
                return_value=(10, 0),
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter._get_pod_counts",
                return_value=(100, 99, 1),
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter._get_resource_utilization",
                return_value=(0.5, 0.5),
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter._get_cert_counts",
                return_value=(0, 0),
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter._get_security_violations",
                return_value=0,
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter._get_failing_pipelines",
                return_value=0,
            ),
        ):
            adapter = FleetHealthAdapter()
            result = adapter.get_cluster_raw_metrics("prod-east")
            assert isinstance(result, ClusterRawMetrics)
            assert result.context_name == "prod-east"
            assert result.nodes_total == 10  # noqa: PLR2004
            assert result.nodes_not_ready == 0
            assert result.pods_total == 100  # noqa: PLR2004
            assert result.pods_running == 99  # noqa: PLR2004
            assert result.cpu_utilization == 0.5  # noqa: PLR2004

    def test_get_cluster_raw_metrics_with_prometheus(self) -> None:
        mock_api = Mock()
        with (
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter.load_kubeconfig",
                return_value=mock_api,
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter.validate_connection",
                return_value={"status": "connected"},
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter._get_node_counts",
                return_value=(5, 1),
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter._get_pod_counts",
                return_value=(50, 45, 5),
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter._get_resource_utilization",
                return_value=(0.8, 0.6),
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter._get_cert_counts",
                return_value=(2, 3),
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter._get_security_violations",
                return_value=2,
            ),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter._get_failing_pipelines",
                return_value=0,
            ),
        ):
            adapter = FleetHealthAdapter(prometheus_url="http://prom:9090")
            result = adapter.get_cluster_raw_metrics("prod-east")
            assert result.prometheus_available is True
            assert result.pods_crashloop == 5  # noqa: PLR2004
            assert result.certs_expiring_critical == 2  # noqa: PLR2004
            assert result.certs_expiring_warning == 3  # noqa: PLR2004
            assert result.security_violations == 2  # noqa: PLR2004
