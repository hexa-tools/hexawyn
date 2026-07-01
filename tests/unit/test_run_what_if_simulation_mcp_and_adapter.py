from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.what_if_simulation_port import (
    DependentServiceData,
    WhatIfSimulationPort,
)


class TestWhatIfSimulationPort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(WhatIfSimulationPort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            WhatIfSimulationPort()  # type: ignore[abstract]


class TestVanillaAdapterImplementsWhatIfSimulationPort:
    def test_vanilla_adapter_implements_port(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        adapter = VanillaAdapter(cluster_name="test-cluster")
        assert isinstance(adapter, WhatIfSimulationPort)

    def test_get_current_replicas_returns_zero_for_unknown(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        with patch.object(VanillaAdapter, "_apps_api_client") as mock_apps:
            mock_api = MagicMock()
            mock_api.list_deployment_for_all_namespaces.return_value = type(
                "obj", (object,), {"items": []}
            )()
            mock_apps.return_value = mock_api

            adapter = VanillaAdapter(cluster_name="test-cluster")
            result = adapter.get_current_replicas(namespace="ns", service_name="unknown")
            assert result == 0

    def test_get_current_replicas_returns_count_for_match(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        with patch.object(VanillaAdapter, "_apps_api_client") as mock_apps:
            mock_api = MagicMock()

            class FakeMeta:
                namespace = "production"
                name = "auth-service"

            class FakeSpec:
                replicas = 3

            class FakeDep:
                metadata = FakeMeta()
                spec = FakeSpec()

            mock_api.list_deployment_for_all_namespaces.return_value = type(
                "obj", (object,), {"items": [FakeDep()]}
            )()
            mock_apps.return_value = mock_api

            adapter = VanillaAdapter(cluster_name="test-cluster")
            result = adapter.get_current_replicas(
                namespace="production", service_name="auth-service"
            )
            assert result == 3

    def test_get_current_replicas_handles_exception(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        with patch.object(VanillaAdapter, "_apps_api_client", side_effect=RuntimeError("boom")):
            adapter = VanillaAdapter(cluster_name="test-cluster")
            result = adapter.get_current_replicas(namespace="ns", service_name="any")
            assert result == 0

    def test_get_pdb_info_returns_none_when_no_pdb(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        with patch.object(VanillaAdapter, "_api_client") as mock_api_cls:
            mock_api = MagicMock()
            mock_api.list_namespaced_pod_disruption_budget.return_value = type(
                "obj", (object,), {"items": []}
            )()
            mock_api_cls.return_value = mock_api

            adapter = VanillaAdapter(cluster_name="test-cluster")
            result = adapter.get_pdb_info(namespace="ns", service_name="auth")
            assert result is None

    def test_get_pdb_info_returns_data_for_match(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        with patch.object(VanillaAdapter, "_api_client") as mock_api_cls:
            mock_api = MagicMock()

            class FakeMeta:
                name = "auth-service-pdb"

            class FakeSpec:
                min_available = 2

            class FakePdb:
                metadata = FakeMeta()
                spec = FakeSpec()

            mock_api.list_namespaced_pod_disruption_budget.return_value = type(
                "obj", (object,), {"items": [FakePdb()]}
            )()
            mock_api_cls.return_value = mock_api

            adapter = VanillaAdapter(cluster_name="test-cluster")
            result = adapter.get_pdb_info(namespace="ns", service_name="auth-service")
            assert result is not None
            assert result["min_available"] == 2

    def test_get_pdb_info_handles_exception(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        with patch.object(VanillaAdapter, "_api_client", side_effect=RuntimeError("boom")):
            adapter = VanillaAdapter(cluster_name="test-cluster")
            result = adapter.get_pdb_info(namespace="ns", service_name="auth")
            assert result is None

    def test_get_hpa_info_returns_none_when_no_hpa(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        with patch.object(VanillaAdapter, "_api_client") as mock_api_cls:
            mock_api = MagicMock()
            mock_api.list_namespaced_horizontal_pod_autoscaler.return_value = type(
                "obj", (object,), {"items": []}
            )()
            mock_api_cls.return_value = mock_api

            adapter = VanillaAdapter(cluster_name="test-cluster")
            result = adapter.get_hpa_info(namespace="ns", service_name="auth")
            assert result is None

    def test_get_hpa_info_returns_data_for_match(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        with patch("kubernetes.client.AutoscalingV2Api") as mock_auto:
            mock_api = MagicMock()

            class FakeMeta:
                name = "auth-service-hpa"

            class FakeSpec:
                min_replicas = 1
                max_replicas = 5

            class FakeStatus:
                current_replicas = 3

            class FakeHpa:
                metadata = FakeMeta()
                spec = FakeSpec()
                status = FakeStatus()

            mock_api.list_namespaced_horizontal_pod_autoscaler.return_value = type(
                "obj", (object,), {"items": [FakeHpa()]}
            )()
            mock_auto.return_value = mock_api

            adapter = VanillaAdapter(cluster_name="test-cluster")
            result = adapter.get_hpa_info(namespace="ns", service_name="auth-service")
            assert result is not None
            assert result["min_replicas"] == 1
            assert result["max_replicas"] == 5
            assert result["current_replicas"] == 3

    def test_get_hpa_info_handles_exception(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        with patch("kubernetes.client.AutoscalingV2Api", side_effect=RuntimeError("boom")):
            adapter = VanillaAdapter(cluster_name="test-cluster")
            result = adapter.get_hpa_info(namespace="ns", service_name="auth")
            assert result is None

    def test_get_current_cpu_utilization_returns_zero_for_unknown(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        with patch.object(VanillaAdapter, "_apps_api_client") as mock_apps:
            mock_api = MagicMock()
            mock_api.list_deployment_for_all_namespaces.return_value = type(
                "obj", (object,), {"items": []}
            )()
            mock_apps.return_value = mock_api

            adapter = VanillaAdapter(cluster_name="test-cluster")
            result = adapter.get_current_cpu_utilization(namespace="ns", service_name="unknown")
            assert result == 0.0

    def test_get_current_cpu_utilization_with_prometheus(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        adapter = VanillaAdapter(cluster_name="test-cluster", prometheus_url="http://prom:9090")

        with patch("httpx.get") as mock_get:
            mock_resp = MagicMock()
            mock_resp.raise_for_status.return_value = None
            mock_resp.json.return_value = {"data": {"result": [{"value": [1700000000, "62.5"]}]}}
            mock_get.return_value = mock_resp

            result = adapter.get_current_cpu_utilization(
                namespace="ns", service_name="auth-service"
            )
            assert result == 62.5

    def test_get_current_cpu_utilization_prometheus_timeout(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        adapter = VanillaAdapter(cluster_name="test-cluster", prometheus_url="http://prom:9090")

        with patch("httpx.get", side_effect=Exception("timeout")):
            result = adapter.get_current_cpu_utilization(
                namespace="ns", service_name="auth-service"
            )
            assert result == 0.0

    def test_get_service_topology_empty_for_unknown(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        adapter = VanillaAdapter(cluster_name="test-cluster")
        result = adapter.get_service_topology(namespace="ns", service_name="unknown")
        assert result == {}

    def test_get_dependency_graph_empty(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        adapter = VanillaAdapter(cluster_name="test-cluster")
        result = adapter.get_dependency_graph(namespace="ns")
        assert result == {}


class TestMCPToolRunWhatIfSimulation:
    def test_tool_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.run_what_if_simulation import run_what_if_simulation

        with patch(
            "hexawyn.mcp.server.build_what_if_simulation_adapter",
            side_effect=RuntimeError("cluster down"),
        ):
            result = run_what_if_simulation(
                target_service="auth-service",
                namespace="production",
                proposed_replicas=1,
            )
            assert result["error"] is not None
            assert "cluster down" in str(result["error"])

    def test_tool_returns_structured_result(self) -> None:
        from hexawyn.mcp.tools.run_what_if_simulation import run_what_if_simulation

        mock_adapter = MagicMock(spec=WhatIfSimulationPort)
        mock_adapter.get_current_replicas.return_value = 3
        mock_adapter.get_current_cpu_utilization.return_value = 62.0
        mock_adapter.get_service_topology.return_value = {
            "auth-service": [
                DependentServiceData(name="checkout-service", calls_per_second=450),
            ],
        }
        mock_adapter.get_pdb_info.return_value = None
        mock_adapter.get_hpa_info.return_value = None
        mock_adapter.get_dependency_graph.return_value = {}

        with patch(
            "hexawyn.mcp.server.build_what_if_simulation_adapter",
            return_value=mock_adapter,
        ):
            result = run_what_if_simulation(
                target_service="auth-service",
                namespace="production",
                proposed_replicas=1,
            )
            assert result["error"] is None
            assert result["target_service"] == "auth-service"
            assert result["risk"] == "HIGH"
            assert len(result["affected_services"]) == 1

    def test_register_adds_tool(self) -> None:
        from hexawyn.mcp.tools.run_what_if_simulation import register

        mock_mcp = MagicMock()
        decorator = MagicMock()
        mock_mcp.tool.return_value = decorator

        register(mock_mcp)

        mock_mcp.tool.assert_called_once()
        decorator.assert_called_once()


class TestBuildWhatIfSimulationAdapter:
    def test_returns_vanilla_adapter(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
        from hexawyn.mcp.server import build_what_if_simulation_adapter

        adapter = build_what_if_simulation_adapter()
        assert isinstance(adapter, VanillaAdapter)
        assert isinstance(adapter, WhatIfSimulationPort)
