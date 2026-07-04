from __future__ import annotations

from typing import Literal

from hexawyn.domain.models.namespace_overview import NamespaceHealthStatus, UnhealthyResource

_UNHEALTHY_POD_STATUSES = frozenset(
    {
        "CrashLoop",
        "CrashLoopBackOff",
        "Error",
        "ImagePullBackOff",
        "Pending",
        "Unknown",
        "Terminating",
        "Failed",
    }
)

DeploymentClassification = Literal["degraded", "critical"]


def is_pod_unhealthy(status: str) -> bool:
    return status in _UNHEALTHY_POD_STATUSES


def classify_deployment(ready: int, desired: int) -> DeploymentClassification | None:
    """A deployment intentionally scaled to 0 (desired=0) is never an issue."""
    if desired == 0:
        return None
    if ready == 0:
        return "critical"
    if ready < desired:
        return "degraded"
    return None


def compute_health_status(has_critical: bool, has_degraded: bool) -> NamespaceHealthStatus:
    if has_critical:
        return NamespaceHealthStatus.CRITICAL
    if has_degraded:
        return NamespaceHealthStatus.DEGRADED
    return NamespaceHealthStatus.HEALTHY


def build_root_cause(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "Deployment"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"
