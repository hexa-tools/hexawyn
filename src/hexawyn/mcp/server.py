from __future__ import annotations

import os
from typing import TYPE_CHECKING

from fastmcp import FastMCP

from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.infrastructure.config.cache_manager import get_cache_stats
from hexawyn.infrastructure.config.config_manager import get_api_key
from hexawyn.infrastructure.config.kubeconfig_reader import (
    get_active_context,
    load_kubeconfig,
    validate_connection,
)
from hexawyn.infrastructure.memory.duckdb_client import get_connection

if TYPE_CHECKING:
    from hexawyn.application.ports.driven.canary_comparison_port import (
        CanaryComparisonPort,
    )
    from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
    from hexawyn.application.ports.driven.cost_forecast_port import CostForecastPort
    from hexawyn.application.ports.driven.cost_profiling_port import CostProfilingPort
    from hexawyn.application.ports.driven.cost_saving_estimation_port import (
        CostSavingEstimationPort,
    )
    from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
    from hexawyn.application.ports.driven.gitops_port import GitOpsPort
    from hexawyn.application.ports.driven.istio_topology_port import IstioTopologyPort
    from hexawyn.application.ports.driven.k8s_port import K8sPort
    from hexawyn.application.ports.driven.keda_port import KedaPort
    from hexawyn.application.ports.driven.kubernetes_topology_port import KubernetesTopologyPort
    from hexawyn.application.ports.driven.latency_percentile_port import (
        LatencyPercentilePort,
    )
    from hexawyn.application.ports.driven.memory_saturation_port import (
        MemorySaturationPort,
    )
    from hexawyn.application.ports.driven.metric_correlation_port import (
        MetricCorrelationPort,
    )
    from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort
    from hexawyn.application.ports.driven.policy_port import PolicyPort
    from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort
    from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
    from hexawyn.application.ports.driven.span_bottleneck_port import (
        SpanBottleneckPort,
    )
    from hexawyn.application.ports.driven.tekton_port import TektonPort
    from hexawyn.application.ports.driven.topology_snapshot_port import TopologySnapshotPort
    from hexawyn.application.ports.driven.trace_log_correlation_port import (
        TraceLogCorrelationPort,
    )
    from hexawyn.application.ports.driven.what_if_simulation_port import (
        WhatIfSimulationPort,
    )
    from hexawyn.application.ports.driven.zombie_detection_port import ZombieDetectionPort

# Initialize FastMCP server
mcp = FastMCP(
    name="hexawyn",
    version="0.1.0b0",
    instructions="AI-powered Kubernetes diagnostic agent",
)

# ── Startup kubeconfig validation ─────────────────────────
_k8s_api = None
_cluster_status: dict[str, str] = {"status": "not_initialized"}

context_name = "unknown"

try:
    _k8s_api = load_kubeconfig()
    active_ctx = get_active_context()
    context_name = str(active_ctx["name"]) if active_ctx else "unknown"
    _cluster_status = validate_connection(_k8s_api, context_name)
except ClusterUnreachableError as e:
    _cluster_status = {
        "status": "no_kubeconfig",
        "error": str(e),
    }
    print("[hexawyn] \u26a0\ufe0f  No kubeconfig found — starting in degraded mode")


def build_k8s_adapter() -> K8sPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_tekton_adapter() -> TektonPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_rightsizing_adapter() -> RightsizingPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_what_if_simulation_adapter() -> WhatIfSimulationPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_cost_forecast_adapter() -> CostForecastPort:
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


def build_cost_saving_adapter() -> CostSavingEstimationPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def build_fleet_health_adapter() -> FleetHealthPort:
    from hexawyn.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return FleetHealthAdapter(prometheus_url=prometheus_url)


def build_kubernetes_topology_adapter() -> KubernetesTopologyPort:
    from hexawyn.adapters.secondary.kubernetes_topology_adapter import KubernetesTopologyAdapter

    context = context_name if context_name != "unknown" else None
    return KubernetesTopologyAdapter(cluster_name=context or "default")


def build_istio_topology_adapter() -> IstioTopologyPort:
    from hexawyn.adapters.secondary.istio_topology_adapter import IstioTopologyAdapter

    return IstioTopologyAdapter()


def build_gitops_adapter() -> GitOpsPort:
    from hexawyn.adapters.secondary.gitops.gitops_detector import GitOpsDetector

    return GitOpsDetector()


def build_topology_snapshot_adapter() -> TopologySnapshotPort:
    from hexawyn.infrastructure.memory.topology_snapshot_repository import (
        TopologySnapshotRepository,
    )

    return TopologySnapshotRepository(conn=get_connection())


def build_rollouts_adapter() -> RolloutsPort:
    from hexawyn.adapters.secondary.gitops.argo_rollouts_detector import ArgoRolloutsDetector

    return ArgoRolloutsDetector()


def build_policy_adapter() -> PolicyPort:
    from hexawyn.adapters.secondary.gitops.policy_detector import PolicyDetector

    return PolicyDetector()


def build_cert_manager_adapter() -> CertManagerPort:
    from hexawyn.adapters.secondary.gitops.cert_manager_detector import (
        CertManagerDetector,
    )

    return CertManagerDetector()


def build_keda_adapter() -> KedaPort:
    from hexawyn.adapters.secondary.gitops.keda_detector import KedaDetector

    return KedaDetector()


def build_canary_comparison_adapter() -> CanaryComparisonPort:
    from hexawyn.adapters.secondary.gitops.otel_canary_comparison_adapter import (
        OTelCanaryComparisonAdapter,
    )

    return OTelCanaryComparisonAdapter()


def build_cost_profiling_adapter() -> CostProfilingPort:
    from hexawyn.adapters.secondary.gitops.otel_cost_profiling_adapter import (
        OTelCostProfilingAdapter,
    )

    return OTelCostProfilingAdapter()


def build_memory_saturation_adapter() -> MemorySaturationPort:
    from hexawyn.adapters.secondary.gitops.prometheus_memory_adapter import (
        PrometheusMemoryAdapter,
    )

    return PrometheusMemoryAdapter()


def build_span_bottleneck_adapter() -> SpanBottleneckPort:
    from hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter import (
        OTelSpanBreakdownAdapter,
    )

    return OTelSpanBreakdownAdapter()


def build_latency_percentile_adapter() -> LatencyPercentilePort:
    from hexawyn.adapters.secondary.gitops.otel_latency_adapter import (
        OTelPrometheusLatencyAdapter,
    )

    return OTelPrometheusLatencyAdapter()


def build_metric_correlation_adapter() -> MetricCorrelationPort:
    from hexawyn.adapters.secondary.gitops.otel_correlation_adapter import (
        OTelPrometheusCorrelationAdapter,
    )

    return OTelPrometheusCorrelationAdapter()


def build_trace_log_correlation_adapter() -> TraceLogCorrelationPort:
    from hexawyn.adapters.secondary.gitops.otel_trace_log_adapter import (
        OTelTraceLogAdapter,
    )

    return OTelTraceLogAdapter()


def register_tools(server: FastMCP) -> None:
    """Auto-discover and register all MCP tools from mcp/tools/ modules."""
    import importlib
    from pathlib import Path

    tools_dir = Path(__file__).parent / "tools"
    for module_path in sorted(tools_dir.glob("*.py")):
        module_name = module_path.stem
        if module_name.startswith("_"):
            continue
        try:
            mod = importlib.import_module(f"hexawyn.mcp.tools.{module_name}")
            register_fn = getattr(mod, "register", None)
            if callable(register_fn):
                register_fn(server)
        except Exception:
            pass


@mcp.tool()
def health() -> dict[str, str]:
    """
    Health check endpoint — used by Docker, CI, and Marketplace readiness probes.
    Returns status, version, DuckDB connectivity, API key status, and cluster connectivity.
    """
    db_ok = False
    try:
        conn = get_connection()
        conn.execute("SELECT 1").fetchone()
        db_ok = True
    except Exception:
        db_ok = False

    api_key_ok = get_api_key() is not None
    cache_stats = get_cache_stats()
    slack_configured = bool(os.environ.get("HEXAWYN_SLACK_WEBHOOK_URL"))

    return {
        "status": "ok" if db_ok else "degraded",
        "version": "0.1.0b0",
        "duckdb": "connected" if db_ok else "unavailable",
        "api_key": "configured" if api_key_ok else "missing",
        "cluster": _cluster_status.get("status", "unknown"),
        "context": _cluster_status.get("context", "none"),
        "cache_l1_size": str(cache_stats["l1_size"]),
        "cache_l1_ttl": str(cache_stats["l1_ttl_seconds"]),
        "slack": "configured" if slack_configured else "not_configured",
    }


# ── Register all tools ──────────────────────────────────────
register_tools(mcp)


if __name__ == "__main__":  # pragma: no cover
    port = int(os.environ.get("HEXAWYN_PORT", "8000"))
    mcp.run(host="0.0.0.0", port=port)
