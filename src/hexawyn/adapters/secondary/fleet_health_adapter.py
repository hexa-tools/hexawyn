"""FleetHealthAdapter — collects raw metrics per kubeconfig context for fleet health checks."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.domain.models.fleet_health import ClusterRawMetrics
from hexawyn.infrastructure.config.kubeconfig_reader import (
    list_available_contexts,
    load_kubeconfig,
    validate_connection,
)

_K8S_TIMEOUT = 5  # seconds per API call within fleet checks

_TEKTON_GROUP = "tekton.dev"
_TEKTON_VERSION = "v1"
_PIPELINERUNS_PLURAL = "pipelineruns"
_FAILED_STATUSES = {"False"}  # Tekton condition status for failure


class FleetHealthAdapter(FleetHealthPort):
    def __init__(self, prometheus_url: str = "") -> None:
        self._prometheus_url = prometheus_url

    # ── FleetHealthPort ───────────────────────────────────────

    def list_contexts(self) -> list[str]:
        return [ctx["name"] for ctx in list_available_contexts()]

    def get_cluster_raw_metrics(self, context_name: str) -> ClusterRawMetrics:
        try:
            api = load_kubeconfig(context=context_name)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot load kubeconfig for context {context_name!r}",
                context={"error": str(exc)},
            ) from exc

        status = validate_connection(api, context_name)
        if status.get("status") != "connected":
            reason = str(status.get("error", "unknown"))
            raise ClusterUnreachableError(
                f"Cluster {context_name!r} is unreachable: {reason}",
                context={"context": context_name},
            )

        from kubernetes import client as k8s

        nodes_total, nodes_not_ready = _get_node_counts(api)
        pods_total, pods_running, pods_crashloop = _get_pod_counts(api)
        cpu_util, mem_util = _get_resource_utilization(context_name, self._prometheus_url)
        certs_critical, certs_warning = _get_cert_counts(api)
        security_violations = _get_security_violations(api)
        pipelines_failing = _get_failing_pipelines(k8s.CustomObjectsApi())
        prometheus_available = bool(self._prometheus_url) and cpu_util is not None

        return ClusterRawMetrics(
            context_name=context_name,
            nodes_total=nodes_total,
            nodes_not_ready=nodes_not_ready,
            pods_total=pods_total,
            pods_running=pods_running,
            pods_crashloop=pods_crashloop,
            cpu_utilization=cpu_util,
            memory_utilization=mem_util,
            certs_expiring_critical=certs_critical,
            certs_expiring_warning=certs_warning,
            security_violations=security_violations,
            pipelines_failing=pipelines_failing,
            prometheus_available=prometheus_available,
        )


# ── Per-category helpers ──────────────────────────────────────────────────


def _items(api_response: object) -> list[object]:
    return list(getattr(api_response, "items", None) or [])


def _get_node_counts(api: object) -> tuple[int, int]:
    try:
        node_list = getattr(api, "list_node")(timeout_seconds=_K8S_TIMEOUT)
        nodes = _items(node_list)
        not_ready = sum(1 for n in nodes if not _node_ready(n))
        return len(nodes), not_ready
    except Exception:
        return 0, 0


def _node_ready(node: object) -> bool:
    status = getattr(node, "status", None)
    conditions = getattr(status, "conditions", None) or []
    for cond in conditions:
        if getattr(cond, "type", "") == "Ready":
            return str(getattr(cond, "status", "Unknown")) == "True"
    return False


def _get_pod_counts(api: object) -> tuple[int, int, int]:
    try:
        pod_list = getattr(api, "list_pod_for_all_namespaces")(timeout_seconds=_K8S_TIMEOUT)
        pods = _items(pod_list)
        total = len(pods)
        running = sum(1 for p in pods if _pod_phase(p) in {"Running", "Succeeded"})
        crashloop = sum(1 for p in pods if _pod_is_crashloop(p))
        return total, running, crashloop
    except Exception:
        return 0, 0, 0


def _pod_phase(pod: object) -> str:
    status = getattr(pod, "status", None)
    return str(getattr(status, "phase", "Unknown") or "Unknown")


def _pod_is_crashloop(pod: object) -> bool:
    status = getattr(pod, "status", None)
    for cs in getattr(status, "container_statuses", None) or []:
        waiting = getattr(getattr(cs, "state", None), "waiting", None)
        if waiting and getattr(waiting, "reason", "") == "CrashLoopBackOff":
            return True
    return False


def _get_resource_utilization(
    context_name: str, prometheus_url: str
) -> tuple[float | None, float | None]:
    if not prometheus_url:
        return None, None
    try:
        import requests

        def _query(q: str) -> float | None:
            resp = requests.get(
                f"{prometheus_url}/api/v1/query",
                params={"query": q},
                timeout=5,
            )
            resp.raise_for_status()
            result = resp.json().get("data", {}).get("result", [])
            if result:
                return float(result[0]["value"][1])
            return None

        cpu = _query("1 - avg(rate(node_cpu_seconds_total{mode='idle'}[5m]))")
        mem = _query("1 - sum(node_memory_MemAvailable_bytes) / sum(node_memory_MemTotal_bytes)")
        return cpu, mem
    except Exception:
        return None, None


def _get_cert_counts(api: object) -> tuple[int, int]:
    try:
        secret_list = getattr(api, "list_secret_for_all_namespaces")(timeout_seconds=_K8S_TIMEOUT)
        secrets = _items(secret_list)
        now = datetime.now(UTC)
        critical_threshold = now + timedelta(days=7)
        warning_threshold = now + timedelta(days=30)
        critical = 0
        warning = 0
        for secret in secrets:
            if getattr(getattr(secret, "type", ""), "__str__", lambda: "")() != "kubernetes.io/tls":
                if str(getattr(secret, "type", "")) != "kubernetes.io/tls":
                    continue
            data = getattr(secret, "data", None) or {}
            cert_b64 = data.get("tls.crt") if isinstance(data, dict) else None
            if not cert_b64:
                continue
            try:
                import base64

                from cryptography import x509

                cert_bytes = base64.b64decode(cert_b64)
                cert = x509.load_pem_x509_certificate(cert_bytes)
                not_after = cert.not_valid_after_utc
                if not_after <= critical_threshold:
                    critical += 1
                elif not_after <= warning_threshold:
                    warning += 1
            except Exception:
                continue
        return critical, warning
    except Exception:
        return 0, 0


def _get_security_violations(api: object) -> int:
    try:
        pod_list = getattr(api, "list_pod_for_all_namespaces")(timeout_seconds=_K8S_TIMEOUT)
        pods = _items(pod_list)
        count = 0
        for pod in pods:
            spec = getattr(pod, "spec", None)
            for container in getattr(spec, "containers", None) or []:
                sc = getattr(container, "security_context", None)
                if sc and getattr(sc, "privileged", False):
                    count += 1
                    break
        return count
    except Exception:
        return 0


def _get_failing_pipelines(crd_api: object) -> int:
    try:
        raw = getattr(crd_api, "list_cluster_custom_object")(
            group=_TEKTON_GROUP,
            version=_TEKTON_VERSION,
            plural=_PIPELINERUNS_PLURAL,
        )
        items = list((raw or {}).get("items", []) if isinstance(raw, dict) else [])
        failing = 0
        for item in items:
            conditions = (
                (item.get("status") or {}).get("conditions") or [] if isinstance(item, dict) else []
            )
            for cond in conditions:
                if (
                    isinstance(cond, dict)
                    and cond.get("type") == "Succeeded"
                    and cond.get("status") in _FAILED_STATUSES
                ):
                    failing += 1
                    break
        return failing
    except Exception:
        return 0
