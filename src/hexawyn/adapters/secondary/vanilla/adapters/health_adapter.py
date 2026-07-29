from __future__ import annotations

from hexawyn.adapters.secondary.vanilla.adapters._helpers import (
    conditions,
    items_from,
    text_attr,
)
from hexawyn.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesCoreApi,
)
from hexawyn.application.ports.driven.k8s_port import (
    ClusterHealthPort,
    Finding,
    K8sPort,
    PodInfo,
)

_HEALTHY_POD_STATUSES = {"Running", "Succeeded"}
_RESTART_ALERT_THRESHOLD = 10


class VanillaHealthAdapter(ClusterHealthPort):
    def __init__(self, k8s_port: K8sPort, api: KubernetesCoreApi) -> None:
        self._k8s_port = k8s_port
        self._api = api

    def get_findings(self) -> list[Finding]:
        return [*self._pod_findings(), *self._node_findings()]

    def get_health_score(self) -> int:
        findings = self.get_findings()
        critical_count = self._severity_count(findings, "critical")
        warning_count = self._severity_count(findings, "warning")
        return max(0, 100 - critical_count * 30 - warning_count * 10)

    def get_health_status(self) -> str:
        findings = self.get_findings()
        if self._severity_count(findings, "critical") > 0:
            return "critical"
        if self._severity_count(findings, "warning") > 0:
            return "degraded"
        return "healthy"

    def _pod_findings(self) -> list[Finding]:
        findings: list[Finding] = []
        for pod in self._k8s_port.list_pods():
            if pod["status"] not in _HEALTHY_POD_STATUSES:
                findings.append(self._unhealthy_pod_finding(pod))
            elif pod["restarts"] >= _RESTART_ALERT_THRESHOLD:
                findings.append(self._restarted_pod_finding(pod))
        return findings

    def _node_findings(self) -> list[Finding]:
        findings: list[Finding] = []
        for node in self._node_items():
            if not self._node_is_ready(node):
                findings.append(self._not_ready_node_finding(node))
        return findings

    def _node_items(self) -> list[object]:
        return items_from(self._api.list_node(timeout_seconds=5))

    def _node_is_ready(self, node: object) -> bool:
        node_status = getattr(node, "status", None)
        for condition in conditions(node_status):
            if text_attr(condition, "type", "") == "Ready":
                return text_attr(condition, "status", "False") == "True"
        return False

    def _unhealthy_pod_finding(self, pod: PodInfo) -> Finding:
        return {
            "severity": "critical" if pod["status"] == "CrashLoop" else "warning",
            "message": f"Pod {pod['namespace']}/{pod['name']} is {pod['status']}",
            "remediation": self._pod_remediation(pod["status"]),
        }

    def _restarted_pod_finding(self, pod: PodInfo) -> Finding:
        return {
            "severity": "warning",
            "message": f"Pod {pod['namespace']}/{pod['name']} restarted {pod['restarts']} times",
            "remediation": "Inspect recent logs and events for this pod.",
        }

    def _not_ready_node_finding(self, node: object) -> Finding:
        node_name = text_attr(getattr(node, "metadata", None), "name", "unknown")
        return {
            "severity": "critical",
            "message": f"Node {node_name} is NotReady",
            "remediation": "Inspect node conditions, kubelet status, and recent node events.",
        }

    @staticmethod
    def _pod_remediation(status: str) -> str:
        if status == "CrashLoop":
            return "Inspect container logs, probes, image pull errors, and recent rollout changes."
        if status == "Pending":
            return "Check scheduling events, resource requests, and node capacity."
        return "Inspect pod events and container state for the reported status."

    @staticmethod
    def _severity_count(findings: list[Finding], severity: str) -> int:
        return sum(1 for finding in findings if finding["severity"] == severity)
