from __future__ import annotations

from hexawyn.domain.models.constants import NamespaceOverviewConstants
from hexawyn.domain.models.namespace_overview import (
    NamespaceCounts,
    NamespaceHealthStatus,
    UnhealthyResource,
)

_cfg = NamespaceOverviewConstants()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_estimate_tokens__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_estimate_tokens__mutmut)
def estimate_tokens(text: str) -> int:
    """Same chars-per-token heuristic as `AdaptiveLogProcessor.estimate_tokens_from_lines`."""
    return max(1, int(len(text) / _cfg.chars_per_token_divisor))


def x_estimate_tokens__mutmut_orig(text: str) -> int:
    """Same chars-per-token heuristic as `AdaptiveLogProcessor.estimate_tokens_from_lines`."""
    return max(1, int(len(text) / _cfg.chars_per_token_divisor))


def x_estimate_tokens__mutmut_1(text: str) -> int:
    """Same chars-per-token heuristic as `AdaptiveLogProcessor.estimate_tokens_from_lines`."""
    return max(None, int(len(text) / _cfg.chars_per_token_divisor))


def x_estimate_tokens__mutmut_2(text: str) -> int:
    """Same chars-per-token heuristic as `AdaptiveLogProcessor.estimate_tokens_from_lines`."""
    return max(1, None)


def x_estimate_tokens__mutmut_3(text: str) -> int:
    """Same chars-per-token heuristic as `AdaptiveLogProcessor.estimate_tokens_from_lines`."""
    return max(int(len(text) / _cfg.chars_per_token_divisor))


def x_estimate_tokens__mutmut_4(text: str) -> int:
    """Same chars-per-token heuristic as `AdaptiveLogProcessor.estimate_tokens_from_lines`."""
    return max(1, )


def x_estimate_tokens__mutmut_5(text: str) -> int:
    """Same chars-per-token heuristic as `AdaptiveLogProcessor.estimate_tokens_from_lines`."""
    return max(2, int(len(text) / _cfg.chars_per_token_divisor))


def x_estimate_tokens__mutmut_6(text: str) -> int:
    """Same chars-per-token heuristic as `AdaptiveLogProcessor.estimate_tokens_from_lines`."""
    return max(1, int(None))


def x_estimate_tokens__mutmut_7(text: str) -> int:
    """Same chars-per-token heuristic as `AdaptiveLogProcessor.estimate_tokens_from_lines`."""
    return max(1, int(len(text) * _cfg.chars_per_token_divisor))

mutants_x_estimate_tokens__mutmut['_mutmut_orig'] = x_estimate_tokens__mutmut_orig # type: ignore # mutmut generated
mutants_x_estimate_tokens__mutmut['x_estimate_tokens__mutmut_1'] = x_estimate_tokens__mutmut_1 # type: ignore # mutmut generated
mutants_x_estimate_tokens__mutmut['x_estimate_tokens__mutmut_2'] = x_estimate_tokens__mutmut_2 # type: ignore # mutmut generated
mutants_x_estimate_tokens__mutmut['x_estimate_tokens__mutmut_3'] = x_estimate_tokens__mutmut_3 # type: ignore # mutmut generated
mutants_x_estimate_tokens__mutmut['x_estimate_tokens__mutmut_4'] = x_estimate_tokens__mutmut_4 # type: ignore # mutmut generated
mutants_x_estimate_tokens__mutmut['x_estimate_tokens__mutmut_5'] = x_estimate_tokens__mutmut_5 # type: ignore # mutmut generated
mutants_x_estimate_tokens__mutmut['x_estimate_tokens__mutmut_6'] = x_estimate_tokens__mutmut_6 # type: ignore # mutmut generated
mutants_x_estimate_tokens__mutmut['x_estimate_tokens__mutmut_7'] = x_estimate_tokens__mutmut_7 # type: ignore # mutmut generated
mutants_x_format_overview_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_format_overview_summary__mutmut)
def format_overview_summary(  # noqa: PLR0913
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


def x_format_overview_summary__mutmut_orig(  # noqa: PLR0913
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


def x_format_overview_summary__mutmut_1(  # noqa: PLR0913
    namespace: str,
    namespace_status: str,
    counts: NamespaceCounts,
    health_status: NamespaceHealthStatus,
    root_cause: str,
    unhealthy_resources: list[UnhealthyResource],
    warnings: list[str],
) -> str:
    lines = None
    if root_cause:
        lines.append(f"Root cause: {root_cause}")
    lines.extend(
        f"- {resource.kind} {resource.name}: {resource.reason}" for resource in unhealthy_resources
    )
    lines.extend(f"Warning: {warning}" for warning in warnings)
    return "\n".join(lines)


def x_format_overview_summary__mutmut_2(  # noqa: PLR0913
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
        lines.append(None)
    lines.extend(
        f"- {resource.kind} {resource.name}: {resource.reason}" for resource in unhealthy_resources
    )
    lines.extend(f"Warning: {warning}" for warning in warnings)
    return "\n".join(lines)


def x_format_overview_summary__mutmut_3(  # noqa: PLR0913
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
        None
    )
    lines.extend(f"Warning: {warning}" for warning in warnings)
    return "\n".join(lines)


def x_format_overview_summary__mutmut_4(  # noqa: PLR0913
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
    lines.extend(None)
    return "\n".join(lines)


def x_format_overview_summary__mutmut_5(  # noqa: PLR0913
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
    return "\n".join(None)


def x_format_overview_summary__mutmut_6(  # noqa: PLR0913
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
    return "XX\nXX".join(lines)

mutants_x_format_overview_summary__mutmut['_mutmut_orig'] = x_format_overview_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x_format_overview_summary__mutmut['x_format_overview_summary__mutmut_1'] = x_format_overview_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x_format_overview_summary__mutmut['x_format_overview_summary__mutmut_2'] = x_format_overview_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x_format_overview_summary__mutmut['x_format_overview_summary__mutmut_3'] = x_format_overview_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x_format_overview_summary__mutmut['x_format_overview_summary__mutmut_4'] = x_format_overview_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x_format_overview_summary__mutmut['x_format_overview_summary__mutmut_5'] = x_format_overview_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x_format_overview_summary__mutmut['x_format_overview_summary__mutmut_6'] = x_format_overview_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_enforce_token_budget__mutmut)
def enforce_token_budget(  # noqa: PLR0913
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


def x_enforce_token_budget__mutmut_orig(  # noqa: PLR0913
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


def x_enforce_token_budget__mutmut_1(  # noqa: PLR0913
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
    trimmed = None
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


def x_enforce_token_budget__mutmut_2(  # noqa: PLR0913
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
    trimmed = list(None)
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


def x_enforce_token_budget__mutmut_3(  # noqa: PLR0913
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
        summary = None
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


def x_enforce_token_budget__mutmut_4(  # noqa: PLR0913
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
            None, namespace_status, counts, health_status, root_cause, trimmed, warnings
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


def x_enforce_token_budget__mutmut_5(  # noqa: PLR0913
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
            namespace, None, counts, health_status, root_cause, trimmed, warnings
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


def x_enforce_token_budget__mutmut_6(  # noqa: PLR0913
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
            namespace, namespace_status, None, health_status, root_cause, trimmed, warnings
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


def x_enforce_token_budget__mutmut_7(  # noqa: PLR0913
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
            namespace, namespace_status, counts, None, root_cause, trimmed, warnings
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


def x_enforce_token_budget__mutmut_8(  # noqa: PLR0913
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
            namespace, namespace_status, counts, health_status, None, trimmed, warnings
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


def x_enforce_token_budget__mutmut_9(  # noqa: PLR0913
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
            namespace, namespace_status, counts, health_status, root_cause, None, warnings
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


def x_enforce_token_budget__mutmut_10(  # noqa: PLR0913
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
            namespace, namespace_status, counts, health_status, root_cause, trimmed, None
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


def x_enforce_token_budget__mutmut_11(  # noqa: PLR0913
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
            namespace_status, counts, health_status, root_cause, trimmed, warnings
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


def x_enforce_token_budget__mutmut_12(  # noqa: PLR0913
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
            namespace, counts, health_status, root_cause, trimmed, warnings
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


def x_enforce_token_budget__mutmut_13(  # noqa: PLR0913
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
            namespace, namespace_status, health_status, root_cause, trimmed, warnings
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


def x_enforce_token_budget__mutmut_14(  # noqa: PLR0913
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
            namespace, namespace_status, counts, root_cause, trimmed, warnings
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


def x_enforce_token_budget__mutmut_15(  # noqa: PLR0913
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
            namespace, namespace_status, counts, health_status, trimmed, warnings
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


def x_enforce_token_budget__mutmut_16(  # noqa: PLR0913
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
            namespace, namespace_status, counts, health_status, root_cause, warnings
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


def x_enforce_token_budget__mutmut_17(  # noqa: PLR0913
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
            namespace, namespace_status, counts, health_status, root_cause, trimmed, )
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


def x_enforce_token_budget__mutmut_18(  # noqa: PLR0913
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
        tokens = None
        if tokens <= max_tokens:
            remaining = len(unhealthy_resources) - len(trimmed)
            return trimmed, remaining > 0, remaining, tokens
        trimmed = trimmed[:-1]

    summary = format_overview_summary(
        namespace, namespace_status, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_19(  # noqa: PLR0913
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
        tokens = estimate_tokens(None)
        if tokens <= max_tokens:
            remaining = len(unhealthy_resources) - len(trimmed)
            return trimmed, remaining > 0, remaining, tokens
        trimmed = trimmed[:-1]

    summary = format_overview_summary(
        namespace, namespace_status, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_20(  # noqa: PLR0913
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
        if tokens < max_tokens:
            remaining = len(unhealthy_resources) - len(trimmed)
            return trimmed, remaining > 0, remaining, tokens
        trimmed = trimmed[:-1]

    summary = format_overview_summary(
        namespace, namespace_status, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_21(  # noqa: PLR0913
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
            remaining = None
            return trimmed, remaining > 0, remaining, tokens
        trimmed = trimmed[:-1]

    summary = format_overview_summary(
        namespace, namespace_status, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_22(  # noqa: PLR0913
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
            remaining = len(unhealthy_resources) + len(trimmed)
            return trimmed, remaining > 0, remaining, tokens
        trimmed = trimmed[:-1]

    summary = format_overview_summary(
        namespace, namespace_status, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_23(  # noqa: PLR0913
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
            return trimmed, remaining >= 0, remaining, tokens
        trimmed = trimmed[:-1]

    summary = format_overview_summary(
        namespace, namespace_status, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_24(  # noqa: PLR0913
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
            return trimmed, remaining > 1, remaining, tokens
        trimmed = trimmed[:-1]

    summary = format_overview_summary(
        namespace, namespace_status, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_25(  # noqa: PLR0913
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
        trimmed = None

    summary = format_overview_summary(
        namespace, namespace_status, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_26(  # noqa: PLR0913
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
        trimmed = trimmed[:+1]

    summary = format_overview_summary(
        namespace, namespace_status, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_27(  # noqa: PLR0913
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
        trimmed = trimmed[:-2]

    summary = format_overview_summary(
        namespace, namespace_status, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_28(  # noqa: PLR0913
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

    summary = None
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_29(  # noqa: PLR0913
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
        None, namespace_status, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_30(  # noqa: PLR0913
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
        namespace, None, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_31(  # noqa: PLR0913
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
        namespace, namespace_status, None, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_32(  # noqa: PLR0913
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
        namespace, namespace_status, counts, None, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_33(  # noqa: PLR0913
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
        namespace, namespace_status, counts, health_status, None, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_34(  # noqa: PLR0913
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
        namespace, namespace_status, counts, health_status, root_cause, None, warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_35(  # noqa: PLR0913
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
        namespace, namespace_status, counts, health_status, root_cause, [], None
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_36(  # noqa: PLR0913
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
        namespace_status, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_37(  # noqa: PLR0913
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
        namespace, counts, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_38(  # noqa: PLR0913
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
        namespace, namespace_status, health_status, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_39(  # noqa: PLR0913
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
        namespace, namespace_status, counts, root_cause, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_40(  # noqa: PLR0913
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
        namespace, namespace_status, counts, health_status, [], warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_41(  # noqa: PLR0913
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
        namespace, namespace_status, counts, health_status, root_cause, warnings
    )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_42(  # noqa: PLR0913
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
        namespace, namespace_status, counts, health_status, root_cause, [], )
    tokens = estimate_tokens(summary)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_43(  # noqa: PLR0913
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
    tokens = None
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_44(  # noqa: PLR0913
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
    tokens = estimate_tokens(None)
    return [], len(unhealthy_resources) > 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_45(  # noqa: PLR0913
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
    return [], len(unhealthy_resources) >= 0, len(unhealthy_resources), tokens


def x_enforce_token_budget__mutmut_46(  # noqa: PLR0913
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
    return [], len(unhealthy_resources) > 1, len(unhealthy_resources), tokens

mutants_x_enforce_token_budget__mutmut['_mutmut_orig'] = x_enforce_token_budget__mutmut_orig # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_1'] = x_enforce_token_budget__mutmut_1 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_2'] = x_enforce_token_budget__mutmut_2 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_3'] = x_enforce_token_budget__mutmut_3 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_4'] = x_enforce_token_budget__mutmut_4 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_5'] = x_enforce_token_budget__mutmut_5 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_6'] = x_enforce_token_budget__mutmut_6 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_7'] = x_enforce_token_budget__mutmut_7 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_8'] = x_enforce_token_budget__mutmut_8 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_9'] = x_enforce_token_budget__mutmut_9 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_10'] = x_enforce_token_budget__mutmut_10 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_11'] = x_enforce_token_budget__mutmut_11 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_12'] = x_enforce_token_budget__mutmut_12 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_13'] = x_enforce_token_budget__mutmut_13 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_14'] = x_enforce_token_budget__mutmut_14 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_15'] = x_enforce_token_budget__mutmut_15 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_16'] = x_enforce_token_budget__mutmut_16 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_17'] = x_enforce_token_budget__mutmut_17 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_18'] = x_enforce_token_budget__mutmut_18 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_19'] = x_enforce_token_budget__mutmut_19 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_20'] = x_enforce_token_budget__mutmut_20 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_21'] = x_enforce_token_budget__mutmut_21 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_22'] = x_enforce_token_budget__mutmut_22 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_23'] = x_enforce_token_budget__mutmut_23 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_24'] = x_enforce_token_budget__mutmut_24 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_25'] = x_enforce_token_budget__mutmut_25 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_26'] = x_enforce_token_budget__mutmut_26 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_27'] = x_enforce_token_budget__mutmut_27 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_28'] = x_enforce_token_budget__mutmut_28 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_29'] = x_enforce_token_budget__mutmut_29 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_30'] = x_enforce_token_budget__mutmut_30 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_31'] = x_enforce_token_budget__mutmut_31 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_32'] = x_enforce_token_budget__mutmut_32 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_33'] = x_enforce_token_budget__mutmut_33 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_34'] = x_enforce_token_budget__mutmut_34 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_35'] = x_enforce_token_budget__mutmut_35 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_36'] = x_enforce_token_budget__mutmut_36 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_37'] = x_enforce_token_budget__mutmut_37 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_38'] = x_enforce_token_budget__mutmut_38 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_39'] = x_enforce_token_budget__mutmut_39 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_40'] = x_enforce_token_budget__mutmut_40 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_41'] = x_enforce_token_budget__mutmut_41 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_42'] = x_enforce_token_budget__mutmut_42 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_43'] = x_enforce_token_budget__mutmut_43 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_44'] = x_enforce_token_budget__mutmut_44 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_45'] = x_enforce_token_budget__mutmut_45 # type: ignore # mutmut generated
mutants_x_enforce_token_budget__mutmut['x_enforce_token_budget__mutmut_46'] = x_enforce_token_budget__mutmut_46 # type: ignore # mutmut generated
