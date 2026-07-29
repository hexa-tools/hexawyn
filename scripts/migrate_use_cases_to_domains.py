#!/usr/bin/env python3
"""Migrate use_case/ flat dir → domain subdirectories + update all imports."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path("/home/djepeno/sites/hexawyn")
USE_CASE_DIR = ROOT / "src/hexawyn/application/use_case"

DOMAIN_MAP: dict[str, str] = {
    "certs_challenges_list": "cert_manager",
    "certs_detect": "cert_manager",
    "certs_get": "cert_manager",
    "certs_issuer_get": "cert_manager",
    "certs_issuers_list": "cert_manager",
    "certs_list": "cert_manager",
    "certs_requests_list": "cert_manager",
    "certs_status_explain": "cert_manager",
    "check_cluster_certificate_health": "cert_manager",
    "cluster_certificate_health": "cert_manager",
    "investigate_tls_certificate": "cert_manager",
    "tls_certificate_diagnosis": "cert_manager",
    "check_cluster_operator_health": "cluster",
    "check_disruption_risks": "cluster",
    "check_machine_config_pool_status": "cluster",
    "check_resource_constraints": "cluster",
    "cluster_capacity_ceiling_forecast": "cluster",
    "cluster_headroom_simulation": "cluster",
    "compare_cluster_health": "cluster",
    "diff_cluster_resources": "cluster",
    "get_node_status": "cluster",
    "get_quota_usage": "cluster",
    "global_health_check": "cluster",
    "hot_node_analysis": "cluster",
    "list_namespaces": "cluster",
    "live_topology_mapper": "cluster",
    "resource_constraint": "cluster",
    "resource_yaml": "cluster",
    "run_consolidation": "cluster",
    "run_what_if_simulation": "cluster",
    "search_resources_by_labels": "cluster",
    "plan_spike_provisioning": "cluster",
    "analyze_incident_cost": "finops",
    "compare_service_cost": "finops",
    "compute_budget_intelligence": "finops",
    "compute_monthly_incident_report": "finops",
    "compute_optimization_roi": "finops",
    "compute_prediction_roi": "finops",
    "compute_team_cost": "finops",
    "cost_profiling": "finops",
    "detect_over_provisioned_namespaces": "finops",
    "estimate_cost_saving": "finops",
    "estimate_rightsizing_savings": "finops",
    "forecast_cost": "finops",
    "project_budget": "finops",
    "detect_kustomize_patch_conflicts": "gitops",
    "detect_outdated_helm_releases": "gitops",
    "diff_helm_values": "gitops",
    "gitops_app_get": "gitops",
    "gitops_apps_list": "gitops",
    "gitops_app_status": "gitops",
    "gitops_app_sync": "gitops",
    "gitops_detect": "gitops",
    "gitops_source_get": "gitops",
    "gitops_sources_list": "gitops",
    "manual_change_outside_gitops": "gitops",
    "pod_security_standards_audit": "governance",
    "policy_audit": "governance",
    "policy_detect": "governance",
    "policy_explain_denial": "governance",
    "policy_get": "governance",
    "policy_list": "governance",
    "policy_violations_list": "governance",
    "keda_detect": "keda",
    "keda_scaledjob_get": "keda",
    "keda_scaledjobs_list": "keda",
    "keda_scaledobject_get": "keda",
    "keda_scaledobjects_list": "keda",
    "keda_scaledobject_status": "keda",
    "keda_scaledobject_triggers": "keda",
    "keda_triggerauth_get": "keda",
    "keda_triggerauth_list": "keda",
    "detect_network_segmentation_gaps": "networking",
    "detect_unintended_external_exposure": "networking",
    "east_west_network_segmentation": "networking",
    "unintended_external_exposure": "networking",
    "analyze_pod_logs": "observability",
    "correlate_error_latency_spikes": "observability",
    "deployment_latency": "observability",
    "diagnose_latency_spike": "observability",
    "error_attribution": "observability",
    "etcd_logs": "observability",
    "execute_prometheus_query": "observability",
    "get_p99_latency": "observability",
    "get_pod_logs": "observability",
    "latency_diagnostic": "observability",
    "metric_correlation": "observability",
    "p99_latency": "observability",
    "prometheus_query": "observability",
    "redundant_calls": "observability",
    "semantic_log_search": "observability",
    "service_dependency_graph": "observability",
    "slowest_traces": "observability",
    "span_bottleneck_analysis": "observability",
    "trace_log_correlation": "observability",
    "list_openshift_imagestreams": "openshift",
    "list_openshift_projects": "openshift",
    "list_openshift_routes": "openshift",
    "list_openshift_sccs": "openshift",
    "analyze_failed_pipeline": "pipelines",
    "analysis_runs_list": "pipelines",
    "canary_comparison": "pipelines",
    "get_pipeline_run_status": "pipelines",
    "list_pipeline_runs": "pipelines",
    "list_pipeline_runs_in_namespace": "pipelines",
    "list_task_runs": "pipelines",
    "pipeline_for_service": "pipelines",
    "pipeline_performance_baseline": "pipelines",
    "pipeline_run_logs": "pipelines",
    "pipeline_run_status": "pipelines",
    "trace_pipeline_run_dag": "pipelines",
    "version_regression": "pipelines",
    "admin_endpoint_audit": "security",
    "audit_rbac_permissions": "security",
    "audit_secret_rotation": "security",
    "audit_tls_compliance": "security",
    "check_readiness_liveness_probes": "security",
    "compute_security_posture": "security",
    "configuration_drift_detection": "security",
    "container_image_vulnerability": "security",
    "detect_container_image_drift": "security",
    "detect_missing_probes": "security",
    "detect_privileged_pods": "security",
    "report_critical_vulnerabilities": "security",
    "report_stale_credentials": "security",
    "report_unauthorized_access": "security",
    "scan_container_vulnerabilities": "security",
    "secret_rotation_audit": "security",
    "sensitive_data_audit": "security",
    "adaptive_namespace_investigation": "troubleshooting",
    "advanced_namespace_event_analytics": "troubleshooting",
    "analyze_advanced_namespace_events": "troubleshooting",
    "analyze_critical_namespace_events": "troubleshooting",
    "chat_cli": "troubleshooting",
    "chat_slack": "troubleshooting",
    "conservative_namespace_overview": "troubleshooting",
    "detect_cross_cluster_incident": "troubleshooting",
    "detect_log_anomalies": "troubleshooting",
    "detect_pod_anomalies": "troubleshooting",
    "detect_recurring_incidents": "troubleshooting",
    "detect_zombies": "troubleshooting",
    "generate_incident_triage_report": "troubleshooting",
    "get_namespace_events": "troubleshooting",
    "get_pod_events": "troubleshooting",
    "memory_saturation": "troubleshooting",
    "query_kubearchive": "troubleshooting",
    "summarize_namespace_events": "troubleshooting",
    "trace_k8s_events": "troubleshooting",
    "watch_pod_logs": "troubleshooting",
    "compute_mttr_trend": "workloads",
    "compute_slo_error_budget": "workloads",
    "describe_pod": "workloads",
    "generate_sla_report": "workloads",
    "generate_weekly_reliability_report": "workloads",
    "list_pods": "workloads",
    "report_night_interventions": "workloads",
    "report_platform_reliability": "workloads",
    "rollout_get": "workloads",
    "rollouts_detect": "workloads",
    "rollouts_list": "workloads",
    "rollout_status": "workloads",
    "slo_breach_prediction": "workloads",
}


def main() -> None:
    moved: list[tuple[str, str, str]] = []

    # 1. Create domain directories and move use cases
    for uc_name, domain in DOMAIN_MAP.items():
        src = USE_CASE_DIR / uc_name
        dst_dir = USE_CASE_DIR / domain
        dst = dst_dir / uc_name

        if not src.exists():
            print(f"  SKIP (not found): {uc_name}")
            continue

        dst_dir.mkdir(exist_ok=True)
        (dst_dir / "__init__.py").touch()

        if dst.exists():
            shutil.rmtree(str(dst))
        shutil.move(str(src), str(dst))
        moved.append((uc_name, domain, str(src.relative_to(ROOT))))
        print(f"  MOVED: {uc_name} → {domain}/{uc_name}")

    print(f"\n{len(moved)} use cases moved.\n")

    # 2. Update all imports in the codebase
    python_files = list(ROOT.glob("src/**/*.py")) + \
                   list(ROOT.glob("tests/**/*.py")) + \
                   list(ROOT.glob("datasets/**/*.yaml"))

    old_new: dict[str, str] = {
        f"hexawyn.application.use_case.{uc}": f"hexawyn.application.use_case.{domain}.{uc}"
        for uc, domain in DOMAIN_MAP.items()
    }

    pattern = re.compile(
        r"(hexawyn\.application\.use_case\.)(" + "|".join(map(re.escape, DOMAIN_MAP.keys())) + r")(\.|$|\s)"
    )

    updated = 0
    for py_file in python_files:
        if not py_file.exists() or py_file.is_dir():
            continue
        try:
            content = py_file.read_text(encoding="utf-8")
        except Exception:
            continue

        new_content = content
        for old_str, new_str in old_new.items():
            if old_str in new_content:
                new_content = new_content.replace(old_str, new_str)

        if new_content != content:
            py_file.write_text(new_content, encoding="utf-8")
            updated += 1

    print(f"{updated} files updated with new import paths.\n")

    # 3. Verify no stale references remain
    stale = 0
    for uc_name in DOMAIN_MAP:
        old_path = f"use_case/{uc_name}/"
        for py_file in python_files:
            if not py_file.exists() or py_file.is_dir():
                continue
            try:
                content = py_file.read_text(encoding="utf-8")
            except Exception:
                continue
            if old_path in content:
                print(f"  STALE REF: {py_file.relative_to(ROOT)} — still references {old_path}")
                stale += 1

    if stale == 0:
        print("ZERO stale references found.")
    else:
        print(f"\n{stale} stale references remaining (may need manual fix).")

    print("\nDone. Run: poetry run pytest tests/unit/ -q --tb=short")


if __name__ == "__main__":
    main()
