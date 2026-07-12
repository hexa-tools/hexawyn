# hexawyn — MCP Tools Reference

Auto-generated from `tools/list`. 138 tools available.

> ⚠️ This file is auto-generated — do not edit manually.
> Run `python scripts/generate_mcp_docs.py` to regenerate.

---

## Core Operations

### `compare_cluster_health`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "compare_cluster_health",
  "arguments": {}
}
```

---

### `compute_budget_intelligence`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "compute_budget_intelligence",
  "arguments": {}
}
```

---

### `etcd_logs`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "etcd_logs",
  "arguments": {}
}
```

---

### `get_namespace_events`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "get_namespace_events",
  "arguments": {}
}
```

---

### `list_namespaces`

List all Kubernetes namespaces with a quick age overview.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "list_namespaces",
  "arguments": {}
}
```

---

### `list_pods`

List all pods in a namespace with health overview.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "list_pods",
  "arguments": {}
}
```

---

## Observability

### `deployment_latency`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "deployment_latency",
  "arguments": {}
}
```

---

### `detect_container_image_drift`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_container_image_drift",
  "arguments": {}
}
```

---

### `detect_kustomize_patch_conflicts`

Detect conflicting or redundant patches in Kustomize overlays.

Parses a Kustomize overlay directory and identifies fields patched
by multiple patch files with different values (conflicts) or same
values (redundancies).

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_kustomize_patch_conflicts",
  "arguments": {}
}
```

---

### `detect_log_anomalies`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_log_anomalies",
  "arguments": {}
}
```

---

### `detect_manual_changes_outside_gitops`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_manual_changes_outside_gitops",
  "arguments": {}
}
```

---

### `detect_missing_probes`

Find deployments/pods with no liveness or readiness probes.

Scans all workloads across namespaces and identifies those missing
liveness probes, readiness probes, or both. Prioritizes critical
workloads in production with external exposure.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_missing_probes",
  "arguments": {}
}
```

---

### `detect_pod_anomalies`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_pod_anomalies",
  "arguments": {}
}
```

---

### `detect_unintended_external_exposure`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_unintended_external_exposure",
  "arguments": {}
}
```

---

### `global_health_check`

Return a global health overview for all clusters in the kubeconfig.

Analyzes every cluster in parallel. Unreachable clusters are marked as
such and excluded from the aggregate fleet score.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "global_health_check",
  "arguments": {}
}
```

---

### `hot_node_analysis`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "hot_node_analysis",
  "arguments": {}
}
```

---

### `latency_diagnostic`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "latency_diagnostic",
  "arguments": {}
}
```

---

### `memory_saturation`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "memory_saturation",
  "arguments": {}
}
```

---

### `p99_latency`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "p99_latency",
  "arguments": {}
}
```

---

### `prometheus_query`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "prometheus_query",
  "arguments": {}
}
```

---

### `span_bottleneck_analysis`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "span_bottleneck_analysis",
  "arguments": {}
}
```

---

## FinOps

### `compare_service_cost`

Compare infrastructure cost of a service: current month vs previous month.

Computes total CPU + memory cost, provides pod-level breakdown,
and a trend indicator (increasing/decreasing/stable).

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "compare_service_cost",
  "arguments": {}
}
```

---

### `compute_team_cost`

Aggregate cluster resource cost per team.

Maps namespaces to teams via K8s labels, computes CPU/memory/storage
cost per team, ranks from highest to lowest cost, and includes
month-over-month comparison.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "compute_team_cost",
  "arguments": {}
}
```

---

### `cost_profiling`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "cost_profiling",
  "arguments": {}
}
```

---

### `detect_outdated_helm_releases`

Detect Helm releases that are outdated compared to the latest chart version.

Lists all Helm releases with their current version, queries repositories
for the latest version, and computes the version delta (major/minor/patch).

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_outdated_helm_releases",
  "arguments": {}
}
```

---

### `detect_over_provisioned_namespaces`

Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_over_provisioned_namespaces",
  "arguments": {}
}
```

---

### `detect_zombies`

Find pods with zero network traffic — zombie deployments that waste resources.

Identifies pods with 0 RPS/bytes over the analysis window,
classifies risk, and computes wasted CPU/memory.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_zombies",
  "arguments": {}
}
```

---

### `estimate_cost_saving`

Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "estimate_cost_saving",
  "arguments": {}
}
```

---

### `estimate_rightsizing_savings`

Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "estimate_rightsizing_savings",
  "arguments": {}
}
```

---

### `forecast_cost`

Project end-of-month Kubernetes cluster spend based on resource request trends.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "forecast_cost",
  "arguments": {}
}
```

---

### `project_budget`

Project infrastructure cost for the next N months at the current growth.

Returns the projected monthly cost with optimistic / realistic / pessimistic
scenarios, a per-category breakdown (compute / storage / network), the
detected growth model (linear / exponential / decreasing), a confidence
level based on available history, and a budget-threshold alert with the
month the budget is first exceeded.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "project_budget",
  "arguments": {}
}
```

---

## Security

### `admin_endpoint_audit`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "admin_endpoint_audit",
  "arguments": {}
}
```

---

### `audit_rbac_permissions`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "audit_rbac_permissions",
  "arguments": {}
}
```

---

### `audit_secret_rotation`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "audit_secret_rotation",
  "arguments": {}
}
```

---

### `audit_tls_compliance`

Audit services for TLS compliance: expired certs, no TLS, self-signed.

Returns all services with no TLS configured, expired certificates,
or certificates expiring within 30 days, ranked by severity.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "audit_tls_compliance",
  "arguments": {}
}
```

---

### `compute_security_posture`

Compute the overall security compliance posture across all workloads.

Returns the overall compliance score (%), a per-category breakdown (TLS,
RBAC, Pod Security, image scanning, secret rotation), a priority-ordered
remediation list, and the quarter-over-quarter trend when a previous score
is provided. Categories without a defined policy are reported as such —
never silently counted as compliant.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "compute_security_posture",
  "arguments": {}
}
```

---

### `detect_privileged_pods`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_privileged_pods",
  "arguments": {}
}
```

---

### `report_critical_vulnerabilities`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "report_critical_vulnerabilities",
  "arguments": {}
}
```

---

### `report_night_interventions`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "report_night_interventions",
  "arguments": {}
}
```

---

### `report_stale_credentials`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "report_stale_credentials",
  "arguments": {}
}
```

---

### `report_unauthorized_access`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "report_unauthorized_access",
  "arguments": {}
}
```

---

### `scan_container_vulnerabilities`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "scan_container_vulnerabilities",
  "arguments": {}
}
```

---

### `sensitive_data_audit`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "sensitive_data_audit",
  "arguments": {}
}
```

---

## Reliability

### `analyze_incident_cost`

Estimate the business financial impact of an incident.

Returns the affected business service, downtime, revenue impact, support
cost and SLA penalty (each in euros), the number of impacted business
services, and the resolution time. Every euro amount is deterministic and
traceable via ``calculation_basis``. When ``revenue_per_minute`` is not
configured, no euro amount is produced — an explanation is returned instead.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "analyze_incident_cost",
  "arguments": {}
}
```

---

### `compute_monthly_incident_report`

Monthly incident report: count, downtime, severity breakdown, most impacted services.

Returns total incident count and downtime broken down by severity (P1/P2/P3),
most impacted services ranked by downtime, and month-over-month comparison.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "compute_monthly_incident_report",
  "arguments": {}
}
```

---

### `compute_mttr_trend`

Track Mean Time To Recovery (MTTR) trend over the last 3 months.

Returns MTTR per month broken down by severity (P1/P2/P3),
trend indicator (improving/degrading/stable), top 3 slowest incidents,
and benchark comparison against industry standards.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "compute_mttr_trend",
  "arguments": {}
}
```

---

### `compute_slo_error_budget`

Compute SLO error budget burn rate for a service.

Queries Prometheus for actual success rate, computes total error budget,
consumed budget, remaining budget, burn rate multiplier, and time-to-exhaustion.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "compute_slo_error_budget",
  "arguments": {}
}
```

---

### `detect_cross_cluster_incident`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_cross_cluster_incident",
  "arguments": {}
}
```

---

### `detect_recurring_incidents`

Detect services with the most recurring incidents for tech debt prioritization.

Returns top 10 services ranked by incident frequency over the window,
with recurring pattern detection (same root cause >3 times flagged),
average duration, and investment recommendations.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_recurring_incidents",
  "arguments": {}
}
```

---

### `generate_incident_triage_report`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "generate_incident_triage_report",
  "arguments": {}
}
```

---

### `generate_sla_report`

Generate an executive SLA report for a quarter.

Returns per-service uptime vs SLA target, all breaches (date, duration,
impacted users, root-cause reference), mid-quarter proration for services
onboarded late, and the quarter-over-quarter reliability trend. Output is
chart-ready — no raw logs. Warns when incident data is missing rather than
reporting a misleading 100% uptime.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "generate_sla_report",
  "arguments": {}
}
```

---

### `generate_weekly_reliability_report`

Generate a weekly reliability report for all production services.

Queries Prometheus for uptime, error rates, p99 latency, SLO compliance,
and top incidents across the specified window.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "generate_weekly_reliability_report",
  "arguments": {}
}
```

---

### `report_platform_reliability`

Report platform reliability for a period in plain business language.

Returns availability in human terms, the number of incidents by severity,
the average resolution time with its trend vs the previous period, and an
honest financial impact (only when pricing is configured). ``executive_summary``
is a jargon-free, sub-five-sentence summary; ``incidents`` provides the
technical drill-down on demand.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "report_platform_reliability",
  "arguments": {}
}
```

---

### `slo_breach_prediction`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "slo_breach_prediction",
  "arguments": {}
}
```

---

## Capacity

### `cluster_capacity_ceiling_forecast`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "cluster_capacity_ceiling_forecast",
  "arguments": {}
}
```

---

### `cluster_headroom_simulation`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "cluster_headroom_simulation",
  "arguments": {}
}
```

---

### `plan_spike_provisioning`

Plan node provisioning ahead of a traffic spike.

Returns current cluster headroom, the projected peak utilisation under the
traffic multiplier, whether action is needed (or the autoscaler covers it),
the recommended number and type of nodes to add (compute- vs
memory-optimized), and a safe provisioning deadline that accounts for the
cloud provider's node lead time.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "plan_spike_provisioning",
  "arguments": {}
}
```

---

## Network

### `detect_network_segmentation_gaps`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "detect_network_segmentation_gaps",
  "arguments": {}
}
```

---

## Logs

### `analyze_pod_logs`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "analyze_pod_logs",
  "arguments": {}
}
```

---

### `semantic_log_search`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "semantic_log_search",
  "arguments": {}
}
```

---

### `trace_log_correlation`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "trace_log_correlation",
  "arguments": {}
}
```

---

### `watch_pod_logs`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "watch_pod_logs",
  "arguments": {}
}
```

---

## GitOps

### `gitops_app_get`

Get detailed status of a specific GitOps application.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "gitops_app_get",
  "arguments": {}
}
```

---

### `gitops_app_status`

Get sync and health status with last reconciliation timestamp.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "gitops_app_status",
  "arguments": {}
}
```

---

### `gitops_app_sync`

Get the last sync status — read-only, never triggers a sync.

Use `flux reconcile` or Argo CD UI to trigger a sync manually.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "gitops_app_sync",
  "arguments": {}
}
```

---

### `gitops_apps_list`

List all GitOps applications (Flux HelmRelease/Kustomization or ArgoCD Application).

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "gitops_apps_list",
  "arguments": {}
}
```

---

### `gitops_detect`

Detect which GitOps engine (Flux CD or Argo CD) is installed in the cluster.

Returns engine type, version, namespace, and app counts.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "gitops_detect",
  "arguments": {}
}
```

---

### `gitops_source_get`

Get detailed status of a specific GitOps source (GitRepository, HelmRepository, etc.).

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "gitops_source_get",
  "arguments": {}
}
```

---

### `gitops_sources_list`

List all GitOps sources (GitRepository, HelmRepository, Bucket).

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "gitops_sources_list",
  "arguments": {}
}
```

---

## Certificates

### `certs_challenges_list`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "certs_challenges_list",
  "arguments": {}
}
```

---

### `certs_detect`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "certs_detect",
  "arguments": {}
}
```

---

### `certs_get`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "certs_get",
  "arguments": {}
}
```

---

### `certs_issuer_get`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "certs_issuer_get",
  "arguments": {}
}
```

---

### `certs_issuers_list`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "certs_issuers_list",
  "arguments": {}
}
```

---

### `certs_list`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "certs_list",
  "arguments": {}
}
```

---

### `certs_requests_list`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "certs_requests_list",
  "arguments": {}
}
```

---

### `certs_status_explain`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "certs_status_explain",
  "arguments": {}
}
```

---

## Pipelines

### `analyze_failed_pipeline`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "analyze_failed_pipeline",
  "arguments": {}
}
```

---

### `get_pipeline_run_status`

Return a status report for all Tekton PipelineRuns in a namespace.

Aggregates counts by status (Running / Succeeded / Failed / Cancelled),
surfaces the most recent failed run with its failure reason, and identifies
the slowest completed run.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "get_pipeline_run_status",
  "arguments": {}
}
```

---

### `list_pipeline_runs`

List the last N PipelineRuns for a service with success rate, average duration,
fastest/slowest run, and outlier detection (runs exceeding 2x average duration).

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "list_pipeline_runs",
  "arguments": {}
}
```

---

### `list_pipeline_runs_in_namespace`

List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "list_pipeline_runs_in_namespace",
  "arguments": {}
}
```

---

### `list_task_runs`

List all TaskRuns for a given Tekton pipeline with status and step-level detail.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "list_task_runs",
  "arguments": {}
}
```

---

### `pipeline_for_service`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "pipeline_for_service",
  "arguments": {}
}
```

---

### `pipeline_run_logs`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "pipeline_run_logs",
  "arguments": {}
}
```

---

### `trace_pipeline_run_dag`

Trace the full execution DAG of a Tekton PipelineRun.

Returns the PipelineRun status, all child TaskRuns with start times,
durations, dependencies, the critical path (longest sequential chain),
and any failed or skipped tasks.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "trace_pipeline_run_dag",
  "arguments": {}
}
```

---

## Policy

### `policy_audit`

Run a global compliance audit with per-namespace breakdown.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "policy_audit",
  "arguments": {}
}
```

---

### `policy_detect`

Detect which policy engine is installed (Kyverno or OPA Gatekeeper).

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "policy_detect",
  "arguments": {}
}
```

---

### `policy_explain_denial`

Explain in natural language why a resource was rejected by the policy engine.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "policy_explain_denial",
  "arguments": {}
}
```

---

### `policy_get`

Get detailed status of a specific policy.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "policy_get",
  "arguments": {}
}
```

---

### `policy_list`

List all policies with action, violations count, and readiness.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "policy_list",
  "arguments": {}
}
```

---

### `policy_violations_list`

List current policy violations with severity and message.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "policy_violations_list",
  "arguments": {}
}
```

---

## Rollouts

### `canary_comparison`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "canary_comparison",
  "arguments": {}
}
```

---

### `rollouts_detect`

Detect if Argo Rollouts is installed in the cluster and return summary counts.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "rollouts_detect",
  "arguments": {}
}
```

---

### `rollouts_list`

List all Argo Rollouts with their strategy and current phase.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "rollouts_list",
  "arguments": {}
}
```

---

## KEDA Autoscaling

### `keda_detect`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "keda_detect",
  "arguments": {}
}
```

---

### `keda_scaledjob_get`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "keda_scaledjob_get",
  "arguments": {}
}
```

---

### `keda_scaledjobs_list`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "keda_scaledjobs_list",
  "arguments": {}
}
```

---

### `keda_scaledobject_get`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "keda_scaledobject_get",
  "arguments": {}
}
```

---

### `keda_scaledobject_status`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "keda_scaledobject_status",
  "arguments": {}
}
```

---

### `keda_scaledobject_triggers`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "keda_scaledobject_triggers",
  "arguments": {}
}
```

---

### `keda_scaledobjects_list`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "keda_scaledobjects_list",
  "arguments": {}
}
```

---

### `keda_triggerauth_get`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "keda_triggerauth_get",
  "arguments": {}
}
```

---

### `keda_triggerauth_list`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "keda_triggerauth_list",
  "arguments": {}
}
```

---

## Drift / Config

### `configuration_drift_detection`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "configuration_drift_detection",
  "arguments": {}
}
```

---

### `diff_cluster_resources`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "diff_cluster_resources",
  "arguments": {}
}
```

---

### `diff_helm_values`

Diff the effective Helm values of a release between two environments.

Retrieves the effective values (helm get values -a) for the release in the
source and target namespaces, computes a structured diff grouped by impact
(critical / warning / informational), redacts secret values, flags type
mismatches, and suggests which differences could explain behaviour gaps.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "diff_helm_values",
  "arguments": {}
}
```

---

## Custom Tools

### `custom_tool_describe`

Describe a custom tool: parameters, output schema, transport, endpoint.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "custom_tool_describe",
  "arguments": {}
}
```

---

### `custom_tool_run`

Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "custom_tool_run",
  "arguments": {}
}
```

---

### `custom_tools_list`

List all registered custom tools with transport, endpoint, and description.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "custom_tools_list",
  "arguments": {}
}
```

---

## Other

### `adaptive_namespace_investigation`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "adaptive_namespace_investigation",
  "arguments": {}
}
```

---

### `advanced_namespace_event_analytics`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "advanced_namespace_event_analytics",
  "arguments": {}
}
```

---

### `analysis_runs_list`

List AnalysisRuns, optionally filtered by rollout name.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "analysis_runs_list",
  "arguments": {}
}
```

---

### `analyze_critical_namespace_events`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "analyze_critical_namespace_events",
  "arguments": {}
}
```

---

### `check_cluster_certificate_health`

Return a full TLS certificate health report for all namespaces in the cluster.

Scans every TLS secret across all namespaces, computes expiry dates, maps each
certificate to the ingresses that reference it, and returns a sorted report:
critical (≤7d), warning (≤30d), healthy (>30d), expired (<0d).

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "check_cluster_certificate_health",
  "arguments": {}
}
```

---

### `check_cluster_operator_health`

Check the health of all OpenShift ClusterOperators.

Lists every ClusterOperator with its Available/Progressing/Degraded
conditions, highlights Degraded and Progressing operators with their
root-cause message, flags operators degraded for more than 15 minutes as
chronic, and returns a summary (total, healthy, degraded, progressing).

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "check_cluster_operator_health",
  "arguments": {}
}
```

---

### `check_disruption_risks`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "check_disruption_risks",
  "arguments": {}
}
```

---

### `check_machine_config_pool_status`

Report the status of all OpenShift MachineConfigPools.

Lists every MachineConfigPool with its derived state (ready, updating,
degraded, degraded+updating, paused), the machine counts, the current vs
desired MachineConfig, the degraded machine count and reason, flags pools
stuck updating for more than 30 minutes, and returns a summary (total,
healthy, degraded, updating, paused).

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "check_machine_config_pool_status",
  "arguments": {}
}
```

---

### `check_resource_constraints`

Return a resource pressure report for all pods in a namespace.

Identifies containers throttled on CPU (usage > cpu_threshold_pct of limit)
and at OOMKill risk (memory usage > memory_threshold_pct of limit).
Sorted CRITICAL first.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "check_resource_constraints",
  "arguments": {}
}
```

---

### `compute_optimization_roi`

Measure the ROI of an optimization sprint.

Returns cost before and after the sprint, monthly and projected annual
savings, the highest-impact optimizations, and the performance impact
(flagging any cost/performance trade-off). Savings are normalized against
traffic growth. When no pre-sprint baseline exists, returns guidance to
establish one first rather than a misleading zero.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "compute_optimization_roi",
  "arguments": {}
}
```

---

### `compute_prediction_roi`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "compute_prediction_roi",
  "arguments": {}
}
```

---

### `conservative_namespace_overview`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "conservative_namespace_overview",
  "arguments": {}
}
```

---

### `error_attribution`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "error_attribution",
  "arguments": {}
}
```

---

### `health`

Health check endpoint — used by Docker, CI, and Marketplace readiness probes.
Returns status, version, DuckDB connectivity, API key status, and cluster connectivity.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "health",
  "arguments": {}
}
```

---

### `live_topology_mapper`

Generate a live dependency map of services running in the cluster.

Discovers all Services, infers caller→callee edges from Istio
VirtualServices (falling back to NetworkPolicies when the mesh is not
installed), flags single points of failure and cycles, and returns a
structured graph ready for Mermaid rendering.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "live_topology_mapper",
  "arguments": {}
}
```

---

### `metric_correlation`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "metric_correlation",
  "arguments": {}
}
```

---

### `query_kubearchive`

Query KubeArchive for the historical state of Kubernetes resources at a given timestamp.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "query_kubearchive",
  "arguments": {}
}
```

---

### `redundant_calls`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "redundant_calls",
  "arguments": {}
}
```

---

### `resource_yaml`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "resource_yaml",
  "arguments": {}
}
```

---

### `rollout_get`

Get detailed status of a specific Argo Rollout with step information.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "rollout_get",
  "arguments": {}
}
```

---

### `rollout_status`

Get real-time status of a Rollout: phase, step, canary weight.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "rollout_status",
  "arguments": {}
}
```

---

### `run_what_if_simulation`

Simulate the impact of scaling a service in the cluster.

**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "run_what_if_simulation",
  "arguments": {}
}
```

---

### `search_resources_by_labels`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "search_resources_by_labels",
  "arguments": {}
}
```

---

### `service_dependency_graph`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "service_dependency_graph",
  "arguments": {}
}
```

---

### `slowest_traces`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "slowest_traces",
  "arguments": {}
}
```

---

### `summarize_namespace_events`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "summarize_namespace_events",
  "arguments": {}
}
```

---

### `tls_certificate_diagnosis`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "tls_certificate_diagnosis",
  "arguments": {}
}
```

---

### `trace_k8s_events`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "trace_k8s_events",
  "arguments": {}
}
```

---

### `version_regression`



**Parameters:**

No parameters.

**Example:**
```json
{
  "tool": "version_regression",
  "arguments": {}
}
```

---
