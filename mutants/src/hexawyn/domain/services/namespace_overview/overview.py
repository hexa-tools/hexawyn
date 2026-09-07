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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_namespace_overview__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_namespace_overview__mutmut)
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


def x_build_namespace_overview__mutmut_orig(
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


def x_build_namespace_overview__mutmut_1(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = None
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


def x_build_namespace_overview__mutmut_2(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(None, raw_data["deployments"], raw_data["services_count"])
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


def x_build_namespace_overview__mutmut_3(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], None, raw_data["services_count"])
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


def x_build_namespace_overview__mutmut_4(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], None)
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


def x_build_namespace_overview__mutmut_5(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["deployments"], raw_data["services_count"])
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


def x_build_namespace_overview__mutmut_6(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["services_count"])
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


def x_build_namespace_overview__mutmut_7(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], )
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


def x_build_namespace_overview__mutmut_8(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["XXpodsXX"], raw_data["deployments"], raw_data["services_count"])
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


def x_build_namespace_overview__mutmut_9(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["PODS"], raw_data["deployments"], raw_data["services_count"])
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


def x_build_namespace_overview__mutmut_10(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["XXdeploymentsXX"], raw_data["services_count"])
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


def x_build_namespace_overview__mutmut_11(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["DEPLOYMENTS"], raw_data["services_count"])
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


def x_build_namespace_overview__mutmut_12(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["XXservices_countXX"])
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


def x_build_namespace_overview__mutmut_13(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["SERVICES_COUNT"])
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


def x_build_namespace_overview__mutmut_14(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["services_count"])
    namespace_status = None

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


def x_build_namespace_overview__mutmut_15(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["services_count"])
    namespace_status = raw_data["XXnamespace_statusXX"]

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


def x_build_namespace_overview__mutmut_16(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["services_count"])
    namespace_status = raw_data["NAMESPACE_STATUS"]

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


def x_build_namespace_overview__mutmut_17(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["services_count"])
    namespace_status = raw_data["namespace_status"]

    is_empty = None
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


def x_build_namespace_overview__mutmut_18(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["services_count"])
    namespace_status = raw_data["namespace_status"]

    is_empty = (
        counts.pods_total == 0 and counts.deployments_total == 0 or counts.services_total == 0
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


def x_build_namespace_overview__mutmut_19(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["services_count"])
    namespace_status = raw_data["namespace_status"]

    is_empty = (
        counts.pods_total == 0 or counts.deployments_total == 0 and counts.services_total == 0
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


def x_build_namespace_overview__mutmut_20(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["services_count"])
    namespace_status = raw_data["namespace_status"]

    is_empty = (
        counts.pods_total != 0 and counts.deployments_total == 0 and counts.services_total == 0
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


def x_build_namespace_overview__mutmut_21(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["services_count"])
    namespace_status = raw_data["namespace_status"]

    is_empty = (
        counts.pods_total == 1 and counts.deployments_total == 0 and counts.services_total == 0
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


def x_build_namespace_overview__mutmut_22(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["services_count"])
    namespace_status = raw_data["namespace_status"]

    is_empty = (
        counts.pods_total == 0 and counts.deployments_total != 0 and counts.services_total == 0
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


def x_build_namespace_overview__mutmut_23(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["services_count"])
    namespace_status = raw_data["namespace_status"]

    is_empty = (
        counts.pods_total == 0 and counts.deployments_total == 1 and counts.services_total == 0
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


def x_build_namespace_overview__mutmut_24(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["services_count"])
    namespace_status = raw_data["namespace_status"]

    is_empty = (
        counts.pods_total == 0 and counts.deployments_total == 0 and counts.services_total != 0
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


def x_build_namespace_overview__mutmut_25(
    request: NamespaceOverviewRequest, raw_data: NamespaceOverviewRawData
) -> NamespaceOverviewReport:
    """Composes count aggregation, health scoring, and token-budget
    enforcement into one compact report. Pure domain function — raw_data is
    already fetched through NamespaceOverviewPort.
    """
    counts = aggregate_counts(raw_data["pods"], raw_data["deployments"], raw_data["services_count"])
    namespace_status = raw_data["namespace_status"]

    is_empty = (
        counts.pods_total == 0 and counts.deployments_total == 0 and counts.services_total == 1
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


def x_build_namespace_overview__mutmut_26(
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
            namespace=None,
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


def x_build_namespace_overview__mutmut_27(
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
            namespace_status=None,
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


def x_build_namespace_overview__mutmut_28(
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
            counts=None,
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


def x_build_namespace_overview__mutmut_29(
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
            health_status=None,
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


def x_build_namespace_overview__mutmut_30(
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
            is_empty=None,
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


def x_build_namespace_overview__mutmut_31(
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
            summary=None,
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


def x_build_namespace_overview__mutmut_32(
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


def x_build_namespace_overview__mutmut_33(
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


def x_build_namespace_overview__mutmut_34(
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


def x_build_namespace_overview__mutmut_35(
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


def x_build_namespace_overview__mutmut_36(
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


def x_build_namespace_overview__mutmut_37(
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


def x_build_namespace_overview__mutmut_38(
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
            is_empty=False,
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


def x_build_namespace_overview__mutmut_39(
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

    unhealthy_resources, has_critical, has_degraded = None
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


def x_build_namespace_overview__mutmut_40(
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

    unhealthy_resources, has_critical, has_degraded = _find_unhealthy_resources(None)
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


def x_build_namespace_overview__mutmut_41(
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
        key=None
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


def x_build_namespace_overview__mutmut_42(
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
        key=lambda resource: None
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


def x_build_namespace_overview__mutmut_43(
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

    health_status = None
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


def x_build_namespace_overview__mutmut_44(
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

    health_status = compute_health_status(None, has_degraded)
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


def x_build_namespace_overview__mutmut_45(
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

    health_status = compute_health_status(has_critical, None)
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


def x_build_namespace_overview__mutmut_46(
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

    health_status = compute_health_status(has_degraded)
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


def x_build_namespace_overview__mutmut_47(
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

    health_status = compute_health_status(has_critical, )
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


def x_build_namespace_overview__mutmut_48(
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
    root_cause = None
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


def x_build_namespace_overview__mutmut_49(
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
    root_cause = build_root_cause(None)
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


def x_build_namespace_overview__mutmut_50(
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
    warnings = None

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


def x_build_namespace_overview__mutmut_51(
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
    warnings = _find_hpa_warnings(None)

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


def x_build_namespace_overview__mutmut_52(
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

    trimmed, has_more, remaining, tokens = None

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


def x_build_namespace_overview__mutmut_53(
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
        None,
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


def x_build_namespace_overview__mutmut_54(
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
        None,
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


def x_build_namespace_overview__mutmut_55(
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
        None,
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


def x_build_namespace_overview__mutmut_56(
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
        None,
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


def x_build_namespace_overview__mutmut_57(
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
        None,
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


def x_build_namespace_overview__mutmut_58(
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
        None,
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


def x_build_namespace_overview__mutmut_59(
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
        None,
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


def x_build_namespace_overview__mutmut_60(
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
        None,
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


def x_build_namespace_overview__mutmut_61(
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


def x_build_namespace_overview__mutmut_62(
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


def x_build_namespace_overview__mutmut_63(
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


def x_build_namespace_overview__mutmut_64(
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


def x_build_namespace_overview__mutmut_65(
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


def x_build_namespace_overview__mutmut_66(
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


def x_build_namespace_overview__mutmut_67(
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


def x_build_namespace_overview__mutmut_68(
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


def x_build_namespace_overview__mutmut_69(
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
        namespace=None,
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


def x_build_namespace_overview__mutmut_70(
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
        namespace_status=None,
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


def x_build_namespace_overview__mutmut_71(
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
        counts=None,
        health_status=health_status,
        root_cause=root_cause,
        unhealthy_resources=trimmed,
        warnings=warnings,
        has_more_unhealthy=has_more,
        remaining_unhealthy_count=remaining,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_72(
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
        health_status=None,
        root_cause=root_cause,
        unhealthy_resources=trimmed,
        warnings=warnings,
        has_more_unhealthy=has_more,
        remaining_unhealthy_count=remaining,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_73(
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
        root_cause=None,
        unhealthy_resources=trimmed,
        warnings=warnings,
        has_more_unhealthy=has_more,
        remaining_unhealthy_count=remaining,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_74(
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
        unhealthy_resources=None,
        warnings=warnings,
        has_more_unhealthy=has_more,
        remaining_unhealthy_count=remaining,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_75(
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
        warnings=None,
        has_more_unhealthy=has_more,
        remaining_unhealthy_count=remaining,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_76(
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
        has_more_unhealthy=None,
        remaining_unhealthy_count=remaining,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_77(
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
        remaining_unhealthy_count=None,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_78(
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
        estimated_tokens=None,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_79(
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
        summary=None,
    )


def x_build_namespace_overview__mutmut_80(
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


def x_build_namespace_overview__mutmut_81(
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


def x_build_namespace_overview__mutmut_82(
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
        health_status=health_status,
        root_cause=root_cause,
        unhealthy_resources=trimmed,
        warnings=warnings,
        has_more_unhealthy=has_more,
        remaining_unhealthy_count=remaining,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_83(
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
        root_cause=root_cause,
        unhealthy_resources=trimmed,
        warnings=warnings,
        has_more_unhealthy=has_more,
        remaining_unhealthy_count=remaining,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_84(
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
        unhealthy_resources=trimmed,
        warnings=warnings,
        has_more_unhealthy=has_more,
        remaining_unhealthy_count=remaining,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_85(
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
        warnings=warnings,
        has_more_unhealthy=has_more,
        remaining_unhealthy_count=remaining,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_86(
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
        has_more_unhealthy=has_more,
        remaining_unhealthy_count=remaining,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_87(
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
        remaining_unhealthy_count=remaining,
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_88(
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
        estimated_tokens=tokens,
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_89(
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
        summary=_build_summary(request.namespace, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_90(
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
        )


def x_build_namespace_overview__mutmut_91(
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
        summary=_build_summary(None, unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_92(
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
        summary=_build_summary(request.namespace, None),
    )


def x_build_namespace_overview__mutmut_93(
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
        summary=_build_summary(unhealthy_resources),
    )


def x_build_namespace_overview__mutmut_94(
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
        summary=_build_summary(request.namespace, ),
    )

mutants_x_build_namespace_overview__mutmut['_mutmut_orig'] = x_build_namespace_overview__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_1'] = x_build_namespace_overview__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_2'] = x_build_namespace_overview__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_3'] = x_build_namespace_overview__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_4'] = x_build_namespace_overview__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_5'] = x_build_namespace_overview__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_6'] = x_build_namespace_overview__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_7'] = x_build_namespace_overview__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_8'] = x_build_namespace_overview__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_9'] = x_build_namespace_overview__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_10'] = x_build_namespace_overview__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_11'] = x_build_namespace_overview__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_12'] = x_build_namespace_overview__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_13'] = x_build_namespace_overview__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_14'] = x_build_namespace_overview__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_15'] = x_build_namespace_overview__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_16'] = x_build_namespace_overview__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_17'] = x_build_namespace_overview__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_18'] = x_build_namespace_overview__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_19'] = x_build_namespace_overview__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_20'] = x_build_namespace_overview__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_21'] = x_build_namespace_overview__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_22'] = x_build_namespace_overview__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_23'] = x_build_namespace_overview__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_24'] = x_build_namespace_overview__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_25'] = x_build_namespace_overview__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_26'] = x_build_namespace_overview__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_27'] = x_build_namespace_overview__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_28'] = x_build_namespace_overview__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_29'] = x_build_namespace_overview__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_30'] = x_build_namespace_overview__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_31'] = x_build_namespace_overview__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_32'] = x_build_namespace_overview__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_33'] = x_build_namespace_overview__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_34'] = x_build_namespace_overview__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_35'] = x_build_namespace_overview__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_36'] = x_build_namespace_overview__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_37'] = x_build_namespace_overview__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_38'] = x_build_namespace_overview__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_39'] = x_build_namespace_overview__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_40'] = x_build_namespace_overview__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_41'] = x_build_namespace_overview__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_42'] = x_build_namespace_overview__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_43'] = x_build_namespace_overview__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_44'] = x_build_namespace_overview__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_45'] = x_build_namespace_overview__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_46'] = x_build_namespace_overview__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_47'] = x_build_namespace_overview__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_48'] = x_build_namespace_overview__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_49'] = x_build_namespace_overview__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_50'] = x_build_namespace_overview__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_51'] = x_build_namespace_overview__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_52'] = x_build_namespace_overview__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_53'] = x_build_namespace_overview__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_54'] = x_build_namespace_overview__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_55'] = x_build_namespace_overview__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_56'] = x_build_namespace_overview__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_57'] = x_build_namespace_overview__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_58'] = x_build_namespace_overview__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_59'] = x_build_namespace_overview__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_60'] = x_build_namespace_overview__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_61'] = x_build_namespace_overview__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_62'] = x_build_namespace_overview__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_63'] = x_build_namespace_overview__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_64'] = x_build_namespace_overview__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_65'] = x_build_namespace_overview__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_66'] = x_build_namespace_overview__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_67'] = x_build_namespace_overview__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_68'] = x_build_namespace_overview__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_69'] = x_build_namespace_overview__mutmut_69 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_70'] = x_build_namespace_overview__mutmut_70 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_71'] = x_build_namespace_overview__mutmut_71 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_72'] = x_build_namespace_overview__mutmut_72 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_73'] = x_build_namespace_overview__mutmut_73 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_74'] = x_build_namespace_overview__mutmut_74 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_75'] = x_build_namespace_overview__mutmut_75 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_76'] = x_build_namespace_overview__mutmut_76 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_77'] = x_build_namespace_overview__mutmut_77 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_78'] = x_build_namespace_overview__mutmut_78 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_79'] = x_build_namespace_overview__mutmut_79 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_80'] = x_build_namespace_overview__mutmut_80 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_81'] = x_build_namespace_overview__mutmut_81 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_82'] = x_build_namespace_overview__mutmut_82 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_83'] = x_build_namespace_overview__mutmut_83 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_84'] = x_build_namespace_overview__mutmut_84 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_85'] = x_build_namespace_overview__mutmut_85 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_86'] = x_build_namespace_overview__mutmut_86 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_87'] = x_build_namespace_overview__mutmut_87 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_88'] = x_build_namespace_overview__mutmut_88 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_89'] = x_build_namespace_overview__mutmut_89 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_90'] = x_build_namespace_overview__mutmut_90 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_91'] = x_build_namespace_overview__mutmut_91 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_92'] = x_build_namespace_overview__mutmut_92 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_93'] = x_build_namespace_overview__mutmut_93 # type: ignore # mutmut generated
mutants_x_build_namespace_overview__mutmut['x_build_namespace_overview__mutmut_94'] = x_build_namespace_overview__mutmut_94 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__find_unhealthy_resources__mutmut)
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


def x__find_unhealthy_resources__mutmut_orig(
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


def x__find_unhealthy_resources__mutmut_1(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = None
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


def x__find_unhealthy_resources__mutmut_2(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = None
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


def x__find_unhealthy_resources__mutmut_3(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = True
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


def x__find_unhealthy_resources__mutmut_4(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = None

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


def x__find_unhealthy_resources__mutmut_5(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = True

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


def x__find_unhealthy_resources__mutmut_6(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["XXpodsXX"]:
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


def x__find_unhealthy_resources__mutmut_7(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["PODS"]:
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


def x__find_unhealthy_resources__mutmut_8(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(None):
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


def x__find_unhealthy_resources__mutmut_9(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["XXstatusXX"]):
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


def x__find_unhealthy_resources__mutmut_10(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["STATUS"]):
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


def x__find_unhealthy_resources__mutmut_11(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = None
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


def x__find_unhealthy_resources__mutmut_12(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = False
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


def x__find_unhealthy_resources__mutmut_13(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                None
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


def x__find_unhealthy_resources__mutmut_14(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(name=None, kind="Pod", reason=pod["status"])
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


def x__find_unhealthy_resources__mutmut_15(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(name=pod["name"], kind=None, reason=pod["status"])
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


def x__find_unhealthy_resources__mutmut_16(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(name=pod["name"], kind="Pod", reason=None)
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


def x__find_unhealthy_resources__mutmut_17(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(kind="Pod", reason=pod["status"])
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


def x__find_unhealthy_resources__mutmut_18(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(name=pod["name"], reason=pod["status"])
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


def x__find_unhealthy_resources__mutmut_19(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(name=pod["name"], kind="Pod", )
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


def x__find_unhealthy_resources__mutmut_20(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(name=pod["XXnameXX"], kind="Pod", reason=pod["status"])
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


def x__find_unhealthy_resources__mutmut_21(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(name=pod["NAME"], kind="Pod", reason=pod["status"])
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


def x__find_unhealthy_resources__mutmut_22(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(name=pod["name"], kind="XXPodXX", reason=pod["status"])
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


def x__find_unhealthy_resources__mutmut_23(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(name=pod["name"], kind="pod", reason=pod["status"])
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


def x__find_unhealthy_resources__mutmut_24(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(name=pod["name"], kind="POD", reason=pod["status"])
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


def x__find_unhealthy_resources__mutmut_25(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(name=pod["name"], kind="Pod", reason=pod["XXstatusXX"])
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


def x__find_unhealthy_resources__mutmut_26(
    raw_data: NamespaceOverviewRawData,
) -> tuple[list[UnhealthyResource], bool, bool]:
    unhealthy_resources: list[UnhealthyResource] = []
    has_critical = False
    has_degraded = False

    for pod in raw_data["pods"]:
        if is_pod_unhealthy(pod["status"]):
            has_degraded = True
            unhealthy_resources.append(
                UnhealthyResource(name=pod["name"], kind="Pod", reason=pod["STATUS"])
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


def x__find_unhealthy_resources__mutmut_27(
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

    for deployment in raw_data["XXdeploymentsXX"]:
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


def x__find_unhealthy_resources__mutmut_28(
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

    for deployment in raw_data["DEPLOYMENTS"]:
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


def x__find_unhealthy_resources__mutmut_29(
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
        classification = None
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


def x__find_unhealthy_resources__mutmut_30(
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
            None, deployment["desired_replicas"]
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


def x__find_unhealthy_resources__mutmut_31(
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
            deployment["ready_replicas"], None
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


def x__find_unhealthy_resources__mutmut_32(
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
            deployment["desired_replicas"]
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


def x__find_unhealthy_resources__mutmut_33(
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
            deployment["ready_replicas"], )
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


def x__find_unhealthy_resources__mutmut_34(
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
            deployment["XXready_replicasXX"], deployment["desired_replicas"]
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


def x__find_unhealthy_resources__mutmut_35(
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
            deployment["READY_REPLICAS"], deployment["desired_replicas"]
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


def x__find_unhealthy_resources__mutmut_36(
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
            deployment["ready_replicas"], deployment["XXdesired_replicasXX"]
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


def x__find_unhealthy_resources__mutmut_37(
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
            deployment["ready_replicas"], deployment["DESIRED_REPLICAS"]
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


def x__find_unhealthy_resources__mutmut_38(
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
        if classification != "critical":
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


def x__find_unhealthy_resources__mutmut_39(
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
        if classification == "XXcriticalXX":
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


def x__find_unhealthy_resources__mutmut_40(
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
        if classification == "CRITICAL":
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


def x__find_unhealthy_resources__mutmut_41(
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
            has_critical = None
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


def x__find_unhealthy_resources__mutmut_42(
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
            has_critical = False
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


def x__find_unhealthy_resources__mutmut_43(
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
        elif classification != "degraded":
            has_degraded = True
        if classification is not None:
            reason = (
                f"{deployment['ready_replicas']}/{deployment['desired_replicas']} replicas ready"
            )
            unhealthy_resources.append(
                UnhealthyResource(name=deployment["name"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_44(
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
        elif classification == "XXdegradedXX":
            has_degraded = True
        if classification is not None:
            reason = (
                f"{deployment['ready_replicas']}/{deployment['desired_replicas']} replicas ready"
            )
            unhealthy_resources.append(
                UnhealthyResource(name=deployment["name"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_45(
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
        elif classification == "DEGRADED":
            has_degraded = True
        if classification is not None:
            reason = (
                f"{deployment['ready_replicas']}/{deployment['desired_replicas']} replicas ready"
            )
            unhealthy_resources.append(
                UnhealthyResource(name=deployment["name"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_46(
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
            has_degraded = None
        if classification is not None:
            reason = (
                f"{deployment['ready_replicas']}/{deployment['desired_replicas']} replicas ready"
            )
            unhealthy_resources.append(
                UnhealthyResource(name=deployment["name"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_47(
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
            has_degraded = False
        if classification is not None:
            reason = (
                f"{deployment['ready_replicas']}/{deployment['desired_replicas']} replicas ready"
            )
            unhealthy_resources.append(
                UnhealthyResource(name=deployment["name"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_48(
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
        if classification is None:
            reason = (
                f"{deployment['ready_replicas']}/{deployment['desired_replicas']} replicas ready"
            )
            unhealthy_resources.append(
                UnhealthyResource(name=deployment["name"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_49(
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
            reason = None
            unhealthy_resources.append(
                UnhealthyResource(name=deployment["name"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_50(
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
                f"{deployment['XXready_replicasXX']}/{deployment['desired_replicas']} replicas ready"
            )
            unhealthy_resources.append(
                UnhealthyResource(name=deployment["name"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_51(
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
                f"{deployment['READY_REPLICAS']}/{deployment['desired_replicas']} replicas ready"
            )
            unhealthy_resources.append(
                UnhealthyResource(name=deployment["name"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_52(
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
                f"{deployment['ready_replicas']}/{deployment['XXdesired_replicasXX']} replicas ready"
            )
            unhealthy_resources.append(
                UnhealthyResource(name=deployment["name"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_53(
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
                f"{deployment['ready_replicas']}/{deployment['DESIRED_REPLICAS']} replicas ready"
            )
            unhealthy_resources.append(
                UnhealthyResource(name=deployment["name"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_54(
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
                None
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_55(
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
                UnhealthyResource(name=None, kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_56(
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
                UnhealthyResource(name=deployment["name"], kind=None, reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_57(
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
                UnhealthyResource(name=deployment["name"], kind="Deployment", reason=None)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_58(
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
                UnhealthyResource(kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_59(
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
                UnhealthyResource(name=deployment["name"], reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_60(
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
                UnhealthyResource(name=deployment["name"], kind="Deployment", )
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_61(
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
                UnhealthyResource(name=deployment["XXnameXX"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_62(
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
                UnhealthyResource(name=deployment["NAME"], kind="Deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_63(
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
                UnhealthyResource(name=deployment["name"], kind="XXDeploymentXX", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_64(
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
                UnhealthyResource(name=deployment["name"], kind="deployment", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded


def x__find_unhealthy_resources__mutmut_65(
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
                UnhealthyResource(name=deployment["name"], kind="DEPLOYMENT", reason=reason)
            )

    return unhealthy_resources, has_critical, has_degraded

mutants_x__find_unhealthy_resources__mutmut['_mutmut_orig'] = x__find_unhealthy_resources__mutmut_orig # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_1'] = x__find_unhealthy_resources__mutmut_1 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_2'] = x__find_unhealthy_resources__mutmut_2 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_3'] = x__find_unhealthy_resources__mutmut_3 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_4'] = x__find_unhealthy_resources__mutmut_4 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_5'] = x__find_unhealthy_resources__mutmut_5 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_6'] = x__find_unhealthy_resources__mutmut_6 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_7'] = x__find_unhealthy_resources__mutmut_7 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_8'] = x__find_unhealthy_resources__mutmut_8 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_9'] = x__find_unhealthy_resources__mutmut_9 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_10'] = x__find_unhealthy_resources__mutmut_10 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_11'] = x__find_unhealthy_resources__mutmut_11 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_12'] = x__find_unhealthy_resources__mutmut_12 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_13'] = x__find_unhealthy_resources__mutmut_13 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_14'] = x__find_unhealthy_resources__mutmut_14 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_15'] = x__find_unhealthy_resources__mutmut_15 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_16'] = x__find_unhealthy_resources__mutmut_16 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_17'] = x__find_unhealthy_resources__mutmut_17 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_18'] = x__find_unhealthy_resources__mutmut_18 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_19'] = x__find_unhealthy_resources__mutmut_19 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_20'] = x__find_unhealthy_resources__mutmut_20 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_21'] = x__find_unhealthy_resources__mutmut_21 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_22'] = x__find_unhealthy_resources__mutmut_22 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_23'] = x__find_unhealthy_resources__mutmut_23 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_24'] = x__find_unhealthy_resources__mutmut_24 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_25'] = x__find_unhealthy_resources__mutmut_25 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_26'] = x__find_unhealthy_resources__mutmut_26 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_27'] = x__find_unhealthy_resources__mutmut_27 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_28'] = x__find_unhealthy_resources__mutmut_28 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_29'] = x__find_unhealthy_resources__mutmut_29 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_30'] = x__find_unhealthy_resources__mutmut_30 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_31'] = x__find_unhealthy_resources__mutmut_31 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_32'] = x__find_unhealthy_resources__mutmut_32 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_33'] = x__find_unhealthy_resources__mutmut_33 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_34'] = x__find_unhealthy_resources__mutmut_34 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_35'] = x__find_unhealthy_resources__mutmut_35 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_36'] = x__find_unhealthy_resources__mutmut_36 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_37'] = x__find_unhealthy_resources__mutmut_37 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_38'] = x__find_unhealthy_resources__mutmut_38 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_39'] = x__find_unhealthy_resources__mutmut_39 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_40'] = x__find_unhealthy_resources__mutmut_40 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_41'] = x__find_unhealthy_resources__mutmut_41 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_42'] = x__find_unhealthy_resources__mutmut_42 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_43'] = x__find_unhealthy_resources__mutmut_43 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_44'] = x__find_unhealthy_resources__mutmut_44 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_45'] = x__find_unhealthy_resources__mutmut_45 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_46'] = x__find_unhealthy_resources__mutmut_46 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_47'] = x__find_unhealthy_resources__mutmut_47 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_48'] = x__find_unhealthy_resources__mutmut_48 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_49'] = x__find_unhealthy_resources__mutmut_49 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_50'] = x__find_unhealthy_resources__mutmut_50 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_51'] = x__find_unhealthy_resources__mutmut_51 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_52'] = x__find_unhealthy_resources__mutmut_52 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_53'] = x__find_unhealthy_resources__mutmut_53 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_54'] = x__find_unhealthy_resources__mutmut_54 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_55'] = x__find_unhealthy_resources__mutmut_55 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_56'] = x__find_unhealthy_resources__mutmut_56 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_57'] = x__find_unhealthy_resources__mutmut_57 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_58'] = x__find_unhealthy_resources__mutmut_58 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_59'] = x__find_unhealthy_resources__mutmut_59 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_60'] = x__find_unhealthy_resources__mutmut_60 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_61'] = x__find_unhealthy_resources__mutmut_61 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_62'] = x__find_unhealthy_resources__mutmut_62 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_63'] = x__find_unhealthy_resources__mutmut_63 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_64'] = x__find_unhealthy_resources__mutmut_64 # type: ignore # mutmut generated
mutants_x__find_unhealthy_resources__mutmut['x__find_unhealthy_resources__mutmut_65'] = x__find_unhealthy_resources__mutmut_65 # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__find_hpa_warnings__mutmut)
def _find_hpa_warnings(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['current_replicas']}/{hpa['max_replicas']})"
        for hpa in raw_data["hpas"]
        if hpa["current_replicas"] >= hpa["max_replicas"]
    ]


def x__find_hpa_warnings__mutmut_orig(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['current_replicas']}/{hpa['max_replicas']})"
        for hpa in raw_data["hpas"]
        if hpa["current_replicas"] >= hpa["max_replicas"]
    ]


def x__find_hpa_warnings__mutmut_1(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['XXnameXX']} is at max replicas ({hpa['current_replicas']}/{hpa['max_replicas']})"
        for hpa in raw_data["hpas"]
        if hpa["current_replicas"] >= hpa["max_replicas"]
    ]


def x__find_hpa_warnings__mutmut_2(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['NAME']} is at max replicas ({hpa['current_replicas']}/{hpa['max_replicas']})"
        for hpa in raw_data["hpas"]
        if hpa["current_replicas"] >= hpa["max_replicas"]
    ]


def x__find_hpa_warnings__mutmut_3(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['XXcurrent_replicasXX']}/{hpa['max_replicas']})"
        for hpa in raw_data["hpas"]
        if hpa["current_replicas"] >= hpa["max_replicas"]
    ]


def x__find_hpa_warnings__mutmut_4(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['CURRENT_REPLICAS']}/{hpa['max_replicas']})"
        for hpa in raw_data["hpas"]
        if hpa["current_replicas"] >= hpa["max_replicas"]
    ]


def x__find_hpa_warnings__mutmut_5(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['current_replicas']}/{hpa['XXmax_replicasXX']})"
        for hpa in raw_data["hpas"]
        if hpa["current_replicas"] >= hpa["max_replicas"]
    ]


def x__find_hpa_warnings__mutmut_6(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['current_replicas']}/{hpa['MAX_REPLICAS']})"
        for hpa in raw_data["hpas"]
        if hpa["current_replicas"] >= hpa["max_replicas"]
    ]


def x__find_hpa_warnings__mutmut_7(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['current_replicas']}/{hpa['max_replicas']})"
        for hpa in raw_data["XXhpasXX"]
        if hpa["current_replicas"] >= hpa["max_replicas"]
    ]


def x__find_hpa_warnings__mutmut_8(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['current_replicas']}/{hpa['max_replicas']})"
        for hpa in raw_data["HPAS"]
        if hpa["current_replicas"] >= hpa["max_replicas"]
    ]


def x__find_hpa_warnings__mutmut_9(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['current_replicas']}/{hpa['max_replicas']})"
        for hpa in raw_data["hpas"]
        if hpa["XXcurrent_replicasXX"] >= hpa["max_replicas"]
    ]


def x__find_hpa_warnings__mutmut_10(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['current_replicas']}/{hpa['max_replicas']})"
        for hpa in raw_data["hpas"]
        if hpa["CURRENT_REPLICAS"] >= hpa["max_replicas"]
    ]


def x__find_hpa_warnings__mutmut_11(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['current_replicas']}/{hpa['max_replicas']})"
        for hpa in raw_data["hpas"]
        if hpa["current_replicas"] > hpa["max_replicas"]
    ]


def x__find_hpa_warnings__mutmut_12(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['current_replicas']}/{hpa['max_replicas']})"
        for hpa in raw_data["hpas"]
        if hpa["current_replicas"] >= hpa["XXmax_replicasXX"]
    ]


def x__find_hpa_warnings__mutmut_13(raw_data: NamespaceOverviewRawData) -> list[str]:
    return [
        f"{hpa['name']} is at max replicas ({hpa['current_replicas']}/{hpa['max_replicas']})"
        for hpa in raw_data["hpas"]
        if hpa["current_replicas"] >= hpa["MAX_REPLICAS"]
    ]

mutants_x__find_hpa_warnings__mutmut['_mutmut_orig'] = x__find_hpa_warnings__mutmut_orig # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut['x__find_hpa_warnings__mutmut_1'] = x__find_hpa_warnings__mutmut_1 # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut['x__find_hpa_warnings__mutmut_2'] = x__find_hpa_warnings__mutmut_2 # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut['x__find_hpa_warnings__mutmut_3'] = x__find_hpa_warnings__mutmut_3 # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut['x__find_hpa_warnings__mutmut_4'] = x__find_hpa_warnings__mutmut_4 # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut['x__find_hpa_warnings__mutmut_5'] = x__find_hpa_warnings__mutmut_5 # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut['x__find_hpa_warnings__mutmut_6'] = x__find_hpa_warnings__mutmut_6 # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut['x__find_hpa_warnings__mutmut_7'] = x__find_hpa_warnings__mutmut_7 # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut['x__find_hpa_warnings__mutmut_8'] = x__find_hpa_warnings__mutmut_8 # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut['x__find_hpa_warnings__mutmut_9'] = x__find_hpa_warnings__mutmut_9 # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut['x__find_hpa_warnings__mutmut_10'] = x__find_hpa_warnings__mutmut_10 # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut['x__find_hpa_warnings__mutmut_11'] = x__find_hpa_warnings__mutmut_11 # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut['x__find_hpa_warnings__mutmut_12'] = x__find_hpa_warnings__mutmut_12 # type: ignore # mutmut generated
mutants_x__find_hpa_warnings__mutmut['x__find_hpa_warnings__mutmut_13'] = x__find_hpa_warnings__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_summary__mutmut)
def _build_summary(namespace: str, unhealthy_resources: list[UnhealthyResource]) -> str:
    if not unhealthy_resources:
        return f"Namespace {namespace!r} is healthy."
    return f"{len(unhealthy_resources)} unhealthy resource(s) found in {namespace!r}."


def x__build_summary__mutmut_orig(namespace: str, unhealthy_resources: list[UnhealthyResource]) -> str:
    if not unhealthy_resources:
        return f"Namespace {namespace!r} is healthy."
    return f"{len(unhealthy_resources)} unhealthy resource(s) found in {namespace!r}."


def x__build_summary__mutmut_1(namespace: str, unhealthy_resources: list[UnhealthyResource]) -> str:
    if unhealthy_resources:
        return f"Namespace {namespace!r} is healthy."
    return f"{len(unhealthy_resources)} unhealthy resource(s) found in {namespace!r}."

mutants_x__build_summary__mutmut['_mutmut_orig'] = x__build_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_1'] = x__build_summary__mutmut_1 # type: ignore # mutmut generated
