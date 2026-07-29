from __future__ import annotations

from hexawyn.domain.models.adaptive_namespace_investigation import (
    RankedFailingResource,
    UnhealthyResourceRef,
)

_KIND_PRIORITY = {"Deployment": 0, "Pod": 1}
_NON_DRILLABLE_POD_REASONS = frozenset({"Pending", "Terminating", "Unknown"})


def select_top_critical(
    unhealthy: list[UnhealthyResourceRef],
    restart_counts: dict[str, int],
    depth: int,
) -> tuple[list[RankedFailingResource], bool, int]:
    """Filters to drillable resources (excludes Pending/Terminating/Unknown
    pods — they have no concrete failure to investigate the same way),
    ranks worst-first by (kind priority, -restart_count, name), and slices
    to the top `depth`. Mirrors the has_more/remaining_count idiom from
    `event_analysis/namespace_event_filter.py`."""
    drillable = [resource for resource in unhealthy if _is_drillable(resource)]

    def _sort_key(resource: UnhealthyResourceRef) -> tuple[int, int, str]:
        restart_count = restart_counts.get(resource.name, 0) if resource.kind == "Pod" else 0
        return (_KIND_PRIORITY.get(resource.kind, 2), -restart_count, resource.name)

    drillable.sort(key=_sort_key)

    total = len(drillable)
    top = drillable[:depth]
    remaining = max(0, total - depth)

    ranked = [
        RankedFailingResource(
            name=resource.name,
            kind=resource.kind,
            reason=resource.reason,
            restart_count=restart_counts.get(resource.name, 0) if resource.kind == "Pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def detect_node_pressure_context(
    unhealthy: list[UnhealthyResourceRef],
    ranked: list[RankedFailingResource],
) -> str | None:
    """If no resources were selected for drill-down but some were excluded as
    Pending, that's likely cluster resource pressure rather than a simple
    absence of failures — surface it as a note instead of an empty report."""
    if ranked:
        return None
    pending_count = sum(1 for resource in unhealthy if resource.reason == "Pending")
    if pending_count == 0:
        return None
    return (
        f"{pending_count} pod(s) pending — likely cluster resource pressure; check node capacity."
    )


def _is_drillable(resource: UnhealthyResourceRef) -> bool:
    if resource.kind == "Pod":
        return resource.reason not in _NON_DRILLABLE_POD_REASONS
    return True
