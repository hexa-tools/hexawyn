from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.headroom_simulation_port import HeadroomSimulationPort
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _node(cpu: str = "4000m", memory: str = "16Gi") -> MagicMock:
    node = MagicMock()
    node.status.allocatable = {"cpu": cpu, "memory": memory}
    return node


def _node_list(*nodes: MagicMock) -> MagicMock:
    node_list = MagicMock()
    node_list.items = list(nodes)
    return node_list


def _deployment(name: str) -> MagicMock:
    deployment = MagicMock()
    deployment.metadata.name = name
    return deployment


def _deployment_list(*names: str) -> MagicMock:
    dep_list = MagicMock()
    dep_list.items = [_deployment(name) for name in names]
    return dep_list


class TestKubernetesHeadroomSimulationAdapterIsPort:
    def test_is_headroom_simulation_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
            KubernetesHeadroomSimulationAdapter,
        )

        assert isinstance(KubernetesHeadroomSimulationAdapter(), HeadroomSimulationPort)


class TestNodeCapacityInfo:
    def test_sums_totals_and_finds_largest_node(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
            KubernetesHeadroomSimulationAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.return_value = _node_list(
            _node(cpu="4000m", memory="16Gi"),
            _node(cpu="8000m", memory="32Gi"),
            _node(cpu="2000m", memory="8Gi"),
        )
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list("coredns")

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
        ):
            adapter = KubernetesHeadroomSimulationAdapter()
            info = adapter.get_node_capacity_info()

        assert info["total_allocatable_cpu_cores"] == pytest.approx(14.0)
        assert info["total_allocatable_memory_gb"] == pytest.approx(56.0)
        assert info["node_count"] == 3
        assert info["largest_node_cpu_cores"] == pytest.approx(8.0)
        assert info["largest_node_memory_gb"] == pytest.approx(32.0)
        assert info["autoscaler_enabled"] is False

    def test_handles_microcore_nanocore_and_bare_numeric_cpu(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
            KubernetesHeadroomSimulationAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.return_value = _node_list(
            _node(cpu="2000000u", memory="1Mi"),
            _node(cpu="2000000000n", memory="1Ki"),
            _node(cpu="2", memory="1073741824"),
        )
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list()

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
        ):
            adapter = KubernetesHeadroomSimulationAdapter()
            info = adapter.get_node_capacity_info()

        assert info["total_allocatable_cpu_cores"] == pytest.approx(6.0)
        assert info["total_allocatable_memory_gb"] == pytest.approx(1.0 + 1 / 1024 + 1 / 1024**2)

    def test_unparseable_values_return_zero(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
            KubernetesHeadroomSimulationAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.return_value = _node_list(_node(cpu="not-a-number", memory="garbage"))
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list()

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
        ):
            adapter = KubernetesHeadroomSimulationAdapter()
            info = adapter.get_node_capacity_info()

        assert info["total_allocatable_cpu_cores"] == 0.0
        assert info["total_allocatable_memory_gb"] == 0.0

    def test_no_nodes_returns_zero_largest(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
            KubernetesHeadroomSimulationAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.return_value = _node_list()
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list()

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
        ):
            adapter = KubernetesHeadroomSimulationAdapter()
            info = adapter.get_node_capacity_info()

        assert info["node_count"] == 0
        assert info["largest_node_cpu_cores"] == 0.0
        assert info["largest_node_memory_gb"] == 0.0


class TestAutoscalerDetection:
    def test_detects_cluster_autoscaler_deployment(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
            KubernetesHeadroomSimulationAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.return_value = _node_list(_node())
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list(
            "coredns", "cluster-autoscaler"
        )

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
        ):
            adapter = KubernetesHeadroomSimulationAdapter()
            info = adapter.get_node_capacity_info()

        assert info["autoscaler_enabled"] is True

    def test_autoscaler_check_failure_defaults_to_false(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
            KubernetesHeadroomSimulationAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.return_value = _node_list(_node())
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.side_effect = Exception("kube-system unreachable")

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
        ):
            adapter = KubernetesHeadroomSimulationAdapter()
            info = adapter.get_node_capacity_info()

        assert info["autoscaler_enabled"] is False


class TestErrorHandling:
    def test_forbidden_translates_to_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
            KubernetesHeadroomSimulationAdapter,
        )

        core_api = MagicMock()
        forbidden = Exception("forbidden")
        forbidden.status = 403  # type: ignore[attr-defined]
        core_api.list_node.side_effect = forbidden

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesHeadroomSimulationAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.get_node_capacity_info()

    def test_other_errors_translate_to_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
            KubernetesHeadroomSimulationAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.side_effect = Exception("connection reset")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesHeadroomSimulationAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.get_node_capacity_info()
