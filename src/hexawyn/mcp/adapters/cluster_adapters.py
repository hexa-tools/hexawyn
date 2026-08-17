from __future__ import annotations

import os

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
from hexawyn.application.ports.driven.kubernetes_topology_port import (
    KubernetesTopologyPort,
)
from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort
from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort
from hexawyn.application.ports.driven.pod_metrics_port import PodMetricsPort
from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort
from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.ports.driven.spike_provisioning_port import SpikeProvisioningPort
from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.ports.driven.topology_snapshot_port import TopologySnapshotPort
from hexawyn.application.ports.driven.what_if_simulation_port import WhatIfSimulationPort
from hexawyn.application.ports.driven.zombie_detection_port import ZombieDetectionPort
from hexawyn.infrastructure.config.kubeconfig_reader import load_kubeconfig
from hexawyn.infrastructure.memory.duckdb_client import get_connection
from hexawyn.mcp.providers.detector import (
    _current_cluster_context,
    _is_aws_eks_context,
    _is_datadog_enabled,
    context_name,
)


def build_k8s_adapter() -> K8sPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_tekton_adapter() -> TektonPort:
    from hexawyn.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = VanillaAdapter(cluster_name=context or "default")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def build_rightsizing_adapter() -> RightsizingPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_what_if_simulation_adapter() -> WhatIfSimulationPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_waste_adapter() -> NamespaceWasteAnalysisPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def build_zombie_detection_adapter() -> ZombieDetectionPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_fleet_health_adapter() -> FleetHealthPort:
    from hexawyn.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return FleetHealthAdapter(prometheus_url=prometheus_url)


def build_cluster_certificate_health_adapter() -> ClusterCertificateHealthPort:
    from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
        KubernetesClusterCertificateAdapter,
    )

    api = load_kubeconfig()
    return KubernetesClusterCertificateAdapter(api=api)


def build_kubernetes_topology_adapter() -> KubernetesTopologyPort:
    from hexawyn.adapters.secondary.kubernetes_topology_adapter import (
        KubernetesTopologyAdapter,
    )

    context = context_name if context_name != "unknown" else None
    return KubernetesTopologyAdapter(cluster_name=context or "default")


def build_istio_topology_adapter() -> IstioTopologyPort:
    from hexawyn.adapters.secondary.istio_topology_adapter import IstioTopologyAdapter

    return IstioTopologyAdapter()


def build_topology_snapshot_adapter() -> TopologySnapshotPort:
    from hexawyn.infrastructure.memory.topology_snapshot_repository import (
        TopologySnapshotRepository,
    )

    return TopologySnapshotRepository(conn=get_connection())


def build_rollouts_adapter() -> RolloutsPort:
    from hexawyn.adapters.secondary.gitops.argo_rollouts_detector import (
        ArgoRolloutsDetector,
    )

    return ArgoRolloutsDetector()


def build_policy_adapter() -> PolicyPort:
    from hexawyn.adapters.secondary.gitops.policy_detector import PolicyDetector

    return PolicyDetector()


def build_cert_manager_adapter() -> CertManagerPort:
    from hexawyn.adapters.secondary.gitops.cert_manager_adapter import (
        CertManagerAdapter,
    )
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CertManagerAdapter(VanillaAdapter(cluster_name="default"))


def build_keda_adapter() -> KedaPort:
    from hexawyn.adapters.secondary.gitops.keda_adapter import KedaAdapter
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return KedaAdapter(VanillaAdapter(cluster_name="default"))


def build_canary_comparison_adapter() -> CanaryComparisonPort:
    from hexawyn.adapters.secondary.gitops.otel_canary_comparison_adapter import (
        OTelCanaryComparisonAdapter,
    )

    return OTelCanaryComparisonAdapter()


def build_memory_saturation_adapter() -> MemorySaturationPort:
    from hexawyn.adapters.secondary.gitops.prometheus_memory_adapter import (
        PrometheusMemoryAdapter,
    )

    return PrometheusMemoryAdapter()


def build_capacity_forecast_adapter() -> CapacityForecastPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
        KubernetesCapacityForecastAdapter,
    )

    return KubernetesCapacityForecastAdapter()


def build_headroom_simulation_adapter() -> HeadroomSimulationPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
        KubernetesHeadroomSimulationAdapter,
    )

    return KubernetesHeadroomSimulationAdapter()


def build_spike_provisioning_adapter() -> SpikeProvisioningPort:
    from hexawyn.adapters.secondary.gitops.spike_provisioning_adapter import (
        SpikeProvisioningAdapter,
    )

    return SpikeProvisioningAdapter(
        headroom_port=build_headroom_simulation_adapter(),
        current_cpu_used_cores=0.0,
        current_memory_used_gb=0.0,
    )


def build_node_analysis_adapter() -> HotNodeAnalysisPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
        KubernetesNodeAnalysisAdapter,
    )

    return KubernetesNodeAnalysisAdapter()


def build_cluster_resource_metrics_adapter() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def build_cluster_diff_adapter() -> ClusterDiffPort:
    from hexawyn.adapters.secondary.gitops.cluster_diff_adapter import (
        ClusterDiffAdapter,
    )
    from hexawyn.adapters.secondary.gitops.cluster_diff_source import (
        EmptyClusterInventorySource,
    )

    return ClusterDiffAdapter(source=EmptyClusterInventorySource())


def build_pod_metrics_adapter() -> PodMetricsPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")
