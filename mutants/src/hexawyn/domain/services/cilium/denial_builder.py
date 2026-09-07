"""Pure Cilium dropped-flow aggregation — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumDenialGroup,
    CiliumDenialsQuery,
    CiliumDenialsResult,
    CiliumFlowEntry,
)

_NOT_INSTALLED_NOTE = "Hubble relay is not available in this cluster"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_denials__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_denials__mutmut)
def build_denials(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_orig(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_1(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = None
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_2(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.upper() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_3(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() == "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_4(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "XXdroppedXX":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_5(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "DROPPED":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_6(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            break
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_7(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = None
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_8(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason and "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_9(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "XXUNKNOWNXX"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_10(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "unknown"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_11(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = None
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_12(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key not in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_13(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = None
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_14(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = None
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_15(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=None,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_16(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=None,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_17(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=None,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_18(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=None,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_19(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=None,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_20(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=None,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_21(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=None,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_22(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_23(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_24(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_25(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_26(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_27(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_28(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_29(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count - 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_30(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 2,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_31(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = None
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_32(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=None,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_33(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=None,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_34(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=None,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_35(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=None,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_36(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=None,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_37(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=None,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_38(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=None,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_39(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_40(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_41(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_42(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_43(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_44(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_45(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_46(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=2,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_47(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = None
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_48(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(None, key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_49(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=None)
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_50(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_51(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), )
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_52(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: None)
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_53(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (+g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_54(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = None
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_55(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(None)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_56(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=None,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_57(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status=None,
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_58(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=None,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_59(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=None,
        note=None,
    )


def x_build_denials__mutmut_60(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_61(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_62(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_63(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        note=None,
    )


def x_build_denials__mutmut_64(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        )


def x_build_denials__mutmut_65(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=False,
        status="present" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_66(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="XXpresentXX" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_67(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="PRESENT" if groups else "none",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_68(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "XXnoneXX",
        total_denials=total,
        groups=groups,
        note=None,
    )


def x_build_denials__mutmut_69(flows: list[CiliumFlowEntry], query: CiliumDenialsQuery) -> CiliumDenialsResult:
    """Aggregate dropped flows into per-policy/source/destination/reason counts."""
    grouped: dict[tuple[str | None, str, str, str], CiliumDenialGroup] = {}
    for flow in flows:
        if flow.verdict.lower() != "dropped":
            continue
        reason = flow.drop_reason or "UNKNOWN"
        key = (flow.policy, flow.source, flow.destination, reason)
        if key in grouped:
            existing = grouped[key]
            grouped[key] = CiliumDenialGroup(
                policy=existing.policy,
                source=existing.source,
                destination=existing.destination,
                source_namespace=existing.source_namespace,
                destination_namespace=existing.destination_namespace,
                reason=existing.reason,
                count=existing.count + 1,
            )
        else:
            grouped[key] = CiliumDenialGroup(
                policy=flow.policy,
                source=flow.source,
                destination=flow.destination,
                source_namespace=flow.source_namespace,
                destination_namespace=flow.destination_namespace,
                reason=reason,
                count=1,
            )
    groups = sorted(grouped.values(), key=lambda g: (-g.count, g.source, g.destination))
    total = sum(group.count for group in groups)
    return CiliumDenialsResult(
        installed=True,
        status="present" if groups else "NONE",
        total_denials=total,
        groups=groups,
        note=None,
    )

mutants_x_build_denials__mutmut['_mutmut_orig'] = x_build_denials__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_1'] = x_build_denials__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_2'] = x_build_denials__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_3'] = x_build_denials__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_4'] = x_build_denials__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_5'] = x_build_denials__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_6'] = x_build_denials__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_7'] = x_build_denials__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_8'] = x_build_denials__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_9'] = x_build_denials__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_10'] = x_build_denials__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_11'] = x_build_denials__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_12'] = x_build_denials__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_13'] = x_build_denials__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_14'] = x_build_denials__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_15'] = x_build_denials__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_16'] = x_build_denials__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_17'] = x_build_denials__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_18'] = x_build_denials__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_19'] = x_build_denials__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_20'] = x_build_denials__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_21'] = x_build_denials__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_22'] = x_build_denials__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_23'] = x_build_denials__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_24'] = x_build_denials__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_25'] = x_build_denials__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_26'] = x_build_denials__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_27'] = x_build_denials__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_28'] = x_build_denials__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_29'] = x_build_denials__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_30'] = x_build_denials__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_31'] = x_build_denials__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_32'] = x_build_denials__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_33'] = x_build_denials__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_34'] = x_build_denials__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_35'] = x_build_denials__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_36'] = x_build_denials__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_37'] = x_build_denials__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_38'] = x_build_denials__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_39'] = x_build_denials__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_40'] = x_build_denials__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_41'] = x_build_denials__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_42'] = x_build_denials__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_43'] = x_build_denials__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_44'] = x_build_denials__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_45'] = x_build_denials__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_46'] = x_build_denials__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_47'] = x_build_denials__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_48'] = x_build_denials__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_49'] = x_build_denials__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_50'] = x_build_denials__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_51'] = x_build_denials__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_52'] = x_build_denials__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_53'] = x_build_denials__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_54'] = x_build_denials__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_55'] = x_build_denials__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_56'] = x_build_denials__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_57'] = x_build_denials__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_58'] = x_build_denials__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_59'] = x_build_denials__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_60'] = x_build_denials__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_61'] = x_build_denials__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_62'] = x_build_denials__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_63'] = x_build_denials__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_64'] = x_build_denials__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_65'] = x_build_denials__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_66'] = x_build_denials__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_67'] = x_build_denials__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_68'] = x_build_denials__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_denials__mutmut['x_build_denials__mutmut_69'] = x_build_denials__mutmut_69 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_not_installed_denials_result__mutmut)
def not_installed_denials_result() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        status="not_installed",
        total_denials=0,
        groups=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_denials_result__mutmut_orig() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        status="not_installed",
        total_denials=0,
        groups=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_denials_result__mutmut_1() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=None,
        status="not_installed",
        total_denials=0,
        groups=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_denials_result__mutmut_2() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        status=None,
        total_denials=0,
        groups=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_denials_result__mutmut_3() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        status="not_installed",
        total_denials=None,
        groups=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_denials_result__mutmut_4() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        status="not_installed",
        total_denials=0,
        groups=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_denials_result__mutmut_5() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        status="not_installed",
        total_denials=0,
        groups=[],
        note=None,
    )


def x_not_installed_denials_result__mutmut_6() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        status="not_installed",
        total_denials=0,
        groups=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_denials_result__mutmut_7() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        total_denials=0,
        groups=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_denials_result__mutmut_8() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        status="not_installed",
        groups=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_denials_result__mutmut_9() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        status="not_installed",
        total_denials=0,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_denials_result__mutmut_10() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        status="not_installed",
        total_denials=0,
        groups=[],
        )


def x_not_installed_denials_result__mutmut_11() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=True,
        status="not_installed",
        total_denials=0,
        groups=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_denials_result__mutmut_12() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        status="XXnot_installedXX",
        total_denials=0,
        groups=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_denials_result__mutmut_13() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        status="NOT_INSTALLED",
        total_denials=0,
        groups=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_denials_result__mutmut_14() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        status="not_installed",
        total_denials=1,
        groups=[],
        note=_NOT_INSTALLED_NOTE,
    )

mutants_x_not_installed_denials_result__mutmut['_mutmut_orig'] = x_not_installed_denials_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_1'] = x_not_installed_denials_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_2'] = x_not_installed_denials_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_3'] = x_not_installed_denials_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_4'] = x_not_installed_denials_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_5'] = x_not_installed_denials_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_6'] = x_not_installed_denials_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_7'] = x_not_installed_denials_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_8'] = x_not_installed_denials_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_9'] = x_not_installed_denials_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_10'] = x_not_installed_denials_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_11'] = x_not_installed_denials_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_12'] = x_not_installed_denials_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_13'] = x_not_installed_denials_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_not_installed_denials_result__mutmut['x_not_installed_denials_result__mutmut_14'] = x_not_installed_denials_result__mutmut_14 # type: ignore # mutmut generated
