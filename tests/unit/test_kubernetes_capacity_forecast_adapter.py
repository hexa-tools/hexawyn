from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.capacity_forecast_port import CapacityForecastPort
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


class TestKubernetesCapacityForecastAdapterIsPort:
    def test_is_capacity_forecast_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
            KubernetesCapacityForecastAdapter,
        )

        assert isinstance(KubernetesCapacityForecastAdapter(), CapacityForecastPort)


class TestAllocatableCapacity:
    def test_sums_allocatable_cpu_and_memory_across_nodes(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
            KubernetesCapacityForecastAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.return_value = _node_list(
            _node(cpu="4000m", memory="16Gi"), _node(cpu="2000m", memory="8Gi")
        )
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list("coredns")

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
        ):
            adapter = KubernetesCapacityForecastAdapter()
            info = adapter.get_cluster_capacity_info()

        assert info["total_allocatable_cpu_cores"] == pytest.approx(6.0)
        assert info["total_allocatable_memory_gb"] == pytest.approx(24.0)
        assert info["autoscaler_enabled"] is False

    def test_handles_nanocore_and_bare_numeric_cpu_units(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
            KubernetesCapacityForecastAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.return_value = _node_list(_node(cpu="2", memory="4Gi"))
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list()

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
        ):
            adapter = KubernetesCapacityForecastAdapter()
            info = adapter.get_cluster_capacity_info()

        assert info["total_allocatable_cpu_cores"] == pytest.approx(2.0)

    def test_handles_microcore_and_nanocore_cpu_suffixes(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
            KubernetesCapacityForecastAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.return_value = _node_list(
            _node(cpu="2000000u", memory="1Mi"), _node(cpu="2000000000n", memory="1Ki")
        )
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list()

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
        ):
            adapter = KubernetesCapacityForecastAdapter()
            info = adapter.get_cluster_capacity_info()

        assert info["total_allocatable_cpu_cores"] == pytest.approx(4.0)

    def test_handles_ti_memory_suffix_and_unparseable_values(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
            KubernetesCapacityForecastAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.return_value = _node_list(
            _node(cpu="not-a-number", memory="1Ti"), _node(cpu="1", memory="1073741824")
        )
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list()

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
        ):
            adapter = KubernetesCapacityForecastAdapter()
            info = adapter.get_cluster_capacity_info()

        assert info["total_allocatable_cpu_cores"] == pytest.approx(1.0)
        assert info["total_allocatable_memory_gb"] == pytest.approx(1025.0)


class TestAutoscalerDetection:
    def test_detects_cluster_autoscaler_deployment(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
            KubernetesCapacityForecastAdapter,
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
            adapter = KubernetesCapacityForecastAdapter()
            info = adapter.get_cluster_capacity_info()

        assert info["autoscaler_enabled"] is True

    def test_autoscaler_check_failure_defaults_to_false(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
            KubernetesCapacityForecastAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.return_value = _node_list(_node())
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.side_effect = Exception("kube-system unreachable")

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
        ):
            adapter = KubernetesCapacityForecastAdapter()
            info = adapter.get_cluster_capacity_info()

        assert info["autoscaler_enabled"] is False


class TestErrorHandling:
    def test_forbidden_translates_to_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
            KubernetesCapacityForecastAdapter,
        )

        core_api = MagicMock()
        forbidden = Exception("forbidden")
        forbidden.status = 403  # type: ignore[attr-defined]
        core_api.list_node.side_effect = forbidden

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesCapacityForecastAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.get_cluster_capacity_info()

    def test_other_errors_translate_to_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
            KubernetesCapacityForecastAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.side_effect = Exception("connection reset")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesCapacityForecastAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.get_cluster_capacity_info()
