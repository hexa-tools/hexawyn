"""Pure Cilium dropped-flow aggregation — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumDenialGroup,
    CiliumDenialsQuery,
    CiliumDenialsResult,
    CiliumFlowEntry,
)

_NOT_INSTALLED_NOTE = "Hubble relay is not available in this cluster"


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


def not_installed_denials_result() -> CiliumDenialsResult:
    """Honest NOT_INSTALLED marker — no fabricated denials."""
    return CiliumDenialsResult(
        installed=False,
        status="not_installed",
        total_denials=0,
        groups=[],
        note=_NOT_INSTALLED_NOTE,
    )
