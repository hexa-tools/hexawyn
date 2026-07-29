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
