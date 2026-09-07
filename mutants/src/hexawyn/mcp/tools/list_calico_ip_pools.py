"""MCP tool: list_calico_ip_pools — list Calico IPPools."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.list_calico_ip_pools.command import (
    ListCalicoIpPoolsCommand,
)
from hexawyn.application.use_case.calico.list_calico_ip_pools.list_calico_ip_pools_use_case import (
    ListCalicoIpPoolsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__pool_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__pool_dict__mutmut)
def _pool_dict(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_orig(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_1(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "XXnameXX": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_2(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "NAME": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_3(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(None, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_4(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, None, None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_5(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr("name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_6(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_7(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", ),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_8(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "XXnameXX", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_9(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "NAME", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_10(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "XXcidrXX": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_11(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "CIDR": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_12(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(None, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_13(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, None, None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_14(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr("cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_15(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_16(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", ),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_17(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "XXcidrXX", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_18(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "CIDR", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_19(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "XXdisabledXX": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_20(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "DISABLED": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_21(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(None, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_22(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, None, False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_23(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", None),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_24(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr("disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_25(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_26(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", ),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_27(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "XXdisabledXX", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_28(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "DISABLED", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_29(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", True),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_30(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "XXnat_outgoingXX": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_31(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "NAT_OUTGOING": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_32(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(None, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_33(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, None, False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_34(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", None),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_35(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr("nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_36(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_37(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", ),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_38(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "XXnat_outgoingXX", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_39(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "NAT_OUTGOING", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_40(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", True),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_41(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "XXnode_selectorXX": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_42(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "NODE_SELECTOR": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_43(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(None, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_44(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, None, ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_45(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", None),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_46(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr("node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_47(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_48(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_49(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "XXnode_selectorXX", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_50(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "NODE_SELECTOR", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_51(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", "XXXX"),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_52(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "XXipip_modeXX": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_53(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "IPIP_MODE": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_54(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(None, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_55(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, None, None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_56(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr("ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_57(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_58(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", ),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_59(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "XXipip_modeXX", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_60(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "IPIP_MODE", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_61(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "XXvxlan_modeXX": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_62(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "VXLAN_MODE": getattr(pool, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_63(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(None, "vxlan_mode", None),
    }


def x__pool_dict__mutmut_64(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, None, None),
    }


def x__pool_dict__mutmut_65(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr("vxlan_mode", None),
    }


def x__pool_dict__mutmut_66(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, None),
    }


def x__pool_dict__mutmut_67(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", ),
    }


def x__pool_dict__mutmut_68(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "XXvxlan_modeXX", None),
    }


def x__pool_dict__mutmut_69(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "VXLAN_MODE", None),
    }

mutants_x__pool_dict__mutmut['_mutmut_orig'] = x__pool_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_1'] = x__pool_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_2'] = x__pool_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_3'] = x__pool_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_4'] = x__pool_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_5'] = x__pool_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_6'] = x__pool_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_7'] = x__pool_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_8'] = x__pool_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_9'] = x__pool_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_10'] = x__pool_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_11'] = x__pool_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_12'] = x__pool_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_13'] = x__pool_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_14'] = x__pool_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_15'] = x__pool_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_16'] = x__pool_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_17'] = x__pool_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_18'] = x__pool_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_19'] = x__pool_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_20'] = x__pool_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_21'] = x__pool_dict__mutmut_21 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_22'] = x__pool_dict__mutmut_22 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_23'] = x__pool_dict__mutmut_23 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_24'] = x__pool_dict__mutmut_24 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_25'] = x__pool_dict__mutmut_25 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_26'] = x__pool_dict__mutmut_26 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_27'] = x__pool_dict__mutmut_27 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_28'] = x__pool_dict__mutmut_28 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_29'] = x__pool_dict__mutmut_29 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_30'] = x__pool_dict__mutmut_30 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_31'] = x__pool_dict__mutmut_31 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_32'] = x__pool_dict__mutmut_32 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_33'] = x__pool_dict__mutmut_33 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_34'] = x__pool_dict__mutmut_34 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_35'] = x__pool_dict__mutmut_35 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_36'] = x__pool_dict__mutmut_36 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_37'] = x__pool_dict__mutmut_37 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_38'] = x__pool_dict__mutmut_38 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_39'] = x__pool_dict__mutmut_39 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_40'] = x__pool_dict__mutmut_40 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_41'] = x__pool_dict__mutmut_41 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_42'] = x__pool_dict__mutmut_42 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_43'] = x__pool_dict__mutmut_43 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_44'] = x__pool_dict__mutmut_44 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_45'] = x__pool_dict__mutmut_45 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_46'] = x__pool_dict__mutmut_46 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_47'] = x__pool_dict__mutmut_47 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_48'] = x__pool_dict__mutmut_48 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_49'] = x__pool_dict__mutmut_49 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_50'] = x__pool_dict__mutmut_50 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_51'] = x__pool_dict__mutmut_51 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_52'] = x__pool_dict__mutmut_52 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_53'] = x__pool_dict__mutmut_53 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_54'] = x__pool_dict__mutmut_54 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_55'] = x__pool_dict__mutmut_55 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_56'] = x__pool_dict__mutmut_56 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_57'] = x__pool_dict__mutmut_57 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_58'] = x__pool_dict__mutmut_58 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_59'] = x__pool_dict__mutmut_59 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_60'] = x__pool_dict__mutmut_60 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_61'] = x__pool_dict__mutmut_61 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_62'] = x__pool_dict__mutmut_62 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_63'] = x__pool_dict__mutmut_63 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_64'] = x__pool_dict__mutmut_64 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_65'] = x__pool_dict__mutmut_65 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_66'] = x__pool_dict__mutmut_66 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_67'] = x__pool_dict__mutmut_67 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_68'] = x__pool_dict__mutmut_68 # type: ignore # mutmut generated
mutants_x__pool_dict__mutmut['x__pool_dict__mutmut_69'] = x__pool_dict__mutmut_69 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_calico_ip_pools__mutmut)
def list_calico_ip_pools() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = None
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=None)
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = None
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "XXinstalledXX": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "INSTALLED": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "XXnot_installed_markerXX": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "NOT_INSTALLED_MARKER": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "XXtotalXX": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "TOTAL": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "XXpoolsXX": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "POOLS": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(None) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXnot_installed_markerXX": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "NOT_INSTALLED_MARKER": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "XXNOT_INSTALLEDXX",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "not_installed",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "XXtotalXX": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_24() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "TOTAL": 0,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_25() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 1,
            "pools": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_26() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "XXpoolsXX": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_27() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "POOLS": [],
            "error": str(exc),
        }


def x_list_calico_ip_pools__mutmut_28() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "XXerrorXX": str(exc),
        }


def x_list_calico_ip_pools__mutmut_29() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "ERROR": str(exc),
        }


def x_list_calico_ip_pools__mutmut_30() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(None),
        }

mutants_x_list_calico_ip_pools__mutmut['_mutmut_orig'] = x_list_calico_ip_pools__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_1'] = x_list_calico_ip_pools__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_2'] = x_list_calico_ip_pools__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_3'] = x_list_calico_ip_pools__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_4'] = x_list_calico_ip_pools__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_5'] = x_list_calico_ip_pools__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_6'] = x_list_calico_ip_pools__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_7'] = x_list_calico_ip_pools__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_8'] = x_list_calico_ip_pools__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_9'] = x_list_calico_ip_pools__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_10'] = x_list_calico_ip_pools__mutmut_10 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_11'] = x_list_calico_ip_pools__mutmut_11 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_12'] = x_list_calico_ip_pools__mutmut_12 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_13'] = x_list_calico_ip_pools__mutmut_13 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_14'] = x_list_calico_ip_pools__mutmut_14 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_15'] = x_list_calico_ip_pools__mutmut_15 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_16'] = x_list_calico_ip_pools__mutmut_16 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_17'] = x_list_calico_ip_pools__mutmut_17 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_18'] = x_list_calico_ip_pools__mutmut_18 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_19'] = x_list_calico_ip_pools__mutmut_19 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_20'] = x_list_calico_ip_pools__mutmut_20 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_21'] = x_list_calico_ip_pools__mutmut_21 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_22'] = x_list_calico_ip_pools__mutmut_22 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_23'] = x_list_calico_ip_pools__mutmut_23 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_24'] = x_list_calico_ip_pools__mutmut_24 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_25'] = x_list_calico_ip_pools__mutmut_25 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_26'] = x_list_calico_ip_pools__mutmut_26 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_27'] = x_list_calico_ip_pools__mutmut_27 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_28'] = x_list_calico_ip_pools__mutmut_28 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_29'] = x_list_calico_ip_pools__mutmut_29 # type: ignore # mutmut generated
mutants_x_list_calico_ip_pools__mutmut['x_list_calico_ip_pools__mutmut_30'] = x_list_calico_ip_pools__mutmut_30 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(list_calico_ip_pools)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(list_calico_ip_pools)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
