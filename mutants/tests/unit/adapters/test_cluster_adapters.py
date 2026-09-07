"""Unit tests for mcp/adapters/cluster_adapters.py — every build_*_adapter() function."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.canary_comparison_port import CanaryComparisonPort
from hexawyn.application.ports.driven.capacity_forecast_port import CapacityForecastPort
from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.ports.driven.cluster_certificate_health_port import (
    ClusterCertificateHealthPort,
)
from hexawyn.application.ports.driven.cluster_diff_port import ClusterDiffPort
from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
)
from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
from hexawyn.application.ports.driven.headroom_simulation_port import (
    HeadroomSimulationPort,
)
from hexawyn.application.ports.driven.hot_node_analysis_port import HotNodeAnalysisPort
from hexawyn.application.ports.driven.istio_topology_port import IstioTopologyPort
from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.ports.driven.kubernetes_topology_port import KubernetesTopologyPort
from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort
from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort
from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort
from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.ports.driven.spike_provisioning_port import SpikeProvisioningPort
from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.ports.driven.topology_snapshot_port import TopologySnapshotPort
from hexawyn.application.ports.driven.what_if_simulation_port import WhatIfSimulationPort
from hexawyn.application.ports.driven.zombie_detection_port import ZombieDetectionPort


def _mock_kubeconfig() -> MagicMock:
    return MagicMock()


class TestClusterAdapters:
    """Verify each builder returns the correct port type."""

    def test_build_k8s_adapter_returns_k8s_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import build_k8s_adapter

        result = build_k8s_adapter()
        assert isinstance(result, K8sPort)

    def test_build_tekton_adapter_returns_tekton_port(self) -> None:
        from unittest.mock import patch

        from hexawyn.mcp.adapters.cluster_adapters import build_tekton_adapter

        with patch("hexawyn.mcp.adapters.cluster_adapters.get_connection") as mock_conn:
            result = build_tekton_adapter()
        assert isinstance(result, TektonPort)
        mock_conn.assert_called_once()

    def test_build_rightsizing_adapter_returns_rightsizing_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import build_rightsizing_adapter

        result = build_rightsizing_adapter()
        assert isinstance(result, RightsizingPort)

    def test_build_what_if_simulation_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_what_if_simulation_adapter,
        )

        result = build_what_if_simulation_adapter()
        assert isinstance(result, WhatIfSimulationPort)

    def test_build_waste_adapter_returns_waste_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import build_waste_adapter

        result = build_waste_adapter()
        assert isinstance(result, NamespaceWasteAnalysisPort)

    def test_build_zombie_detection_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_zombie_detection_adapter,
        )

        result = build_zombie_detection_adapter()
        assert isinstance(result, ZombieDetectionPort)

    def test_build_fleet_health_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import build_fleet_health_adapter

        result = build_fleet_health_adapter()
        assert isinstance(result, FleetHealthPort)

    def test_build_cluster_certificate_health_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_cluster_certificate_health_adapter,
        )

        with patch(
            "hexawyn.mcp.adapters.cluster_adapters.load_kubeconfig",
            return_value=MagicMock(),
        ):
            result = build_cluster_certificate_health_adapter()
            assert isinstance(result, ClusterCertificateHealthPort)

    def test_build_kubernetes_topology_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_kubernetes_topology_adapter,
        )

        result = build_kubernetes_topology_adapter()
        assert isinstance(result, KubernetesTopologyPort)

    def test_build_istio_topology_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_istio_topology_adapter,
        )

        result = build_istio_topology_adapter()
        assert isinstance(result, IstioTopologyPort)

    def test_build_topology_snapshot_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_topology_snapshot_adapter,
        )

        with patch(
            "hexawyn.mcp.adapters.cluster_adapters.get_connection",
            return_value=MagicMock(),
        ):
            result = build_topology_snapshot_adapter()
            assert isinstance(result, TopologySnapshotPort)

    def test_build_rollouts_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import build_rollouts_adapter

        result = build_rollouts_adapter()
        assert isinstance(result, RolloutsPort)

    def test_build_policy_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import build_policy_adapter

        result = build_policy_adapter()
        assert isinstance(result, PolicyPort)

    def test_build_cert_manager_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import build_cert_manager_adapter

        result = build_cert_manager_adapter()
        assert isinstance(result, CertManagerPort)

    def test_build_keda_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import build_keda_adapter

        result = build_keda_adapter()
        assert isinstance(result, KedaPort)

    def test_build_canary_comparison_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_canary_comparison_adapter,
        )

        result = build_canary_comparison_adapter()
        assert isinstance(result, CanaryComparisonPort)

    def test_build_memory_saturation_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_memory_saturation_adapter,
        )

        result = build_memory_saturation_adapter()
        assert isinstance(result, MemorySaturationPort)

    def test_build_capacity_forecast_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_capacity_forecast_adapter,
        )

        result = build_capacity_forecast_adapter()
        assert isinstance(result, CapacityForecastPort)

    def test_build_headroom_simulation_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_headroom_simulation_adapter,
        )

        result = build_headroom_simulation_adapter()
        assert isinstance(result, HeadroomSimulationPort)

    def test_build_spike_provisioning_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_spike_provisioning_adapter,
        )

        result = build_spike_provisioning_adapter()
        assert isinstance(result, SpikeProvisioningPort)

    def test_build_node_analysis_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import build_node_analysis_adapter

        result = build_node_analysis_adapter()
        assert isinstance(result, HotNodeAnalysisPort)

    def test_build_cluster_resource_metrics_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.k8s_port import ClusterContext
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_cluster_resource_metrics_adapter,
        )

        vanilla_ctx: ClusterContext = {
            "name": "vanilla",
            "cluster": "test",
            "provider": "vanilla",
            "namespace": "ns",
        }
        with patch(
            "hexawyn.mcp.adapters.cluster_adapters._current_cluster_context",
            return_value=vanilla_ctx,
        ):
            with patch(
                "hexawyn.mcp.adapters.cluster_adapters._is_datadog_enabled",
                return_value=False,
            ):
                with patch(
                    "hexawyn.mcp.adapters.cluster_adapters._is_aws_eks_context",
                    return_value=False,
                ):
                    result = build_cluster_resource_metrics_adapter()
                    assert isinstance(result, ClusterResourceMetricsPort)

    def test_build_cluster_resource_metrics_datadog_branch(self) -> None:
        from hexawyn.application.ports.driven.k8s_port import ClusterContext
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_cluster_resource_metrics_adapter,
        )

        dd_ctx: ClusterContext = {
            "name": "dd-cluster",
            "cluster": "dd",
            "provider": "datadog",
            "namespace": "default",
        }
        with patch(
            "hexawyn.mcp.adapters.cluster_adapters._current_cluster_context",
            return_value=dd_ctx,
        ):
            with patch(
                "hexawyn.mcp.adapters.cluster_adapters._is_datadog_enabled",
                return_value=True,
            ):
                with patch(
                    "hexawyn.infrastructure.config.datadog_config.get_datadog_config",
                    return_value={"key": "k", "app_key": "a", "site": "us1"},
                ):
                    result = build_cluster_resource_metrics_adapter()
                    assert isinstance(result, ClusterResourceMetricsPort)

    def test_build_cluster_resource_metrics_aws_branch(self) -> None:
        from hexawyn.application.ports.driven.k8s_port import ClusterContext
        from hexawyn.mcp.adapters.cluster_adapters import (
            build_cluster_resource_metrics_adapter,
        )

        aws_ctx: ClusterContext = {
            "name": "arn:aws:eks:eu-west-1:123:cluster/prod",
            "cluster": "eks",
            "provider": "aws",
            "namespace": "default",
        }
        with patch(
            "hexawyn.mcp.adapters.cluster_adapters._current_cluster_context",
            return_value=aws_ctx,
        ):
            with patch(
                "hexawyn.mcp.adapters.cluster_adapters._is_datadog_enabled",
                return_value=False,
            ):
                with patch(
                    "hexawyn.mcp.adapters.cluster_adapters._is_aws_eks_context",
                    return_value=True,
                ):
                    result = build_cluster_resource_metrics_adapter()
                    assert isinstance(result, ClusterResourceMetricsPort)

    def test_build_cluster_diff_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.cluster_adapters import build_cluster_diff_adapter

        result = build_cluster_diff_adapter()
        assert isinstance(result, ClusterDiffPort)
