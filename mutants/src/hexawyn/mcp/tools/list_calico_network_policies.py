"""MCP tool: list_calico_network_policies — list Calico NetworkPolicy + GNP."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.list_calico_network_policies.command import (
    ListCalicoNetworkPoliciesCommand,
)
from hexawyn.application.use_case.calico.list_calico_network_policies.list_calico_network_policies_use_case import (  # noqa: E501
    ListCalicoNetworkPoliciesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__policy_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__policy_dict__mutmut)
def _policy_dict(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_orig(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_1(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "XXnameXX": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_2(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "NAME": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_3(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(None, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_4(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, None, None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_5(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr("name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_6(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_7(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", ),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_8(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "XXnameXX", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_9(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "NAME", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_10(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "XXkindXX": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_11(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "KIND": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_12(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(None, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_13(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, None, None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_14(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr("kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_15(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_16(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", ),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_17(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "XXkindXX", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_18(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "KIND", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_19(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "XXnamespaceXX": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_20(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "NAMESPACE": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_21(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(None, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_22(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, None, None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_23(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr("namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_24(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_25(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", ),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_26(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "XXnamespaceXX", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_27(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "NAMESPACE", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_28(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "XXselectorXX": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_29(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "SELECTOR": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_30(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(None, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_31(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, None, None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_32(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr("selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_33(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_34(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", ),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_35(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "XXselectorXX", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_36(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "SELECTOR", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_37(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "XXactionXX": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_38(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "ACTION": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_39(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(None, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_40(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, None, None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_41(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr("action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_42(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_43(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", ),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_44(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "XXactionXX", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_45(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "ACTION", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_46(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "XXingress_rule_countXX": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_47(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "INGRESS_RULE_COUNT": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_48(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(None, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_49(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, None, 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_50(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", None),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_51(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr("ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_52(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_53(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", ),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_54(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "XXingress_rule_countXX", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_55(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "INGRESS_RULE_COUNT", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_56(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 1),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_57(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "XXegress_rule_countXX": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_58(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "EGRESS_RULE_COUNT": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_59(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(None, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_60(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, None, 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_61(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_62(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr("egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_63(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_64(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", ),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_65(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "XXegress_rule_countXX", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_66(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "EGRESS_RULE_COUNT", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_67(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 1),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_68(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "XXingress_rulesXX": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_69(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "INGRESS_RULES": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_70(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(None),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_71(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(None, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_72(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, None, ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_73(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", None)),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_74(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr("ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_75(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_76(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", )),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_77(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "XXingress_rulesXX", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_78(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "INGRESS_RULES", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_79(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "XXegress_rulesXX": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_80(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "EGRESS_RULES": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_81(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(None),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_82(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(None, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_83(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, None, ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_84(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", None)),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_85(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr("egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_86(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_87(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", )),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_88(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "XXegress_rulesXX", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_89(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "EGRESS_RULES", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_90(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "XXorderXX": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_91(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ORDER": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_92(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(None, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_93(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, None, 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_94(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", None),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_95(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr("order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_96(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_97(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", ),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_98(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "XXorderXX", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_99(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "ORDER", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_100(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 1.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_101(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "XXapply_on_forwardXX": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_102(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "APPLY_ON_FORWARD": getattr(policy, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_103(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(None, "apply_on_forward", False),
    }


def x__policy_dict__mutmut_104(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, None, False),
    }


def x__policy_dict__mutmut_105(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", None),
    }


def x__policy_dict__mutmut_106(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr("apply_on_forward", False),
    }


def x__policy_dict__mutmut_107(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, False),
    }


def x__policy_dict__mutmut_108(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", ),
    }


def x__policy_dict__mutmut_109(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "XXapply_on_forwardXX", False),
    }


def x__policy_dict__mutmut_110(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "APPLY_ON_FORWARD", False),
    }


def x__policy_dict__mutmut_111(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", True),
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
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_54'] = x__policy_dict__mutmut_54 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_55'] = x__policy_dict__mutmut_55 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_56'] = x__policy_dict__mutmut_56 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_57'] = x__policy_dict__mutmut_57 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_58'] = x__policy_dict__mutmut_58 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_59'] = x__policy_dict__mutmut_59 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_60'] = x__policy_dict__mutmut_60 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_61'] = x__policy_dict__mutmut_61 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_62'] = x__policy_dict__mutmut_62 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_63'] = x__policy_dict__mutmut_63 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_64'] = x__policy_dict__mutmut_64 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_65'] = x__policy_dict__mutmut_65 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_66'] = x__policy_dict__mutmut_66 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_67'] = x__policy_dict__mutmut_67 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_68'] = x__policy_dict__mutmut_68 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_69'] = x__policy_dict__mutmut_69 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_70'] = x__policy_dict__mutmut_70 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_71'] = x__policy_dict__mutmut_71 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_72'] = x__policy_dict__mutmut_72 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_73'] = x__policy_dict__mutmut_73 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_74'] = x__policy_dict__mutmut_74 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_75'] = x__policy_dict__mutmut_75 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_76'] = x__policy_dict__mutmut_76 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_77'] = x__policy_dict__mutmut_77 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_78'] = x__policy_dict__mutmut_78 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_79'] = x__policy_dict__mutmut_79 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_80'] = x__policy_dict__mutmut_80 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_81'] = x__policy_dict__mutmut_81 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_82'] = x__policy_dict__mutmut_82 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_83'] = x__policy_dict__mutmut_83 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_84'] = x__policy_dict__mutmut_84 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_85'] = x__policy_dict__mutmut_85 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_86'] = x__policy_dict__mutmut_86 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_87'] = x__policy_dict__mutmut_87 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_88'] = x__policy_dict__mutmut_88 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_89'] = x__policy_dict__mutmut_89 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_90'] = x__policy_dict__mutmut_90 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_91'] = x__policy_dict__mutmut_91 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_92'] = x__policy_dict__mutmut_92 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_93'] = x__policy_dict__mutmut_93 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_94'] = x__policy_dict__mutmut_94 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_95'] = x__policy_dict__mutmut_95 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_96'] = x__policy_dict__mutmut_96 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_97'] = x__policy_dict__mutmut_97 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_98'] = x__policy_dict__mutmut_98 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_99'] = x__policy_dict__mutmut_99 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_100'] = x__policy_dict__mutmut_100 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_101'] = x__policy_dict__mutmut_101 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_102'] = x__policy_dict__mutmut_102 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_103'] = x__policy_dict__mutmut_103 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_104'] = x__policy_dict__mutmut_104 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_105'] = x__policy_dict__mutmut_105 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_106'] = x__policy_dict__mutmut_106 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_107'] = x__policy_dict__mutmut_107 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_108'] = x__policy_dict__mutmut_108 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_109'] = x__policy_dict__mutmut_109 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_110'] = x__policy_dict__mutmut_110 # type: ignore # mutmut generated
mutants_x__policy_dict__mutmut['x__policy_dict__mutmut_111'] = x__policy_dict__mutmut_111 # type: ignore # mutmut generated
mutants_x__empty__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__empty__mutmut)
def _empty(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_orig(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_1(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "XXinstalledXX": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_2(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "INSTALLED": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_3(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": True,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_4(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "XXnot_installed_markerXX": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_5(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "NOT_INSTALLED_MARKER": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_6(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "XXNOT_INSTALLEDXX",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_7(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "not_installed",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_8(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "XXtotalXX": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_9(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "TOTAL": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_10(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 1,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_11(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "XXglobal_countXX": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_12(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "GLOBAL_COUNT": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_13(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 1,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_14(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "XXnamespaced_countXX": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_15(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "NAMESPACED_COUNT": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_16(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 1,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_17(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "XXnamespaceXX": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_18(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "NAMESPACE": namespace,
        "policies": [],
        "error": error,
    }


def x__empty__mutmut_19(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "XXpoliciesXX": [],
        "error": error,
    }


def x__empty__mutmut_20(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "POLICIES": [],
        "error": error,
    }


def x__empty__mutmut_21(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "XXerrorXX": error,
    }


def x__empty__mutmut_22(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
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
mutants_x_list_calico_network_policies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_calico_network_policies__mutmut)
def list_calico_network_policies(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_1(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = None
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_2(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=None)
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_3(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = None
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_4(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_5(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=None))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_6(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "XXinstalledXX": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_7(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "INSTALLED": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_8(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "XXnot_installed_markerXX": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_9(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "NOT_INSTALLED_MARKER": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_10(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "XXtotalXX": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_11(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "TOTAL": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_12(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "XXglobal_countXX": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_13(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "GLOBAL_COUNT": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_14(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "XXnamespaced_countXX": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_15(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "NAMESPACED_COUNT": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_16(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "XXnamespaceXX": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_17(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "NAMESPACE": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_18(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "XXpoliciesXX": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_19(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "POLICIES": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_20(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(None) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_21(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_22(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "ERROR": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def x_list_calico_network_policies__mutmut_23(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(None, error=str(exc))


def x_list_calico_network_policies__mutmut_24(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=None)


def x_list_calico_network_policies__mutmut_25(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def x_list_calico_network_policies__mutmut_26(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, )


def x_list_calico_network_policies__mutmut_27(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(None))

mutants_x_list_calico_network_policies__mutmut['_mutmut_orig'] = x_list_calico_network_policies__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_1'] = x_list_calico_network_policies__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_2'] = x_list_calico_network_policies__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_3'] = x_list_calico_network_policies__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_4'] = x_list_calico_network_policies__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_5'] = x_list_calico_network_policies__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_6'] = x_list_calico_network_policies__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_7'] = x_list_calico_network_policies__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_8'] = x_list_calico_network_policies__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_9'] = x_list_calico_network_policies__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_10'] = x_list_calico_network_policies__mutmut_10 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_11'] = x_list_calico_network_policies__mutmut_11 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_12'] = x_list_calico_network_policies__mutmut_12 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_13'] = x_list_calico_network_policies__mutmut_13 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_14'] = x_list_calico_network_policies__mutmut_14 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_15'] = x_list_calico_network_policies__mutmut_15 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_16'] = x_list_calico_network_policies__mutmut_16 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_17'] = x_list_calico_network_policies__mutmut_17 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_18'] = x_list_calico_network_policies__mutmut_18 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_19'] = x_list_calico_network_policies__mutmut_19 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_20'] = x_list_calico_network_policies__mutmut_20 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_21'] = x_list_calico_network_policies__mutmut_21 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_22'] = x_list_calico_network_policies__mutmut_22 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_23'] = x_list_calico_network_policies__mutmut_23 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_24'] = x_list_calico_network_policies__mutmut_24 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_25'] = x_list_calico_network_policies__mutmut_25 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_26'] = x_list_calico_network_policies__mutmut_26 # type: ignore # mutmut generated
mutants_x_list_calico_network_policies__mutmut['x_list_calico_network_policies__mutmut_27'] = x_list_calico_network_policies__mutmut_27 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(list_calico_network_policies)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(list_calico_network_policies)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
