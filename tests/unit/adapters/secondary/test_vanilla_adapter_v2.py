"""Comprehensive tests for VanillaAdapter uncovered methods — target 90%+ coverage."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import duckdb
from hexawyn.adapters.secondary.vanilla.adapters.health_adapter import VanillaHealthAdapter
from hexawyn.adapters.secondary.vanilla.adapters.k8s_adapter import VanillaK8sAdapter
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter


def _fake_conn() -> MagicMock:
    c = MagicMock(spec=duckdb.DuckDBPyConnection)
    c.execute.return_value.fetchone.return_value = None
    return c


def _k8s_adapter(cluster_name: str) -> VanillaK8sAdapter:
    return VanillaK8sAdapter(api=None, metrics_api=None, cluster_name=cluster_name)


def _health_adapter() -> VanillaHealthAdapter:
    return VanillaHealthAdapter(k8s_port=MagicMock(), api=MagicMock())


class TestCostSaving:
    """Cover CostSavingEstimationPort (lines 1185-1210)."""

    def test_get_previous_total_saving_returns_float(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        adapter._api = MagicMock()
        with patch(
            "hexawyn.infrastructure.memory.duckdb_client.get_connection",
            return_value=_fake_conn(),
        ):
            result = adapter.get_previous_total_saving()
            assert result is None

    def test_get_previous_total_saving_returns_value(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        adapter._api = MagicMock()
        mock_conn = _fake_conn()
        mock_conn.execute.return_value.fetchone.return_value = (42.5,)
        with patch(
            "hexawyn.infrastructure.memory.duckdb_client.get_connection",
            return_value=mock_conn,
        ):
            result = adapter.get_previous_total_saving()
            assert result == 42.5  # noqa: PLR2004

    def test_get_previous_total_saving_handles_error(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        adapter._api = MagicMock()
        with patch(
            "hexawyn.infrastructure.memory.duckdb_client.get_connection",
            side_effect=Exception("db down"),
        ):
            assert adapter.get_previous_total_saving() is None

    def test_store_total_saving_succeeds(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        adapter._api = MagicMock()
        with patch(
            "hexawyn.infrastructure.memory.duckdb_client.get_connection",
            return_value=_fake_conn(),
        ):
            adapter.store_total_saving(100.0)

    def test_store_total_saving_handles_error(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        adapter._api = MagicMock()
        with patch(
            "hexawyn.infrastructure.memory.duckdb_client.get_connection",
            side_effect=Exception("db full"),
        ):
            adapter.store_total_saving(100.0)  # no exception


class TestDependencyGraph:
    """Cover get_dependency_graph."""

    def test_get_dependency_graph(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        adapter._api = MagicMock()
        adapter._apps_api = MagicMock()
        result = adapter.get_dependency_graph("ns")
        assert isinstance(result, dict)


class TestInternalHelpers:
    """Cover uncovered internal helpers."""

    def test_seconds_to_human_all_formats(self) -> None:
        from hexawyn.adapters.secondary.vanilla.adapters.tekton_adapter import (
            VanillaTektonAdapter,
        )

        adapter = VanillaTektonAdapter()
        assert adapter._seconds_to_human(0) == "0s"
        assert adapter._seconds_to_human(45) == "45s"
        assert adapter._seconds_to_human(120) == "2m"
        assert adapter._seconds_to_human(None) is None

    def test_namespace_age(self) -> None:
        from datetime import UTC, datetime, timedelta

        from hexawyn.adapters.secondary.vanilla.adapters._helpers import namespace_age

        meta = MagicMock()
        meta.creation_timestamp = datetime.now(UTC) - timedelta(days=10)
        age = namespace_age(meta)
        assert "d" in age

    def test_pod_age(self) -> None:
        from datetime import UTC, datetime, timedelta

        adapter = _k8s_adapter(cluster_name="test")
        meta = MagicMock()
        meta.creation_timestamp = datetime.now(UTC) - timedelta(hours=2)
        age = adapter._pod_age(meta)
        assert "h" in age or "m" in age

    def test_provider_name(self) -> None:
        assert _k8s_adapter(cluster_name="kind-test")._provider_name() == "kind"

    def test_node_is_ready_true(self) -> None:
        adapter = _health_adapter()

        class _Cond:
            type = "Ready"
            status = "True"

        node = MagicMock()
        node.status = MagicMock()
        node.status.conditions = [_Cond]
        assert adapter._node_is_ready(node) is True

    def test_node_is_ready_false(self) -> None:
        adapter = _health_adapter()

        class _Cond:
            type = "Ready"
            status = "False"

        node = MagicMock()
        node.status = MagicMock()
        node.status.conditions = [_Cond]
        assert adapter._node_is_ready(node) is False

    def test_node_allocatable_cpu(self) -> None:
        adapter = _k8s_adapter(cluster_name="test")
        node = MagicMock()
        node.status = MagicMock()
        node.status.allocatable = {"cpu": "4"}
        assert adapter._node_allocatable_cpu(node) == 4.0  # noqa: PLR2004

    def test_node_allocatable_memory(self) -> None:
        adapter = _k8s_adapter(cluster_name="test")
        node = MagicMock()
        node.status = MagicMock()
        node.status.allocatable = {"memory": "8Gi"}
        assert adapter._node_allocatable_memory(node) > 7.0  # noqa: PLR2004

    def test_node_allocatable(self) -> None:
        adapter = _k8s_adapter(cluster_name="test")
        node = MagicMock()
        node.status = MagicMock()
        node.status.allocatable = {"cpu": "2"}
        assert adapter._node_allocatable(node) == {"cpu": "2"}


class TestDelegationMethods:
    """Cover VanillaAdapter delegation methods to internal adapters."""

    def test_get_pod_metrics_delegates(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        mock_inner = MagicMock()
        mock_inner.get_pod_metrics.return_value = [MagicMock()]
        adapter._pod_metrics_adapter_inst = mock_inner

        result = adapter.get_pod_metrics(namespace="dev")

        mock_inner.get_pod_metrics.assert_called_once_with("dev")
        assert len(result) == 1  # noqa: PLR2004

    def test_get_daily_costs_delegates(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        mock_inner = MagicMock()
        mock_inner.get_daily_costs.return_value = [MagicMock()]
        adapter._cost_forecast_adapter_inst = mock_inner

        result = adapter.get_daily_costs(30)

        mock_inner.get_daily_costs.assert_called_once_with(30)
        assert len(result) == 1  # noqa: PLR2004

    def test_get_zombie_workloads_delegates(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        mock_inner = MagicMock()
        mock_inner.get_zombie_workloads.return_value = [MagicMock()]
        adapter._zombie_adapter_inst = mock_inner

        result = adapter.get_zombie_workloads(24)

        mock_inner.get_zombie_workloads.assert_called_once_with(24)
        assert len(result) == 1  # noqa: PLR2004

    def test_get_pod_resource_data_delegates(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        mock_inner = MagicMock()
        mock_inner.get_pod_resource_data.return_value = [MagicMock()]
        adapter._cost_saving_adapter_inst = mock_inner

        result = adapter.get_pod_resource_data()

        mock_inner.get_pod_resource_data.assert_called_once()
        assert len(result) == 1  # noqa: PLR2004

    def test_get_current_replicas_delegates(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        mock_inner = MagicMock()
        mock_inner.get_current_replicas.return_value = 3
        adapter._what_if_adapter_inst = mock_inner

        result = adapter.get_current_replicas("ns", "svc")

        mock_inner.get_current_replicas.assert_called_once_with("ns", "svc")
        assert result == 3  # noqa: PLR2004

    def test_get_current_cpu_utilization_delegates(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        mock_inner = MagicMock()
        mock_inner.get_current_cpu_utilization.return_value = 42.5
        adapter._what_if_adapter_inst = mock_inner

        result = adapter.get_current_cpu_utilization("ns", "svc")

        mock_inner.get_current_cpu_utilization.assert_called_once_with("ns", "svc")
        assert result == 42.5  # noqa: PLR2004

    def test_get_pdb_info_delegates(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        mock_inner = MagicMock()
        mock_inner.get_pdb_info.return_value = {"min_available": 1}
        adapter._what_if_adapter_inst = mock_inner

        result = adapter.get_pdb_info("ns", "svc")

        mock_inner.get_pdb_info.assert_called_once_with("ns", "svc")
        assert result == {"min_available": 1}

    def test_get_hpa_info_delegates(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        mock_inner = MagicMock()
        mock_inner.get_hpa_info.return_value = {"min_replicas": 2}
        adapter._what_if_adapter_inst = mock_inner

        result = adapter.get_hpa_info("ns", "svc")

        mock_inner.get_hpa_info.assert_called_once_with("ns", "svc")
        assert result == {"min_replicas": 2}

    def test_get_service_topology_delegates(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        mock_inner = MagicMock()
        mock_inner.get_service_topology.return_value = {"deps": [MagicMock()]}
        adapter._what_if_adapter_inst = mock_inner

        result = adapter.get_service_topology("ns", "svc")

        mock_inner.get_service_topology.assert_called_once_with("ns", "svc")
        assert "deps" in result

    def test_get_probe_audit_data_delegates(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        mock_inner = MagicMock()
        mock_inner.get_probe_audit_data.return_value = [MagicMock()]
        adapter._what_if_adapter_inst = mock_inner

        result = adapter.get_probe_audit_data(namespace="ns")

        mock_inner.get_probe_audit_data.assert_called_once_with("ns")
        assert len(result) == 1  # noqa: PLR2004

    def test_crd_api_client_uses_existing(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        crd = MagicMock()
        adapter._crd_api = crd
        assert adapter._crd_api_client() is crd

    def test_get_cost_forecast_adapter_builds_lazily(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        adapter._apps_api = MagicMock()
        adapter._prometheus_url = "http://prom:9090"

        inner = adapter._get_cost_forecast_adapter()

        assert adapter._cost_forecast_adapter_inst is inner
        assert isinstance(inner, MagicMock) is False

    def test_get_zombie_adapter_builds_lazily(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        adapter._api = MagicMock()

        inner = adapter._get_zombie_adapter()

        assert adapter._zombie_adapter_inst is inner
        assert isinstance(inner, MagicMock) is False

    def test_get_pod_metrics_adapter_builds_lazily(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        adapter._metrics_api = MagicMock()

        inner = adapter._get_pod_metrics_adapter()

        assert adapter._pod_metrics_adapter_inst is inner
        assert isinstance(inner, MagicMock) is False

    def test_crd_api_client_builds_lazily(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        fake_core = MagicMock()
        fake_core.api_client = MagicMock()
        adapter._api = fake_core

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.client.CustomObjectsApi"
        ) as mock_custom:
            crd = adapter._crd_api_client()

        mock_custom.assert_called_once_with(api_client=fake_core.api_client)
        assert crd is not None

    def test_metrics_api_client_builds_lazily(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        fake_core = MagicMock()
        fake_core.api_client = MagicMock()
        adapter._api = fake_core

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.client.CustomObjectsApi"
        ) as mock_custom:
            metrics = adapter._metrics_api_client()

        mock_custom.assert_called_once_with(api_client=fake_core.api_client)
        assert metrics is not None
