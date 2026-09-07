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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_segmentation_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_segmentation_audit__mutmut)
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


def x_build_segmentation_audit__mutmut_orig(
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


def x_build_segmentation_audit__mutmut_1(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = None
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


def x_build_segmentation_audit__mutmut_2(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = len(identities)
    if identities:
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


def x_build_segmentation_audit__mutmut_3(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = len(identities)
    if not identities:
        return CiliumSegmentationAuditResult(
            installed=None,
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


def x_build_segmentation_audit__mutmut_4(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = len(identities)
    if not identities:
        return CiliumSegmentationAuditResult(
            installed=True,
            status=None,
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


def x_build_segmentation_audit__mutmut_5(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = len(identities)
    if not identities:
        return CiliumSegmentationAuditResult(
            installed=True,
            status="empty",
            view=None,
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


def x_build_segmentation_audit__mutmut_6(
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
            total_identities=None,
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


def x_build_segmentation_audit__mutmut_7(
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
            total_paths=None,
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


def x_build_segmentation_audit__mutmut_8(
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
            uncovered_paths=None,
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


def x_build_segmentation_audit__mutmut_9(
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
            findings=None,
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


def x_build_segmentation_audit__mutmut_10(
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
            summary=None,
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


def x_build_segmentation_audit__mutmut_11(
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
            note=None,
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


def x_build_segmentation_audit__mutmut_12(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = len(identities)
    if not identities:
        return CiliumSegmentationAuditResult(
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


def x_build_segmentation_audit__mutmut_13(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = len(identities)
    if not identities:
        return CiliumSegmentationAuditResult(
            installed=True,
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


def x_build_segmentation_audit__mutmut_14(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = len(identities)
    if not identities:
        return CiliumSegmentationAuditResult(
            installed=True,
            status="empty",
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


def x_build_segmentation_audit__mutmut_15(
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


def x_build_segmentation_audit__mutmut_16(
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


def x_build_segmentation_audit__mutmut_17(
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


def x_build_segmentation_audit__mutmut_18(
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


def x_build_segmentation_audit__mutmut_19(
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


def x_build_segmentation_audit__mutmut_20(
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


def x_build_segmentation_audit__mutmut_21(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = len(identities)
    if not identities:
        return CiliumSegmentationAuditResult(
            installed=False,
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


def x_build_segmentation_audit__mutmut_22(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = len(identities)
    if not identities:
        return CiliumSegmentationAuditResult(
            installed=True,
            status="XXemptyXX",
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


def x_build_segmentation_audit__mutmut_23(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = len(identities)
    if not identities:
        return CiliumSegmentationAuditResult(
            installed=True,
            status="EMPTY",
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


def x_build_segmentation_audit__mutmut_24(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = len(identities)
    if not identities:
        return CiliumSegmentationAuditResult(
            installed=True,
            status="empty",
            view="XXciliumXX",
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


def x_build_segmentation_audit__mutmut_25(
    identities: list[CiliumIdentityInfo],
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumSegmentationAuditResult:
    """Compute allowed-but-unrestricted east-west paths between identities."""
    total = len(identities)
    if not identities:
        return CiliumSegmentationAuditResult(
            installed=True,
            status="empty",
            view="CILIUM",
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


def x_build_segmentation_audit__mutmut_26(
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
            total_identities=1,
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


def x_build_segmentation_audit__mutmut_27(
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
            total_paths=1,
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


def x_build_segmentation_audit__mutmut_28(
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
            uncovered_paths=1,
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


def x_build_segmentation_audit__mutmut_29(
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
            summary="XXNo Cilium identities found to auditXX",
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


def x_build_segmentation_audit__mutmut_30(
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
            summary="no cilium identities found to audit",
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


def x_build_segmentation_audit__mutmut_31(
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
            summary="NO CILIUM IDENTITIES FOUND TO AUDIT",
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


def x_build_segmentation_audit__mutmut_32(
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
            note="XXNo Cilium identities found to auditXX",
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


def x_build_segmentation_audit__mutmut_33(
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
            note="no cilium identities found to audit",
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


def x_build_segmentation_audit__mutmut_34(
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
            note="NO CILIUM IDENTITIES FOUND TO AUDIT",
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


def x_build_segmentation_audit__mutmut_35(
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
    findings: list[CiliumPathFinding] = None
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


def x_build_segmentation_audit__mutmut_36(
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
            if source.id != destination.id:
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


def x_build_segmentation_audit__mutmut_37(
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
                break
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


def x_build_segmentation_audit__mutmut_38(
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
            if _path_unrestricted(None, destination, policies):
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


def x_build_segmentation_audit__mutmut_39(
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
            if _path_unrestricted(source, None, policies):
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


def x_build_segmentation_audit__mutmut_40(
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
            if _path_unrestricted(source, destination, None):
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


def x_build_segmentation_audit__mutmut_41(
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
            if _path_unrestricted(destination, policies):
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


def x_build_segmentation_audit__mutmut_42(
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
            if _path_unrestricted(source, policies):
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


def x_build_segmentation_audit__mutmut_43(
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
            if _path_unrestricted(source, destination, ):
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


def x_build_segmentation_audit__mutmut_44(
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
                findings.append(None)
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


def x_build_segmentation_audit__mutmut_45(
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
                findings.append(_finding(None, destination))
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


def x_build_segmentation_audit__mutmut_46(
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
                findings.append(_finding(source, None))
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


def x_build_segmentation_audit__mutmut_47(
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
                findings.append(_finding(destination))
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


def x_build_segmentation_audit__mutmut_48(
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
                findings.append(_finding(source, ))
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


def x_build_segmentation_audit__mutmut_49(
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
    total_paths = None
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


def x_build_segmentation_audit__mutmut_50(
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
    total_paths = total / (total - 1)
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


def x_build_segmentation_audit__mutmut_51(
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
    total_paths = total * (total + 1)
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


def x_build_segmentation_audit__mutmut_52(
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
    total_paths = total * (total - 2)
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


def x_build_segmentation_audit__mutmut_53(
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
        installed=None,
        status="gaps_found" if findings else "isolated",
        view="cilium",
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_54(
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
        status=None,
        view="cilium",
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_55(
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
        view=None,
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_56(
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
        total_identities=None,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_57(
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
        total_paths=None,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_58(
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
        uncovered_paths=None,
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_59(
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
        findings=None,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_60(
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
        summary=None,
        note=None,
    )


def x_build_segmentation_audit__mutmut_61(
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
        status="gaps_found" if findings else "isolated",
        view="cilium",
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_62(
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
        view="cilium",
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_63(
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
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_64(
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
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_65(
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
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_66(
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
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_67(
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
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_68(
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
        note=None,
    )


def x_build_segmentation_audit__mutmut_69(
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
        )


def x_build_segmentation_audit__mutmut_70(
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
        installed=False,
        status="gaps_found" if findings else "isolated",
        view="cilium",
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_71(
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
        status="XXgaps_foundXX" if findings else "isolated",
        view="cilium",
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_72(
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
        status="GAPS_FOUND" if findings else "isolated",
        view="cilium",
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_73(
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
        status="gaps_found" if findings else "XXisolatedXX",
        view="cilium",
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_74(
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
        status="gaps_found" if findings else "ISOLATED",
        view="cilium",
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_75(
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
        view="XXciliumXX",
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )


def x_build_segmentation_audit__mutmut_76(
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
        view="CILIUM",
        total_identities=total,
        total_paths=total_paths,
        uncovered_paths=len(findings),
        findings=findings,
        summary=f"{len(findings)} unrestricted path(s) out of {total_paths}",
        note=None,
    )

mutants_x_build_segmentation_audit__mutmut['_mutmut_orig'] = x_build_segmentation_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_1'] = x_build_segmentation_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_2'] = x_build_segmentation_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_3'] = x_build_segmentation_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_4'] = x_build_segmentation_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_5'] = x_build_segmentation_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_6'] = x_build_segmentation_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_7'] = x_build_segmentation_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_8'] = x_build_segmentation_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_9'] = x_build_segmentation_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_10'] = x_build_segmentation_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_11'] = x_build_segmentation_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_12'] = x_build_segmentation_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_13'] = x_build_segmentation_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_14'] = x_build_segmentation_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_15'] = x_build_segmentation_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_16'] = x_build_segmentation_audit__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_17'] = x_build_segmentation_audit__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_18'] = x_build_segmentation_audit__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_19'] = x_build_segmentation_audit__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_20'] = x_build_segmentation_audit__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_21'] = x_build_segmentation_audit__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_22'] = x_build_segmentation_audit__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_23'] = x_build_segmentation_audit__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_24'] = x_build_segmentation_audit__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_25'] = x_build_segmentation_audit__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_26'] = x_build_segmentation_audit__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_27'] = x_build_segmentation_audit__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_28'] = x_build_segmentation_audit__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_29'] = x_build_segmentation_audit__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_30'] = x_build_segmentation_audit__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_31'] = x_build_segmentation_audit__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_32'] = x_build_segmentation_audit__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_33'] = x_build_segmentation_audit__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_34'] = x_build_segmentation_audit__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_35'] = x_build_segmentation_audit__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_36'] = x_build_segmentation_audit__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_37'] = x_build_segmentation_audit__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_38'] = x_build_segmentation_audit__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_39'] = x_build_segmentation_audit__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_40'] = x_build_segmentation_audit__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_41'] = x_build_segmentation_audit__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_42'] = x_build_segmentation_audit__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_43'] = x_build_segmentation_audit__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_44'] = x_build_segmentation_audit__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_45'] = x_build_segmentation_audit__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_46'] = x_build_segmentation_audit__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_47'] = x_build_segmentation_audit__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_48'] = x_build_segmentation_audit__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_49'] = x_build_segmentation_audit__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_50'] = x_build_segmentation_audit__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_51'] = x_build_segmentation_audit__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_52'] = x_build_segmentation_audit__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_53'] = x_build_segmentation_audit__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_54'] = x_build_segmentation_audit__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_55'] = x_build_segmentation_audit__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_56'] = x_build_segmentation_audit__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_57'] = x_build_segmentation_audit__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_58'] = x_build_segmentation_audit__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_59'] = x_build_segmentation_audit__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_60'] = x_build_segmentation_audit__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_61'] = x_build_segmentation_audit__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_62'] = x_build_segmentation_audit__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_63'] = x_build_segmentation_audit__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_64'] = x_build_segmentation_audit__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_65'] = x_build_segmentation_audit__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_66'] = x_build_segmentation_audit__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_67'] = x_build_segmentation_audit__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_68'] = x_build_segmentation_audit__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_69'] = x_build_segmentation_audit__mutmut_69 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_70'] = x_build_segmentation_audit__mutmut_70 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_71'] = x_build_segmentation_audit__mutmut_71 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_72'] = x_build_segmentation_audit__mutmut_72 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_73'] = x_build_segmentation_audit__mutmut_73 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_74'] = x_build_segmentation_audit__mutmut_74 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_75'] = x_build_segmentation_audit__mutmut_75 # type: ignore # mutmut generated
mutants_x_build_segmentation_audit__mutmut['x_build_segmentation_audit__mutmut_76'] = x_build_segmentation_audit__mutmut_76 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_not_installed_segmentation_audit__mutmut)
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


def x_not_installed_segmentation_audit__mutmut_orig() -> CiliumSegmentationAuditResult:
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


def x_not_installed_segmentation_audit__mutmut_1() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=None,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_2() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status=None,
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_3() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view=None,
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_4() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=None,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_5() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=None,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_6() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=None,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_7() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=None,
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_8() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_9() -> CiliumSegmentationAuditResult:
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
        note=None,
    )


def x_not_installed_segmentation_audit__mutmut_10() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_11() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_12() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_13() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_14() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_15() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_16() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_17() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_18() -> CiliumSegmentationAuditResult:
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
        )


def x_not_installed_segmentation_audit__mutmut_19() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=True,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_20() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="XXnot_installedXX",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_21() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="NOT_INSTALLED",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_22() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="XXvanillaXX",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_23() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="VANILLA",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_24() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=1,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_25() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=1,
        uncovered_paths=0,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_26() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=1,
        findings=[],
        summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_27() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="XXCilium is not installed; vanilla NetworkPolicy view is out of scopeXX",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_28() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="cilium is not installed; vanilla networkpolicy view is out of scope",
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_segmentation_audit__mutmut_29() -> CiliumSegmentationAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated reachability matrix."""
    return CiliumSegmentationAuditResult(
        installed=False,
        status="not_installed",
        view="vanilla",
        total_identities=0,
        total_paths=0,
        uncovered_paths=0,
        findings=[],
        summary="CILIUM IS NOT INSTALLED; VANILLA NETWORKPOLICY VIEW IS OUT OF SCOPE",
        note=_NOT_INSTALLED_NOTE,
    )

mutants_x_not_installed_segmentation_audit__mutmut['_mutmut_orig'] = x_not_installed_segmentation_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_1'] = x_not_installed_segmentation_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_2'] = x_not_installed_segmentation_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_3'] = x_not_installed_segmentation_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_4'] = x_not_installed_segmentation_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_5'] = x_not_installed_segmentation_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_6'] = x_not_installed_segmentation_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_7'] = x_not_installed_segmentation_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_8'] = x_not_installed_segmentation_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_9'] = x_not_installed_segmentation_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_10'] = x_not_installed_segmentation_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_11'] = x_not_installed_segmentation_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_12'] = x_not_installed_segmentation_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_13'] = x_not_installed_segmentation_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_14'] = x_not_installed_segmentation_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_15'] = x_not_installed_segmentation_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_16'] = x_not_installed_segmentation_audit__mutmut_16 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_17'] = x_not_installed_segmentation_audit__mutmut_17 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_18'] = x_not_installed_segmentation_audit__mutmut_18 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_19'] = x_not_installed_segmentation_audit__mutmut_19 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_20'] = x_not_installed_segmentation_audit__mutmut_20 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_21'] = x_not_installed_segmentation_audit__mutmut_21 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_22'] = x_not_installed_segmentation_audit__mutmut_22 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_23'] = x_not_installed_segmentation_audit__mutmut_23 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_24'] = x_not_installed_segmentation_audit__mutmut_24 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_25'] = x_not_installed_segmentation_audit__mutmut_25 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_26'] = x_not_installed_segmentation_audit__mutmut_26 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_27'] = x_not_installed_segmentation_audit__mutmut_27 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_28'] = x_not_installed_segmentation_audit__mutmut_28 # type: ignore # mutmut generated
mutants_x_not_installed_segmentation_audit__mutmut['x_not_installed_segmentation_audit__mutmut_29'] = x_not_installed_segmentation_audit__mutmut_29 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__path_unrestricted__mutmut)
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


def x__path_unrestricted__mutmut_orig(
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


def x__path_unrestricted__mutmut_1(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = None
    source_egress = any(
        _policy_selects(policy, source) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_2(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        None
    )
    source_egress = any(
        _policy_selects(policy, source) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_3(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, destination) or policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(policy, source) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_4(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(None, destination) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(policy, source) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_5(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, None) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(policy, source) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_6(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(destination) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(policy, source) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_7(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, ) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(policy, source) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_8(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, destination) and policy.ingress_rule_count >= 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(policy, source) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_9(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, destination) and policy.ingress_rule_count > 1
        for policy in policies
    )
    source_egress = any(
        _policy_selects(policy, source) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_10(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, destination) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = None
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_11(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, destination) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        None
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_12(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, destination) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(policy, source) or policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_13(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, destination) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(None, source) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_14(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, destination) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(policy, None) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_15(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, destination) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(source) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_16(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, destination) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(policy, ) and policy.egress_rule_count > 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_17(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, destination) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(policy, source) and policy.egress_rule_count >= 0 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_18(
    source: CiliumIdentityInfo,
    destination: CiliumIdentityInfo,
    policies: list[CiliumNetworkPolicyInfo],
) -> bool:
    destination_ingress = any(
        _policy_selects(policy, destination) and policy.ingress_rule_count > 0
        for policy in policies
    )
    source_egress = any(
        _policy_selects(policy, source) and policy.egress_rule_count > 1 for policy in policies
    )
    return not destination_ingress and not source_egress


def x__path_unrestricted__mutmut_19(
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
    return not destination_ingress or not source_egress


def x__path_unrestricted__mutmut_20(
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
    return destination_ingress and not source_egress


def x__path_unrestricted__mutmut_21(
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
    return not destination_ingress and source_egress

mutants_x__path_unrestricted__mutmut['_mutmut_orig'] = x__path_unrestricted__mutmut_orig # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_1'] = x__path_unrestricted__mutmut_1 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_2'] = x__path_unrestricted__mutmut_2 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_3'] = x__path_unrestricted__mutmut_3 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_4'] = x__path_unrestricted__mutmut_4 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_5'] = x__path_unrestricted__mutmut_5 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_6'] = x__path_unrestricted__mutmut_6 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_7'] = x__path_unrestricted__mutmut_7 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_8'] = x__path_unrestricted__mutmut_8 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_9'] = x__path_unrestricted__mutmut_9 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_10'] = x__path_unrestricted__mutmut_10 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_11'] = x__path_unrestricted__mutmut_11 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_12'] = x__path_unrestricted__mutmut_12 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_13'] = x__path_unrestricted__mutmut_13 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_14'] = x__path_unrestricted__mutmut_14 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_15'] = x__path_unrestricted__mutmut_15 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_16'] = x__path_unrestricted__mutmut_16 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_17'] = x__path_unrestricted__mutmut_17 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_18'] = x__path_unrestricted__mutmut_18 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_19'] = x__path_unrestricted__mutmut_19 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_20'] = x__path_unrestricted__mutmut_20 # type: ignore # mutmut generated
mutants_x__path_unrestricted__mutmut['x__path_unrestricted__mutmut_21'] = x__path_unrestricted__mutmut_21 # type: ignore # mutmut generated
mutants_x__policy_selects__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__policy_selects__mutmut)
def _policy_selects(policy: CiliumNetworkPolicyInfo, identity: CiliumIdentityInfo) -> bool:
    return selector_matches(_labels_to_dict(identity.labels), policy.endpoint_labels)


def x__policy_selects__mutmut_orig(policy: CiliumNetworkPolicyInfo, identity: CiliumIdentityInfo) -> bool:
    return selector_matches(_labels_to_dict(identity.labels), policy.endpoint_labels)


def x__policy_selects__mutmut_1(policy: CiliumNetworkPolicyInfo, identity: CiliumIdentityInfo) -> bool:
    return selector_matches(None, policy.endpoint_labels)


def x__policy_selects__mutmut_2(policy: CiliumNetworkPolicyInfo, identity: CiliumIdentityInfo) -> bool:
    return selector_matches(_labels_to_dict(identity.labels), None)


def x__policy_selects__mutmut_3(policy: CiliumNetworkPolicyInfo, identity: CiliumIdentityInfo) -> bool:
    return selector_matches(policy.endpoint_labels)


def x__policy_selects__mutmut_4(policy: CiliumNetworkPolicyInfo, identity: CiliumIdentityInfo) -> bool:
    return selector_matches(_labels_to_dict(identity.labels), )


def x__policy_selects__mutmut_5(policy: CiliumNetworkPolicyInfo, identity: CiliumIdentityInfo) -> bool:
    return selector_matches(_labels_to_dict(None), policy.endpoint_labels)

mutants_x__policy_selects__mutmut['_mutmut_orig'] = x__policy_selects__mutmut_orig # type: ignore # mutmut generated
mutants_x__policy_selects__mutmut['x__policy_selects__mutmut_1'] = x__policy_selects__mutmut_1 # type: ignore # mutmut generated
mutants_x__policy_selects__mutmut['x__policy_selects__mutmut_2'] = x__policy_selects__mutmut_2 # type: ignore # mutmut generated
mutants_x__policy_selects__mutmut['x__policy_selects__mutmut_3'] = x__policy_selects__mutmut_3 # type: ignore # mutmut generated
mutants_x__policy_selects__mutmut['x__policy_selects__mutmut_4'] = x__policy_selects__mutmut_4 # type: ignore # mutmut generated
mutants_x__policy_selects__mutmut['x__policy_selects__mutmut_5'] = x__policy_selects__mutmut_5 # type: ignore # mutmut generated
mutants_x__labels_to_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__labels_to_dict__mutmut)
def _labels_to_dict(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "=" in label:
            key, value = label.split("=", 1)
            result[key] = value
    return result


def x__labels_to_dict__mutmut_orig(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "=" in label:
            key, value = label.split("=", 1)
            result[key] = value
    return result


def x__labels_to_dict__mutmut_1(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = None
    for label in labels:
        if "=" in label:
            key, value = label.split("=", 1)
            result[key] = value
    return result


def x__labels_to_dict__mutmut_2(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "XX=XX" in label:
            key, value = label.split("=", 1)
            result[key] = value
    return result


def x__labels_to_dict__mutmut_3(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "=" not in label:
            key, value = label.split("=", 1)
            result[key] = value
    return result


def x__labels_to_dict__mutmut_4(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "=" in label:
            key, value = None
            result[key] = value
    return result


def x__labels_to_dict__mutmut_5(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "=" in label:
            key, value = label.split(None, 1)
            result[key] = value
    return result


def x__labels_to_dict__mutmut_6(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "=" in label:
            key, value = label.split("=", None)
            result[key] = value
    return result


def x__labels_to_dict__mutmut_7(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "=" in label:
            key, value = label.split(1)
            result[key] = value
    return result


def x__labels_to_dict__mutmut_8(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "=" in label:
            key, value = label.split("=", )
            result[key] = value
    return result


def x__labels_to_dict__mutmut_9(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "=" in label:
            key, value = label.rsplit("=", 1)
            result[key] = value
    return result


def x__labels_to_dict__mutmut_10(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "=" in label:
            key, value = label.split("XX=XX", 1)
            result[key] = value
    return result


def x__labels_to_dict__mutmut_11(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "=" in label:
            key, value = label.split("=", 2)
            result[key] = value
    return result


def x__labels_to_dict__mutmut_12(labels: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for label in labels:
        if "=" in label:
            key, value = label.split("=", 1)
            result[key] = None
    return result

mutants_x__labels_to_dict__mutmut['_mutmut_orig'] = x__labels_to_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__labels_to_dict__mutmut['x__labels_to_dict__mutmut_1'] = x__labels_to_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__labels_to_dict__mutmut['x__labels_to_dict__mutmut_2'] = x__labels_to_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__labels_to_dict__mutmut['x__labels_to_dict__mutmut_3'] = x__labels_to_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__labels_to_dict__mutmut['x__labels_to_dict__mutmut_4'] = x__labels_to_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__labels_to_dict__mutmut['x__labels_to_dict__mutmut_5'] = x__labels_to_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__labels_to_dict__mutmut['x__labels_to_dict__mutmut_6'] = x__labels_to_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__labels_to_dict__mutmut['x__labels_to_dict__mutmut_7'] = x__labels_to_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__labels_to_dict__mutmut['x__labels_to_dict__mutmut_8'] = x__labels_to_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__labels_to_dict__mutmut['x__labels_to_dict__mutmut_9'] = x__labels_to_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__labels_to_dict__mutmut['x__labels_to_dict__mutmut_10'] = x__labels_to_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__labels_to_dict__mutmut['x__labels_to_dict__mutmut_11'] = x__labels_to_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__labels_to_dict__mutmut['x__labels_to_dict__mutmut_12'] = x__labels_to_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__finding__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__finding__mutmut)
def _finding(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=destination.id,
        source_labels=source.labels,
        destination_labels=destination.labels,
        severity="high",
        note=_UNRESTRICTED_NOTE,
    )


def x__finding__mutmut_orig(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=destination.id,
        source_labels=source.labels,
        destination_labels=destination.labels,
        severity="high",
        note=_UNRESTRICTED_NOTE,
    )


def x__finding__mutmut_1(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=None,
        destination_id=destination.id,
        source_labels=source.labels,
        destination_labels=destination.labels,
        severity="high",
        note=_UNRESTRICTED_NOTE,
    )


def x__finding__mutmut_2(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=None,
        source_labels=source.labels,
        destination_labels=destination.labels,
        severity="high",
        note=_UNRESTRICTED_NOTE,
    )


def x__finding__mutmut_3(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=destination.id,
        source_labels=None,
        destination_labels=destination.labels,
        severity="high",
        note=_UNRESTRICTED_NOTE,
    )


def x__finding__mutmut_4(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=destination.id,
        source_labels=source.labels,
        destination_labels=None,
        severity="high",
        note=_UNRESTRICTED_NOTE,
    )


def x__finding__mutmut_5(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=destination.id,
        source_labels=source.labels,
        destination_labels=destination.labels,
        severity=None,
        note=_UNRESTRICTED_NOTE,
    )


def x__finding__mutmut_6(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=destination.id,
        source_labels=source.labels,
        destination_labels=destination.labels,
        severity="high",
        note=None,
    )


def x__finding__mutmut_7(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        destination_id=destination.id,
        source_labels=source.labels,
        destination_labels=destination.labels,
        severity="high",
        note=_UNRESTRICTED_NOTE,
    )


def x__finding__mutmut_8(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        source_labels=source.labels,
        destination_labels=destination.labels,
        severity="high",
        note=_UNRESTRICTED_NOTE,
    )


def x__finding__mutmut_9(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=destination.id,
        destination_labels=destination.labels,
        severity="high",
        note=_UNRESTRICTED_NOTE,
    )


def x__finding__mutmut_10(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=destination.id,
        source_labels=source.labels,
        severity="high",
        note=_UNRESTRICTED_NOTE,
    )


def x__finding__mutmut_11(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=destination.id,
        source_labels=source.labels,
        destination_labels=destination.labels,
        note=_UNRESTRICTED_NOTE,
    )


def x__finding__mutmut_12(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=destination.id,
        source_labels=source.labels,
        destination_labels=destination.labels,
        severity="high",
        )


def x__finding__mutmut_13(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=destination.id,
        source_labels=source.labels,
        destination_labels=destination.labels,
        severity="XXhighXX",
        note=_UNRESTRICTED_NOTE,
    )


def x__finding__mutmut_14(source: CiliumIdentityInfo, destination: CiliumIdentityInfo) -> CiliumPathFinding:
    return CiliumPathFinding(
        source_id=source.id,
        destination_id=destination.id,
        source_labels=source.labels,
        destination_labels=destination.labels,
        severity="HIGH",
        note=_UNRESTRICTED_NOTE,
    )

mutants_x__finding__mutmut['_mutmut_orig'] = x__finding__mutmut_orig # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_1'] = x__finding__mutmut_1 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_2'] = x__finding__mutmut_2 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_3'] = x__finding__mutmut_3 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_4'] = x__finding__mutmut_4 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_5'] = x__finding__mutmut_5 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_6'] = x__finding__mutmut_6 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_7'] = x__finding__mutmut_7 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_8'] = x__finding__mutmut_8 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_9'] = x__finding__mutmut_9 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_10'] = x__finding__mutmut_10 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_11'] = x__finding__mutmut_11 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_12'] = x__finding__mutmut_12 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_13'] = x__finding__mutmut_13 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_14'] = x__finding__mutmut_14 # type: ignore # mutmut generated
