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


def _has_default_deny(
    tier: str,
    ns_policies: dict[str, list[CalicoNetworkPolicy]],
    global_policies: list[CalicoNetworkPolicy],
) -> bool:
    applicable = ns_policies.get(tier, []) + global_policies
    return any(policy.action in _RESTRICTING_ACTIONS for policy in applicable)


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


def _edge_note(source: str, destination: str) -> str:
    return (
        f"Allowed by default (no Calico default-deny on '{source}' egress "
        f"or '{destination}' ingress)"
    )


def _summary(gap_count: int, total_paths: int) -> str:
    if gap_count == 0:
        return f"No unrestricted tier-to-tier paths out of {total_paths}."
    return (
        f"{gap_count} of {total_paths} tier-to-tier paths are allowed without "
        "a Calico default-deny."
    )
