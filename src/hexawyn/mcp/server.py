from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING

import yaml
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
from hexawyn.mcp.adapters.cluster_adapters import (
    build_canary_comparison_adapter,
    build_capacity_forecast_adapter,
    build_cert_manager_adapter,
    build_cluster_certificate_health_adapter,
    build_cluster_diff_adapter,
    build_cluster_resource_metrics_adapter,
    build_fleet_health_adapter,
    build_headroom_simulation_adapter,
    build_ingress_adapter,
    build_istio_topology_adapter,
    build_k8s_adapter,
    build_keda_adapter,
    build_kubernetes_topology_adapter,
    build_memory_saturation_adapter,
    build_node_analysis_adapter,
    build_pod_metrics_adapter,
    build_policy_adapter,
    build_rightsizing_adapter,
    build_rollouts_adapter,
    build_spike_provisioning_adapter,
    build_tekton_adapter,
    build_topology_snapshot_adapter,
    build_waste_adapter,
    build_what_if_simulation_adapter,
    build_zombie_detection_adapter,
)
from hexawyn.mcp.adapters.finops_adapters import (
    build_budget_intelligence_adapter,
    build_budget_projection_adapter,
    build_cost_adapter,
    build_cost_forecast_adapter,
    build_cost_profiling_adapter,
    build_cost_saving_adapter,
    build_disruption_risk_adapter,
    build_incident_cost_adapter,
    build_monthly_incident_adapter,
    build_mttr_trend_adapter,
    build_night_intervention_adapter,
    build_optimization_roi_adapter,
    build_platform_reliability_adapter,
    build_prediction_roi_adapter,
    build_service_cost_adapter,
    build_sla_report_adapter,
    build_team_cost_adapter,
)
from hexawyn.mcp.adapters.observability_adapters import (
    build_cross_namespace_traffic_adapter,
    build_deployment_latency_comparison_adapter,
    build_error_attribution_adapter,
    build_error_budget_adapter,
    build_latency_percentile_adapter,
    build_log_search_adapter,
    build_metric_correlation_adapter,
    build_metrics_query_adapter,
    build_namespace_events_adapter,
    build_namespace_overview_adapter,
    build_pod_log_watch_adapter,
    build_pod_logs_adapter,
    build_pod_metrics_baseline_adapter,
    build_redundant_call_detection_adapter,
    build_service_dependency_graph_adapter,
    build_slo_breach_prediction_adapter,
    build_slow_trace_search_adapter,
    build_span_bottleneck_adapter,
    build_trace_event_correlation_adapter,
    build_trace_log_correlation_adapter,
    build_trace_query_adapter,
)
from hexawyn.mcp.adapters.security_adapters import (
    build_audit_log_adapter,
    build_compliance_audit_adapter,
    build_critical_cve_adapter,
    build_external_exposure_audit_adapter,
    build_image_drift_adapter,
    build_image_inventory_adapter,
    build_image_vulnerability_scan_adapter,
    build_live_resource_adapter,
    build_network_policy_audit_adapter,
    build_pod_security_adapter,
    build_probe_audit_adapter,
    build_rbac_audit_adapter,
    build_secret_rotation_audit_adapter,
    build_security_audit_adapter,
    build_security_posture_adapter,
    build_stale_credentials_adapter,
    build_tls_compliance_adapter,
    build_unauthorized_access_adapter,
    build_version_regression_adapter,
)

__all__ = [
    "build_audit_log_adapter",
    "build_budget_intelligence_adapter",
    "build_budget_projection_adapter",
    "build_canary_comparison_adapter",
    "build_capacity_forecast_adapter",
    "build_cert_manager_adapter",
    "build_cluster_certificate_health_adapter",
    "build_cluster_diff_adapter",
    "build_cluster_resource_metrics_adapter",
    "build_compliance_audit_adapter",
    "build_cost_adapter",
    "build_cost_forecast_adapter",
    "build_cost_profiling_adapter",
    "build_cost_saving_adapter",
    "build_critical_cve_adapter",
    "build_cross_namespace_traffic_adapter",
    "build_deployment_latency_comparison_adapter",
    "build_disruption_risk_adapter",
    "build_error_attribution_adapter",
    "build_error_budget_adapter",
    "build_external_exposure_audit_adapter",
    "build_fleet_health_adapter",
    "build_headroom_simulation_adapter",
    "build_image_drift_adapter",
    "build_image_inventory_adapter",
    "build_image_vulnerability_scan_adapter",
    "build_incident_cost_adapter",
    "build_ingress_adapter",
    "build_istio_topology_adapter",
    "build_k8s_adapter",
    "build_keda_adapter",
    "build_kubernetes_topology_adapter",
    "build_latency_percentile_adapter",
    "build_live_resource_adapter",
    "build_log_search_adapter",
    "build_memory_saturation_adapter",
    "build_metric_correlation_adapter",
    "build_metrics_query_adapter",
    "build_monthly_incident_adapter",
    "build_mttr_trend_adapter",
    "build_namespace_events_adapter",
    "build_namespace_overview_adapter",
    "build_network_policy_audit_adapter",
    "build_night_intervention_adapter",
    "build_node_analysis_adapter",
    "build_optimization_roi_adapter",
    "build_platform_reliability_adapter",
    "build_pod_logs_adapter",
    "build_pod_log_watch_adapter",
    "build_pod_metrics_adapter",
    "build_pod_metrics_baseline_adapter",
    "build_pod_security_adapter",
    "build_policy_adapter",
    "build_prediction_roi_adapter",
    "build_probe_audit_adapter",
    "build_rbac_audit_adapter",
    "build_redundant_call_detection_adapter",
    "build_rightsizing_adapter",
    "build_rollouts_adapter",
    "build_secret_rotation_audit_adapter",
    "build_security_audit_adapter",
    "build_security_posture_adapter",
    "build_service_cost_adapter",
    "build_service_dependency_graph_adapter",
    "build_sla_report_adapter",
    "build_slo_breach_prediction_adapter",
    "build_slow_trace_search_adapter",
    "build_span_bottleneck_adapter",
    "build_spike_provisioning_adapter",
    "build_stale_credentials_adapter",
    "build_team_cost_adapter",
    "build_tekton_adapter",
    "build_tls_compliance_adapter",
    "build_topology_snapshot_adapter",
    "build_trace_event_correlation_adapter",
    "build_trace_log_correlation_adapter",
    "build_trace_query_adapter",
    "build_unauthorized_access_adapter",
    "build_version_regression_adapter",
    "build_waste_adapter",
    "build_what_if_simulation_adapter",
    "build_zombie_detection_adapter",
]

if TYPE_CHECKING:
    from hexawyn.application.ports.driven.adaptive_investigation_port import (
        AdaptiveInvestigationPort,
    )
    from hexawyn.application.ports.driven.alert_notification_port import (
        AlertNotificationPort,
    )
    from hexawyn.application.ports.driven.certificate_investigation_port import (
        CertificateInvestigationPort,
    )
    from hexawyn.application.ports.driven.cluster_operator_status_port import (
        ClusterOperatorStatusPort,
    )
    from hexawyn.application.ports.driven.consolidation_port import (
        ConsolidationPort,
    )
    from hexawyn.application.ports.driven.cross_cluster_incident_port import (
        CrossClusterIncidentPort,
    )
    from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort
    from hexawyn.application.ports.driven.etcd_logs_port import ETCDLogsPort
    from hexawyn.application.ports.driven.gitops_port import GitOpsPort
    from hexawyn.application.ports.driven.helm_release_version_port import (
        HelmReleaseVersionPort,
    )
    from hexawyn.application.ports.driven.helm_values_diff_port import (
        HelmValuesDiffPort,
    )
    from hexawyn.application.ports.driven.incident_memory_port import IncidentMemoryPort
    from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
        KustomizePatchAnalysisPort,
    )
    from hexawyn.application.ports.driven.machine_config_pool_port import (
        MachineConfigPoolPort,
    )
    from hexawyn.application.ports.driven.openshift_resource_port import (
        OpenShiftResourcePort,
    )
    from hexawyn.application.ports.driven.pipeline_baseline_port import (
        PipelineBaselinePort,
    )
    from hexawyn.application.ports.driven.pipeline_for_service_port import (
        PipelineForServicePort,
    )
    from hexawyn.application.ports.driven.pipeline_run_logs_port import (
        PipelineRunLogsPort,
    )
    from hexawyn.application.ports.driven.plan_port import PlanPort
    from hexawyn.application.ports.driven.recurring_incident_port import (
        RecurringIncidentPort,
    )
    from hexawyn.application.ports.driven.resource_search_port import ResourceSearchPort
    from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort
    from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort
    from hexawyn.application.ports.driven.weekly_reliability_report_port import (
        WeeklyReliabilityReportPort,
    )

_INTENTS_PATH = Path(__file__).parent.parent.parent.parent / "datasets" / "intent_examples.yaml"

# Max sample user-queries appended to each tool description.
EXAMPLES_LIMIT: int = 5

# Initialize FastMCP server
mcp = FastMCP(
    name="hexawyn",
    version="0.1.0b16",
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


def build_gitops_adapter() -> GitOpsPort:
    from hexawyn.adapters.secondary.gitops.gitops_adapter import GitOpsAdapter
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return GitOpsAdapter(VanillaAdapter(cluster_name="default"))


def build_incident_memory_adapter() -> IncidentMemoryPort:
    from hexawyn.infrastructure.memory.incident_memory_repository import (
        IncidentMemoryRepository,
    )

    return IncidentMemoryRepository(conn=get_connection())


def build_cross_cluster_incident_adapter() -> CrossClusterIncidentPort:
    from hexawyn.adapters.secondary.gitops.cross_cluster_incident_adapter import (
        CrossClusterIncidentAdapter,
    )
    from hexawyn.adapters.secondary.gitops.cross_cluster_incident_source import (
        EmptyFailureSignatureSource,
    )

    return CrossClusterIncidentAdapter(source=EmptyFailureSignatureSource())


def build_helm_drift_adapter() -> DriftDetectionPort:
    from hexawyn.adapters.secondary.gitops.helm_drift_adapter import HelmDriftAdapter

    return HelmDriftAdapter()


def build_kustomize_drift_adapter() -> DriftDetectionPort:
    from hexawyn.adapters.secondary.gitops.kustomize_drift_adapter import (
        KustomizeDriftAdapter,
    )

    return KustomizeDriftAdapter()


def build_certificate_investigation_adapter() -> CertificateInvestigationPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_certificate_adapter import (
        KubernetesCertificateAdapter,
    )

    return KubernetesCertificateAdapter()


def build_resource_yaml_adapter() -> ResourceYAMLPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_resource_yaml_adapter import (
        KubernetesResourceYAMLAdapter,
    )

    return KubernetesResourceYAMLAdapter()


def build_pipeline_run_logs_adapter() -> PipelineRunLogsPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_pipeline_run_logs_adapter import (
        KubernetesPipelineRunLogsAdapter,
    )

    return KubernetesPipelineRunLogsAdapter()


def build_etcd_logs_adapter() -> ETCDLogsPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_etcd_logs_adapter import (
        KubernetesETCDLogsAdapter,
    )

    return KubernetesETCDLogsAdapter()


def build_resource_search_adapter() -> ResourceSearchPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
        KubernetesLabelSearchAdapter,
    )

    return KubernetesLabelSearchAdapter()


def build_adaptive_investigation_adapter() -> AdaptiveInvestigationPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
        KubernetesAdaptiveInvestigationAdapter,
    )

    return KubernetesAdaptiveInvestigationAdapter()


def build_alert_notification_adapter() -> AlertNotificationPort:
    from hexawyn.adapters.secondary.slack.slack_alert_adapter import SlackAlertAdapter

    return SlackAlertAdapter()


def build_pipeline_baseline_adapter() -> PipelineBaselinePort:
    from hexawyn.adapters.secondary.tekton_pipeline_baseline_adapter import (
        TektonPipelineBaselineAdapter,
    )

    return TektonPipelineBaselineAdapter()


def build_pipeline_for_service_adapter() -> PipelineForServicePort:
    from hexawyn.adapters.secondary.gitops.kubernetes_pipeline_for_service_adapter import (
        KubernetesPipelineForServiceAdapter,
    )

    return KubernetesPipelineForServiceAdapter()


def build_reliability_report_adapter() -> WeeklyReliabilityReportPort:
    from hexawyn.adapters.secondary.gitops.prometheus_reliability_adapter import (
        PrometheusReliabilityAdapter,
    )

    return PrometheusReliabilityAdapter(metrics_query_port=build_metrics_query_adapter())


def build_helm_release_version_adapter() -> HelmReleaseVersionPort:
    from hexawyn.adapters.secondary.gitops.helm_release_version_adapter import (
        HelmReleaseVersionAdapter,
    )

    return HelmReleaseVersionAdapter()


def build_helm_values_diff_adapter() -> HelmValuesDiffPort:
    from hexawyn.adapters.secondary.gitops.helm_values_adapter import (
        HelmValuesAdapter,
    )

    return HelmValuesAdapter()


def build_kustomize_patch_analysis_adapter() -> KustomizePatchAnalysisPort:
    from hexawyn.adapters.secondary.gitops.kustomize_patch_adapter import (
        KustomizeCLIPatchAdapter,
    )

    return KustomizeCLIPatchAdapter()


def build_recurring_incident_adapter() -> RecurringIncidentPort:
    from hexawyn.adapters.secondary.gitops.recurring_incident_adapter import (
        RecurringIncidentAdapter,
    )

    return RecurringIncidentAdapter()


def build_openshift_resource_adapter() -> OpenShiftResourcePort:
    from hexawyn.adapters.secondary.openshift.openshift_adapter import (
        OpenShiftAdapter,
    )

    return OpenShiftAdapter()  # type: ignore


def build_cluster_operator_status_adapter() -> ClusterOperatorStatusPort:
    from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
        OpenShiftClusterOperatorAdapter,
    )

    return OpenShiftClusterOperatorAdapter()


def build_machine_config_pool_adapter() -> MachineConfigPoolPort:
    from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
        OpenShiftMachineConfigAdapter,
    )

    return OpenShiftMachineConfigAdapter()


def build_pricing_plan_adapter() -> PlanPort:
    from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

    return PricingPlanAdapter()


def build_usage_meter_adapter() -> UsageMeterPort:
    from hexawyn.adapters.secondary.usage_meter_adapter import UsageMeterAdapter

    return UsageMeterAdapter()


def build_consolidation_adapter() -> ConsolidationPort:
    from hexawyn.infrastructure.memory.consolidation_repository import (
        DuckDBConsolidationRepository,
    )

    return DuckDBConsolidationRepository(conn=get_connection())


def build_tool_descriptions() -> dict[str, str]:
    """Load tool descriptions from datasets/intent_examples.yaml.

    Control-plane is the source of truth for tool descriptions; hexawyn keeps a
    synchronized local copy. Each use case maps its MCP `tool` name to a
    `description` used by coding agents to decide when to call it. When several
    use cases target the same tool, the use case whose key matches the tool
    name wins (canonical identity over aliases).
    """
    try:
        data = yaml.safe_load(_INTENTS_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    if not isinstance(data, dict):
        return {}

    descriptions: dict[str, str] = {}
    exact_matches: dict[str, str] = {}
    for use_case, entry in data.items():
        if not isinstance(entry, dict):
            continue
        tool = entry.get("tool")
        description = entry.get("description")
        if not isinstance(tool, str) or not isinstance(description, str) or not description:
            continue
        if use_case == tool:
            exact_matches[tool] = description
        else:
            descriptions.setdefault(tool, description)

    descriptions.update(exact_matches)
    return descriptions


def append_examples_to_description(
    description: str, questions: list[str], limit: int = EXAMPLES_LIMIT
) -> str:
    """Append up to ``limit`` sample user queries to a tool description.

    MCP has no standard ``examples`` field, so the queries are embedded in the
    description — the only text visible to a connecting coding agent via
    ``tools/list``.
    """
    if not questions:
        return description
    block = "\n".join(f"- {question}" for question in questions[:limit])
    return f"{description}\n\nExamples:\n{block}"


def _questions_for_tool(tool: str, data: dict[str, object]) -> list[str]:
    """Sample user queries for a tool, aggregated across its use-case aliases."""
    questions: list[str] = []
    for entry in data.values():
        if not isinstance(entry, dict) or entry.get("tool") != tool:
            continue
        raw = entry.get("questions")
        if isinstance(raw, list):
            questions.extend(q for q in raw if isinstance(q, str))
    return questions


def build_enriched_tool_descriptions() -> dict[str, str]:
    """Tool descriptions padded with up to ``EXAMPLES_LIMIT`` sample queries.

    Coding agents that read the MCP tool list see the description plus a few
    representative user queries, which helps them pick the correct tool. The
    underlying ``intent_examples.yaml`` and the control-plane contract are left
    unchanged.
    """
    try:
        data = yaml.safe_load(_INTENTS_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    if not isinstance(data, dict):
        return {}

    enriched: dict[str, str] = {}
    for tool, description in build_tool_descriptions().items():
        enriched[tool] = append_examples_to_description(
            description, _questions_for_tool(tool, data)
        )
    return enriched


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

    descriptions = build_enriched_tool_descriptions()
    if descriptions:
        import asyncio

        coro = server.list_tools()
        try:
            tools = asyncio.run(coro)
        except RuntimeError:
            coro.close()
            return
        for tool in tools:
            description = descriptions.get(tool.name)
            if description:
                tool.description = description


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
        "version": "0.1.0b16",
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
