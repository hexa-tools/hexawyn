"""Pure Calico east-west segmentation matrix — no infrastructure imports.

Calico has no Cilium-style identities, so reachability is derived from the
observed endpoint selectors and the allow/deny action of each policy, plus the
Calico ordering (GlobalNetworkPolicy before namespaced NetworkPolicy — broad
global default-deny therefore restricts every tier). A directed tier-to-tier
path is reported restricted when either the destination tier (ingress) or the
source tier (egress) carries a default-deny policy; otherwise the path is
allowed by Calico's default-allow and is flagged as an
allowed-but-unrestricted path.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence

from hexawyn.domain.models.calico import (
    CalicoNetworkPolicy,
    CalicoSegmentationAuditResult,
    CalicoSegmentationEdge,
    CalicoWorkload,
)
from hexawyn.domain.models.constants import NetworkPolicyConstants

_KIND_GLOBAL = "GlobalNetworkPolicy"
_RESTRICTING_ACTIONS = {"deny", "mixed"}
_BROAD_SELECTORS = {"", "all()"}
_DEFAULT_EXCLUDED = NetworkPolicyConstants().system_namespaces


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_calico_segmentation_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_calico_segmentation_audit__mutmut)
def build_calico_segmentation_audit(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_orig(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_1(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = None
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_2(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(None) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_3(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_4(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(None)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_5(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = None
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_6(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        None
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_7(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 or workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_8(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count >= 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_9(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 1 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_10(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_11(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_12(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=None,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_13(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view=None,
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_14(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=None,
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_15(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=None,
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_16(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=None,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_17(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=None,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_18(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary=None,
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_19(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_20(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_21(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_22(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_23(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_24(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_25(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_26(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_27(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_28(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=False,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_29(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="XXcalicoXX",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_30(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="CALICO",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_31(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=1,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_32(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=1,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_33(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="XXNo workload tiers to audit.XX",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_34(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="no workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_35(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="NO WORKLOAD TIERS TO AUDIT.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_36(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = None
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_37(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind != _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_38(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector not in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_39(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(None)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_40(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault(None, []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_41(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", None).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_42(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault([]).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_43(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", ).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_44(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("XX__global__XX", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_45(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__GLOBAL__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_46(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(None)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_47(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(None, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_48(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, None).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_49(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault([]).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_50(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, ).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_51(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = None

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_52(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get(None, [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_53(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", None)

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_54(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get([])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_55(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", )

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_56(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("XX__global__XX", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_57(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__GLOBAL__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_58(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = None
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_59(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source != destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_60(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                break
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_61(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = None
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_62(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(None, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_63(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, None, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_64(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, None)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_65(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_66(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_67(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, )
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_68(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = None
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_69(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(None, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_70(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, None, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_71(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, None)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_72(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_73(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_74(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, )
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_75(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = None
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_76(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny and dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_77(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = None
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_78(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(None, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_79(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, None, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_80(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, None, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_81(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, None)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_82(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_83(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_84(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_85(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, )
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_86(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                None
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_87(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=None,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_88(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=None,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_89(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=None,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_90(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=None,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_91(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None,
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_92(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_93(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_94(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_95(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_96(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_97(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(None, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_98(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, None),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_99(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_100(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, ),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_101(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = None
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_102(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(None)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_103(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(2 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_104(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_105(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=None,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_106(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view=None,
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_107(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=None,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_108(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=None,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_109(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=None,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_110(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=None,
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_111(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=None,
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_112(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_113(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_114(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_115(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_116(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_117(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_118(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_119(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_120(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        )


def x_build_calico_segmentation_audit__mutmut_121(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=False,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_122(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="XXcalicoXX",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_123(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="CALICO",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_124(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(None, len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_125(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, None),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_126(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(len(edges)),
        error=None,
    )


def x_build_calico_segmentation_audit__mutmut_127(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoSegmentationAuditResult:
    """Build the Calico tier-to-tier segmentation matrix."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )
    tiers = sorted(
        {
            workload.namespace
            for workload in workloads
            if workload.pod_count > 0 and workload.namespace not in excluded
        }
    )
    if not tiers:
        return CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary="No workload tiers to audit.",
            error=None,
        )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            if policy.selector in _BROAD_SELECTORS:
                ns_policies.setdefault("__global__", []).append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    global_policies = ns_policies.get("__global__", [])

    edges: list[CalicoSegmentationEdge] = []
    for source in tiers:
        for destination in tiers:
            if source == destination:
                continue
            source_deny = _has_default_deny(source, ns_policies, global_policies)
            dest_deny = _has_default_deny(destination, ns_policies, global_policies)
            restricted = source_deny or dest_deny
            selectors = _edge_selectors(source, destination, ns_policies, global_policies)
            edges.append(
                CalicoSegmentationEdge(
                    source=source,
                    destination=destination,
                    restricted=restricted,
                    selectors=selectors,
                    note=None if restricted else _edge_note(source, destination),
                )
            )

    gap_count = sum(1 for edge in edges if not edge.restricted)
    return CalicoSegmentationAuditResult(
        installed=True,
        not_installed_marker=None,
        view="calico",
        tiers=tiers,
        edges=edges,
        gap_count=gap_count,
        total_paths=len(edges),
        summary=_summary(gap_count, ),
        error=None,
    )

mutants_x_build_calico_segmentation_audit__mutmut['_mutmut_orig'] = x_build_calico_segmentation_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_1'] = x_build_calico_segmentation_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_2'] = x_build_calico_segmentation_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_3'] = x_build_calico_segmentation_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_4'] = x_build_calico_segmentation_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_5'] = x_build_calico_segmentation_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_6'] = x_build_calico_segmentation_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_7'] = x_build_calico_segmentation_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_8'] = x_build_calico_segmentation_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_9'] = x_build_calico_segmentation_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_10'] = x_build_calico_segmentation_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_11'] = x_build_calico_segmentation_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_12'] = x_build_calico_segmentation_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_13'] = x_build_calico_segmentation_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_14'] = x_build_calico_segmentation_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_15'] = x_build_calico_segmentation_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_16'] = x_build_calico_segmentation_audit__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_17'] = x_build_calico_segmentation_audit__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_18'] = x_build_calico_segmentation_audit__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_19'] = x_build_calico_segmentation_audit__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_20'] = x_build_calico_segmentation_audit__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_21'] = x_build_calico_segmentation_audit__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_22'] = x_build_calico_segmentation_audit__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_23'] = x_build_calico_segmentation_audit__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_24'] = x_build_calico_segmentation_audit__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_25'] = x_build_calico_segmentation_audit__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_26'] = x_build_calico_segmentation_audit__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_27'] = x_build_calico_segmentation_audit__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_28'] = x_build_calico_segmentation_audit__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_29'] = x_build_calico_segmentation_audit__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_30'] = x_build_calico_segmentation_audit__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_31'] = x_build_calico_segmentation_audit__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_32'] = x_build_calico_segmentation_audit__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_33'] = x_build_calico_segmentation_audit__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_34'] = x_build_calico_segmentation_audit__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_35'] = x_build_calico_segmentation_audit__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_36'] = x_build_calico_segmentation_audit__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_37'] = x_build_calico_segmentation_audit__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_38'] = x_build_calico_segmentation_audit__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_39'] = x_build_calico_segmentation_audit__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_40'] = x_build_calico_segmentation_audit__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_41'] = x_build_calico_segmentation_audit__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_42'] = x_build_calico_segmentation_audit__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_43'] = x_build_calico_segmentation_audit__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_44'] = x_build_calico_segmentation_audit__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_45'] = x_build_calico_segmentation_audit__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_46'] = x_build_calico_segmentation_audit__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_47'] = x_build_calico_segmentation_audit__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_48'] = x_build_calico_segmentation_audit__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_49'] = x_build_calico_segmentation_audit__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_50'] = x_build_calico_segmentation_audit__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_51'] = x_build_calico_segmentation_audit__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_52'] = x_build_calico_segmentation_audit__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_53'] = x_build_calico_segmentation_audit__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_54'] = x_build_calico_segmentation_audit__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_55'] = x_build_calico_segmentation_audit__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_56'] = x_build_calico_segmentation_audit__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_57'] = x_build_calico_segmentation_audit__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_58'] = x_build_calico_segmentation_audit__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_59'] = x_build_calico_segmentation_audit__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_60'] = x_build_calico_segmentation_audit__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_61'] = x_build_calico_segmentation_audit__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_62'] = x_build_calico_segmentation_audit__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_63'] = x_build_calico_segmentation_audit__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_64'] = x_build_calico_segmentation_audit__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_65'] = x_build_calico_segmentation_audit__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_66'] = x_build_calico_segmentation_audit__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_67'] = x_build_calico_segmentation_audit__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_68'] = x_build_calico_segmentation_audit__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_69'] = x_build_calico_segmentation_audit__mutmut_69 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_70'] = x_build_calico_segmentation_audit__mutmut_70 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_71'] = x_build_calico_segmentation_audit__mutmut_71 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_72'] = x_build_calico_segmentation_audit__mutmut_72 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_73'] = x_build_calico_segmentation_audit__mutmut_73 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_74'] = x_build_calico_segmentation_audit__mutmut_74 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_75'] = x_build_calico_segmentation_audit__mutmut_75 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_76'] = x_build_calico_segmentation_audit__mutmut_76 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_77'] = x_build_calico_segmentation_audit__mutmut_77 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_78'] = x_build_calico_segmentation_audit__mutmut_78 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_79'] = x_build_calico_segmentation_audit__mutmut_79 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_80'] = x_build_calico_segmentation_audit__mutmut_80 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_81'] = x_build_calico_segmentation_audit__mutmut_81 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_82'] = x_build_calico_segmentation_audit__mutmut_82 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_83'] = x_build_calico_segmentation_audit__mutmut_83 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_84'] = x_build_calico_segmentation_audit__mutmut_84 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_85'] = x_build_calico_segmentation_audit__mutmut_85 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_86'] = x_build_calico_segmentation_audit__mutmut_86 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_87'] = x_build_calico_segmentation_audit__mutmut_87 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_88'] = x_build_calico_segmentation_audit__mutmut_88 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_89'] = x_build_calico_segmentation_audit__mutmut_89 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_90'] = x_build_calico_segmentation_audit__mutmut_90 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_91'] = x_build_calico_segmentation_audit__mutmut_91 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_92'] = x_build_calico_segmentation_audit__mutmut_92 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_93'] = x_build_calico_segmentation_audit__mutmut_93 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_94'] = x_build_calico_segmentation_audit__mutmut_94 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_95'] = x_build_calico_segmentation_audit__mutmut_95 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_96'] = x_build_calico_segmentation_audit__mutmut_96 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_97'] = x_build_calico_segmentation_audit__mutmut_97 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_98'] = x_build_calico_segmentation_audit__mutmut_98 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_99'] = x_build_calico_segmentation_audit__mutmut_99 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_100'] = x_build_calico_segmentation_audit__mutmut_100 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_101'] = x_build_calico_segmentation_audit__mutmut_101 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_102'] = x_build_calico_segmentation_audit__mutmut_102 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_103'] = x_build_calico_segmentation_audit__mutmut_103 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_104'] = x_build_calico_segmentation_audit__mutmut_104 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_105'] = x_build_calico_segmentation_audit__mutmut_105 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_106'] = x_build_calico_segmentation_audit__mutmut_106 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_107'] = x_build_calico_segmentation_audit__mutmut_107 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_108'] = x_build_calico_segmentation_audit__mutmut_108 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_109'] = x_build_calico_segmentation_audit__mutmut_109 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_110'] = x_build_calico_segmentation_audit__mutmut_110 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_111'] = x_build_calico_segmentation_audit__mutmut_111 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_112'] = x_build_calico_segmentation_audit__mutmut_112 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_113'] = x_build_calico_segmentation_audit__mutmut_113 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_114'] = x_build_calico_segmentation_audit__mutmut_114 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_115'] = x_build_calico_segmentation_audit__mutmut_115 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_116'] = x_build_calico_segmentation_audit__mutmut_116 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_117'] = x_build_calico_segmentation_audit__mutmut_117 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_118'] = x_build_calico_segmentation_audit__mutmut_118 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_119'] = x_build_calico_segmentation_audit__mutmut_119 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_120'] = x_build_calico_segmentation_audit__mutmut_120 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_121'] = x_build_calico_segmentation_audit__mutmut_121 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_122'] = x_build_calico_segmentation_audit__mutmut_122 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_123'] = x_build_calico_segmentation_audit__mutmut_123 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_124'] = x_build_calico_segmentation_audit__mutmut_124 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_125'] = x_build_calico_segmentation_audit__mutmut_125 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_126'] = x_build_calico_segmentation_audit__mutmut_126 # type: ignore # mutmut generated
mutants_x_build_calico_segmentation_audit__mutmut['x_build_calico_segmentation_audit__mutmut_127'] = x_build_calico_segmentation_audit__mutmut_127 # type: ignore # mutmut generated
mutants_x__has_default_deny__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__has_default_deny__mutmut)
def _has_default_deny(
    tier: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> bool:
    applicable = ns_policies.get(tier, []) + global_policies
    return any(policy.action in _RESTRICTING_ACTIONS for policy in applicable)


def x__has_default_deny__mutmut_orig(
    tier: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> bool:
    applicable = ns_policies.get(tier, []) + global_policies
    return any(policy.action in _RESTRICTING_ACTIONS for policy in applicable)


def x__has_default_deny__mutmut_1(
    tier: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> bool:
    applicable = None
    return any(policy.action in _RESTRICTING_ACTIONS for policy in applicable)


def x__has_default_deny__mutmut_2(
    tier: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> bool:
    applicable = ns_policies.get(tier, []) - global_policies
    return any(policy.action in _RESTRICTING_ACTIONS for policy in applicable)


def x__has_default_deny__mutmut_3(
    tier: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> bool:
    applicable = ns_policies.get(None, []) + global_policies
    return any(policy.action in _RESTRICTING_ACTIONS for policy in applicable)


def x__has_default_deny__mutmut_4(
    tier: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> bool:
    applicable = ns_policies.get(tier, None) + global_policies
    return any(policy.action in _RESTRICTING_ACTIONS for policy in applicable)


def x__has_default_deny__mutmut_5(
    tier: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> bool:
    applicable = ns_policies.get([]) + global_policies
    return any(policy.action in _RESTRICTING_ACTIONS for policy in applicable)


def x__has_default_deny__mutmut_6(
    tier: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> bool:
    applicable = ns_policies.get(tier, ) + global_policies
    return any(policy.action in _RESTRICTING_ACTIONS for policy in applicable)


def x__has_default_deny__mutmut_7(
    tier: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> bool:
    applicable = ns_policies.get(tier, []) + global_policies
    return any(None)


def x__has_default_deny__mutmut_8(
    tier: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> bool:
    applicable = ns_policies.get(tier, []) + global_policies
    return any(policy.action not in _RESTRICTING_ACTIONS for policy in applicable)

mutants_x__has_default_deny__mutmut['_mutmut_orig'] = x__has_default_deny__mutmut_orig # type: ignore # mutmut generated
mutants_x__has_default_deny__mutmut['x__has_default_deny__mutmut_1'] = x__has_default_deny__mutmut_1 # type: ignore # mutmut generated
mutants_x__has_default_deny__mutmut['x__has_default_deny__mutmut_2'] = x__has_default_deny__mutmut_2 # type: ignore # mutmut generated
mutants_x__has_default_deny__mutmut['x__has_default_deny__mutmut_3'] = x__has_default_deny__mutmut_3 # type: ignore # mutmut generated
mutants_x__has_default_deny__mutmut['x__has_default_deny__mutmut_4'] = x__has_default_deny__mutmut_4 # type: ignore # mutmut generated
mutants_x__has_default_deny__mutmut['x__has_default_deny__mutmut_5'] = x__has_default_deny__mutmut_5 # type: ignore # mutmut generated
mutants_x__has_default_deny__mutmut['x__has_default_deny__mutmut_6'] = x__has_default_deny__mutmut_6 # type: ignore # mutmut generated
mutants_x__has_default_deny__mutmut['x__has_default_deny__mutmut_7'] = x__has_default_deny__mutmut_7 # type: ignore # mutmut generated
mutants_x__has_default_deny__mutmut['x__has_default_deny__mutmut_8'] = x__has_default_deny__mutmut_8 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__edge_selectors__mutmut)
def _edge_selectors(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(source, []) + ns_policies.get(destination, []) + global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_orig(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(source, []) + ns_policies.get(destination, []) + global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_1(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = None
    for policy in ns_policies.get(source, []) + ns_policies.get(destination, []) + global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_2(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(source, []) + ns_policies.get(destination, []) - global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_3(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(source, []) - ns_policies.get(destination, []) + global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_4(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(None, []) + ns_policies.get(destination, []) + global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_5(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(source, None) + ns_policies.get(destination, []) + global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_6(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get([]) + ns_policies.get(destination, []) + global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_7(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(source, ) + ns_policies.get(destination, []) + global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_8(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(source, []) + ns_policies.get(None, []) + global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_9(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(source, []) + ns_policies.get(destination, None) + global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_10(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(source, []) + ns_policies.get([]) + global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_11(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(source, []) + ns_policies.get(destination, ) + global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_12(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(source, []) + ns_policies.get(destination, []) + global_policies:
        if policy.selector or policy.selector not in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_13(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(source, []) + ns_policies.get(destination, []) + global_policies:
        if policy.selector and policy.selector in selectors:
            selectors.append(policy.selector)
    return selectors


def x__edge_selectors__mutmut_14(
    source: str,
    destination: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> list[str]:
    selectors: list[str] = []
    for policy in ns_policies.get(source, []) + ns_policies.get(destination, []) + global_policies:
        if policy.selector and policy.selector not in selectors:
            selectors.append(None)
    return selectors

mutants_x__edge_selectors__mutmut['_mutmut_orig'] = x__edge_selectors__mutmut_orig # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_1'] = x__edge_selectors__mutmut_1 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_2'] = x__edge_selectors__mutmut_2 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_3'] = x__edge_selectors__mutmut_3 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_4'] = x__edge_selectors__mutmut_4 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_5'] = x__edge_selectors__mutmut_5 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_6'] = x__edge_selectors__mutmut_6 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_7'] = x__edge_selectors__mutmut_7 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_8'] = x__edge_selectors__mutmut_8 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_9'] = x__edge_selectors__mutmut_9 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_10'] = x__edge_selectors__mutmut_10 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_11'] = x__edge_selectors__mutmut_11 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_12'] = x__edge_selectors__mutmut_12 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_13'] = x__edge_selectors__mutmut_13 # type: ignore # mutmut generated
mutants_x__edge_selectors__mutmut['x__edge_selectors__mutmut_14'] = x__edge_selectors__mutmut_14 # type: ignore # mutmut generated


def _edge_note(source: str, destination: str) -> str:
    return (
        f"Allowed by default (no Calico default-deny on '{source}' egress "
        f"or '{destination}' ingress)"
    )
mutants_x__summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__summary__mutmut)
def _summary(gap_count: int, total_paths: int) -> str:
    if gap_count == 0:
        return f"No unrestricted tier-to-tier paths out of {total_paths}."
    return (
        f"{gap_count} of {total_paths} tier-to-tier paths are allowed without "
        "a Calico default-deny."
    )


def x__summary__mutmut_orig(gap_count: int, total_paths: int) -> str:
    if gap_count == 0:
        return f"No unrestricted tier-to-tier paths out of {total_paths}."
    return (
        f"{gap_count} of {total_paths} tier-to-tier paths are allowed without "
        "a Calico default-deny."
    )


def x__summary__mutmut_1(gap_count: int, total_paths: int) -> str:
    if gap_count != 0:
        return f"No unrestricted tier-to-tier paths out of {total_paths}."
    return (
        f"{gap_count} of {total_paths} tier-to-tier paths are allowed without "
        "a Calico default-deny."
    )


def x__summary__mutmut_2(gap_count: int, total_paths: int) -> str:
    if gap_count == 1:
        return f"No unrestricted tier-to-tier paths out of {total_paths}."
    return (
        f"{gap_count} of {total_paths} tier-to-tier paths are allowed without "
        "a Calico default-deny."
    )


def x__summary__mutmut_3(gap_count: int, total_paths: int) -> str:
    if gap_count == 0:
        return f"No unrestricted tier-to-tier paths out of {total_paths}."
    return (
        f"{gap_count} of {total_paths} tier-to-tier paths are allowed without "
        "XXa Calico default-deny.XX"
    )


def x__summary__mutmut_4(gap_count: int, total_paths: int) -> str:
    if gap_count == 0:
        return f"No unrestricted tier-to-tier paths out of {total_paths}."
    return (
        f"{gap_count} of {total_paths} tier-to-tier paths are allowed without "
        "a calico default-deny."
    )


def x__summary__mutmut_5(gap_count: int, total_paths: int) -> str:
    if gap_count == 0:
        return f"No unrestricted tier-to-tier paths out of {total_paths}."
    return (
        f"{gap_count} of {total_paths} tier-to-tier paths are allowed without "
        "A CALICO DEFAULT-DENY."
    )

mutants_x__summary__mutmut['_mutmut_orig'] = x__summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_1'] = x__summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_2'] = x__summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_3'] = x__summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_4'] = x__summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_5'] = x__summary__mutmut_5 # type: ignore # mutmut generated
