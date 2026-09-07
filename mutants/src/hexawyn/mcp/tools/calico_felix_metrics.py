"""MCP tool: calico_felix_metrics — per-policy Felix allow/deny counters."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_felix_metrics.calico_felix_metrics_use_case import (
    CalicoFelixMetricsUseCase,
)
from hexawyn.application.use_case.calico.calico_felix_metrics.command import (
    CalicoFelixMetricsCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__policy_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__policy_dict__mutmut)
def _policy_dict(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_orig(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_1(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "XXpolicyXX": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_2(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "POLICY": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_3(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(None, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_4(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, None, None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_5(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr("policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_6(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_7(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", ),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_8(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "XXpolicyXX", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_9(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "POLICY", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_10(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "XXallow_packetsXX": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_11(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "ALLOW_PACKETS": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_12(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(None, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_13(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, None, 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_14(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", None),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_15(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr("allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_16(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_17(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", ),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_18(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "XXallow_packetsXX", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_19(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "ALLOW_PACKETS", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_20(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 1),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_21(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "XXdeny_packetsXX": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_22(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "DENY_PACKETS": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_23(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(None, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_24(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, None, 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_25(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", None),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_26(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr("deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_27(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_28(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", ),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_29(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "XXdeny_packetsXX", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_30(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "DENY_PACKETS", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_31(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 1),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_32(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "XXallow_bytesXX": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_33(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "ALLOW_BYTES": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_34(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(None, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_35(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, None, 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_36(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", None),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_37(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr("allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_38(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_39(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", ),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_40(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "XXallow_bytesXX", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_41(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "ALLOW_BYTES", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_42(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 1),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_43(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "XXdeny_bytesXX": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_44(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "DENY_BYTES": getattr(counter, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_45(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(None, "deny_bytes", 0),
    }


def x__policy_dict__mutmut_46(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, None, 0),
    }


def x__policy_dict__mutmut_47(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", None),
    }


def x__policy_dict__mutmut_48(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr("deny_bytes", 0),
    }


def x__policy_dict__mutmut_49(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, 0),
    }


def x__policy_dict__mutmut_50(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", ),
    }


def x__policy_dict__mutmut_51(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "XXdeny_bytesXX", 0),
    }


def x__policy_dict__mutmut_52(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "DENY_BYTES", 0),
    }


def x__policy_dict__mutmut_53(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 1),
    }

mutants_x__policy_dict__mutmut['_mutmut_orig'] = x__policy_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_1'] = x__policy_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_2'] = x__policy_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_3'] = x__policy_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_4'] = x__policy_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_5'] = x__policy_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_6'] = x__policy_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_7'] = x__policy_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_8'] = x__policy_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_9'] = x__policy_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_10'] = x__policy_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_11'] = x__policy_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_12'] = x__policy_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_13'] = x__policy_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_14'] = x__policy_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_15'] = x__policy_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_16'] = x__policy_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_17'] = x__policy_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_18'] = x__policy_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_19'] = x__policy_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_20'] = x__policy_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_21'] = x__policy_dict__mutmut_21 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_22'] = x__policy_dict__mutmut_22 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_23'] = x__policy_dict__mutmut_23 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_24'] = x__policy_dict__mutmut_24 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_25'] = x__policy_dict__mutmut_25 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_26'] = x__policy_dict__mutmut_26 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_27'] = x__policy_dict__mutmut_27 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_28'] = x__policy_dict__mutmut_28 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_29'] = x__policy_dict__mutmut_29 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_30'] = x__policy_dict__mutmut_30 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_31'] = x__policy_dict__mutmut_31 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_32'] = x__policy_dict__mutmut_32 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_33'] = x__policy_dict__mutmut_33 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_34'] = x__policy_dict__mutmut_34 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_35'] = x__policy_dict__mutmut_35 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_36'] = x__policy_dict__mutmut_36 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_37'] = x__policy_dict__mutmut_37 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_38'] = x__policy_dict__mutmut_38 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_39'] = x__policy_dict__mutmut_39 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_40'] = x__policy_dict__mutmut_40 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_41'] = x__policy_dict__mutmut_41 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_42'] = x__policy_dict__mutmut_42 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_43'] = x__policy_dict__mutmut_43 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_44'] = x__policy_dict__mutmut_44 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_45'] = x__policy_dict__mutmut_45 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_46'] = x__policy_dict__mutmut_46 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_47'] = x__policy_dict__mutmut_47 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_48'] = x__policy_dict__mutmut_48 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_49'] = x__policy_dict__mutmut_49 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_50'] = x__policy_dict__mutmut_50 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_51'] = x__policy_dict__mutmut_51 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_52'] = x__policy_dict__mutmut_52 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_53'] = x__policy_dict__mutmut_53 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_calico_felix_metrics__mutmut)
def calico_felix_metrics() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = None
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=None)
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = None
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "XXinstalledXX": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "INSTALLED": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "XXnot_installed_markerXX": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "NOT_INSTALLED_MARKER": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "XXmetrics_availableXX": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "METRICS_AVAILABLE": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "XXmetrics_messageXX": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "METRICS_MESSAGE": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "XXtotal_deniesXX": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "TOTAL_DENIES": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "XXtotal_allowsXX": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "TOTAL_ALLOWS": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "XXdeny_policy_countXX": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "DENY_POLICY_COUNT": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "XXpoliciesXX": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "POLICIES": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(None) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_24() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_25() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_26() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_27() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXnot_installed_markerXX": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_28() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "NOT_INSTALLED_MARKER": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_29() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "XXNOT_INSTALLEDXX",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_30() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "not_installed",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_31() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "XXmetrics_availableXX": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_32() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "METRICS_AVAILABLE": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_33() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": True,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_34() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "XXmetrics_messageXX": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_35() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "METRICS_MESSAGE": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_36() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "XXtotal_deniesXX": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_37() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "TOTAL_DENIES": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_38() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 1,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_39() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "XXtotal_allowsXX": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_40() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "TOTAL_ALLOWS": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_41() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 1,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_42() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "XXdeny_policy_countXX": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_43() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "DENY_POLICY_COUNT": 0,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_44() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 1,
            "policies": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_45() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "XXpoliciesXX": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_46() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "POLICIES": [],
            "error": str(exc),
        }


def x_calico_felix_metrics__mutmut_47() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "XXerrorXX": str(exc),
        }


def x_calico_felix_metrics__mutmut_48() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "ERROR": str(exc),
        }


def x_calico_felix_metrics__mutmut_49() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(None),
        }

mutants_x_calico_felix_metrics__mutmut['_mutmut_orig'] = x_calico_felix_metrics__mutmut_orig # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_1'] = x_calico_felix_metrics__mutmut_1 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_2'] = x_calico_felix_metrics__mutmut_2 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_3'] = x_calico_felix_metrics__mutmut_3 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_4'] = x_calico_felix_metrics__mutmut_4 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_5'] = x_calico_felix_metrics__mutmut_5 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_6'] = x_calico_felix_metrics__mutmut_6 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_7'] = x_calico_felix_metrics__mutmut_7 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_8'] = x_calico_felix_metrics__mutmut_8 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_9'] = x_calico_felix_metrics__mutmut_9 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_10'] = x_calico_felix_metrics__mutmut_10 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_11'] = x_calico_felix_metrics__mutmut_11 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_12'] = x_calico_felix_metrics__mutmut_12 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_13'] = x_calico_felix_metrics__mutmut_13 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_14'] = x_calico_felix_metrics__mutmut_14 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_15'] = x_calico_felix_metrics__mutmut_15 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_16'] = x_calico_felix_metrics__mutmut_16 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_17'] = x_calico_felix_metrics__mutmut_17 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_18'] = x_calico_felix_metrics__mutmut_18 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_19'] = x_calico_felix_metrics__mutmut_19 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_20'] = x_calico_felix_metrics__mutmut_20 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_21'] = x_calico_felix_metrics__mutmut_21 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_22'] = x_calico_felix_metrics__mutmut_22 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_23'] = x_calico_felix_metrics__mutmut_23 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_24'] = x_calico_felix_metrics__mutmut_24 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_25'] = x_calico_felix_metrics__mutmut_25 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_26'] = x_calico_felix_metrics__mutmut_26 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_27'] = x_calico_felix_metrics__mutmut_27 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_28'] = x_calico_felix_metrics__mutmut_28 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_29'] = x_calico_felix_metrics__mutmut_29 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_30'] = x_calico_felix_metrics__mutmut_30 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_31'] = x_calico_felix_metrics__mutmut_31 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_32'] = x_calico_felix_metrics__mutmut_32 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_33'] = x_calico_felix_metrics__mutmut_33 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_34'] = x_calico_felix_metrics__mutmut_34 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_35'] = x_calico_felix_metrics__mutmut_35 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_36'] = x_calico_felix_metrics__mutmut_36 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_37'] = x_calico_felix_metrics__mutmut_37 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_38'] = x_calico_felix_metrics__mutmut_38 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_39'] = x_calico_felix_metrics__mutmut_39 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_40'] = x_calico_felix_metrics__mutmut_40 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_41'] = x_calico_felix_metrics__mutmut_41 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_42'] = x_calico_felix_metrics__mutmut_42 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_43'] = x_calico_felix_metrics__mutmut_43 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_44'] = x_calico_felix_metrics__mutmut_44 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_45'] = x_calico_felix_metrics__mutmut_45 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_46'] = x_calico_felix_metrics__mutmut_46 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_47'] = x_calico_felix_metrics__mutmut_47 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_48'] = x_calico_felix_metrics__mutmut_48 # type: ignore # mutmut generated
mutants_x_calico_felix_metrics__mutmut['x_calico_felix_metrics__mutmut_49'] = x_calico_felix_metrics__mutmut_49 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_felix_metrics)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(calico_felix_metrics)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
