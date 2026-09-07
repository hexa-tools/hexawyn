"""Pure Cilium network-policy rule summarisation — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumNetworkPoliciesResult,
    CiliumNetworkPolicyInfo,
)

_NOT_INSTALLED_NOTE = "Cilium is not installed in this cluster"
_NAMESPACED_KIND = "CiliumNetworkPolicy"
_CLUSTERWIDE_KIND = "CiliumClusterwideNetworkPolicy"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


def _as_dict(value: object) -> dict[str, object]:
    return value if isinstance(value, dict) else {}
mutants_x_build_network_policy__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_network_policy__mutmut)
def build_network_policy(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_orig(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_1(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = None
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_2(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(None)
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_3(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get(None))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_4(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("XXmetadataXX"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_5(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("METADATA"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_6(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = None
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_7(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(None)
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_8(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get(None))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_9(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("XXspecXX"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_10(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("SPEC"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_11(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = None
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_12(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get(None, [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_13(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", None)
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_14(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get([])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_15(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", )
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_16(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("XXingressXX", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_17(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("INGRESS", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_18(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = None
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_19(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get(None, [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_20(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", None)
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_21(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get([])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_22(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", )
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_23(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("XXegressXX", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_24(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("EGRESS", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_25(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = None
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_26(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = None
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_27(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = None
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_28(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(None, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_29(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, None)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_30(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_31(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, )
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_32(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = None
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_33(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get(None)
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_34(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("XXnamespaceXX")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_35(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("NAMESPACE")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_36(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=None,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_37(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=None,
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_38(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_39(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=None,
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_40(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=None,
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_41(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=None,
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_42(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=None,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_43(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=None,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_44(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=None,
    )


def x_build_network_policy__mutmut_45(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_46(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_47(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_48(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_49(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_50(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_51(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_52(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_53(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        )


def x_build_network_policy__mutmut_54(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(None),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_55(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get(None, "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_56(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", None)),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_57(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_58(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", )),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_59(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("XXnameXX", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_60(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("NAME", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_61(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "XXXX")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_62(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(None) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_63(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(None),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_64(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get(None)),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_65(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("XXendpointSelectorXX")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_66(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointselector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_67(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("ENDPOINTSELECTOR")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointSelector")),
    )


def x_build_network_policy__mutmut_68(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(None),
    )


def x_build_network_policy__mutmut_69(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get(None)),
    )


def x_build_network_policy__mutmut_70(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("XXendpointSelectorXX")),
    )


def x_build_network_policy__mutmut_71(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("endpointselector")),
    )


def x_build_network_policy__mutmut_72(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
        endpoint_labels=_extract_endpoint_labels(spec.get("ENDPOINTSELECTOR")),
    )

mutants_x_build_network_policy__mutmut['_mutmut_orig'] = x_build_network_policy__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_1'] = x_build_network_policy__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_2'] = x_build_network_policy__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_3'] = x_build_network_policy__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_4'] = x_build_network_policy__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_5'] = x_build_network_policy__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_6'] = x_build_network_policy__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_7'] = x_build_network_policy__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_8'] = x_build_network_policy__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_9'] = x_build_network_policy__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_10'] = x_build_network_policy__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_11'] = x_build_network_policy__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_12'] = x_build_network_policy__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_13'] = x_build_network_policy__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_14'] = x_build_network_policy__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_15'] = x_build_network_policy__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_16'] = x_build_network_policy__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_17'] = x_build_network_policy__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_18'] = x_build_network_policy__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_19'] = x_build_network_policy__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_20'] = x_build_network_policy__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_21'] = x_build_network_policy__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_22'] = x_build_network_policy__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_23'] = x_build_network_policy__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_24'] = x_build_network_policy__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_25'] = x_build_network_policy__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_26'] = x_build_network_policy__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_27'] = x_build_network_policy__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_28'] = x_build_network_policy__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_29'] = x_build_network_policy__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_30'] = x_build_network_policy__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_31'] = x_build_network_policy__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_32'] = x_build_network_policy__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_33'] = x_build_network_policy__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_34'] = x_build_network_policy__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_35'] = x_build_network_policy__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_36'] = x_build_network_policy__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_37'] = x_build_network_policy__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_38'] = x_build_network_policy__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_39'] = x_build_network_policy__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_40'] = x_build_network_policy__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_41'] = x_build_network_policy__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_42'] = x_build_network_policy__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_43'] = x_build_network_policy__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_44'] = x_build_network_policy__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_45'] = x_build_network_policy__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_46'] = x_build_network_policy__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_47'] = x_build_network_policy__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_48'] = x_build_network_policy__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_49'] = x_build_network_policy__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_50'] = x_build_network_policy__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_51'] = x_build_network_policy__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_52'] = x_build_network_policy__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_53'] = x_build_network_policy__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_54'] = x_build_network_policy__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_55'] = x_build_network_policy__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_56'] = x_build_network_policy__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_57'] = x_build_network_policy__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_58'] = x_build_network_policy__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_59'] = x_build_network_policy__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_60'] = x_build_network_policy__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_61'] = x_build_network_policy__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_62'] = x_build_network_policy__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_63'] = x_build_network_policy__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_64'] = x_build_network_policy__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_65'] = x_build_network_policy__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_66'] = x_build_network_policy__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_67'] = x_build_network_policy__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_68'] = x_build_network_policy__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_69'] = x_build_network_policy__mutmut_69 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_70'] = x_build_network_policy__mutmut_70 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_71'] = x_build_network_policy__mutmut_71 # type: ignore # mutmut generated
mutants_x_build_network_policy__mutmut['x_build_network_policy__mutmut_72'] = x_build_network_policy__mutmut_72 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_policies_result__mutmut)
def build_policies_result(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_orig(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_1(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = None
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_2(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(None)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_3(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(2 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_4(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind != _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_5(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = None
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_6(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(None)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_7(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(2 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_8(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind != _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_9(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=None,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_10(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status=None,
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_11(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=None,
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_12(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=None,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_13(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=None,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_14(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=None,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_15(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None,
    )


def x_build_policies_result__mutmut_16(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_17(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_18(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_19(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_20(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_21(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_22(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        )


def x_build_policies_result__mutmut_23(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_24(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="XXpresentXX" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_25(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="PRESENT" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_26(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "XXemptyXX",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_27(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "EMPTY",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def x_build_policies_result__mutmut_28(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "XXNo Cilium network policies foundXX",
    )


def x_build_policies_result__mutmut_29(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "no cilium network policies found",
    )


def x_build_policies_result__mutmut_30(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "NO CILIUM NETWORK POLICIES FOUND",
    )

mutants_x_build_policies_result__mutmut['_mutmut_orig'] = x_build_policies_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_1'] = x_build_policies_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_2'] = x_build_policies_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_3'] = x_build_policies_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_4'] = x_build_policies_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_5'] = x_build_policies_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_6'] = x_build_policies_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_7'] = x_build_policies_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_8'] = x_build_policies_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_9'] = x_build_policies_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_10'] = x_build_policies_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_11'] = x_build_policies_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_12'] = x_build_policies_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_13'] = x_build_policies_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_14'] = x_build_policies_result__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_15'] = x_build_policies_result__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_16'] = x_build_policies_result__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_17'] = x_build_policies_result__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_18'] = x_build_policies_result__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_19'] = x_build_policies_result__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_20'] = x_build_policies_result__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_21'] = x_build_policies_result__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_22'] = x_build_policies_result__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_23'] = x_build_policies_result__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_24'] = x_build_policies_result__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_25'] = x_build_policies_result__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_26'] = x_build_policies_result__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_27'] = x_build_policies_result__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_28'] = x_build_policies_result__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_29'] = x_build_policies_result__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_policies_result__mutmut['x_build_policies_result__mutmut_30'] = x_build_policies_result__mutmut_30 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_not_installed_policies_result__mutmut)
def not_installed_policies_result() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_orig() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_1() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=None,
        status="not_installed",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_2() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status=None,
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_3() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=None,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_4() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=0,
        namespaced_count=None,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_5() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=None,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_6() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        policies=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_7() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=None,
    )


def x_not_installed_policies_result__mutmut_8() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        status="not_installed",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_9() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_10() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_11() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_12() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=0,
        namespaced_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_13() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_14() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        )


def x_not_installed_policies_result__mutmut_15() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="not_installed",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_16() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="XXnot_installedXX",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_17() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="NOT_INSTALLED",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_18() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=1,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_19() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=0,
        namespaced_count=1,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_policies_result__mutmut_20() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=1,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )

mutants_x_not_installed_policies_result__mutmut['_mutmut_orig'] = x_not_installed_policies_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_1'] = x_not_installed_policies_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_2'] = x_not_installed_policies_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_3'] = x_not_installed_policies_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_4'] = x_not_installed_policies_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_5'] = x_not_installed_policies_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_6'] = x_not_installed_policies_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_7'] = x_not_installed_policies_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_8'] = x_not_installed_policies_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_9'] = x_not_installed_policies_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_10'] = x_not_installed_policies_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_11'] = x_not_installed_policies_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_12'] = x_not_installed_policies_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_13'] = x_not_installed_policies_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_14'] = x_not_installed_policies_result__mutmut_14 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_15'] = x_not_installed_policies_result__mutmut_15 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_16'] = x_not_installed_policies_result__mutmut_16 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_17'] = x_not_installed_policies_result__mutmut_17 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_18'] = x_not_installed_policies_result__mutmut_18 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_19'] = x_not_installed_policies_result__mutmut_19 # type: ignore # mutmut generated
mutants_x_not_installed_policies_result__mutmut['x_not_installed_policies_result__mutmut_20'] = x_not_installed_policies_result__mutmut_20 # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_endpoint_labels__mutmut)
def _extract_endpoint_labels(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = selector.get("matchLabels")
    if match_labels is None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(sorted((str(k), str(v)) for k, v in match_labels.items()))


def x__extract_endpoint_labels__mutmut_orig(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = selector.get("matchLabels")
    if match_labels is None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(sorted((str(k), str(v)) for k, v in match_labels.items()))


def x__extract_endpoint_labels__mutmut_1(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is not None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = selector.get("matchLabels")
    if match_labels is None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(sorted((str(k), str(v)) for k, v in match_labels.items()))


def x__extract_endpoint_labels__mutmut_2(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if isinstance(selector, dict):
        return None
    match_labels = selector.get("matchLabels")
    if match_labels is None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(sorted((str(k), str(v)) for k, v in match_labels.items()))


def x__extract_endpoint_labels__mutmut_3(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = None
    if match_labels is None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(sorted((str(k), str(v)) for k, v in match_labels.items()))


def x__extract_endpoint_labels__mutmut_4(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = selector.get(None)
    if match_labels is None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(sorted((str(k), str(v)) for k, v in match_labels.items()))


def x__extract_endpoint_labels__mutmut_5(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = selector.get("XXmatchLabelsXX")
    if match_labels is None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(sorted((str(k), str(v)) for k, v in match_labels.items()))


def x__extract_endpoint_labels__mutmut_6(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = selector.get("matchlabels")
    if match_labels is None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(sorted((str(k), str(v)) for k, v in match_labels.items()))


def x__extract_endpoint_labels__mutmut_7(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = selector.get("MATCHLABELS")
    if match_labels is None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(sorted((str(k), str(v)) for k, v in match_labels.items()))


def x__extract_endpoint_labels__mutmut_8(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = selector.get("matchLabels")
    if match_labels is not None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(sorted((str(k), str(v)) for k, v in match_labels.items()))


def x__extract_endpoint_labels__mutmut_9(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = selector.get("matchLabels")
    if match_labels is None:
        return ()
    if isinstance(match_labels, dict):
        return None
    return tuple(sorted((str(k), str(v)) for k, v in match_labels.items()))


def x__extract_endpoint_labels__mutmut_10(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = selector.get("matchLabels")
    if match_labels is None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(None)


def x__extract_endpoint_labels__mutmut_11(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = selector.get("matchLabels")
    if match_labels is None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(sorted(None))


def x__extract_endpoint_labels__mutmut_12(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = selector.get("matchLabels")
    if match_labels is None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(sorted((str(None), str(v)) for k, v in match_labels.items()))


def x__extract_endpoint_labels__mutmut_13(
    selector: object,
) -> tuple[tuple[str, str], ...] | None:
    """Structured endpoint matchLabels for workload matching.

    ``None`` means the selector cannot be parsed (never claims coverage); an
    empty tuple means an empty selector (matches every workload).
    """
    if selector is None:
        return ()
    if not isinstance(selector, dict):
        return None
    match_labels = selector.get("matchLabels")
    if match_labels is None:
        return ()
    if not isinstance(match_labels, dict):
        return None
    return tuple(sorted((str(k), str(None)) for k, v in match_labels.items()))

mutants_x__extract_endpoint_labels__mutmut['_mutmut_orig'] = x__extract_endpoint_labels__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut['x__extract_endpoint_labels__mutmut_1'] = x__extract_endpoint_labels__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut['x__extract_endpoint_labels__mutmut_2'] = x__extract_endpoint_labels__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut['x__extract_endpoint_labels__mutmut_3'] = x__extract_endpoint_labels__mutmut_3 # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut['x__extract_endpoint_labels__mutmut_4'] = x__extract_endpoint_labels__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut['x__extract_endpoint_labels__mutmut_5'] = x__extract_endpoint_labels__mutmut_5 # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut['x__extract_endpoint_labels__mutmut_6'] = x__extract_endpoint_labels__mutmut_6 # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut['x__extract_endpoint_labels__mutmut_7'] = x__extract_endpoint_labels__mutmut_7 # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut['x__extract_endpoint_labels__mutmut_8'] = x__extract_endpoint_labels__mutmut_8 # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut['x__extract_endpoint_labels__mutmut_9'] = x__extract_endpoint_labels__mutmut_9 # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut['x__extract_endpoint_labels__mutmut_10'] = x__extract_endpoint_labels__mutmut_10 # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut['x__extract_endpoint_labels__mutmut_11'] = x__extract_endpoint_labels__mutmut_11 # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut['x__extract_endpoint_labels__mutmut_12'] = x__extract_endpoint_labels__mutmut_12 # type: ignore # mutmut generated
mutants_x__extract_endpoint_labels__mutmut['x__extract_endpoint_labels__mutmut_13'] = x__extract_endpoint_labels__mutmut_13 # type: ignore # mutmut generated
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
mutants_x__l7_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__l7_summary__mutmut)
def _l7_summary(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_orig(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_1(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = None
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_2(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = None
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_3(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 1
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_4(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_5(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            break
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_6(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = None
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_7(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get(None, [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_8(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", None)
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_9(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get([])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_10(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", )
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_11(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("XXtoPortsXX", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_12(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toports", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_13(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("TOPORTS", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_14(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_15(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            break
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_16(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_17(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                break
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_18(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = None
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_19(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get(None, {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_20(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", None)
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_21(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get({})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_22(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", )
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_23(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("XXrulesXX", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_24(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("RULES", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_25(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) and not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_26(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_27(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_28(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                break
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_29(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count = 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_30(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count -= 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_31(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 2
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_32(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(None)
    return count, tuple(sorted(protocols))


def x__l7_summary__mutmut_33(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(None)


def x__l7_summary__mutmut_34(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(None))

mutants_x__l7_summary__mutmut['_mutmut_orig'] = x__l7_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_1'] = x__l7_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_2'] = x__l7_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_3'] = x__l7_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_4'] = x__l7_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_5'] = x__l7_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_6'] = x__l7_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_7'] = x__l7_summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_8'] = x__l7_summary__mutmut_8 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_9'] = x__l7_summary__mutmut_9 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_10'] = x__l7_summary__mutmut_10 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_11'] = x__l7_summary__mutmut_11 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_12'] = x__l7_summary__mutmut_12 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_13'] = x__l7_summary__mutmut_13 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_14'] = x__l7_summary__mutmut_14 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_15'] = x__l7_summary__mutmut_15 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_16'] = x__l7_summary__mutmut_16 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_17'] = x__l7_summary__mutmut_17 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_18'] = x__l7_summary__mutmut_18 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_19'] = x__l7_summary__mutmut_19 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_20'] = x__l7_summary__mutmut_20 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_21'] = x__l7_summary__mutmut_21 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_22'] = x__l7_summary__mutmut_22 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_23'] = x__l7_summary__mutmut_23 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_24'] = x__l7_summary__mutmut_24 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_25'] = x__l7_summary__mutmut_25 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_26'] = x__l7_summary__mutmut_26 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_27'] = x__l7_summary__mutmut_27 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_28'] = x__l7_summary__mutmut_28 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_29'] = x__l7_summary__mutmut_29 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_30'] = x__l7_summary__mutmut_30 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_31'] = x__l7_summary__mutmut_31 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_32'] = x__l7_summary__mutmut_32 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_33'] = x__l7_summary__mutmut_33 # type: ignore # mutmut generated
mutants_x__l7_summary__mutmut['x__l7_summary__mutmut_34'] = x__l7_summary__mutmut_34 # type: ignore # mutmut generated
