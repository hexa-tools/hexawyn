from typing import cast

from hexawyn.adapters.secondary.mock.scenarios.aws_eks import AWS_EKS_SCENARIO
from hexawyn.adapters.secondary.mock.scenarios.azure_aks import AZURE_AKS_SCENARIO
from hexawyn.adapters.secondary.mock.scenarios.datadog import DATADOG_SCENARIO
from hexawyn.adapters.secondary.mock.scenarios.gcp_gke import GCP_GKE_SCENARIO
from hexawyn.adapters.secondary.mock.scenarios.openshift import OPENSHIFT_SCENARIO
from hexawyn.application.ports.driven.k8s_port import (
    ClusterContext,
    ClusterMetrics,
    Finding,
    K8sPort,
    PodInfo,
)
from hexawyn.application.ports.driven.logs_port import LogEntry, LogsPort
from hexawyn.application.ports.driven.metrics_port import MetricsPort
from hexawyn.application.ports.driven.traces_port import SlowTrace, TracesPort

SCENARIO_MAP = {
    "aws_eks": AWS_EKS_SCENARIO,
    "azure_aks": AZURE_AKS_SCENARIO,
    "gcp_gke": GCP_GKE_SCENARIO,
    "openshift": OPENSHIFT_SCENARIO,
    "datadog": DATADOG_SCENARIO,
}

_AUGMENTED_PODS: list[PodInfo] = [
    {"name": "api-gateway-9f3b2a-kl7m", "status": "Running", "restarts": 0, "namespace": "production"},
    {"name": "worker-queue-5c8d1e-np4x", "status": "Running", "restarts": 2, "namespace": "production"},
    {"name": "cache-redis-3a7f9b-hq2w", "status": "Running", "restarts": 1, "namespace": "production"},
]


class DemoAdapter(K8sPort, MetricsPort, TracesPort, LogsPort):
    """In-memory demo adapter for testing without a real cluster."""

    def __init__(self, scenario: str = "aws_eks") -> None:
        self.scenario = scenario if scenario in SCENARIO_MAP else "aws_eks"
        self._data: dict[str, object] = SCENARIO_MAP[self.scenario]

    # ── K8sPort ──────────────────────────────────────────

    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        scenario_pods = cast(list[dict[str, str | int]], self._data["pods"])
        pods: list[PodInfo] = [
            {
                "name": str(p["name"]),
                "namespace": str(p.get("namespace", "")),
                "status": str(p["status"]),
                "restarts": int(p.get("restarts", 0)),
            }
            for p in scenario_pods
        ]
        all_pods: list[PodInfo] = pods + _AUGMENTED_PODS
        if namespace:
            return [p for p in all_pods if p["namespace"] == namespace]
        return all_pods

    def get_cluster_metrics(self) -> ClusterMetrics:
        scenario_metrics = cast(dict[str, str | int | float], self._data["metrics"])
        scenario_pods = cast(list[dict[str, str | int]], self._data["pods"])
        return {
            "cpu_usage_pct": float(scenario_metrics.get("cpu_usage_pct", 0)),
            "memory_usage_pct": float(scenario_metrics.get("memory_usage_pct", 0)),
            "node_count": int(scenario_metrics.get("node_count", 0)),
            "pod_count": int(scenario_metrics.get("pod_count", 0)),
            "cpu_utilization": float(scenario_metrics.get("cpu_usage_pct", 0)),
            "memory_utilization": float(scenario_metrics.get("memory_usage_pct", 0)),
            "pods_crashloop": len([p for p in scenario_pods if p["status"] == "CrashLoop"]),
            "p99_latency_ms": int(scenario_metrics.get("p99_latency_ms", 0)),
            "slo_threshold_ms": int(scenario_metrics.get("slo_threshold_ms", 0)),
        }  # type: ignore[typeddict-unknown-key]

    def get_findings(self) -> list[Finding]:
        scenario_findings = cast(list[dict[str, str]], self._data["findings"])
        return [
            {
                "severity": str(f["severity"]),
                "message": str(f["message"]),
                "remediation": str(f["remediation"]),
            }
            for f in scenario_findings
        ]

    def get_health_score(self) -> int:
        health = cast(dict[str, str | int], self._data["health"])
        return int(health["score"])

    def get_health_status(self) -> str:
        health = cast(dict[str, str | int], self._data["health"])
        return str(health["status"])

    def get_cluster_context(self) -> ClusterContext:
        ctx = cast(dict[str, str], self._data["context"])
        return {
            "name": str(ctx.get("name", "")),
            "cluster": str(ctx.get("cluster", "")),
            "provider": str(ctx.get("provider", "")),
            "namespace": str(ctx.get("namespace", "")),
        }

    # ── OpenShift extras ─────────────────────────────────

    def get_suggestion_chips(self) -> list[str]:
        raw_chips = cast(list[str], self._data.get("chips", []))
        return raw_chips

    def get_slack_message(self) -> str:
        return str(self._data.get("slack_message", ""))

    def list_projects(self) -> list[dict[str, str]]:
        raw_projects = cast(list[str], self._data.get("projects", []))
        return [{"name": p} for p in raw_projects]

    def list_routes(self) -> list[dict[str, str | bool]]:
        raw_routes = cast(list[dict[str, str | bool]], self._data.get("routes", []))
        return [
            {"name": str(r.get("name", "")), "tls": bool(r.get("tls", False))}
            for r in raw_routes
        ]

    def list_pipeline_runs(self) -> list[dict[str, str]]:
        raw_runs = cast(list[dict[str, str]], self._data.get("pipeline_runs", []))
        return [
            {"name": str(r.get("name", "")), "status": str(r.get("status", ""))}
            for r in raw_runs
        ]

    # ── Datadog extras ───────────────────────────────────

    def get_triggered_monitors(self) -> list[dict[str, str | int | float]]:
        raw_monitors = cast(list[dict[str, str | int | float]], self._data.get("triggered_monitors", []))
        return [
            {
                "name": str(m["name"]),
                "status": str(m["status"]),
                "value": m["value"],
            }
            for m in raw_monitors
        ]

    def get_apm_services(self) -> list[dict[str, str | int | float]]:
        raw_apm = cast(list[dict[str, str | int | float]], self._data.get("apm_services", []))
        return [
            {
                "service": str(s["service"]),
                "p99_ms": int(s.get("p99_ms", 0)),
                "error_rate": float(s.get("error_rate", 0.0)),
            }
            for s in raw_apm
        ]

    # ── TracesPort ───────────────────────────────────────

    def get_slow_traces(
        self,
        service: str,
        threshold_ms: int,
        time_window_minutes: int,
    ) -> list[SlowTrace]:
        raw_apm = cast(list[dict[str, str | int | float]], self._data.get("apm_services", []))
        traces: list[SlowTrace] = []
        for s in raw_apm:
            p99 = int(s.get("p99_ms", 0))
            if p99 > threshold_ms and s.get("service") == service:
                traces.append(cast(SlowTrace, {
                    "trace_id": f"trace-{service}-mock-001",
                    "service": service,
                    "duration_ms": p99,
                    "is_error": p99 > threshold_ms,
                    "p99_ms": p99,
                }))
        if not traces and service:
            traces.append(cast(SlowTrace, {
                "trace_id": f"trace-{service}-mock-default",
                "service": service,
                "duration_ms": threshold_ms + 100,
                "is_error": True,
                "p99_ms": threshold_ms + 100,
            }))
        return traces

    # ── LogsPort ─────────────────────────────────────────

    def search_logs(
        self,
        pattern: str,
        time_window_minutes: int,
        namespace: str | None = None,
    ) -> list[LogEntry]:
        return [
            {
                "timestamp": "2025-06-20T14:23:05Z",
                "message": f"Mock log matching pattern '{pattern}' in namespace {namespace or 'all'}",
                "severity": "ERROR",
            },
            {
                "timestamp": "2025-06-20T14:22:58Z",
                "message": f"Previous occurrence of '{pattern}' detected in pod logs",
                "severity": "WARN",
            },
        ]
