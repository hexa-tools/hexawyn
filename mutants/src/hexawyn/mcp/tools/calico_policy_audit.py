"""MCP tool: calico_policy_audit — audit Calico L3/L4 coverage gaps."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_policy_audit.calico_policy_audit_use_case import (
    CalicoPolicyAuditUseCase,
)
from hexawyn.application.use_case.calico.calico_policy_audit.command import (
    CalicoPolicyAuditCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__gap_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__gap_dict__mutmut)
def _gap_dict(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_orig(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_1(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "XXnamespaceXX": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_2(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "NAMESPACE": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_3(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(None, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_4(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, None, None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_5(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr("namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_6(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_7(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", ),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_8(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "XXnamespaceXX", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_9(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "NAMESPACE", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_10(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "XXworkload_countXX": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_11(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "WORKLOAD_COUNT": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_12(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(None, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_13(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, None, 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_14(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", None),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_15(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr("workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_16(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_17(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", ),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_18(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "XXworkload_countXX", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_19(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "WORKLOAD_COUNT", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_20(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 1),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_21(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "XXpolicy_countXX": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_22(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "POLICY_COUNT": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_23(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(None, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_24(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, None, 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_25(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", None),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_26(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr("policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_27(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_28(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", ),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_29(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "XXpolicy_countXX", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_30(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "POLICY_COUNT", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_31(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 1),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_32(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "XXissueXX": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_33(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "ISSUE": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_34(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(None, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_35(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, None, None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_36(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr("issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_37(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_38(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", ),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_39(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "XXissueXX", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_40(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "ISSUE", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_41(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "XXnetwork_statusXX": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_42(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "NETWORK_STATUS": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_43(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(None, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_44(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, None, None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_45(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr("network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_46(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_47(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", ),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_48(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "XXnetwork_statusXX", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_49(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "NETWORK_STATUS", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_50(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "XXrisk_levelXX": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_51(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "RISK_LEVEL": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_52(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(None, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_53(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, None, None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_54(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr("risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_55(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_56(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", ),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_57(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "XXrisk_levelXX", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_58(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "RISK_LEVEL", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_59(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "XXselectorsXX": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_60(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "SELECTORS": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_61(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(None),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_62(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(None, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_63(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, None, ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_64(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", None)),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_65(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr("selectors", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_66(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_67(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", )),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_68(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "XXselectorsXX", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_69(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "SELECTORS", ())),
        "note": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_70(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "XXnoteXX": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_71(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "NOTE": getattr(gap, "note", None),
    }


def x__gap_dict__mutmut_72(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(None, "note", None),
    }


def x__gap_dict__mutmut_73(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, None, None),
    }


def x__gap_dict__mutmut_74(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr("note", None),
    }


def x__gap_dict__mutmut_75(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, None),
    }


def x__gap_dict__mutmut_76(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", ),
    }


def x__gap_dict__mutmut_77(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "XXnoteXX", None),
    }


def x__gap_dict__mutmut_78(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "NOTE", None),
    }

mutants_x__gap_dict__mutmut['_mutmut_orig'] = x__gap_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_1'] = x__gap_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_2'] = x__gap_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_3'] = x__gap_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_4'] = x__gap_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_5'] = x__gap_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_6'] = x__gap_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_7'] = x__gap_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_8'] = x__gap_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_9'] = x__gap_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_10'] = x__gap_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_11'] = x__gap_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_12'] = x__gap_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_13'] = x__gap_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_14'] = x__gap_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_15'] = x__gap_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_16'] = x__gap_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_17'] = x__gap_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_18'] = x__gap_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_19'] = x__gap_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_20'] = x__gap_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_21'] = x__gap_dict__mutmut_21 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_22'] = x__gap_dict__mutmut_22 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_23'] = x__gap_dict__mutmut_23 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_24'] = x__gap_dict__mutmut_24 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_25'] = x__gap_dict__mutmut_25 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_26'] = x__gap_dict__mutmut_26 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_27'] = x__gap_dict__mutmut_27 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_28'] = x__gap_dict__mutmut_28 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_29'] = x__gap_dict__mutmut_29 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_30'] = x__gap_dict__mutmut_30 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_31'] = x__gap_dict__mutmut_31 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_32'] = x__gap_dict__mutmut_32 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_33'] = x__gap_dict__mutmut_33 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_34'] = x__gap_dict__mutmut_34 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_35'] = x__gap_dict__mutmut_35 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_36'] = x__gap_dict__mutmut_36 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_37'] = x__gap_dict__mutmut_37 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_38'] = x__gap_dict__mutmut_38 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_39'] = x__gap_dict__mutmut_39 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_40'] = x__gap_dict__mutmut_40 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_41'] = x__gap_dict__mutmut_41 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_42'] = x__gap_dict__mutmut_42 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_43'] = x__gap_dict__mutmut_43 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_44'] = x__gap_dict__mutmut_44 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_45'] = x__gap_dict__mutmut_45 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_46'] = x__gap_dict__mutmut_46 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_47'] = x__gap_dict__mutmut_47 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_48'] = x__gap_dict__mutmut_48 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_49'] = x__gap_dict__mutmut_49 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_50'] = x__gap_dict__mutmut_50 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_51'] = x__gap_dict__mutmut_51 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_52'] = x__gap_dict__mutmut_52 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_53'] = x__gap_dict__mutmut_53 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_54'] = x__gap_dict__mutmut_54 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_55'] = x__gap_dict__mutmut_55 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_56'] = x__gap_dict__mutmut_56 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_57'] = x__gap_dict__mutmut_57 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_58'] = x__gap_dict__mutmut_58 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_59'] = x__gap_dict__mutmut_59 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_60'] = x__gap_dict__mutmut_60 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_61'] = x__gap_dict__mutmut_61 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_62'] = x__gap_dict__mutmut_62 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_63'] = x__gap_dict__mutmut_63 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_64'] = x__gap_dict__mutmut_64 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_65'] = x__gap_dict__mutmut_65 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_66'] = x__gap_dict__mutmut_66 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_67'] = x__gap_dict__mutmut_67 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_68'] = x__gap_dict__mutmut_68 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_69'] = x__gap_dict__mutmut_69 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_70'] = x__gap_dict__mutmut_70 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_71'] = x__gap_dict__mutmut_71 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_72'] = x__gap_dict__mutmut_72 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_73'] = x__gap_dict__mutmut_73 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_74'] = x__gap_dict__mutmut_74 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_75'] = x__gap_dict__mutmut_75 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_76'] = x__gap_dict__mutmut_76 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_77'] = x__gap_dict__mutmut_77 # type: ignore # mutmut generated
mutants_x__gap_dict__mutmut['x__gap_dict__mutmut_78'] = x__gap_dict__mutmut_78 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_calico_policy_audit__mutmut)
def calico_policy_audit(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_orig(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_1(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = None
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_2(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=None)
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_3(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = None
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_4(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=None,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_5(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=None,
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_6(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_7(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_8(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces and (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_9(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = None
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_10(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_11(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "XXinstalledXX": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_12(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "INSTALLED": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_13(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "XXnot_installed_markerXX": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_14(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "NOT_INSTALLED_MARKER": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_15(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "XXdegraded_to_vanillaXX": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_16(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "DEGRADED_TO_VANILLA": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_17(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "XXtotal_namespaces_checkedXX": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_18(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "TOTAL_NAMESPACES_CHECKED": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_19(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "XXgap_countXX": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_20(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "GAP_COUNT": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_21(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "XXfindingsXX": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_22(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "FINDINGS": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_23(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(None) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_24(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "XXsummaryXX": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_25(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "SUMMARY": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_26(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_27(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_28(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_29(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_30(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_31(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXnot_installed_markerXX": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_32(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "NOT_INSTALLED_MARKER": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_33(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "XXNOT_INSTALLEDXX",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_34(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "not_installed",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_35(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "XXdegraded_to_vanillaXX": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_36(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "DEGRADED_TO_VANILLA": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_37(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": False,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_38(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "XXtotal_namespaces_checkedXX": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_39(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "TOTAL_NAMESPACES_CHECKED": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_40(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 1,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_41(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "XXgap_countXX": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_42(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "GAP_COUNT": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_43(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 1,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_44(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "XXfindingsXX": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_45(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "FINDINGS": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_46(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "XXsummaryXX": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_47(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "SUMMARY": None,
            "error": str(exc),
        }


def x_calico_policy_audit__mutmut_48(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "XXerrorXX": str(exc),
        }


def x_calico_policy_audit__mutmut_49(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "ERROR": str(exc),
        }


def x_calico_policy_audit__mutmut_50(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(None),
        }

mutants_x_calico_policy_audit__mutmut['_mutmut_orig'] = x_calico_policy_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_1'] = x_calico_policy_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_2'] = x_calico_policy_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_3'] = x_calico_policy_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_4'] = x_calico_policy_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_5'] = x_calico_policy_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_6'] = x_calico_policy_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_7'] = x_calico_policy_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_8'] = x_calico_policy_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_9'] = x_calico_policy_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_10'] = x_calico_policy_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_11'] = x_calico_policy_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_12'] = x_calico_policy_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_13'] = x_calico_policy_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_14'] = x_calico_policy_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_15'] = x_calico_policy_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_16'] = x_calico_policy_audit__mutmut_16 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_17'] = x_calico_policy_audit__mutmut_17 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_18'] = x_calico_policy_audit__mutmut_18 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_19'] = x_calico_policy_audit__mutmut_19 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_20'] = x_calico_policy_audit__mutmut_20 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_21'] = x_calico_policy_audit__mutmut_21 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_22'] = x_calico_policy_audit__mutmut_22 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_23'] = x_calico_policy_audit__mutmut_23 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_24'] = x_calico_policy_audit__mutmut_24 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_25'] = x_calico_policy_audit__mutmut_25 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_26'] = x_calico_policy_audit__mutmut_26 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_27'] = x_calico_policy_audit__mutmut_27 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_28'] = x_calico_policy_audit__mutmut_28 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_29'] = x_calico_policy_audit__mutmut_29 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_30'] = x_calico_policy_audit__mutmut_30 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_31'] = x_calico_policy_audit__mutmut_31 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_32'] = x_calico_policy_audit__mutmut_32 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_33'] = x_calico_policy_audit__mutmut_33 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_34'] = x_calico_policy_audit__mutmut_34 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_35'] = x_calico_policy_audit__mutmut_35 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_36'] = x_calico_policy_audit__mutmut_36 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_37'] = x_calico_policy_audit__mutmut_37 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_38'] = x_calico_policy_audit__mutmut_38 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_39'] = x_calico_policy_audit__mutmut_39 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_40'] = x_calico_policy_audit__mutmut_40 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_41'] = x_calico_policy_audit__mutmut_41 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_42'] = x_calico_policy_audit__mutmut_42 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_43'] = x_calico_policy_audit__mutmut_43 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_44'] = x_calico_policy_audit__mutmut_44 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_45'] = x_calico_policy_audit__mutmut_45 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_46'] = x_calico_policy_audit__mutmut_46 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_47'] = x_calico_policy_audit__mutmut_47 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_48'] = x_calico_policy_audit__mutmut_48 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_49'] = x_calico_policy_audit__mutmut_49 # type: ignore # mutmut generated
mutants_x_calico_policy_audit__mutmut['x_calico_policy_audit__mutmut_50'] = x_calico_policy_audit__mutmut_50 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_policy_audit)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(calico_policy_audit)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
