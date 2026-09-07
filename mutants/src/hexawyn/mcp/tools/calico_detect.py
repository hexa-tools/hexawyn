"""MCP tool: calico_detect — detect if Calico is the active CNI and its health."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_detect.calico_detect_use_case import (
    CalicoDetectUseCase,
)
from hexawyn.application.use_case.calico.calico_detect.command import CalicoDetectCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__agent_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__agent_dict__mutmut)
def _agent_dict(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_orig(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_1(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "XXnodeXX": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_2(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "NODE": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_3(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(None, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_4(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, None, None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_5(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr("node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_6(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_7(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", ),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_8(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "XXnodeXX", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_9(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "NODE", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_10(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "XXphaseXX": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_11(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "PHASE": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_12(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(None, "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_13(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), None, getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_14(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", None),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_15(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr("value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_16(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_17(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", ),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_18(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(None, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_19(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, None, ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_20(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", None), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_21(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr("phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_22(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_23(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_24(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "XXphaseXX", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_25(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "PHASE", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_26(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", "XXXX"), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_27(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "XXvalueXX", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_28(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "VALUE", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_29(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(None, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_30(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, None, "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_31(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", None)),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_32(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr("phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_33(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_34(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", )),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_35(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "XXphaseXX", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_36(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "PHASE", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_37(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "XXXX")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_38(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "XXreadyXX": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_39(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "READY": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_40(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(None, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_41(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, None, False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_42(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", None),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_43(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr("ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_44(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_45(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", ),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_46(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "XXreadyXX", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_47(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "READY", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_48(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", True),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_49(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "XXready_replicasXX": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_50(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "READY_REPLICAS": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_51(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(None, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_52(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, None, 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_53(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", None),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_54(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr("ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_55(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_56(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", ),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_57(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "XXready_replicasXX", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_58(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "READY_REPLICAS", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_59(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 1),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_60(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "XXdesired_replicasXX": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_61(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "DESIRED_REPLICAS": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_62(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(None, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_63(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, None, 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_64(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", None),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_65(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr("desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_66(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_67(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", ),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_68(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "XXdesired_replicasXX", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_69(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "DESIRED_REPLICAS", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_70(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 1),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_71(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "XXavailable_replicasXX": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_72(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "AVAILABLE_REPLICAS": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_73(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(None, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_74(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, None, 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_75(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", None),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_76(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr("available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_77(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_78(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", ),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_79(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "XXavailable_replicasXX", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_80(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "AVAILABLE_REPLICAS", 0),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_81(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 1),
        "message": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_82(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "XXmessageXX": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_83(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "MESSAGE": getattr(agent, "message", None),
    }


def x__agent_dict__mutmut_84(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(None, "message", None),
    }


def x__agent_dict__mutmut_85(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, None, None),
    }


def x__agent_dict__mutmut_86(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr("message", None),
    }


def x__agent_dict__mutmut_87(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, None),
    }


def x__agent_dict__mutmut_88(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", ),
    }


def x__agent_dict__mutmut_89(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "XXmessageXX", None),
    }


def x__agent_dict__mutmut_90(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "MESSAGE", None),
    }

mutants_x__agent_dict__mutmut['_mutmut_orig'] = x__agent_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_1'] = x__agent_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_2'] = x__agent_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_3'] = x__agent_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_4'] = x__agent_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_5'] = x__agent_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_6'] = x__agent_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_7'] = x__agent_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_8'] = x__agent_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_9'] = x__agent_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_10'] = x__agent_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_11'] = x__agent_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_12'] = x__agent_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_13'] = x__agent_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_14'] = x__agent_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_15'] = x__agent_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_16'] = x__agent_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_17'] = x__agent_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_18'] = x__agent_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_19'] = x__agent_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_20'] = x__agent_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_21'] = x__agent_dict__mutmut_21 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_22'] = x__agent_dict__mutmut_22 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_23'] = x__agent_dict__mutmut_23 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_24'] = x__agent_dict__mutmut_24 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_25'] = x__agent_dict__mutmut_25 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_26'] = x__agent_dict__mutmut_26 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_27'] = x__agent_dict__mutmut_27 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_28'] = x__agent_dict__mutmut_28 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_29'] = x__agent_dict__mutmut_29 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_30'] = x__agent_dict__mutmut_30 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_31'] = x__agent_dict__mutmut_31 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_32'] = x__agent_dict__mutmut_32 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_33'] = x__agent_dict__mutmut_33 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_34'] = x__agent_dict__mutmut_34 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_35'] = x__agent_dict__mutmut_35 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_36'] = x__agent_dict__mutmut_36 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_37'] = x__agent_dict__mutmut_37 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_38'] = x__agent_dict__mutmut_38 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_39'] = x__agent_dict__mutmut_39 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_40'] = x__agent_dict__mutmut_40 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_41'] = x__agent_dict__mutmut_41 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_42'] = x__agent_dict__mutmut_42 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_43'] = x__agent_dict__mutmut_43 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_44'] = x__agent_dict__mutmut_44 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_45'] = x__agent_dict__mutmut_45 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_46'] = x__agent_dict__mutmut_46 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_47'] = x__agent_dict__mutmut_47 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_48'] = x__agent_dict__mutmut_48 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_49'] = x__agent_dict__mutmut_49 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_50'] = x__agent_dict__mutmut_50 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_51'] = x__agent_dict__mutmut_51 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_52'] = x__agent_dict__mutmut_52 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_53'] = x__agent_dict__mutmut_53 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_54'] = x__agent_dict__mutmut_54 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_55'] = x__agent_dict__mutmut_55 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_56'] = x__agent_dict__mutmut_56 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_57'] = x__agent_dict__mutmut_57 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_58'] = x__agent_dict__mutmut_58 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_59'] = x__agent_dict__mutmut_59 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_60'] = x__agent_dict__mutmut_60 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_61'] = x__agent_dict__mutmut_61 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_62'] = x__agent_dict__mutmut_62 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_63'] = x__agent_dict__mutmut_63 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_64'] = x__agent_dict__mutmut_64 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_65'] = x__agent_dict__mutmut_65 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_66'] = x__agent_dict__mutmut_66 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_67'] = x__agent_dict__mutmut_67 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_68'] = x__agent_dict__mutmut_68 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_69'] = x__agent_dict__mutmut_69 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_70'] = x__agent_dict__mutmut_70 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_71'] = x__agent_dict__mutmut_71 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_72'] = x__agent_dict__mutmut_72 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_73'] = x__agent_dict__mutmut_73 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_74'] = x__agent_dict__mutmut_74 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_75'] = x__agent_dict__mutmut_75 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_76'] = x__agent_dict__mutmut_76 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_77'] = x__agent_dict__mutmut_77 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_78'] = x__agent_dict__mutmut_78 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_79'] = x__agent_dict__mutmut_79 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_80'] = x__agent_dict__mutmut_80 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_81'] = x__agent_dict__mutmut_81 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_82'] = x__agent_dict__mutmut_82 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_83'] = x__agent_dict__mutmut_83 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_84'] = x__agent_dict__mutmut_84 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_85'] = x__agent_dict__mutmut_85 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_86'] = x__agent_dict__mutmut_86 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_87'] = x__agent_dict__mutmut_87 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_88'] = x__agent_dict__mutmut_88 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_89'] = x__agent_dict__mutmut_89 # type: ignore # mutmut generated
mutants_x__agent_dict__mutmut['x__agent_dict__mutmut_90'] = x__agent_dict__mutmut_90 # type: ignore # mutmut generated
mutants_x__empty__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__empty__mutmut)
def _empty(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_orig(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_1(error: str | None = None) -> dict[str, object]:
    return {
        "XXinstalledXX": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_2(error: str | None = None) -> dict[str, object]:
    return {
        "INSTALLED": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_3(error: str | None = None) -> dict[str, object]:
    return {
        "installed": True,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_4(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "XXstatusXX": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_5(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "STATUS": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_6(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "XXnot_installedXX",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_7(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "NOT_INSTALLED",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_8(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "XXnot_installed_markerXX": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_9(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "NOT_INSTALLED_MARKER": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_10(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "XXNOT_INSTALLEDXX",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_11(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "not_installed",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_12(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "XXversionXX": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_13(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "VERSION": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_14(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "XXmodeXX": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_15(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "MODE": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_16(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "XXnamespaceXX": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_17(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "NAMESPACE": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_18(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "XXtigera_operatorXX": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_19(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "TIGERA_OPERATOR": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_20(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": True,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_21(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "XXenterpriseXX": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_22(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "ENTERPRISE": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_23(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": True,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_24(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "XXagentsXX": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_25(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "AGENTS": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_26(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "XXtotal_nodesXX": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_27(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "TOTAL_NODES": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_28(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 1,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_29(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "XXready_agentsXX": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_30(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "READY_AGENTS": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_31(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 1,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_32(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "XXdegraded_agentsXX": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_33(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "DEGRADED_AGENTS": 0,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_34(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 1,
        "degraded_summary": None,
        "error": error,
    }


def x__empty__mutmut_35(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "XXdegraded_summaryXX": None,
        "error": error,
    }


def x__empty__mutmut_36(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "DEGRADED_SUMMARY": None,
        "error": error,
    }


def x__empty__mutmut_37(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "XXerrorXX": error,
    }


def x__empty__mutmut_38(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "ERROR": error,
    }

mutants_x__empty__mutmut['_mutmut_orig'] = x__empty__mutmut_orig # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_1'] = x__empty__mutmut_1 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_2'] = x__empty__mutmut_2 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_3'] = x__empty__mutmut_3 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_4'] = x__empty__mutmut_4 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_5'] = x__empty__mutmut_5 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_6'] = x__empty__mutmut_6 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_7'] = x__empty__mutmut_7 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_8'] = x__empty__mutmut_8 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_9'] = x__empty__mutmut_9 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_10'] = x__empty__mutmut_10 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_11'] = x__empty__mutmut_11 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_12'] = x__empty__mutmut_12 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_13'] = x__empty__mutmut_13 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_14'] = x__empty__mutmut_14 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_15'] = x__empty__mutmut_15 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_16'] = x__empty__mutmut_16 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_17'] = x__empty__mutmut_17 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_18'] = x__empty__mutmut_18 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_19'] = x__empty__mutmut_19 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_20'] = x__empty__mutmut_20 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_21'] = x__empty__mutmut_21 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_22'] = x__empty__mutmut_22 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_23'] = x__empty__mutmut_23 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_24'] = x__empty__mutmut_24 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_25'] = x__empty__mutmut_25 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_26'] = x__empty__mutmut_26 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_27'] = x__empty__mutmut_27 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_28'] = x__empty__mutmut_28 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_29'] = x__empty__mutmut_29 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_30'] = x__empty__mutmut_30 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_31'] = x__empty__mutmut_31 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_32'] = x__empty__mutmut_32 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_33'] = x__empty__mutmut_33 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_34'] = x__empty__mutmut_34 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_35'] = x__empty__mutmut_35 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_36'] = x__empty__mutmut_36 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_37'] = x__empty__mutmut_37 # type: ignore # mutmut generated
mutants_x__empty__mutmut['x__empty__mutmut_38'] = x__empty__mutmut_38 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_calico_detect__mutmut)
def calico_detect() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = None
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = None
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=None)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = None
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "XXinstalledXX": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "INSTALLED": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "XXstatusXX": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "STATUS": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "XXnot_installed_markerXX": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "NOT_INSTALLED_MARKER": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "XXversionXX": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "VERSION": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "XXmodeXX": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "MODE": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(None, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, None, result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", None),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr("value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", ),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "XXvalueXX", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "VALUE", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_24() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "XXnamespaceXX": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_25() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "NAMESPACE": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_26() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "XXtigera_operatorXX": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_27() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "TIGERA_OPERATOR": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_28() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "XXenterpriseXX": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_29() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "ENTERPRISE": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_30() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "XXagentsXX": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_31() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "AGENTS": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_32() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(None) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_33() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "XXtotal_nodesXX": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_34() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "TOTAL_NODES": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_35() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "XXready_agentsXX": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_36() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "READY_AGENTS": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_37() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "XXdegraded_agentsXX": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_38() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "DEGRADED_AGENTS": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_39() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "XXdegraded_summaryXX": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_40() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "DEGRADED_SUMMARY": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_41() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_42() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "ERROR": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_calico_detect__mutmut_43() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=None)


def x_calico_detect__mutmut_44() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(None))

mutants_x_calico_detect__mutmut['_mutmut_orig'] = x_calico_detect__mutmut_orig # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_1'] = x_calico_detect__mutmut_1 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_2'] = x_calico_detect__mutmut_2 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_3'] = x_calico_detect__mutmut_3 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_4'] = x_calico_detect__mutmut_4 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_5'] = x_calico_detect__mutmut_5 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_6'] = x_calico_detect__mutmut_6 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_7'] = x_calico_detect__mutmut_7 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_8'] = x_calico_detect__mutmut_8 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_9'] = x_calico_detect__mutmut_9 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_10'] = x_calico_detect__mutmut_10 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_11'] = x_calico_detect__mutmut_11 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_12'] = x_calico_detect__mutmut_12 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_13'] = x_calico_detect__mutmut_13 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_14'] = x_calico_detect__mutmut_14 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_15'] = x_calico_detect__mutmut_15 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_16'] = x_calico_detect__mutmut_16 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_17'] = x_calico_detect__mutmut_17 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_18'] = x_calico_detect__mutmut_18 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_19'] = x_calico_detect__mutmut_19 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_20'] = x_calico_detect__mutmut_20 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_21'] = x_calico_detect__mutmut_21 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_22'] = x_calico_detect__mutmut_22 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_23'] = x_calico_detect__mutmut_23 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_24'] = x_calico_detect__mutmut_24 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_25'] = x_calico_detect__mutmut_25 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_26'] = x_calico_detect__mutmut_26 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_27'] = x_calico_detect__mutmut_27 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_28'] = x_calico_detect__mutmut_28 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_29'] = x_calico_detect__mutmut_29 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_30'] = x_calico_detect__mutmut_30 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_31'] = x_calico_detect__mutmut_31 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_32'] = x_calico_detect__mutmut_32 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_33'] = x_calico_detect__mutmut_33 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_34'] = x_calico_detect__mutmut_34 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_35'] = x_calico_detect__mutmut_35 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_36'] = x_calico_detect__mutmut_36 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_37'] = x_calico_detect__mutmut_37 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_38'] = x_calico_detect__mutmut_38 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_39'] = x_calico_detect__mutmut_39 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_40'] = x_calico_detect__mutmut_40 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_41'] = x_calico_detect__mutmut_41 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_42'] = x_calico_detect__mutmut_42 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_43'] = x_calico_detect__mutmut_43 # type: ignore # mutmut generated
mutants_x_calico_detect__mutmut['x_calico_detect__mutmut_44'] = x_calico_detect__mutmut_44 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_detect)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(calico_detect)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
