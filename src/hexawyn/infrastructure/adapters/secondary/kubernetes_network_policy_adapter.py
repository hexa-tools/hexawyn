from __future__ import annotations

from typing import Any

from hexawyn.application.ports.driven.network_policy_audit_port import (
    NamespaceRaw,
    NetworkPolicyAuditPort,
    NetworkPolicyRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403
_CALICO_GROUP = "projectcalico.org"
_CALICO_VERSION = "v3"
_GLOBAL_NETWORK_POLICIES_PLURAL = "globalnetworkpolicies"
_ISTIO_SECURITY_GROUP = "security.istio.io"
_ISTIO_SECURITY_VERSION = "v1beta1"
_PEER_AUTHENTICATIONS_PLURAL = "peerauthentications"
_STRICT_MTLS_MODE = "STRICT"


class KubernetesNetworkPolicyAdapter(NetworkPolicyAuditPort):
    """Secondary adapter — enumerates namespaces (with pod counts) and
    NetworkPolicies via the K8s API, and checks for Calico GlobalNetworkPolicy
    / Istio strict-mTLS PeerAuthentication CRDs (both degrade to a graceful
    `False` when the CRD isn't installed, mirroring `IstioTopologyAdapter`'s
    "mesh not installed -> None" handling)."""

    def list_namespaces_with_pod_counts(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            namespaces = core_api.list_namespace()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        pod_counts: dict[str, int] = {}
        for pod in pods.items:
            pod_counts[pod.metadata.namespace] = pod_counts.get(pod.metadata.namespace, 0) + 1

        return [
            NamespaceRaw(
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, 0)
            )
            for namespace in namespaces.items
        ]

    def list_network_policies(self) -> list[NetworkPolicyRaw]:
        from kubernetes import client as k8s

        networking_api = k8s.NetworkingV1Api()
        try:
            result = networking_api.list_network_policy_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_network_policy_raw(item) for item in result.items]

    def has_calico_global_network_policies(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_CALICO_GROUP,
                version=_CALICO_VERSION,
                plural=_GLOBAL_NETWORK_POLICIES_PLURAL,
            )
        except Exception:
            return False
        return bool(_items(raw))

    def has_istio_strict_peer_authentication(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_ISTIO_SECURITY_GROUP,
                version=_ISTIO_SECURITY_VERSION,
                plural=_PEER_AUTHENTICATIONS_PLURAL,
            )
        except Exception:
            return False
        return any(_is_strict_mtls(item) for item in _items(raw))


def _to_network_policy_raw(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def _items(raw: object) -> list[Any]:
    if not isinstance(raw, dict):
        return []
    items = raw.get("items")
    return items if isinstance(items, list) else []


def _is_strict_mtls(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Namespace/NetworkPolicy info")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")
