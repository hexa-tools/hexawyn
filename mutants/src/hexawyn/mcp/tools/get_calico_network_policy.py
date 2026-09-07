"""MCP tool: get_calico_network_policy — full detail of a Calico policy."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.get_calico_network_policy.command import (
    GetCalicoNetworkPolicyCommand,
)
from hexawyn.application.use_case.calico.get_calico_network_policy.get_calico_network_policy_use_case import (  # noqa: E501
    GetCalicoNetworkPolicyUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__policy_fields__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__policy_fields__mutmut)
def _policy_fields(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_orig(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_1(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "XXnameXX": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_2(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "NAME": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_3(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(None, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_4(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, None, None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_5(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr("name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_6(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_7(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", ),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_8(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "XXnameXX", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_9(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "NAME", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_10(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "XXnamespaceXX": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_11(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "NAMESPACE": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_12(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(None, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_13(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, None, None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_14(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr("namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_15(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_16(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", ),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_17(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "XXnamespaceXX", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_18(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "NAMESPACE", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_19(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "XXkindXX": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_20(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "KIND": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_21(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(None, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_22(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, None, None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_23(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr("kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_24(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_25(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", ),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_26(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "XXkindXX", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_27(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "KIND", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_28(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "XXselectorXX": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_29(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "SELECTOR": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_30(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(None, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_31(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, None, None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_32(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr("selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_33(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_34(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", ),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_35(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "XXselectorXX", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_36(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "SELECTOR", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_37(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "XXactionXX": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_38(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "ACTION": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_39(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(None, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_40(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, None, None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_41(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr("action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_42(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_43(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", ),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_44(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "XXactionXX", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_45(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "ACTION", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_46(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "XXingress_rulesXX": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_47(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "INGRESS_RULES": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_48(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(None),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_49(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(None, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_50(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, None, ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_51(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", None)),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_52(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr("ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_53(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_54(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", )),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_55(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "XXingress_rulesXX", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_56(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "INGRESS_RULES", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_57(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "XXegress_rulesXX": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_58(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "EGRESS_RULES": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_59(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_60(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(None, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_61(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, None, ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_62(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", None)),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_63(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr("egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_64(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_65(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", )),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_66(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "XXegress_rulesXX", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_67(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "EGRESS_RULES", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_68(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "XXingress_rule_countXX": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_69(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "INGRESS_RULE_COUNT": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_70(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(None, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_71(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, None, 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_72(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", None),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_73(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr("ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_74(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_75(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", ),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_76(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "XXingress_rule_countXX", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_77(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "INGRESS_RULE_COUNT", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_78(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 1),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_79(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "XXegress_rule_countXX": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_80(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "EGRESS_RULE_COUNT": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_81(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(None, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_82(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, None, 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_83(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", None),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_84(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr("egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_85(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_86(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", ),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_87(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "XXegress_rule_countXX", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_88(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "EGRESS_RULE_COUNT", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_89(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 1),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_90(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "XXorderXX": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_91(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ORDER": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_92(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(None, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_93(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, None, 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_94(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", None),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_95(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr("order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_96(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_97(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", ),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_98(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "XXorderXX", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_99(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "ORDER", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_100(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 1.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_101(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "XXapply_on_forwardXX": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_102(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "APPLY_ON_FORWARD": getattr(policy, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_103(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(None, "apply_on_forward", False),
    }


def x__policy_fields__mutmut_104(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, None, False),
    }


def x__policy_fields__mutmut_105(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", None),
    }


def x__policy_fields__mutmut_106(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr("apply_on_forward", False),
    }


def x__policy_fields__mutmut_107(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, False),
    }


def x__policy_fields__mutmut_108(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", ),
    }


def x__policy_fields__mutmut_109(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "XXapply_on_forwardXX", False),
    }


def x__policy_fields__mutmut_110(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "APPLY_ON_FORWARD", False),
    }


def x__policy_fields__mutmut_111(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", True),
    }

mutants_x__policy_fields__mutmut['_mutmut_orig'] = x__policy_fields__mutmut_orig # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_1'] = x__policy_fields__mutmut_1 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_2'] = x__policy_fields__mutmut_2 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_3'] = x__policy_fields__mutmut_3 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_4'] = x__policy_fields__mutmut_4 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_5'] = x__policy_fields__mutmut_5 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_6'] = x__policy_fields__mutmut_6 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_7'] = x__policy_fields__mutmut_7 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_8'] = x__policy_fields__mutmut_8 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_9'] = x__policy_fields__mutmut_9 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_10'] = x__policy_fields__mutmut_10 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_11'] = x__policy_fields__mutmut_11 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_12'] = x__policy_fields__mutmut_12 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_13'] = x__policy_fields__mutmut_13 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_14'] = x__policy_fields__mutmut_14 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_15'] = x__policy_fields__mutmut_15 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_16'] = x__policy_fields__mutmut_16 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_17'] = x__policy_fields__mutmut_17 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_18'] = x__policy_fields__mutmut_18 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_19'] = x__policy_fields__mutmut_19 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_20'] = x__policy_fields__mutmut_20 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_21'] = x__policy_fields__mutmut_21 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_22'] = x__policy_fields__mutmut_22 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_23'] = x__policy_fields__mutmut_23 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_24'] = x__policy_fields__mutmut_24 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_25'] = x__policy_fields__mutmut_25 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_26'] = x__policy_fields__mutmut_26 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_27'] = x__policy_fields__mutmut_27 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_28'] = x__policy_fields__mutmut_28 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_29'] = x__policy_fields__mutmut_29 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_30'] = x__policy_fields__mutmut_30 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_31'] = x__policy_fields__mutmut_31 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_32'] = x__policy_fields__mutmut_32 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_33'] = x__policy_fields__mutmut_33 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_34'] = x__policy_fields__mutmut_34 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_35'] = x__policy_fields__mutmut_35 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_36'] = x__policy_fields__mutmut_36 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_37'] = x__policy_fields__mutmut_37 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_38'] = x__policy_fields__mutmut_38 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_39'] = x__policy_fields__mutmut_39 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_40'] = x__policy_fields__mutmut_40 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_41'] = x__policy_fields__mutmut_41 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_42'] = x__policy_fields__mutmut_42 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_43'] = x__policy_fields__mutmut_43 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_44'] = x__policy_fields__mutmut_44 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_45'] = x__policy_fields__mutmut_45 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_46'] = x__policy_fields__mutmut_46 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_47'] = x__policy_fields__mutmut_47 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_48'] = x__policy_fields__mutmut_48 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_49'] = x__policy_fields__mutmut_49 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_50'] = x__policy_fields__mutmut_50 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_51'] = x__policy_fields__mutmut_51 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_52'] = x__policy_fields__mutmut_52 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_53'] = x__policy_fields__mutmut_53 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_54'] = x__policy_fields__mutmut_54 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_55'] = x__policy_fields__mutmut_55 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_56'] = x__policy_fields__mutmut_56 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_57'] = x__policy_fields__mutmut_57 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_58'] = x__policy_fields__mutmut_58 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_59'] = x__policy_fields__mutmut_59 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_60'] = x__policy_fields__mutmut_60 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_61'] = x__policy_fields__mutmut_61 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_62'] = x__policy_fields__mutmut_62 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_63'] = x__policy_fields__mutmut_63 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_64'] = x__policy_fields__mutmut_64 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_65'] = x__policy_fields__mutmut_65 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_66'] = x__policy_fields__mutmut_66 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_67'] = x__policy_fields__mutmut_67 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_68'] = x__policy_fields__mutmut_68 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_69'] = x__policy_fields__mutmut_69 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_70'] = x__policy_fields__mutmut_70 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_71'] = x__policy_fields__mutmut_71 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_72'] = x__policy_fields__mutmut_72 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_73'] = x__policy_fields__mutmut_73 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_74'] = x__policy_fields__mutmut_74 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_75'] = x__policy_fields__mutmut_75 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_76'] = x__policy_fields__mutmut_76 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_77'] = x__policy_fields__mutmut_77 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_78'] = x__policy_fields__mutmut_78 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_79'] = x__policy_fields__mutmut_79 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_80'] = x__policy_fields__mutmut_80 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_81'] = x__policy_fields__mutmut_81 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_82'] = x__policy_fields__mutmut_82 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_83'] = x__policy_fields__mutmut_83 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_84'] = x__policy_fields__mutmut_84 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_85'] = x__policy_fields__mutmut_85 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_86'] = x__policy_fields__mutmut_86 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_87'] = x__policy_fields__mutmut_87 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_88'] = x__policy_fields__mutmut_88 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_89'] = x__policy_fields__mutmut_89 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_90'] = x__policy_fields__mutmut_90 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_91'] = x__policy_fields__mutmut_91 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_92'] = x__policy_fields__mutmut_92 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_93'] = x__policy_fields__mutmut_93 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_94'] = x__policy_fields__mutmut_94 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_95'] = x__policy_fields__mutmut_95 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_96'] = x__policy_fields__mutmut_96 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_97'] = x__policy_fields__mutmut_97 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_98'] = x__policy_fields__mutmut_98 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_99'] = x__policy_fields__mutmut_99 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_100'] = x__policy_fields__mutmut_100 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_101'] = x__policy_fields__mutmut_101 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_102'] = x__policy_fields__mutmut_102 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_103'] = x__policy_fields__mutmut_103 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_104'] = x__policy_fields__mutmut_104 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_105'] = x__policy_fields__mutmut_105 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_106'] = x__policy_fields__mutmut_106 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_107'] = x__policy_fields__mutmut_107 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_108'] = x__policy_fields__mutmut_108 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_109'] = x__policy_fields__mutmut_109 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_110'] = x__policy_fields__mutmut_110 # type: ignore # mutmut generated
mutants_x__policy_fields__mutmut['x__policy_fields__mutmut_111'] = x__policy_fields__mutmut_111 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_calico_network_policy__mutmut)
def get_calico_network_policy(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_orig(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_1(name: str = "XXXX", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_2(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = None
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_3(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=None)
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_4(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = None
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_5(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_6(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=None, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_7(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=None))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_8(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_9(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, ))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_10(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "XXinstalledXX": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_11(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "INSTALLED": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_12(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "XXnot_installed_markerXX": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_13(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "NOT_INSTALLED_MARKER": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_14(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "XXfoundXX": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_15(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "FOUND": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_16(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "XXnameXX": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_17(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "NAME": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_18(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "XXnamespaceXX": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_19(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "NAMESPACE": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_20(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "XXscopeXX": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_21(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "SCOPE": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_22(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "XXkindXX": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_23(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "KIND": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_24(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "XXselectorXX": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_25(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "SELECTOR": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_26(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "XXactionXX": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_27(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "ACTION": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_28(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "XXingress_rulesXX": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_29(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "INGRESS_RULES": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_30(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(None),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_31(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "XXegress_rulesXX": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_32(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "EGRESS_RULES": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_33(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(None),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_34(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "XXingress_rule_countXX": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_35(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "INGRESS_RULE_COUNT": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_36(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "XXegress_rule_countXX": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_37(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "EGRESS_RULE_COUNT": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_38(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "XXorderXX": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_39(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "ORDER": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_40(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "XXapply_on_forwardXX": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_41(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "APPLY_ON_FORWARD": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_42(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_43(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_44(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_45(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_46(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_47(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXnot_installed_markerXX": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_48(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "NOT_INSTALLED_MARKER": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_49(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "XXNOT_INSTALLEDXX",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_50(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "not_installed",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_51(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "XXfoundXX": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_52(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "FOUND": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_53(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": True,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_54(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "XXnameXX": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_55(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "NAME": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_56(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "XXnamespaceXX": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_57(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "NAMESPACE": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_58(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "XXscopeXX": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_59(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "SCOPE": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_60(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "XXkindXX": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_61(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "KIND": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_62(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "XXselectorXX": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_63(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "SELECTOR": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_64(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "XXactionXX": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_65(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "ACTION": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_66(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "XXingress_rulesXX": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_67(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "INGRESS_RULES": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_68(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "XXegress_rulesXX": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_69(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "EGRESS_RULES": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_70(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "XXingress_rule_countXX": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_71(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "INGRESS_RULE_COUNT": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_72(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 1,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_73(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "XXegress_rule_countXX": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_74(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "EGRESS_RULE_COUNT": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_75(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 1,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_76(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "XXorderXX": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_77(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "ORDER": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_78(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 1.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_79(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "XXapply_on_forwardXX": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_80(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "APPLY_ON_FORWARD": False,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_81(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": True,
            "error": str(exc),
        }


def x_get_calico_network_policy__mutmut_82(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "XXerrorXX": str(exc),
        }


def x_get_calico_network_policy__mutmut_83(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "ERROR": str(exc),
        }


def x_get_calico_network_policy__mutmut_84(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(None),
        }

mutants_x_get_calico_network_policy__mutmut['_mutmut_orig'] = x_get_calico_network_policy__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_1'] = x_get_calico_network_policy__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_2'] = x_get_calico_network_policy__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_3'] = x_get_calico_network_policy__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_4'] = x_get_calico_network_policy__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_5'] = x_get_calico_network_policy__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_6'] = x_get_calico_network_policy__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_7'] = x_get_calico_network_policy__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_8'] = x_get_calico_network_policy__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_9'] = x_get_calico_network_policy__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_10'] = x_get_calico_network_policy__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_11'] = x_get_calico_network_policy__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_12'] = x_get_calico_network_policy__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_13'] = x_get_calico_network_policy__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_14'] = x_get_calico_network_policy__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_15'] = x_get_calico_network_policy__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_16'] = x_get_calico_network_policy__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_17'] = x_get_calico_network_policy__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_18'] = x_get_calico_network_policy__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_19'] = x_get_calico_network_policy__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_20'] = x_get_calico_network_policy__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_21'] = x_get_calico_network_policy__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_22'] = x_get_calico_network_policy__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_23'] = x_get_calico_network_policy__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_24'] = x_get_calico_network_policy__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_25'] = x_get_calico_network_policy__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_26'] = x_get_calico_network_policy__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_27'] = x_get_calico_network_policy__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_28'] = x_get_calico_network_policy__mutmut_28 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_29'] = x_get_calico_network_policy__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_30'] = x_get_calico_network_policy__mutmut_30 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_31'] = x_get_calico_network_policy__mutmut_31 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_32'] = x_get_calico_network_policy__mutmut_32 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_33'] = x_get_calico_network_policy__mutmut_33 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_34'] = x_get_calico_network_policy__mutmut_34 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_35'] = x_get_calico_network_policy__mutmut_35 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_36'] = x_get_calico_network_policy__mutmut_36 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_37'] = x_get_calico_network_policy__mutmut_37 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_38'] = x_get_calico_network_policy__mutmut_38 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_39'] = x_get_calico_network_policy__mutmut_39 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_40'] = x_get_calico_network_policy__mutmut_40 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_41'] = x_get_calico_network_policy__mutmut_41 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_42'] = x_get_calico_network_policy__mutmut_42 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_43'] = x_get_calico_network_policy__mutmut_43 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_44'] = x_get_calico_network_policy__mutmut_44 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_45'] = x_get_calico_network_policy__mutmut_45 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_46'] = x_get_calico_network_policy__mutmut_46 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_47'] = x_get_calico_network_policy__mutmut_47 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_48'] = x_get_calico_network_policy__mutmut_48 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_49'] = x_get_calico_network_policy__mutmut_49 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_50'] = x_get_calico_network_policy__mutmut_50 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_51'] = x_get_calico_network_policy__mutmut_51 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_52'] = x_get_calico_network_policy__mutmut_52 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_53'] = x_get_calico_network_policy__mutmut_53 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_54'] = x_get_calico_network_policy__mutmut_54 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_55'] = x_get_calico_network_policy__mutmut_55 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_56'] = x_get_calico_network_policy__mutmut_56 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_57'] = x_get_calico_network_policy__mutmut_57 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_58'] = x_get_calico_network_policy__mutmut_58 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_59'] = x_get_calico_network_policy__mutmut_59 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_60'] = x_get_calico_network_policy__mutmut_60 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_61'] = x_get_calico_network_policy__mutmut_61 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_62'] = x_get_calico_network_policy__mutmut_62 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_63'] = x_get_calico_network_policy__mutmut_63 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_64'] = x_get_calico_network_policy__mutmut_64 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_65'] = x_get_calico_network_policy__mutmut_65 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_66'] = x_get_calico_network_policy__mutmut_66 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_67'] = x_get_calico_network_policy__mutmut_67 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_68'] = x_get_calico_network_policy__mutmut_68 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_69'] = x_get_calico_network_policy__mutmut_69 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_70'] = x_get_calico_network_policy__mutmut_70 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_71'] = x_get_calico_network_policy__mutmut_71 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_72'] = x_get_calico_network_policy__mutmut_72 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_73'] = x_get_calico_network_policy__mutmut_73 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_74'] = x_get_calico_network_policy__mutmut_74 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_75'] = x_get_calico_network_policy__mutmut_75 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_76'] = x_get_calico_network_policy__mutmut_76 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_77'] = x_get_calico_network_policy__mutmut_77 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_78'] = x_get_calico_network_policy__mutmut_78 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_79'] = x_get_calico_network_policy__mutmut_79 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_80'] = x_get_calico_network_policy__mutmut_80 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_81'] = x_get_calico_network_policy__mutmut_81 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_82'] = x_get_calico_network_policy__mutmut_82 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_83'] = x_get_calico_network_policy__mutmut_83 # type: ignore # mutmut generated
mutants_x_get_calico_network_policy__mutmut['x_get_calico_network_policy__mutmut_84'] = x_get_calico_network_policy__mutmut_84 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(get_calico_network_policy)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(get_calico_network_policy)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
