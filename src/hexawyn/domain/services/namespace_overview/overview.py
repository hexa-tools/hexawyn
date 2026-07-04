from __future__ import annotations

from hexawyn.application.ports.driven.namespace_overview_port import NamespaceOverviewRawData
from hexawyn.domain.models.namespace_overview import (
    NamespaceHealthStatus,
    NamespaceOverviewReport,
    NamespaceOverviewRequest,
    UnhealthyResource,
)
from hexawyn.domain.services.namespace_overview.count_aggregation import aggregate_counts
from hexawyn.domain.services.namespace_overview.health_scoring import (
    build_root_cause,
    classify_deployment,
    compute_health_status,
    is_pod_unhealthy,
)
from hexawyn.domain.services.namespace_overview.token_budget import enforce_token_budget

_KIND_SEVERITY_ORDER = {"Deployment": 0, "Pod": 1}


def build_namespace_overview(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["services_count"])
    namespace_status = raw_data["namespace_status"]

    is_empty = (
        counts.pods_total == 0 and counts.deployments_total == 0 and counts.services_total == 0
    )
    if is_empty:
        return NamespaceOverviewReport(
            namespace=request.namespace,
            namespace_status=namespace_status,
            counts=counts,
            health_status=NamespaceHealthStatus.HEALTHY,
            is_empty=True,
            summary=f"Namespace {request.namespace!r} exists but has no workloads.",
        )

    unhealthy_resources, has_critical, has_degraded = _find_unhealthy_resources(raw_data)
    unhealthy_resources.sort(
        key=lambda resource: (_KIND_SEVERITY_ORDER[resource.kind], resource.name)
    )

    health_status = compute_health_status(has_critical, has_degraded)
    root_cause = build_root_cause(unhealthy_resources)
    warnings = _find_hpa_warnings(raw_data)

    trimmed, has_more, remaining, tokens = enforce_token_budget(
        request.namespace,
        namespace_status,
        counts,
        health_status,
        root_cause,
        unhealthy_resources,
        warnings,
        request.max_tokens,
    )

    return NamespaceOverviewReport(
        namespace=request.namespace,
        namespace_status=namespace_status,
        counts=counts,
        health_status=health_status,
        root_cause=root_cause,
        unhealthy_resources=trimmed,
        warnings=warnings,
        has_more_unhealthy=has_more,
        remaining_unhealthy_count=remaining,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def _find_unhealthy_resources(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(name=pod["name"], kind="Pod", reason=pod["status"])
            )

    for deployment in raw_data["deployments"]:
        classification = classify_deployment(
            deployment["ready_replicas"], deployment["desired_replicas"]
        )
        if classification == "critical":
            has_critical = True
        elif classification == "degraded":
            has_degraded = True
        if classification is not None:
            reason = (
                f"{deployment['ready_replicas']}/{deployment['desired_replicas']} replicas ready"
            )
            unhealthy_resources.append(
                UnhealthyResource(name=deployment["name"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def _find_hpa_warnings(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['current_replicas']}/{hpa['max_replicas']})"
        for hpa in raw_data["hpas"]
        if hpa["current_replicas"] >= hpa["max_replicas"]
    ]


def _build_summary(namespace: str, unhealthy_resources: list[UnhealthyResource]) -> str:
    if not unhealthy_resources:
        return f"Namespace {namespace!r} is healthy."
    return f"{len(unhealthy_resources)} unhealthy resource(s) found in {namespace!r}."
