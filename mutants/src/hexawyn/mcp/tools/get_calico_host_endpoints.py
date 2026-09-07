"""MCP tool: get_calico_host_endpoints — list Calico HostEndpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.get_calico_host_endpoints.command import (
    GetCalicoHostEndpointsCommand,
)
from hexawyn.application.use_case.calico.get_calico_host_endpoints.get_calico_host_endpoints_use_case import (  # noqa: E501
    GetCalicoHostEndpointsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__endpoint_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__endpoint_dict__mutmut)
def _endpoint_dict(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_orig(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_1(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "XXnameXX": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_2(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "NAME": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_3(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(None, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_4(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, None, None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_5(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr("name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_6(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_7(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", ),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_8(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "XXnameXX", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_9(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "NAME", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_10(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "XXnodeXX": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_11(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "NODE": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_12(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(None, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_13(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, None, None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_14(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr("node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_15(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_16(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", ),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_17(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "XXnodeXX", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_18(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "NODE", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_19(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "XXinterface_nameXX": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_20(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "INTERFACE_NAME": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_21(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(None, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_22(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, None, None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_23(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr("interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_24(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_25(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", ),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_26(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "XXinterface_nameXX", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_27(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "INTERFACE_NAME", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_28(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "XXexpected_ipXX": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_29(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "EXPECTED_IP": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_30(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(None, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_31(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, None, None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_32(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr("expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_33(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_34(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", ),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_35(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "XXexpected_ipXX", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_36(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "EXPECTED_IP", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_37(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "XXexpected_ipsXX": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_38(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "EXPECTED_IPS": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_39(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(None),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_40(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(None, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_41(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, None, ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_42(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", None)),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_43(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr("expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_44(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_45(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", )),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_46(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "XXexpected_ipsXX", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_47(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "EXPECTED_IPS", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_48(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "XXlabelsXX": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_49(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "LABELS": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_50(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(None) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_51(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(None, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_52(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, None, ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_53(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", None)],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_54(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr("labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_55(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_56(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", )],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_57(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "XXlabelsXX", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_58(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "LABELS", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_59(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "XXapplied_policiesXX": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_60(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "APPLIED_POLICIES": list(getattr(endpoint, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_61(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(None),
    }


def x__endpoint_dict__mutmut_62(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(None, "applied_policies", ())),
    }


def x__endpoint_dict__mutmut_63(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, None, ())),
    }


def x__endpoint_dict__mutmut_64(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", None)),
    }


def x__endpoint_dict__mutmut_65(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr("applied_policies", ())),
    }


def x__endpoint_dict__mutmut_66(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, ())),
    }


def x__endpoint_dict__mutmut_67(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", )),
    }


def x__endpoint_dict__mutmut_68(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "XXapplied_policiesXX", ())),
    }


def x__endpoint_dict__mutmut_69(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "APPLIED_POLICIES", ())),
    }

mutants_x__endpoint_dict__mutmut['_mutmut_orig'] = x__endpoint_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_1'] = x__endpoint_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_2'] = x__endpoint_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_3'] = x__endpoint_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_4'] = x__endpoint_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_5'] = x__endpoint_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_6'] = x__endpoint_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_7'] = x__endpoint_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_8'] = x__endpoint_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_9'] = x__endpoint_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_10'] = x__endpoint_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_11'] = x__endpoint_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_12'] = x__endpoint_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_13'] = x__endpoint_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_14'] = x__endpoint_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_15'] = x__endpoint_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_16'] = x__endpoint_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_17'] = x__endpoint_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_18'] = x__endpoint_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_19'] = x__endpoint_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_20'] = x__endpoint_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_21'] = x__endpoint_dict__mutmut_21 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_22'] = x__endpoint_dict__mutmut_22 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_23'] = x__endpoint_dict__mutmut_23 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_24'] = x__endpoint_dict__mutmut_24 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_25'] = x__endpoint_dict__mutmut_25 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_26'] = x__endpoint_dict__mutmut_26 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_27'] = x__endpoint_dict__mutmut_27 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_28'] = x__endpoint_dict__mutmut_28 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_29'] = x__endpoint_dict__mutmut_29 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_30'] = x__endpoint_dict__mutmut_30 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_31'] = x__endpoint_dict__mutmut_31 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_32'] = x__endpoint_dict__mutmut_32 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_33'] = x__endpoint_dict__mutmut_33 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_34'] = x__endpoint_dict__mutmut_34 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_35'] = x__endpoint_dict__mutmut_35 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_36'] = x__endpoint_dict__mutmut_36 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_37'] = x__endpoint_dict__mutmut_37 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_38'] = x__endpoint_dict__mutmut_38 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_39'] = x__endpoint_dict__mutmut_39 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_40'] = x__endpoint_dict__mutmut_40 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_41'] = x__endpoint_dict__mutmut_41 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_42'] = x__endpoint_dict__mutmut_42 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_43'] = x__endpoint_dict__mutmut_43 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_44'] = x__endpoint_dict__mutmut_44 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_45'] = x__endpoint_dict__mutmut_45 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_46'] = x__endpoint_dict__mutmut_46 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_47'] = x__endpoint_dict__mutmut_47 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_48'] = x__endpoint_dict__mutmut_48 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_49'] = x__endpoint_dict__mutmut_49 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_50'] = x__endpoint_dict__mutmut_50 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_51'] = x__endpoint_dict__mutmut_51 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_52'] = x__endpoint_dict__mutmut_52 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_53'] = x__endpoint_dict__mutmut_53 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_54'] = x__endpoint_dict__mutmut_54 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_55'] = x__endpoint_dict__mutmut_55 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_56'] = x__endpoint_dict__mutmut_56 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_57'] = x__endpoint_dict__mutmut_57 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_58'] = x__endpoint_dict__mutmut_58 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_59'] = x__endpoint_dict__mutmut_59 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_60'] = x__endpoint_dict__mutmut_60 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_61'] = x__endpoint_dict__mutmut_61 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_62'] = x__endpoint_dict__mutmut_62 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_63'] = x__endpoint_dict__mutmut_63 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_64'] = x__endpoint_dict__mutmut_64 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_65'] = x__endpoint_dict__mutmut_65 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_66'] = x__endpoint_dict__mutmut_66 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_67'] = x__endpoint_dict__mutmut_67 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_68'] = x__endpoint_dict__mutmut_68 # type: ignore # mutmut generated
mutants_x__endpoint_dict__mutmut['x__endpoint_dict__mutmut_69'] = x__endpoint_dict__mutmut_69 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_calico_host_endpoints__mutmut)
def get_calico_host_endpoints() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = None
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=None)
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = None
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "XXinstalledXX": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "INSTALLED": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "XXnot_installed_markerXX": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "NOT_INSTALLED_MARKER": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "XXtotalXX": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "TOTAL": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "XXendpointsXX": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "ENDPOINTS": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(None) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXnot_installed_markerXX": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "NOT_INSTALLED_MARKER": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "XXNOT_INSTALLEDXX",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "not_installed",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "XXtotalXX": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_24() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "TOTAL": 0,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_25() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 1,
            "endpoints": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_26() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "XXendpointsXX": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_27() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "ENDPOINTS": [],
            "error": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_28() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "XXerrorXX": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_29() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "ERROR": str(exc),
        }


def x_get_calico_host_endpoints__mutmut_30() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(None),
        }

mutants_x_get_calico_host_endpoints__mutmut['_mutmut_orig'] = x_get_calico_host_endpoints__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_1'] = x_get_calico_host_endpoints__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_2'] = x_get_calico_host_endpoints__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_3'] = x_get_calico_host_endpoints__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_4'] = x_get_calico_host_endpoints__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_5'] = x_get_calico_host_endpoints__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_6'] = x_get_calico_host_endpoints__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_7'] = x_get_calico_host_endpoints__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_8'] = x_get_calico_host_endpoints__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_9'] = x_get_calico_host_endpoints__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_10'] = x_get_calico_host_endpoints__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_11'] = x_get_calico_host_endpoints__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_12'] = x_get_calico_host_endpoints__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_13'] = x_get_calico_host_endpoints__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_14'] = x_get_calico_host_endpoints__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_15'] = x_get_calico_host_endpoints__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_16'] = x_get_calico_host_endpoints__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_17'] = x_get_calico_host_endpoints__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_18'] = x_get_calico_host_endpoints__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_19'] = x_get_calico_host_endpoints__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_20'] = x_get_calico_host_endpoints__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_21'] = x_get_calico_host_endpoints__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_22'] = x_get_calico_host_endpoints__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_23'] = x_get_calico_host_endpoints__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_24'] = x_get_calico_host_endpoints__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_25'] = x_get_calico_host_endpoints__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_26'] = x_get_calico_host_endpoints__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_27'] = x_get_calico_host_endpoints__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_28'] = x_get_calico_host_endpoints__mutmut_28 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_29'] = x_get_calico_host_endpoints__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_calico_host_endpoints__mutmut['x_get_calico_host_endpoints__mutmut_30'] = x_get_calico_host_endpoints__mutmut_30 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(get_calico_host_endpoints)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(get_calico_host_endpoints)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
