from __future__ import annotations

from hexawyn.domain.models.constants import NamespaceOverviewConstants
from hexawyn.domain.models.namespace_overview import (
    NamespaceCounts,
    NamespaceHealthStatus,
    UnhealthyResource,
)

_cfg = NamespaceOverviewConstants()


def estimate_tokens(text: str) -> int:
    """Same chars-per-token heuristic as `AdaptiveLogProcessor.estimate_tokens_from_lines`."""
    return max(1, int(len(text) / _cfg.chars_per_token_divisor))


def format_overview_summary(
    namespace: str,
    namespace_status: str,
    counts: NamespaceCounts,
    health_status: NamespaceHealthStatus,
    root_cause: str,
    unhealthy_resources: list[UnhealthyResource],
    warnings: list[str],
) -> str:
    lines = [
        f"Namespace: {namespace} ({namespace_status})",
        f"Health: {health_status.value}",
        f"Pods: {counts.pods_total} total, {counts.pods_running} running, "
        f"{counts.pods_failed} failed",
        f"Deployments: {counts.deployments_ready}/{counts.deployments_total} ready",
        f"Services: {counts.services_total}",
    ]
    if root_cause:
        lines.append(f"Root cause: {root_cause}")
    lines.extend(
        f"- {resource.kind} {resource.name}: {resource.reason}" for resource in unhealthy_resources
    )
    lines.extend(f"Warning: {warning}" for warning in warnings)
    return "\n".join(lines)


def enforce_token_budget(
    namespace: str,
    namespace_status: str,
    counts: NamespaceCounts,
    health_status: NamespaceHealthStatus,
    root_cause: str,
    unhealthy_resources: list[UnhealthyResource],
    warnings: list[str],
    max_tokens: int,
) -> tuple[list[UnhealthyResource], bool, int, int]:
    """Trims `unhealthy_resources` from the tail (caller pre-sorts worst-first)
    until the formatted summary fits `max_tokens`. Returns
    (trimmed_resources, has_more, remaining_count, estimated_tokens).
    """
    trimmed = list(unhealthy_resources)
    while trimmed:
        summary = format_overview_summary(
            namespace, namespace_status, counts, health_status, root_cause, trimmed, warnings
        )
        tokens = estimate_tokens(summary)
        if tokens <= max_tokens:
            remaining = len(unhealthy_resources) - len(trimmed)
            return trimmed, remaining > 0, remaining, tokens
        trimmed = trimmed[:-1]

    summary = format_overview_summary(
        namespace, namespace_status, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens
