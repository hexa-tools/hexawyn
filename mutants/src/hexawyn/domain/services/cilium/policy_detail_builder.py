"""Pure Cilium network-policy detail builder — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumL7RuleSummary,
    CiliumNetworkPolicyDetail,
    CiliumRuleSummary,
)

_NOT_INSTALLED_NOTE = "Cilium is not installed in this cluster"
_ENDPOINT_KEYS = (
    "fromEndpoints",
    "toEndpoints",
    "fromEntities",
    "toEntities",
    "fromCIDR",
    "toCIDR",
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


def _as_dict(value: object) -> dict[str, object]:
    return value if isinstance(value, dict) else {}


def _list_field(value: object) -> list[object]:
    return value if isinstance(value, list) else []
mutants_x_build_policy_detail__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_policy_detail__mutmut)
def build_policy_detail(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_orig(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_1(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = None
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_2(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(None)
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_3(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get(None))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_4(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("XXmetadataXX"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_5(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("METADATA"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_6(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = None
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_7(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(None)
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_8(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get(None))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_9(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("XXspecXX"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_10(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("SPEC"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_11(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = None
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_12(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        None
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_13(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule(None, rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_14(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", None)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_15(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule(rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_16(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", )
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_17(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("XXingressXX", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_18(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("INGRESS", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_19(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(None)
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_20(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get(None))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_21(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("XXingressXX"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_22(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("INGRESS"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_23(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = None
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_24(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        None
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_25(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule(None, rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_26(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", None)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_27(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule(rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_28(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", )
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_29(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("XXegressXX", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_30(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("EGRESS", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_31(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(None)
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_32(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get(None))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_33(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("XXegressXX"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_34(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("EGRESS"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_35(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = None
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_36(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols(None)
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_37(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=None,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_38(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status=None,
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_39(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=None,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_40(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=None,
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_41(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_42(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=None,
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_43(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=None,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_44(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=None,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_45(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=None,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_46(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=None,
        note=None,
    )


def x_build_policy_detail__mutmut_47(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_48(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_49(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_50(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_51(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_52(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_53(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_54(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_55(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_56(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        note=None,
    )


def x_build_policy_detail__mutmut_57(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        )


def x_build_policy_detail__mutmut_58(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_59(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="XXokXX",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_60(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="OK",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_61(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(None),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_62(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get(None, "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_63(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", None)),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_64(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_65(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", )),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_66(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("XXnameXX", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_67(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("NAME", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_68(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "XXXX")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_69(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(None),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_70(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get(None)),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_71(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("XXendpointSelectorXX")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_72(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointselector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def x_build_policy_detail__mutmut_73(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("ENDPOINTSELECTOR")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )

mutants_x_build_policy_detail__mutmut['_mutmut_orig'] = x_build_policy_detail__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_1'] = x_build_policy_detail__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_2'] = x_build_policy_detail__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_3'] = x_build_policy_detail__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_4'] = x_build_policy_detail__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_5'] = x_build_policy_detail__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_6'] = x_build_policy_detail__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_7'] = x_build_policy_detail__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_8'] = x_build_policy_detail__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_9'] = x_build_policy_detail__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_10'] = x_build_policy_detail__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_11'] = x_build_policy_detail__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_12'] = x_build_policy_detail__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_13'] = x_build_policy_detail__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_14'] = x_build_policy_detail__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_15'] = x_build_policy_detail__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_16'] = x_build_policy_detail__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_17'] = x_build_policy_detail__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_18'] = x_build_policy_detail__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_19'] = x_build_policy_detail__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_20'] = x_build_policy_detail__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_21'] = x_build_policy_detail__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_22'] = x_build_policy_detail__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_23'] = x_build_policy_detail__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_24'] = x_build_policy_detail__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_25'] = x_build_policy_detail__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_26'] = x_build_policy_detail__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_27'] = x_build_policy_detail__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_28'] = x_build_policy_detail__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_29'] = x_build_policy_detail__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_30'] = x_build_policy_detail__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_31'] = x_build_policy_detail__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_32'] = x_build_policy_detail__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_33'] = x_build_policy_detail__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_34'] = x_build_policy_detail__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_35'] = x_build_policy_detail__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_36'] = x_build_policy_detail__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_37'] = x_build_policy_detail__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_38'] = x_build_policy_detail__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_39'] = x_build_policy_detail__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_40'] = x_build_policy_detail__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_41'] = x_build_policy_detail__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_42'] = x_build_policy_detail__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_43'] = x_build_policy_detail__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_44'] = x_build_policy_detail__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_45'] = x_build_policy_detail__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_46'] = x_build_policy_detail__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_47'] = x_build_policy_detail__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_48'] = x_build_policy_detail__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_49'] = x_build_policy_detail__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_50'] = x_build_policy_detail__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_51'] = x_build_policy_detail__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_52'] = x_build_policy_detail__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_53'] = x_build_policy_detail__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_54'] = x_build_policy_detail__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_55'] = x_build_policy_detail__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_56'] = x_build_policy_detail__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_57'] = x_build_policy_detail__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_58'] = x_build_policy_detail__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_59'] = x_build_policy_detail__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_60'] = x_build_policy_detail__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_61'] = x_build_policy_detail__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_62'] = x_build_policy_detail__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_63'] = x_build_policy_detail__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_64'] = x_build_policy_detail__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_65'] = x_build_policy_detail__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_66'] = x_build_policy_detail__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_67'] = x_build_policy_detail__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_68'] = x_build_policy_detail__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_69'] = x_build_policy_detail__mutmut_69 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_70'] = x_build_policy_detail__mutmut_70 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_71'] = x_build_policy_detail__mutmut_71 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_72'] = x_build_policy_detail__mutmut_72 # type: ignore # mutmut generated
mutants_x_build_policy_detail__mutmut['x_build_policy_detail__mutmut_73'] = x_build_policy_detail__mutmut_73 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_not_installed_policy_detail__mutmut)
def not_installed_policy_detail() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_orig() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_1() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=None,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_2() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status=None,
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_3() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind=None,
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_4() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name=None,
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_5() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector=None,
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_6() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=None,
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_7() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=None,
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_8() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=None,
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_9() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_10() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=None,
    )


def x_not_installed_policy_detail__mutmut_11() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_12() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_13() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_14() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_15() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_16() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_17() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_18() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_19() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_20() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_21() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        )


def x_not_installed_policy_detail__mutmut_22() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_23() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="XXnot_installedXX",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_24() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="NOT_INSTALLED",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_25() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="XXXX",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_26() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="XXXX",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policy_detail__mutmut_27() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="XXXX",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
        note=_NOT_INSTALLED_NOTE,
    )

mutants_x_not_installed_policy_detail__mutmut['_mutmut_orig'] = x_not_installed_policy_detail__mutmut_orig # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_1'] = x_not_installed_policy_detail__mutmut_1 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_2'] = x_not_installed_policy_detail__mutmut_2 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_3'] = x_not_installed_policy_detail__mutmut_3 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_4'] = x_not_installed_policy_detail__mutmut_4 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_5'] = x_not_installed_policy_detail__mutmut_5 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_6'] = x_not_installed_policy_detail__mutmut_6 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_7'] = x_not_installed_policy_detail__mutmut_7 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_8'] = x_not_installed_policy_detail__mutmut_8 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_9'] = x_not_installed_policy_detail__mutmut_9 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_10'] = x_not_installed_policy_detail__mutmut_10 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_11'] = x_not_installed_policy_detail__mutmut_11 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_12'] = x_not_installed_policy_detail__mutmut_12 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_13'] = x_not_installed_policy_detail__mutmut_13 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_14'] = x_not_installed_policy_detail__mutmut_14 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_15'] = x_not_installed_policy_detail__mutmut_15 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_16'] = x_not_installed_policy_detail__mutmut_16 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_17'] = x_not_installed_policy_detail__mutmut_17 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_18'] = x_not_installed_policy_detail__mutmut_18 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_19'] = x_not_installed_policy_detail__mutmut_19 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_20'] = x_not_installed_policy_detail__mutmut_20 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_21'] = x_not_installed_policy_detail__mutmut_21 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_22'] = x_not_installed_policy_detail__mutmut_22 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_23'] = x_not_installed_policy_detail__mutmut_23 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_24'] = x_not_installed_policy_detail__mutmut_24 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_25'] = x_not_installed_policy_detail__mutmut_25 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_26'] = x_not_installed_policy_detail__mutmut_26 # type: ignore # mutmut generated
mutants_x_not_installed_policy_detail__mutmut['x_not_installed_policy_detail__mutmut_27'] = x_not_installed_policy_detail__mutmut_27 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__render_selector__mutmut)
def _render_selector(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_orig(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_1(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is not None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_2(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "XXmatchLabels: {}XX"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_3(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchlabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_4(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "MATCHLABELS: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_5(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = None
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_6(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get(None)
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_7(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("XXmatchLabelsXX")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_8(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchlabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_9(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("MATCHLABELS")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_10(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = None
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_11(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = None
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_12(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(None)
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_13(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = "XX, XX".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_14(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(None))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def x__render_selector__mutmut_15(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "XXmatchLabels: {}XX"
    return str(selector)


def x__render_selector__mutmut_16(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchlabels: {}"
    return str(selector)


def x__render_selector__mutmut_17(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "MATCHLABELS: {}"
    return str(selector)


def x__render_selector__mutmut_18(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(None)

mutants_x__render_selector__mutmut['_mutmut_orig'] = x__render_selector__mutmut_orig # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_1'] = x__render_selector__mutmut_1 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_2'] = x__render_selector__mutmut_2 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_3'] = x__render_selector__mutmut_3 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_4'] = x__render_selector__mutmut_4 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_5'] = x__render_selector__mutmut_5 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_6'] = x__render_selector__mutmut_6 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_7'] = x__render_selector__mutmut_7 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_8'] = x__render_selector__mutmut_8 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_9'] = x__render_selector__mutmut_9 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_10'] = x__render_selector__mutmut_10 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_11'] = x__render_selector__mutmut_11 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_12'] = x__render_selector__mutmut_12 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_13'] = x__render_selector__mutmut_13 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_14'] = x__render_selector__mutmut_14 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_15'] = x__render_selector__mutmut_15 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_16'] = x__render_selector__mutmut_16 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_17'] = x__render_selector__mutmut_17 # type: ignore # mutmut generated
mutants_x__render_selector__mutmut['x__render_selector__mutmut_18'] = x__render_selector__mutmut_18 # type: ignore # mutmut generated
mutants_x__summarize_rule__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__summarize_rule__mutmut)
def _summarize_rule(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_orig(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_1(direction: str, rule: object) -> CiliumRuleSummary:
    if isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_2(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=None, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_3(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=None, ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_4(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=None, l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_5(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=None)
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_6(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_7(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_8(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_9(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), )
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_10(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=None,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_11(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=None,
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_12(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=None,
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_13(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=None,
    )


def x__summarize_rule__mutmut_14(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_15(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_16(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_17(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        )


def x__summarize_rule__mutmut_18(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(None),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_19(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(None),
        l7=_render_l7(rule),
    )


def x__summarize_rule__mutmut_20(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(None),
    )

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
mutants_x__render_endpoints__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__render_endpoints__mutmut)
def _render_endpoints(rule: dict[str, object]) -> tuple[str, ...]:
    rendered: list[str] = []
    for key in _ENDPOINT_KEYS:
        for item in _list_field(rule.get(key)):
            rendered.append(_render_entity(item))
    return tuple(rendered)


def x__render_endpoints__mutmut_orig(rule: dict[str, object]) -> tuple[str, ...]:
    rendered: list[str] = []
    for key in _ENDPOINT_KEYS:
        for item in _list_field(rule.get(key)):
            rendered.append(_render_entity(item))
    return tuple(rendered)


def x__render_endpoints__mutmut_1(rule: dict[str, object]) -> tuple[str, ...]:
    rendered: list[str] = None
    for key in _ENDPOINT_KEYS:
        for item in _list_field(rule.get(key)):
            rendered.append(_render_entity(item))
    return tuple(rendered)


def x__render_endpoints__mutmut_2(rule: dict[str, object]) -> tuple[str, ...]:
    rendered: list[str] = []
    for key in _ENDPOINT_KEYS:
        for item in _list_field(None):
            rendered.append(_render_entity(item))
    return tuple(rendered)


def x__render_endpoints__mutmut_3(rule: dict[str, object]) -> tuple[str, ...]:
    rendered: list[str] = []
    for key in _ENDPOINT_KEYS:
        for item in _list_field(rule.get(None)):
            rendered.append(_render_entity(item))
    return tuple(rendered)


def x__render_endpoints__mutmut_4(rule: dict[str, object]) -> tuple[str, ...]:
    rendered: list[str] = []
    for key in _ENDPOINT_KEYS:
        for item in _list_field(rule.get(key)):
            rendered.append(None)
    return tuple(rendered)


def x__render_endpoints__mutmut_5(rule: dict[str, object]) -> tuple[str, ...]:
    rendered: list[str] = []
    for key in _ENDPOINT_KEYS:
        for item in _list_field(rule.get(key)):
            rendered.append(_render_entity(None))
    return tuple(rendered)


def x__render_endpoints__mutmut_6(rule: dict[str, object]) -> tuple[str, ...]:
    rendered: list[str] = []
    for key in _ENDPOINT_KEYS:
        for item in _list_field(rule.get(key)):
            rendered.append(_render_entity(item))
    return tuple(None)

mutants_x__render_endpoints__mutmut['_mutmut_orig'] = x__render_endpoints__mutmut_orig # type: ignore # mutmut generated
mutants_x__render_endpoints__mutmut['x__render_endpoints__mutmut_1'] = x__render_endpoints__mutmut_1 # type: ignore # mutmut generated
mutants_x__render_endpoints__mutmut['x__render_endpoints__mutmut_2'] = x__render_endpoints__mutmut_2 # type: ignore # mutmut generated
mutants_x__render_endpoints__mutmut['x__render_endpoints__mutmut_3'] = x__render_endpoints__mutmut_3 # type: ignore # mutmut generated
mutants_x__render_endpoints__mutmut['x__render_endpoints__mutmut_4'] = x__render_endpoints__mutmut_4 # type: ignore # mutmut generated
mutants_x__render_endpoints__mutmut['x__render_endpoints__mutmut_5'] = x__render_endpoints__mutmut_5 # type: ignore # mutmut generated
mutants_x__render_endpoints__mutmut['x__render_endpoints__mutmut_6'] = x__render_endpoints__mutmut_6 # type: ignore # mutmut generated
mutants_x__render_entity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__render_entity__mutmut)
def _render_entity(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get("matchLabels")
        if isinstance(labels, dict) and labels:
            pairs = ", ".join(f"{k}={v}" for k, v in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return str(item)
    return str(item)


def x__render_entity__mutmut_orig(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get("matchLabels")
        if isinstance(labels, dict) and labels:
            pairs = ", ".join(f"{k}={v}" for k, v in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return str(item)
    return str(item)


def x__render_entity__mutmut_1(item: object) -> str:
    if isinstance(item, dict):
        labels = None
        if isinstance(labels, dict) and labels:
            pairs = ", ".join(f"{k}={v}" for k, v in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return str(item)
    return str(item)


def x__render_entity__mutmut_2(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get(None)
        if isinstance(labels, dict) and labels:
            pairs = ", ".join(f"{k}={v}" for k, v in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return str(item)
    return str(item)


def x__render_entity__mutmut_3(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get("XXmatchLabelsXX")
        if isinstance(labels, dict) and labels:
            pairs = ", ".join(f"{k}={v}" for k, v in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return str(item)
    return str(item)


def x__render_entity__mutmut_4(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get("matchlabels")
        if isinstance(labels, dict) and labels:
            pairs = ", ".join(f"{k}={v}" for k, v in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return str(item)
    return str(item)


def x__render_entity__mutmut_5(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get("MATCHLABELS")
        if isinstance(labels, dict) and labels:
            pairs = ", ".join(f"{k}={v}" for k, v in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return str(item)
    return str(item)


def x__render_entity__mutmut_6(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get("matchLabels")
        if isinstance(labels, dict) or labels:
            pairs = ", ".join(f"{k}={v}" for k, v in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return str(item)
    return str(item)


def x__render_entity__mutmut_7(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get("matchLabels")
        if isinstance(labels, dict) and labels:
            pairs = None
            return f"matchLabels: {pairs}"
        return str(item)
    return str(item)


def x__render_entity__mutmut_8(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get("matchLabels")
        if isinstance(labels, dict) and labels:
            pairs = ", ".join(None)
            return f"matchLabels: {pairs}"
        return str(item)
    return str(item)


def x__render_entity__mutmut_9(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get("matchLabels")
        if isinstance(labels, dict) and labels:
            pairs = "XX, XX".join(f"{k}={v}" for k, v in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return str(item)
    return str(item)


def x__render_entity__mutmut_10(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get("matchLabels")
        if isinstance(labels, dict) and labels:
            pairs = ", ".join(f"{k}={v}" for k, v in sorted(None))
            return f"matchLabels: {pairs}"
        return str(item)
    return str(item)


def x__render_entity__mutmut_11(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get("matchLabels")
        if isinstance(labels, dict) and labels:
            pairs = ", ".join(f"{k}={v}" for k, v in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return str(None)
    return str(item)


def x__render_entity__mutmut_12(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get("matchLabels")
        if isinstance(labels, dict) and labels:
            pairs = ", ".join(f"{k}={v}" for k, v in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return str(item)
    return str(None)

mutants_x__render_entity__mutmut['_mutmut_orig'] = x__render_entity__mutmut_orig # type: ignore # mutmut generated
mutants_x__render_entity__mutmut['x__render_entity__mutmut_1'] = x__render_entity__mutmut_1 # type: ignore # mutmut generated
mutants_x__render_entity__mutmut['x__render_entity__mutmut_2'] = x__render_entity__mutmut_2 # type: ignore # mutmut generated
mutants_x__render_entity__mutmut['x__render_entity__mutmut_3'] = x__render_entity__mutmut_3 # type: ignore # mutmut generated
mutants_x__render_entity__mutmut['x__render_entity__mutmut_4'] = x__render_entity__mutmut_4 # type: ignore # mutmut generated
mutants_x__render_entity__mutmut['x__render_entity__mutmut_5'] = x__render_entity__mutmut_5 # type: ignore # mutmut generated
mutants_x__render_entity__mutmut['x__render_entity__mutmut_6'] = x__render_entity__mutmut_6 # type: ignore # mutmut generated
mutants_x__render_entity__mutmut['x__render_entity__mutmut_7'] = x__render_entity__mutmut_7 # type: ignore # mutmut generated
mutants_x__render_entity__mutmut['x__render_entity__mutmut_8'] = x__render_entity__mutmut_8 # type: ignore # mutmut generated
mutants_x__render_entity__mutmut['x__render_entity__mutmut_9'] = x__render_entity__mutmut_9 # type: ignore # mutmut generated
mutants_x__render_entity__mutmut['x__render_entity__mutmut_10'] = x__render_entity__mutmut_10 # type: ignore # mutmut generated
mutants_x__render_entity__mutmut['x__render_entity__mutmut_11'] = x__render_entity__mutmut_11 # type: ignore # mutmut generated
mutants_x__render_entity__mutmut['x__render_entity__mutmut_12'] = x__render_entity__mutmut_12 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__render_ports__mutmut)
def _render_ports(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_orig(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_1(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = None
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_2(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(None):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_3(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get(None)):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_4(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("XXtoPortsXX")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_5(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toports")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_6(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("TOPORTS")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_7(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_8(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            break
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_9(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(None):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_10(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get(None)):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_11(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("XXportsXX")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_12(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("PORTS")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_13(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = None
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_14(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get(None)
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_15(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("XXportXX")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_16(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("PORT")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_17(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = None
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_18(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get(None)
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_19(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("XXprotocolXX")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_20(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("PROTOCOL")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_21(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(None)
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_22(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is None:
                    ports.append(str(port))
    return tuple(ports)


def x__render_ports__mutmut_23(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(None)
    return tuple(ports)


def x__render_ports__mutmut_24(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(None))
    return tuple(ports)


def x__render_ports__mutmut_25(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(None)

mutants_x__render_ports__mutmut['_mutmut_orig'] = x__render_ports__mutmut_orig # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_1'] = x__render_ports__mutmut_1 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_2'] = x__render_ports__mutmut_2 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_3'] = x__render_ports__mutmut_3 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_4'] = x__render_ports__mutmut_4 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_5'] = x__render_ports__mutmut_5 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_6'] = x__render_ports__mutmut_6 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_7'] = x__render_ports__mutmut_7 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_8'] = x__render_ports__mutmut_8 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_9'] = x__render_ports__mutmut_9 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_10'] = x__render_ports__mutmut_10 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_11'] = x__render_ports__mutmut_11 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_12'] = x__render_ports__mutmut_12 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_13'] = x__render_ports__mutmut_13 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_14'] = x__render_ports__mutmut_14 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_15'] = x__render_ports__mutmut_15 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_16'] = x__render_ports__mutmut_16 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_17'] = x__render_ports__mutmut_17 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_18'] = x__render_ports__mutmut_18 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_19'] = x__render_ports__mutmut_19 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_20'] = x__render_ports__mutmut_20 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_21'] = x__render_ports__mutmut_21 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_22'] = x__render_ports__mutmut_22 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_23'] = x__render_ports__mutmut_23 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_24'] = x__render_ports__mutmut_24 # type: ignore # mutmut generated
mutants_x__render_ports__mutmut['x__render_ports__mutmut_25'] = x__render_ports__mutmut_25 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__render_l7__mutmut)
def _render_l7(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_orig(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_1(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = None
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_2(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(None):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_3(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get(None)):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_4(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("XXtoPortsXX")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_5(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toports")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_6(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("TOPORTS")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_7(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_8(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            break
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_9(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = None
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_10(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get(None)
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_11(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("XXrulesXX")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_12(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("RULES")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_13(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) and not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_14(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_15(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_16(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            break
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_17(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                None
            )
    return tuple(summaries)


def x__render_l7__mutmut_18(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=None, match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_19(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=None)
            )
    return tuple(summaries)


def x__render_l7__mutmut_20(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_21(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), )
            )
    return tuple(summaries)


def x__render_l7__mutmut_22(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(None), match=_render_match(match))
            )
    return tuple(summaries)


def x__render_l7__mutmut_23(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(None))
            )
    return tuple(summaries)


def x__render_l7__mutmut_24(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(None)

mutants_x__render_l7__mutmut['_mutmut_orig'] = x__render_l7__mutmut_orig # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_1'] = x__render_l7__mutmut_1 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_2'] = x__render_l7__mutmut_2 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_3'] = x__render_l7__mutmut_3 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_4'] = x__render_l7__mutmut_4 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_5'] = x__render_l7__mutmut_5 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_6'] = x__render_l7__mutmut_6 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_7'] = x__render_l7__mutmut_7 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_8'] = x__render_l7__mutmut_8 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_9'] = x__render_l7__mutmut_9 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_10'] = x__render_l7__mutmut_10 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_11'] = x__render_l7__mutmut_11 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_12'] = x__render_l7__mutmut_12 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_13'] = x__render_l7__mutmut_13 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_14'] = x__render_l7__mutmut_14 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_15'] = x__render_l7__mutmut_15 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_16'] = x__render_l7__mutmut_16 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_17'] = x__render_l7__mutmut_17 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_18'] = x__render_l7__mutmut_18 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_19'] = x__render_l7__mutmut_19 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_20'] = x__render_l7__mutmut_20 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_21'] = x__render_l7__mutmut_21 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_22'] = x__render_l7__mutmut_22 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_23'] = x__render_l7__mutmut_23 # type: ignore # mutmut generated
mutants_x__render_l7__mutmut['x__render_l7__mutmut_24'] = x__render_l7__mutmut_24 # type: ignore # mutmut generated
mutants_x__render_match__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__render_match__mutmut)
def _render_match(match: object) -> tuple[str, ...]:
    if isinstance(match, list):
        return tuple(str(item) for item in match)
    if isinstance(match, dict):
        return tuple(f"{k}={v}" for k, v in sorted(match.items()))
    return (str(match),)


def x__render_match__mutmut_orig(match: object) -> tuple[str, ...]:
    if isinstance(match, list):
        return tuple(str(item) for item in match)
    if isinstance(match, dict):
        return tuple(f"{k}={v}" for k, v in sorted(match.items()))
    return (str(match),)


def x__render_match__mutmut_1(match: object) -> tuple[str, ...]:
    if isinstance(match, list):
        return tuple(None)
    if isinstance(match, dict):
        return tuple(f"{k}={v}" for k, v in sorted(match.items()))
    return (str(match),)


def x__render_match__mutmut_2(match: object) -> tuple[str, ...]:
    if isinstance(match, list):
        return tuple(str(None) for item in match)
    if isinstance(match, dict):
        return tuple(f"{k}={v}" for k, v in sorted(match.items()))
    return (str(match),)


def x__render_match__mutmut_3(match: object) -> tuple[str, ...]:
    if isinstance(match, list):
        return tuple(str(item) for item in match)
    if isinstance(match, dict):
        return tuple(None)
    return (str(match),)


def x__render_match__mutmut_4(match: object) -> tuple[str, ...]:
    if isinstance(match, list):
        return tuple(str(item) for item in match)
    if isinstance(match, dict):
        return tuple(f"{k}={v}" for k, v in sorted(None))
    return (str(match),)


def x__render_match__mutmut_5(match: object) -> tuple[str, ...]:
    if isinstance(match, list):
        return tuple(str(item) for item in match)
    if isinstance(match, dict):
        return tuple(f"{k}={v}" for k, v in sorted(match.items()))
    return (str(None),)

mutants_x__render_match__mutmut['_mutmut_orig'] = x__render_match__mutmut_orig # type: ignore # mutmut generated
mutants_x__render_match__mutmut['x__render_match__mutmut_1'] = x__render_match__mutmut_1 # type: ignore # mutmut generated
mutants_x__render_match__mutmut['x__render_match__mutmut_2'] = x__render_match__mutmut_2 # type: ignore # mutmut generated
mutants_x__render_match__mutmut['x__render_match__mutmut_3'] = x__render_match__mutmut_3 # type: ignore # mutmut generated
mutants_x__render_match__mutmut['x__render_match__mutmut_4'] = x__render_match__mutmut_4 # type: ignore # mutmut generated
mutants_x__render_match__mutmut['x__render_match__mutmut_5'] = x__render_match__mutmut_5 # type: ignore # mutmut generated
mutants_x__collect_l7_protocols__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__collect_l7_protocols__mutmut)
def _collect_l7_protocols(rules: tuple[CiliumRuleSummary, ...]) -> tuple[str, ...]:
    protocols: set[str] = set()
    for rule in rules:
        for l7 in rule.l7:
            protocols.add(l7.protocol)
    return tuple(sorted(protocols))


def x__collect_l7_protocols__mutmut_orig(rules: tuple[CiliumRuleSummary, ...]) -> tuple[str, ...]:
    protocols: set[str] = set()
    for rule in rules:
        for l7 in rule.l7:
            protocols.add(l7.protocol)
    return tuple(sorted(protocols))


def x__collect_l7_protocols__mutmut_1(rules: tuple[CiliumRuleSummary, ...]) -> tuple[str, ...]:
    protocols: set[str] = None
    for rule in rules:
        for l7 in rule.l7:
            protocols.add(l7.protocol)
    return tuple(sorted(protocols))


def x__collect_l7_protocols__mutmut_2(rules: tuple[CiliumRuleSummary, ...]) -> tuple[str, ...]:
    protocols: set[str] = set()
    for rule in rules:
        for l7 in rule.l7:
            protocols.add(None)
    return tuple(sorted(protocols))


def x__collect_l7_protocols__mutmut_3(rules: tuple[CiliumRuleSummary, ...]) -> tuple[str, ...]:
    protocols: set[str] = set()
    for rule in rules:
        for l7 in rule.l7:
            protocols.add(l7.protocol)
    return tuple(None)


def x__collect_l7_protocols__mutmut_4(rules: tuple[CiliumRuleSummary, ...]) -> tuple[str, ...]:
    protocols: set[str] = set()
    for rule in rules:
        for l7 in rule.l7:
            protocols.add(l7.protocol)
    return tuple(sorted(None))

mutants_x__collect_l7_protocols__mutmut['_mutmut_orig'] = x__collect_l7_protocols__mutmut_orig # type: ignore # mutmut generated
mutants_x__collect_l7_protocols__mutmut['x__collect_l7_protocols__mutmut_1'] = x__collect_l7_protocols__mutmut_1 # type: ignore # mutmut generated
mutants_x__collect_l7_protocols__mutmut['x__collect_l7_protocols__mutmut_2'] = x__collect_l7_protocols__mutmut_2 # type: ignore # mutmut generated
mutants_x__collect_l7_protocols__mutmut['x__collect_l7_protocols__mutmut_3'] = x__collect_l7_protocols__mutmut_3 # type: ignore # mutmut generated
mutants_x__collect_l7_protocols__mutmut['x__collect_l7_protocols__mutmut_4'] = x__collect_l7_protocols__mutmut_4 # type: ignore # mutmut generated
