"""Pure Calico network-policy rule extraction — no infrastructure imports.

Parses the ``projectcalico.org/v3`` CRD payloads (namespaced
``CalicoNetworkPolicy`` and cluster-scope ``GlobalNetworkPolicy``) into the
frozen ``CalicoNetworkPolicy`` model, deriving the per-rule summary and the
policy-level action. Field values that cannot be interpreted are preserved as
observed — never fabricated.
"""

from __future__ import annotations

from collections.abc import Mapping

from hexawyn.domain.models.calico import CalicoNetworkPolicy

_KIND_NAMESPACED = "CalicoNetworkPolicy"
_KIND_GLOBAL = "GlobalNetworkPolicy"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_parse_calico_network_policy__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_calico_network_policy__mutmut)
def parse_calico_network_policy(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_orig(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_1(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = None
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_2(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(None)
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_3(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get(None))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_4(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("XXmetadataXX"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_5(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("METADATA"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_6(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = None
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_7(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(None)
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_8(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get(None))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_9(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("XXspecXX"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_10(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("SPEC"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_11(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = None
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_12(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(None)
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_13(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get(None))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_14(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("XXingressXX"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_15(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("INGRESS"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_16(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = None
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_17(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(None)
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_18(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get(None))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_19(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("XXegressXX"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_20(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("EGRESS"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_21(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=None,
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_22(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=None,
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_23(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=None,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_24(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=None,
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_25(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=None,
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_26(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=None,
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_27(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=None,
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_28(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=None,
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_29(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=None,
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_30(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=None,
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_31(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=None,
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_32(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=None,
    )


def x_parse_calico_network_policy__mutmut_33(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_34(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_35(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_36(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_37(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_38(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_39(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_40(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_41(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_42(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_43(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_44(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        )


def x_parse_calico_network_policy__mutmut_45(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(None),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_46(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get(None, "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_47(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", None)),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_48(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_49(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", )),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_50(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("XXnameXX", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_51(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("NAME", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_52(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "XXXX")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_53(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(None),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_54(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get(None, "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_55(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", None)),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_56(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_57(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", )),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_58(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("XXnamespaceXX", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_59(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("NAMESPACE", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_60(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "XXXX")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_61(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(None),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_62(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(None),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_63(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get(None, "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_64(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", None)),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_65(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_66(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", )),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_67(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("XXselectorXX", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_68(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("SELECTOR", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_69(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "XXXX")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_70(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(None),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_71(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(None) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_72(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(None),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_73(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(None) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_74(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(None, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_75(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, None),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_76(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_77(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, ),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_78(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(None),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_79(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get(None, False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_80(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", None)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_81(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get(False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_82(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", )),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_83(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("XXapplyOnForwardXX", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_84(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyonforward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_85(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("APPLYONFORWARD", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_86(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", True)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_87(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) and _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_88(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(None) or _has_l7(egress),
    )


def x_parse_calico_network_policy__mutmut_89(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(None),
    )

mutants_x_parse_calico_network_policy__mutmut['_mutmut_orig'] = x_parse_calico_network_policy__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_1'] = x_parse_calico_network_policy__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_2'] = x_parse_calico_network_policy__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_3'] = x_parse_calico_network_policy__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_4'] = x_parse_calico_network_policy__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_5'] = x_parse_calico_network_policy__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_6'] = x_parse_calico_network_policy__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_7'] = x_parse_calico_network_policy__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_8'] = x_parse_calico_network_policy__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_9'] = x_parse_calico_network_policy__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_10'] = x_parse_calico_network_policy__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_11'] = x_parse_calico_network_policy__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_12'] = x_parse_calico_network_policy__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_13'] = x_parse_calico_network_policy__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_14'] = x_parse_calico_network_policy__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_15'] = x_parse_calico_network_policy__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_16'] = x_parse_calico_network_policy__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_17'] = x_parse_calico_network_policy__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_18'] = x_parse_calico_network_policy__mutmut_18 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_19'] = x_parse_calico_network_policy__mutmut_19 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_20'] = x_parse_calico_network_policy__mutmut_20 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_21'] = x_parse_calico_network_policy__mutmut_21 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_22'] = x_parse_calico_network_policy__mutmut_22 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_23'] = x_parse_calico_network_policy__mutmut_23 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_24'] = x_parse_calico_network_policy__mutmut_24 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_25'] = x_parse_calico_network_policy__mutmut_25 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_26'] = x_parse_calico_network_policy__mutmut_26 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_27'] = x_parse_calico_network_policy__mutmut_27 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_28'] = x_parse_calico_network_policy__mutmut_28 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_29'] = x_parse_calico_network_policy__mutmut_29 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_30'] = x_parse_calico_network_policy__mutmut_30 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_31'] = x_parse_calico_network_policy__mutmut_31 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_32'] = x_parse_calico_network_policy__mutmut_32 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_33'] = x_parse_calico_network_policy__mutmut_33 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_34'] = x_parse_calico_network_policy__mutmut_34 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_35'] = x_parse_calico_network_policy__mutmut_35 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_36'] = x_parse_calico_network_policy__mutmut_36 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_37'] = x_parse_calico_network_policy__mutmut_37 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_38'] = x_parse_calico_network_policy__mutmut_38 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_39'] = x_parse_calico_network_policy__mutmut_39 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_40'] = x_parse_calico_network_policy__mutmut_40 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_41'] = x_parse_calico_network_policy__mutmut_41 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_42'] = x_parse_calico_network_policy__mutmut_42 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_43'] = x_parse_calico_network_policy__mutmut_43 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_44'] = x_parse_calico_network_policy__mutmut_44 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_45'] = x_parse_calico_network_policy__mutmut_45 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_46'] = x_parse_calico_network_policy__mutmut_46 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_47'] = x_parse_calico_network_policy__mutmut_47 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_48'] = x_parse_calico_network_policy__mutmut_48 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_49'] = x_parse_calico_network_policy__mutmut_49 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_50'] = x_parse_calico_network_policy__mutmut_50 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_51'] = x_parse_calico_network_policy__mutmut_51 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_52'] = x_parse_calico_network_policy__mutmut_52 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_53'] = x_parse_calico_network_policy__mutmut_53 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_54'] = x_parse_calico_network_policy__mutmut_54 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_55'] = x_parse_calico_network_policy__mutmut_55 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_56'] = x_parse_calico_network_policy__mutmut_56 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_57'] = x_parse_calico_network_policy__mutmut_57 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_58'] = x_parse_calico_network_policy__mutmut_58 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_59'] = x_parse_calico_network_policy__mutmut_59 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_60'] = x_parse_calico_network_policy__mutmut_60 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_61'] = x_parse_calico_network_policy__mutmut_61 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_62'] = x_parse_calico_network_policy__mutmut_62 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_63'] = x_parse_calico_network_policy__mutmut_63 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_64'] = x_parse_calico_network_policy__mutmut_64 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_65'] = x_parse_calico_network_policy__mutmut_65 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_66'] = x_parse_calico_network_policy__mutmut_66 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_67'] = x_parse_calico_network_policy__mutmut_67 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_68'] = x_parse_calico_network_policy__mutmut_68 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_69'] = x_parse_calico_network_policy__mutmut_69 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_70'] = x_parse_calico_network_policy__mutmut_70 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_71'] = x_parse_calico_network_policy__mutmut_71 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_72'] = x_parse_calico_network_policy__mutmut_72 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_73'] = x_parse_calico_network_policy__mutmut_73 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_74'] = x_parse_calico_network_policy__mutmut_74 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_75'] = x_parse_calico_network_policy__mutmut_75 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_76'] = x_parse_calico_network_policy__mutmut_76 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_77'] = x_parse_calico_network_policy__mutmut_77 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_78'] = x_parse_calico_network_policy__mutmut_78 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_79'] = x_parse_calico_network_policy__mutmut_79 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_80'] = x_parse_calico_network_policy__mutmut_80 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_81'] = x_parse_calico_network_policy__mutmut_81 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_82'] = x_parse_calico_network_policy__mutmut_82 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_83'] = x_parse_calico_network_policy__mutmut_83 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_84'] = x_parse_calico_network_policy__mutmut_84 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_85'] = x_parse_calico_network_policy__mutmut_85 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_86'] = x_parse_calico_network_policy__mutmut_86 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_87'] = x_parse_calico_network_policy__mutmut_87 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_88'] = x_parse_calico_network_policy__mutmut_88 # type: ignore # mutmut generated
mutants_x_parse_calico_network_policy__mutmut['x_parse_calico_network_policy__mutmut_89'] = x_parse_calico_network_policy__mutmut_89 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_global_network_policy__mutmut)
def parse_global_network_policy(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_orig(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_1(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = None
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_2(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(None)
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_3(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get(None))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_4(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("XXmetadataXX"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_5(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("METADATA"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_6(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = None
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_7(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(None)
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_8(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get(None))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_9(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("XXspecXX"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_10(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("SPEC"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_11(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = None
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_12(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(None)
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_13(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get(None))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_14(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("XXingressXX"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_15(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("INGRESS"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_16(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = None
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_17(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(None)
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_18(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get(None))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_19(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("XXegressXX"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_20(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("EGRESS"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_21(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=None,
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_22(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=None,
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_23(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=None,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_24(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=None,
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_25(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=None,
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_26(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=None,
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_27(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=None,
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_28(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=None,
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_29(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=None,
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_30(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=None,
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_31(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=None,
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_32(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=None,
    )


def x_parse_global_network_policy__mutmut_33(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_34(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_35(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_36(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_37(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_38(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_39(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_40(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_41(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_42(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_43(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_44(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        )


def x_parse_global_network_policy__mutmut_45(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(None),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_46(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get(None, "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_47(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", None)),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_48(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_49(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", )),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_50(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("XXnameXX", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_51(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("NAME", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_52(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "XXXX")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_53(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="XXXX",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_54(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(None),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_55(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(None),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_56(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get(None, "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_57(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", None)),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_58(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_59(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", )),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_60(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("XXselectorXX", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_61(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("SELECTOR", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_62(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "XXXX")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_63(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(None),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_64(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(None) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_65(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(None),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_66(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(None) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_67(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(None, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_68(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, None),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_69(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_70(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, ),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_71(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(None),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_72(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get(None, False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_73(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", None)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_74(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get(False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_75(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", )),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_76(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("XXapplyOnForwardXX", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_77(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyonforward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_78(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("APPLYONFORWARD", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_79(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", True)),
        has_l7_rule=_has_l7(ingress) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_80(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) and _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_81(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(None) or _has_l7(egress),
    )


def x_parse_global_network_policy__mutmut_82(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
        has_l7_rule=_has_l7(ingress) or _has_l7(None),
    )

mutants_x_parse_global_network_policy__mutmut['_mutmut_orig'] = x_parse_global_network_policy__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_1'] = x_parse_global_network_policy__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_2'] = x_parse_global_network_policy__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_3'] = x_parse_global_network_policy__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_4'] = x_parse_global_network_policy__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_5'] = x_parse_global_network_policy__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_6'] = x_parse_global_network_policy__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_7'] = x_parse_global_network_policy__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_8'] = x_parse_global_network_policy__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_9'] = x_parse_global_network_policy__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_10'] = x_parse_global_network_policy__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_11'] = x_parse_global_network_policy__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_12'] = x_parse_global_network_policy__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_13'] = x_parse_global_network_policy__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_14'] = x_parse_global_network_policy__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_15'] = x_parse_global_network_policy__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_16'] = x_parse_global_network_policy__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_17'] = x_parse_global_network_policy__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_18'] = x_parse_global_network_policy__mutmut_18 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_19'] = x_parse_global_network_policy__mutmut_19 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_20'] = x_parse_global_network_policy__mutmut_20 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_21'] = x_parse_global_network_policy__mutmut_21 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_22'] = x_parse_global_network_policy__mutmut_22 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_23'] = x_parse_global_network_policy__mutmut_23 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_24'] = x_parse_global_network_policy__mutmut_24 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_25'] = x_parse_global_network_policy__mutmut_25 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_26'] = x_parse_global_network_policy__mutmut_26 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_27'] = x_parse_global_network_policy__mutmut_27 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_28'] = x_parse_global_network_policy__mutmut_28 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_29'] = x_parse_global_network_policy__mutmut_29 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_30'] = x_parse_global_network_policy__mutmut_30 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_31'] = x_parse_global_network_policy__mutmut_31 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_32'] = x_parse_global_network_policy__mutmut_32 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_33'] = x_parse_global_network_policy__mutmut_33 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_34'] = x_parse_global_network_policy__mutmut_34 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_35'] = x_parse_global_network_policy__mutmut_35 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_36'] = x_parse_global_network_policy__mutmut_36 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_37'] = x_parse_global_network_policy__mutmut_37 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_38'] = x_parse_global_network_policy__mutmut_38 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_39'] = x_parse_global_network_policy__mutmut_39 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_40'] = x_parse_global_network_policy__mutmut_40 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_41'] = x_parse_global_network_policy__mutmut_41 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_42'] = x_parse_global_network_policy__mutmut_42 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_43'] = x_parse_global_network_policy__mutmut_43 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_44'] = x_parse_global_network_policy__mutmut_44 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_45'] = x_parse_global_network_policy__mutmut_45 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_46'] = x_parse_global_network_policy__mutmut_46 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_47'] = x_parse_global_network_policy__mutmut_47 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_48'] = x_parse_global_network_policy__mutmut_48 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_49'] = x_parse_global_network_policy__mutmut_49 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_50'] = x_parse_global_network_policy__mutmut_50 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_51'] = x_parse_global_network_policy__mutmut_51 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_52'] = x_parse_global_network_policy__mutmut_52 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_53'] = x_parse_global_network_policy__mutmut_53 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_54'] = x_parse_global_network_policy__mutmut_54 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_55'] = x_parse_global_network_policy__mutmut_55 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_56'] = x_parse_global_network_policy__mutmut_56 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_57'] = x_parse_global_network_policy__mutmut_57 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_58'] = x_parse_global_network_policy__mutmut_58 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_59'] = x_parse_global_network_policy__mutmut_59 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_60'] = x_parse_global_network_policy__mutmut_60 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_61'] = x_parse_global_network_policy__mutmut_61 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_62'] = x_parse_global_network_policy__mutmut_62 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_63'] = x_parse_global_network_policy__mutmut_63 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_64'] = x_parse_global_network_policy__mutmut_64 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_65'] = x_parse_global_network_policy__mutmut_65 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_66'] = x_parse_global_network_policy__mutmut_66 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_67'] = x_parse_global_network_policy__mutmut_67 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_68'] = x_parse_global_network_policy__mutmut_68 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_69'] = x_parse_global_network_policy__mutmut_69 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_70'] = x_parse_global_network_policy__mutmut_70 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_71'] = x_parse_global_network_policy__mutmut_71 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_72'] = x_parse_global_network_policy__mutmut_72 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_73'] = x_parse_global_network_policy__mutmut_73 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_74'] = x_parse_global_network_policy__mutmut_74 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_75'] = x_parse_global_network_policy__mutmut_75 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_76'] = x_parse_global_network_policy__mutmut_76 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_77'] = x_parse_global_network_policy__mutmut_77 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_78'] = x_parse_global_network_policy__mutmut_78 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_79'] = x_parse_global_network_policy__mutmut_79 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_80'] = x_parse_global_network_policy__mutmut_80 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_81'] = x_parse_global_network_policy__mutmut_81 # type: ignore # mutmut generated
mutants_x_parse_global_network_policy__mutmut['x_parse_global_network_policy__mutmut_82'] = x_parse_global_network_policy__mutmut_82 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_resolve_action__mutmut)
def resolve_action(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_orig(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_1(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = None
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_2(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).upper()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_3(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(None).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_4(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get(None, "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_5(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", None)).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_6(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_7(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", )).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_8(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("XXactionXX", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_9(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("ACTION", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_10(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "XXXX")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_11(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress - egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_12(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) or rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_13(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get(None)
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_14(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("XXactionXX")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_15(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("ACTION")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_16(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_17(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = None
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_18(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(None)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_19(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) != 1:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_20(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 2:
        return lowered[0]
    return "mixed"


def x_resolve_action__mutmut_21(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[1]
    return "mixed"


def x_resolve_action__mutmut_22(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "XXmixedXX"


def x_resolve_action__mutmut_23(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "MIXED"

mutants_x_resolve_action__mutmut['_mutmut_orig'] = x_resolve_action__mutmut_orig # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_1'] = x_resolve_action__mutmut_1 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_2'] = x_resolve_action__mutmut_2 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_3'] = x_resolve_action__mutmut_3 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_4'] = x_resolve_action__mutmut_4 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_5'] = x_resolve_action__mutmut_5 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_6'] = x_resolve_action__mutmut_6 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_7'] = x_resolve_action__mutmut_7 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_8'] = x_resolve_action__mutmut_8 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_9'] = x_resolve_action__mutmut_9 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_10'] = x_resolve_action__mutmut_10 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_11'] = x_resolve_action__mutmut_11 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_12'] = x_resolve_action__mutmut_12 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_13'] = x_resolve_action__mutmut_13 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_14'] = x_resolve_action__mutmut_14 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_15'] = x_resolve_action__mutmut_15 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_16'] = x_resolve_action__mutmut_16 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_17'] = x_resolve_action__mutmut_17 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_18'] = x_resolve_action__mutmut_18 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_19'] = x_resolve_action__mutmut_19 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_20'] = x_resolve_action__mutmut_20 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_21'] = x_resolve_action__mutmut_21 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_22'] = x_resolve_action__mutmut_22 # type: ignore # mutmut generated
mutants_x_resolve_action__mutmut['x_resolve_action__mutmut_23'] = x_resolve_action__mutmut_23 # type: ignore # mutmut generated


def _as_mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}
mutants_x__order__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__order__mutmut)
def _order(spec: Mapping[str, object]) -> float:
    try:
        return float(spec.get("order", 0.0))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__order__mutmut_orig(spec: Mapping[str, object]) -> float:
    try:
        return float(spec.get("order", 0.0))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__order__mutmut_1(spec: Mapping[str, object]) -> float:
    try:
        return float(None)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__order__mutmut_2(spec: Mapping[str, object]) -> float:
    try:
        return float(spec.get(None, 0.0))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__order__mutmut_3(spec: Mapping[str, object]) -> float:
    try:
        return float(spec.get("order", None))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__order__mutmut_4(spec: Mapping[str, object]) -> float:
    try:
        return float(spec.get(0.0))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__order__mutmut_5(spec: Mapping[str, object]) -> float:
    try:
        return float(spec.get("order", ))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__order__mutmut_6(spec: Mapping[str, object]) -> float:
    try:
        return float(spec.get("XXorderXX", 0.0))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__order__mutmut_7(spec: Mapping[str, object]) -> float:
    try:
        return float(spec.get("ORDER", 0.0))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__order__mutmut_8(spec: Mapping[str, object]) -> float:
    try:
        return float(spec.get("order", 1.0))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__order__mutmut_9(spec: Mapping[str, object]) -> float:
    try:
        return float(spec.get("order", 0.0))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 1.0

mutants_x__order__mutmut['_mutmut_orig'] = x__order__mutmut_orig # type: ignore # mutmut generated
mutants_x__order__mutmut['x__order__mutmut_1'] = x__order__mutmut_1 # type: ignore # mutmut generated
mutants_x__order__mutmut['x__order__mutmut_2'] = x__order__mutmut_2 # type: ignore # mutmut generated
mutants_x__order__mutmut['x__order__mutmut_3'] = x__order__mutmut_3 # type: ignore # mutmut generated
mutants_x__order__mutmut['x__order__mutmut_4'] = x__order__mutmut_4 # type: ignore # mutmut generated
mutants_x__order__mutmut['x__order__mutmut_5'] = x__order__mutmut_5 # type: ignore # mutmut generated
mutants_x__order__mutmut['x__order__mutmut_6'] = x__order__mutmut_6 # type: ignore # mutmut generated
mutants_x__order__mutmut['x__order__mutmut_7'] = x__order__mutmut_7 # type: ignore # mutmut generated
mutants_x__order__mutmut['x__order__mutmut_8'] = x__order__mutmut_8 # type: ignore # mutmut generated
mutants_x__order__mutmut['x__order__mutmut_9'] = x__order__mutmut_9 # type: ignore # mutmut generated
mutants_x__rules__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__rules__mutmut)
def _rules(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, list):
        return []
    return [rule for rule in raw if isinstance(rule, dict)]


def x__rules__mutmut_orig(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, list):
        return []
    return [rule for rule in raw if isinstance(rule, dict)]


def x__rules__mutmut_1(raw: object) -> list[dict[str, object]]:
    if isinstance(raw, list):
        return []
    return [rule for rule in raw if isinstance(rule, dict)]

mutants_x__rules__mutmut['_mutmut_orig'] = x__rules__mutmut_orig # type: ignore # mutmut generated
mutants_x__rules__mutmut['x__rules__mutmut_1'] = x__rules__mutmut_1 # type: ignore # mutmut generated
mutants_x__has_l7__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__has_l7__mutmut)
def _has_l7(rules: list[dict[str, object]]) -> bool:
    """True when any rule carries application-layer (http/tls) semantics."""
    return any("http" in rule or "tls" in rule for rule in rules)


def x__has_l7__mutmut_orig(rules: list[dict[str, object]]) -> bool:
    """True when any rule carries application-layer (http/tls) semantics."""
    return any("http" in rule or "tls" in rule for rule in rules)


def x__has_l7__mutmut_1(rules: list[dict[str, object]]) -> bool:
    """True when any rule carries application-layer (http/tls) semantics."""
    return any(None)


def x__has_l7__mutmut_2(rules: list[dict[str, object]]) -> bool:
    """True when any rule carries application-layer (http/tls) semantics."""
    return any("http" in rule and "tls" in rule for rule in rules)


def x__has_l7__mutmut_3(rules: list[dict[str, object]]) -> bool:
    """True when any rule carries application-layer (http/tls) semantics."""
    return any("XXhttpXX" in rule or "tls" in rule for rule in rules)


def x__has_l7__mutmut_4(rules: list[dict[str, object]]) -> bool:
    """True when any rule carries application-layer (http/tls) semantics."""
    return any("HTTP" in rule or "tls" in rule for rule in rules)


def x__has_l7__mutmut_5(rules: list[dict[str, object]]) -> bool:
    """True when any rule carries application-layer (http/tls) semantics."""
    return any("http" not in rule or "tls" in rule for rule in rules)


def x__has_l7__mutmut_6(rules: list[dict[str, object]]) -> bool:
    """True when any rule carries application-layer (http/tls) semantics."""
    return any("http" in rule or "XXtlsXX" in rule for rule in rules)


def x__has_l7__mutmut_7(rules: list[dict[str, object]]) -> bool:
    """True when any rule carries application-layer (http/tls) semantics."""
    return any("http" in rule or "TLS" in rule for rule in rules)


def x__has_l7__mutmut_8(rules: list[dict[str, object]]) -> bool:
    """True when any rule carries application-layer (http/tls) semantics."""
    return any("http" in rule or "tls" not in rule for rule in rules)

mutants_x__has_l7__mutmut['_mutmut_orig'] = x__has_l7__mutmut_orig # type: ignore # mutmut generated
mutants_x__has_l7__mutmut['x__has_l7__mutmut_1'] = x__has_l7__mutmut_1 # type: ignore # mutmut generated
mutants_x__has_l7__mutmut['x__has_l7__mutmut_2'] = x__has_l7__mutmut_2 # type: ignore # mutmut generated
mutants_x__has_l7__mutmut['x__has_l7__mutmut_3'] = x__has_l7__mutmut_3 # type: ignore # mutmut generated
mutants_x__has_l7__mutmut['x__has_l7__mutmut_4'] = x__has_l7__mutmut_4 # type: ignore # mutmut generated
mutants_x__has_l7__mutmut['x__has_l7__mutmut_5'] = x__has_l7__mutmut_5 # type: ignore # mutmut generated
mutants_x__has_l7__mutmut['x__has_l7__mutmut_6'] = x__has_l7__mutmut_6 # type: ignore # mutmut generated
mutants_x__has_l7__mutmut['x__has_l7__mutmut_7'] = x__has_l7__mutmut_7 # type: ignore # mutmut generated
mutants_x__has_l7__mutmut['x__has_l7__mutmut_8'] = x__has_l7__mutmut_8 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__summarize_rule__mutmut)
def _summarize_rule(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_orig(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_1(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = None
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_2(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).upper()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_3(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(None).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_4(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get(None, "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_5(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", None)).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_6(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_7(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", )).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_8(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("XXactionXX", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_9(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("ACTION", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_10(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "XXallowXX")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_11(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "ALLOW")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_12(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = None
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_13(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).upper()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_14(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(None).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_15(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get(None, "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_16(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", None)).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_17(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_18(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", )).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_19(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("XXprotocolXX", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_20(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("PROTOCOL", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_21(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "XXXX")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_22(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = None
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_23(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(None)
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_24(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get(None))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_25(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("XXdestinationXX"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_26(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("DESTINATION"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_27(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = None
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_28(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") and ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_29(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") and destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_30(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get(None) or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_31(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("XXportsXX") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_32(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("PORTS") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_33(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get(None) or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_34(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("XXportXX") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_35(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("PORT") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_36(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or "XXXX"
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_37(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = None
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_38(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(None)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_39(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = "XX,XX".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_40(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(None) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_41(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = None
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_42(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = None
    if ports:
        summary = f"{summary} {ports}"
    return summary


def x__summarize_rule__mutmut_43(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = None
    return summary

mutants_x__summarize_rule__mutmut['_mutmut_orig'] = x__summarize_rule__mutmut_orig # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_1'] = x__summarize_rule__mutmut_1 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_2'] = x__summarize_rule__mutmut_2 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_3'] = x__summarize_rule__mutmut_3 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_4'] = x__summarize_rule__mutmut_4 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_5'] = x__summarize_rule__mutmut_5 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_6'] = x__summarize_rule__mutmut_6 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_7'] = x__summarize_rule__mutmut_7 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_8'] = x__summarize_rule__mutmut_8 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_9'] = x__summarize_rule__mutmut_9 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_10'] = x__summarize_rule__mutmut_10 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_11'] = x__summarize_rule__mutmut_11 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_12'] = x__summarize_rule__mutmut_12 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_13'] = x__summarize_rule__mutmut_13 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_14'] = x__summarize_rule__mutmut_14 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_15'] = x__summarize_rule__mutmut_15 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_16'] = x__summarize_rule__mutmut_16 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_17'] = x__summarize_rule__mutmut_17 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_18'] = x__summarize_rule__mutmut_18 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_19'] = x__summarize_rule__mutmut_19 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_20'] = x__summarize_rule__mutmut_20 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_21'] = x__summarize_rule__mutmut_21 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_22'] = x__summarize_rule__mutmut_22 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_23'] = x__summarize_rule__mutmut_23 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_24'] = x__summarize_rule__mutmut_24 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_25'] = x__summarize_rule__mutmut_25 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_26'] = x__summarize_rule__mutmut_26 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_27'] = x__summarize_rule__mutmut_27 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_28'] = x__summarize_rule__mutmut_28 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_29'] = x__summarize_rule__mutmut_29 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_30'] = x__summarize_rule__mutmut_30 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_31'] = x__summarize_rule__mutmut_31 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_32'] = x__summarize_rule__mutmut_32 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_33'] = x__summarize_rule__mutmut_33 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_34'] = x__summarize_rule__mutmut_34 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_35'] = x__summarize_rule__mutmut_35 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_36'] = x__summarize_rule__mutmut_36 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_37'] = x__summarize_rule__mutmut_37 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_38'] = x__summarize_rule__mutmut_38 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_39'] = x__summarize_rule__mutmut_39 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_40'] = x__summarize_rule__mutmut_40 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_41'] = x__summarize_rule__mutmut_41 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_42'] = x__summarize_rule__mutmut_42 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut['x__summarize_rule__mutmut_43'] = x__summarize_rule__mutmut_43 # type: ignore # mutmut generated
