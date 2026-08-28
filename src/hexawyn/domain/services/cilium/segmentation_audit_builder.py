"""Pure east-west reachability audit for Cilium — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumIdentityInfo,
    CiliumNetworkPolicyInfo,
    CiliumPathFinding,
    CiliumSegmentationAuditResult,
)
from hexawyn.domain.services.cilium.policy_audit import selector_matches

_NOT_INSTALLED_NOTE = "Cilium is not installed in this cluster"
_UNRESTRICTED_NOTE = (
    "No Cilium policy restricts this path (neither source egress nor destination ingress)"
)


def build_segmentation_audit(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = len(identities)
    if not identities:
        return CiliumSegmentationAuditResult(
            installed=True,
            status="empty",
            view="cilium",
            total_identities=0,
            total_paths=0,
            uncovered_paths=0,
            findings=[],
            summary="No Cilium identities found to audit",
            note="No Cilium identities found to audit",
        )
    findings: list[CiliumPathFinding] = []
    for source in identities:
        for destination in identities:
            if source.id == destination.id:
                continue
            if _path_unrestricted(source, destination, policies):
                findings.append(_finding(source, destination))
    total_paths = total * (total - 1)
    return CiliumSegmentationAuditResult(
        installed=True,
        status="gaps_found" if findings else "isolated",
        view="cilium",
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def not_installed_segmentation_audit() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def _path_unrestricted(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, destination) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(policy, source) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def _policy_selects(policy: CiliumNetworkPolicyInfo, identity: CiliumIdentityInfo) -> bool:
    return selector_matches(_labels_to_dict(identity.labels), policy.endpoint_labels)


def _labels_to_dict(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "=" in label:
            key, value = label.split("=", 1)
            result[key] = value
    return result


def _finding(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=destination.id,
        source_labels=source.labels,
        destination_labels=destination.labels,
        severity="high",
        note=_UNRESTRICTED_NOTE,
    )
