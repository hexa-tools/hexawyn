from __future__ import annotations

from hexawyn.domain.models.adaptive_namespace_investigation import (
    RankedFailingResource,
    UnhealthyResourceRef,
)

_KIND_PRIORITY = {"Deployment": 0, "Pod": 1}
_NON_DRILLABLE_POD_REASONS = frozenset({"Pending", "Terminating", "Unknown"})


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_select_top_critical__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_select_top_critical__mutmut)
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


def x_select_top_critical__mutmut_orig(
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


def x_select_top_critical__mutmut_1(
    unhealthy: list[UnhealthyResourceRef],
    restart_counts: dict[str, int],
    depth: int,
) -> tuple[list[RankedFailingResource], bool, int]:
    """Filters to drillable resources (excludes Pending/Terminating/Unknown
    pods — they have no concrete failure to investigate the same way),
    ranks worst-first by (kind priority, -restart_count, name), and slices
    to the top `depth`. Mirrors the has_more/remaining_count idiom from
    `event_analysis/namespace_event_filter.py`."""
    drillable = None

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


def x_select_top_critical__mutmut_2(
    unhealthy: list[UnhealthyResourceRef],
    restart_counts: dict[str, int],
    depth: int,
) -> tuple[list[RankedFailingResource], bool, int]:
    """Filters to drillable resources (excludes Pending/Terminating/Unknown
    pods — they have no concrete failure to investigate the same way),
    ranks worst-first by (kind priority, -restart_count, name), and slices
    to the top `depth`. Mirrors the has_more/remaining_count idiom from
    `event_analysis/namespace_event_filter.py`."""
    drillable = [resource for resource in unhealthy if _is_drillable(None)]

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


def x_select_top_critical__mutmut_3(
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
        restart_count = None
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


def x_select_top_critical__mutmut_4(
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
        restart_count = restart_counts.get(None, 0) if resource.kind == "Pod" else 0
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


def x_select_top_critical__mutmut_5(
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
        restart_count = restart_counts.get(resource.name, None) if resource.kind == "Pod" else 0
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


def x_select_top_critical__mutmut_6(
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
        restart_count = restart_counts.get(0) if resource.kind == "Pod" else 0
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


def x_select_top_critical__mutmut_7(
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
        restart_count = restart_counts.get(resource.name, ) if resource.kind == "Pod" else 0
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


def x_select_top_critical__mutmut_8(
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
        restart_count = restart_counts.get(resource.name, 1) if resource.kind == "Pod" else 0
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


def x_select_top_critical__mutmut_9(
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
        restart_count = restart_counts.get(resource.name, 0) if resource.kind != "Pod" else 0
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


def x_select_top_critical__mutmut_10(
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
        restart_count = restart_counts.get(resource.name, 0) if resource.kind == "XXPodXX" else 0
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


def x_select_top_critical__mutmut_11(
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
        restart_count = restart_counts.get(resource.name, 0) if resource.kind == "pod" else 0
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


def x_select_top_critical__mutmut_12(
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
        restart_count = restart_counts.get(resource.name, 0) if resource.kind == "POD" else 0
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


def x_select_top_critical__mutmut_13(
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
        restart_count = restart_counts.get(resource.name, 0) if resource.kind == "Pod" else 1
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


def x_select_top_critical__mutmut_14(
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
        return (_KIND_PRIORITY.get(None, 2), -restart_count, resource.name)

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


def x_select_top_critical__mutmut_15(
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
        return (_KIND_PRIORITY.get(resource.kind, None), -restart_count, resource.name)

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


def x_select_top_critical__mutmut_16(
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
        return (_KIND_PRIORITY.get(2), -restart_count, resource.name)

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


def x_select_top_critical__mutmut_17(
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
        return (_KIND_PRIORITY.get(resource.kind, ), -restart_count, resource.name)

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


def x_select_top_critical__mutmut_18(
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
        return (_KIND_PRIORITY.get(resource.kind, 3), -restart_count, resource.name)

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


def x_select_top_critical__mutmut_19(
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
        return (_KIND_PRIORITY.get(resource.kind, 2), +restart_count, resource.name)

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


def x_select_top_critical__mutmut_20(
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

    drillable.sort(key=None)

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


def x_select_top_critical__mutmut_21(
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

    total = None
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


def x_select_top_critical__mutmut_22(
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
    top = None
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


def x_select_top_critical__mutmut_23(
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
    remaining = None

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


def x_select_top_critical__mutmut_24(
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
    remaining = max(None, total - depth)

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


def x_select_top_critical__mutmut_25(
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
    remaining = max(0, None)

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


def x_select_top_critical__mutmut_26(
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
    remaining = max(total - depth)

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


def x_select_top_critical__mutmut_27(
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
    remaining = max(0, )

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


def x_select_top_critical__mutmut_28(
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
    remaining = max(1, total - depth)

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


def x_select_top_critical__mutmut_29(
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
    remaining = max(0, total + depth)

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


def x_select_top_critical__mutmut_30(
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

    ranked = None

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_31(
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
            name=None,
            kind=resource.kind,
            reason=resource.reason,
            restart_count=restart_counts.get(resource.name, 0) if resource.kind == "Pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_32(
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
            kind=None,
            reason=resource.reason,
            restart_count=restart_counts.get(resource.name, 0) if resource.kind == "Pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_33(
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
            reason=None,
            restart_count=restart_counts.get(resource.name, 0) if resource.kind == "Pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_34(
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
            restart_count=None,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_35(
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
            rank=None,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_36(
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
            kind=resource.kind,
            reason=resource.reason,
            restart_count=restart_counts.get(resource.name, 0) if resource.kind == "Pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_37(
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
            reason=resource.reason,
            restart_count=restart_counts.get(resource.name, 0) if resource.kind == "Pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_38(
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
            restart_count=restart_counts.get(resource.name, 0) if resource.kind == "Pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_39(
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
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_40(
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
            )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_41(
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
            restart_count=restart_counts.get(None, 0) if resource.kind == "Pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_42(
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
            restart_count=restart_counts.get(resource.name, None) if resource.kind == "Pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_43(
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
            restart_count=restart_counts.get(0) if resource.kind == "Pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_44(
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
            restart_count=restart_counts.get(resource.name, ) if resource.kind == "Pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_45(
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
            restart_count=restart_counts.get(resource.name, 1) if resource.kind == "Pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_46(
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
            restart_count=restart_counts.get(resource.name, 0) if resource.kind != "Pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_47(
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
            restart_count=restart_counts.get(resource.name, 0) if resource.kind == "XXPodXX" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_48(
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
            restart_count=restart_counts.get(resource.name, 0) if resource.kind == "pod" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_49(
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
            restart_count=restart_counts.get(resource.name, 0) if resource.kind == "POD" else 0,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_50(
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
            restart_count=restart_counts.get(resource.name, 0) if resource.kind == "Pod" else 1,
            rank=index,
        )
        for index, resource in enumerate(top)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_51(
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
        for index, resource in enumerate(None)
    ]

    return ranked, remaining > 0, remaining


def x_select_top_critical__mutmut_52(
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

    return ranked, remaining >= 0, remaining


def x_select_top_critical__mutmut_53(
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

    return ranked, remaining > 1, remaining

mutants_x_select_top_critical__mutmut['_mutmut_orig'] = x_select_top_critical__mutmut_orig # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_1'] = x_select_top_critical__mutmut_1 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_2'] = x_select_top_critical__mutmut_2 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_3'] = x_select_top_critical__mutmut_3 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_4'] = x_select_top_critical__mutmut_4 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_5'] = x_select_top_critical__mutmut_5 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_6'] = x_select_top_critical__mutmut_6 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_7'] = x_select_top_critical__mutmut_7 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_8'] = x_select_top_critical__mutmut_8 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_9'] = x_select_top_critical__mutmut_9 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_10'] = x_select_top_critical__mutmut_10 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_11'] = x_select_top_critical__mutmut_11 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_12'] = x_select_top_critical__mutmut_12 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_13'] = x_select_top_critical__mutmut_13 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_14'] = x_select_top_critical__mutmut_14 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_15'] = x_select_top_critical__mutmut_15 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_16'] = x_select_top_critical__mutmut_16 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_17'] = x_select_top_critical__mutmut_17 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_18'] = x_select_top_critical__mutmut_18 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_19'] = x_select_top_critical__mutmut_19 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_20'] = x_select_top_critical__mutmut_20 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_21'] = x_select_top_critical__mutmut_21 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_22'] = x_select_top_critical__mutmut_22 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_23'] = x_select_top_critical__mutmut_23 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_24'] = x_select_top_critical__mutmut_24 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_25'] = x_select_top_critical__mutmut_25 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_26'] = x_select_top_critical__mutmut_26 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_27'] = x_select_top_critical__mutmut_27 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_28'] = x_select_top_critical__mutmut_28 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_29'] = x_select_top_critical__mutmut_29 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_30'] = x_select_top_critical__mutmut_30 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_31'] = x_select_top_critical__mutmut_31 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_32'] = x_select_top_critical__mutmut_32 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_33'] = x_select_top_critical__mutmut_33 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_34'] = x_select_top_critical__mutmut_34 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_35'] = x_select_top_critical__mutmut_35 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_36'] = x_select_top_critical__mutmut_36 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_37'] = x_select_top_critical__mutmut_37 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_38'] = x_select_top_critical__mutmut_38 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_39'] = x_select_top_critical__mutmut_39 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_40'] = x_select_top_critical__mutmut_40 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_41'] = x_select_top_critical__mutmut_41 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_42'] = x_select_top_critical__mutmut_42 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_43'] = x_select_top_critical__mutmut_43 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_44'] = x_select_top_critical__mutmut_44 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_45'] = x_select_top_critical__mutmut_45 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_46'] = x_select_top_critical__mutmut_46 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_47'] = x_select_top_critical__mutmut_47 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_48'] = x_select_top_critical__mutmut_48 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_49'] = x_select_top_critical__mutmut_49 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_50'] = x_select_top_critical__mutmut_50 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_51'] = x_select_top_critical__mutmut_51 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_52'] = x_select_top_critical__mutmut_52 # type: ignore # mutmut generated
mutants_x_select_top_critical__mutmut['x_select_top_critical__mutmut_53'] = x_select_top_critical__mutmut_53 # type: ignore # mutmut generated
mutants_x_detect_node_pressure_context__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_node_pressure_context__mutmut)
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


def x_detect_node_pressure_context__mutmut_orig(
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


def x_detect_node_pressure_context__mutmut_1(
    unhealthy: list[UnhealthyResourceRef],
    ranked: list[RankedFailingResource],
) -> str | None:
    """If no resources were selected for drill-down but some were excluded as
    Pending, that's likely cluster resource pressure rather than a simple
    absence of failures — surface it as a note instead of an empty report."""
    if ranked:
        return None
    pending_count = None
    if pending_count == 0:
        return None
    return (
        f"{pending_count} pod(s) pending — likely cluster resource pressure; check node capacity."
    )


def x_detect_node_pressure_context__mutmut_2(
    unhealthy: list[UnhealthyResourceRef],
    ranked: list[RankedFailingResource],
) -> str | None:
    """If no resources were selected for drill-down but some were excluded as
    Pending, that's likely cluster resource pressure rather than a simple
    absence of failures — surface it as a note instead of an empty report."""
    if ranked:
        return None
    pending_count = sum(None)
    if pending_count == 0:
        return None
    return (
        f"{pending_count} pod(s) pending — likely cluster resource pressure; check node capacity."
    )


def x_detect_node_pressure_context__mutmut_3(
    unhealthy: list[UnhealthyResourceRef],
    ranked: list[RankedFailingResource],
) -> str | None:
    """If no resources were selected for drill-down but some were excluded as
    Pending, that's likely cluster resource pressure rather than a simple
    absence of failures — surface it as a note instead of an empty report."""
    if ranked:
        return None
    pending_count = sum(2 for resource in unhealthy if resource.reason == "Pending")
    if pending_count == 0:
        return None
    return (
        f"{pending_count} pod(s) pending — likely cluster resource pressure; check node capacity."
    )


def x_detect_node_pressure_context__mutmut_4(
    unhealthy: list[UnhealthyResourceRef],
    ranked: list[RankedFailingResource],
) -> str | None:
    """If no resources were selected for drill-down but some were excluded as
    Pending, that's likely cluster resource pressure rather than a simple
    absence of failures — surface it as a note instead of an empty report."""
    if ranked:
        return None
    pending_count = sum(1 for resource in unhealthy if resource.reason != "Pending")
    if pending_count == 0:
        return None
    return (
        f"{pending_count} pod(s) pending — likely cluster resource pressure; check node capacity."
    )


def x_detect_node_pressure_context__mutmut_5(
    unhealthy: list[UnhealthyResourceRef],
    ranked: list[RankedFailingResource],
) -> str | None:
    """If no resources were selected for drill-down but some were excluded as
    Pending, that's likely cluster resource pressure rather than a simple
    absence of failures — surface it as a note instead of an empty report."""
    if ranked:
        return None
    pending_count = sum(1 for resource in unhealthy if resource.reason == "XXPendingXX")
    if pending_count == 0:
        return None
    return (
        f"{pending_count} pod(s) pending — likely cluster resource pressure; check node capacity."
    )


def x_detect_node_pressure_context__mutmut_6(
    unhealthy: list[UnhealthyResourceRef],
    ranked: list[RankedFailingResource],
) -> str | None:
    """If no resources were selected for drill-down but some were excluded as
    Pending, that's likely cluster resource pressure rather than a simple
    absence of failures — surface it as a note instead of an empty report."""
    if ranked:
        return None
    pending_count = sum(1 for resource in unhealthy if resource.reason == "pending")
    if pending_count == 0:
        return None
    return (
        f"{pending_count} pod(s) pending — likely cluster resource pressure; check node capacity."
    )


def x_detect_node_pressure_context__mutmut_7(
    unhealthy: list[UnhealthyResourceRef],
    ranked: list[RankedFailingResource],
) -> str | None:
    """If no resources were selected for drill-down but some were excluded as
    Pending, that's likely cluster resource pressure rather than a simple
    absence of failures — surface it as a note instead of an empty report."""
    if ranked:
        return None
    pending_count = sum(1 for resource in unhealthy if resource.reason == "PENDING")
    if pending_count == 0:
        return None
    return (
        f"{pending_count} pod(s) pending — likely cluster resource pressure; check node capacity."
    )


def x_detect_node_pressure_context__mutmut_8(
    unhealthy: list[UnhealthyResourceRef],
    ranked: list[RankedFailingResource],
) -> str | None:
    """If no resources were selected for drill-down but some were excluded as
    Pending, that's likely cluster resource pressure rather than a simple
    absence of failures — surface it as a note instead of an empty report."""
    if ranked:
        return None
    pending_count = sum(1 for resource in unhealthy if resource.reason == "Pending")
    if pending_count != 0:
        return None
    return (
        f"{pending_count} pod(s) pending — likely cluster resource pressure; check node capacity."
    )


def x_detect_node_pressure_context__mutmut_9(
    unhealthy: list[UnhealthyResourceRef],
    ranked: list[RankedFailingResource],
) -> str | None:
    """If no resources were selected for drill-down but some were excluded as
    Pending, that's likely cluster resource pressure rather than a simple
    absence of failures — surface it as a note instead of an empty report."""
    if ranked:
        return None
    pending_count = sum(1 for resource in unhealthy if resource.reason == "Pending")
    if pending_count == 1:
        return None
    return (
        f"{pending_count} pod(s) pending — likely cluster resource pressure; check node capacity."
    )

mutants_x_detect_node_pressure_context__mutmut['_mutmut_orig'] = x_detect_node_pressure_context__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_node_pressure_context__mutmut['x_detect_node_pressure_context__mutmut_1'] = x_detect_node_pressure_context__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_node_pressure_context__mutmut['x_detect_node_pressure_context__mutmut_2'] = x_detect_node_pressure_context__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_node_pressure_context__mutmut['x_detect_node_pressure_context__mutmut_3'] = x_detect_node_pressure_context__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_node_pressure_context__mutmut['x_detect_node_pressure_context__mutmut_4'] = x_detect_node_pressure_context__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_node_pressure_context__mutmut['x_detect_node_pressure_context__mutmut_5'] = x_detect_node_pressure_context__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_node_pressure_context__mutmut['x_detect_node_pressure_context__mutmut_6'] = x_detect_node_pressure_context__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_node_pressure_context__mutmut['x_detect_node_pressure_context__mutmut_7'] = x_detect_node_pressure_context__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_node_pressure_context__mutmut['x_detect_node_pressure_context__mutmut_8'] = x_detect_node_pressure_context__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_node_pressure_context__mutmut['x_detect_node_pressure_context__mutmut_9'] = x_detect_node_pressure_context__mutmut_9 # type: ignore # mutmut generated
mutants_x__is_drillable__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_drillable__mutmut)
def _is_drillable(resource: UnhealthyResourceRef) -> bool:
    if resource.kind == "Pod":
        return resource.reason not in _NON_DRILLABLE_POD_REASONS
    return True


def x__is_drillable__mutmut_orig(resource: UnhealthyResourceRef) -> bool:
    if resource.kind == "Pod":
        return resource.reason not in _NON_DRILLABLE_POD_REASONS
    return True


def x__is_drillable__mutmut_1(resource: UnhealthyResourceRef) -> bool:
    if resource.kind != "Pod":
        return resource.reason not in _NON_DRILLABLE_POD_REASONS
    return True


def x__is_drillable__mutmut_2(resource: UnhealthyResourceRef) -> bool:
    if resource.kind == "XXPodXX":
        return resource.reason not in _NON_DRILLABLE_POD_REASONS
    return True


def x__is_drillable__mutmut_3(resource: UnhealthyResourceRef) -> bool:
    if resource.kind == "pod":
        return resource.reason not in _NON_DRILLABLE_POD_REASONS
    return True


def x__is_drillable__mutmut_4(resource: UnhealthyResourceRef) -> bool:
    if resource.kind == "POD":
        return resource.reason not in _NON_DRILLABLE_POD_REASONS
    return True


def x__is_drillable__mutmut_5(resource: UnhealthyResourceRef) -> bool:
    if resource.kind == "Pod":
        return resource.reason in _NON_DRILLABLE_POD_REASONS
    return True


def x__is_drillable__mutmut_6(resource: UnhealthyResourceRef) -> bool:
    if resource.kind == "Pod":
        return resource.reason not in _NON_DRILLABLE_POD_REASONS
    return False

mutants_x__is_drillable__mutmut['_mutmut_orig'] = x__is_drillable__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_drillable__mutmut['x__is_drillable__mutmut_1'] = x__is_drillable__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_drillable__mutmut['x__is_drillable__mutmut_2'] = x__is_drillable__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_drillable__mutmut['x__is_drillable__mutmut_3'] = x__is_drillable__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_drillable__mutmut['x__is_drillable__mutmut_4'] = x__is_drillable__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_drillable__mutmut['x__is_drillable__mutmut_5'] = x__is_drillable__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_drillable__mutmut['x__is_drillable__mutmut_6'] = x__is_drillable__mutmut_6 # type: ignore # mutmut generated
