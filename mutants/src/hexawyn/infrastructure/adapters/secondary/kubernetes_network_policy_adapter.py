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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut: MutantDict = {}  # type: ignore


class KubernetesNetworkPolicyAdapter(NetworkPolicyAuditPort):
    """Secondary adapter — enumerates namespaces (with pod counts) and
    NetworkPolicies via the K8s API, and checks for Calico GlobalNetworkPolicy
    / Istio strict-mTLS PeerAuthentication CRDs (both degrade to a graceful
    `False` when the CRD isn't installed, mirroring `IstioTopologyAdapter`'s
    "mesh not installed -> None" handling)."""

    @_mutmut_mutated(mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut)
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

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_orig(self) -> list[NamespaceRaw]:
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

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_1(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = None
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

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_2(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            namespaces = None
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

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_3(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            namespaces = core_api.list_namespace()
            pods = None
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

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_4(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            namespaces = core_api.list_namespace()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(None) from exc

        pod_counts: dict[str, int] = {}
        for pod in pods.items:
            pod_counts[pod.metadata.namespace] = pod_counts.get(pod.metadata.namespace, 0) + 1

        return [
            NamespaceRaw(
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, 0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_5(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            namespaces = core_api.list_namespace()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        pod_counts: dict[str, int] = None
        for pod in pods.items:
            pod_counts[pod.metadata.namespace] = pod_counts.get(pod.metadata.namespace, 0) + 1

        return [
            NamespaceRaw(
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, 0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_6(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            namespaces = core_api.list_namespace()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        pod_counts: dict[str, int] = {}
        for pod in pods.items:
            pod_counts[pod.metadata.namespace] = None

        return [
            NamespaceRaw(
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, 0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_7(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            namespaces = core_api.list_namespace()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        pod_counts: dict[str, int] = {}
        for pod in pods.items:
            pod_counts[pod.metadata.namespace] = pod_counts.get(pod.metadata.namespace, 0) - 1

        return [
            NamespaceRaw(
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, 0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_8(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            namespaces = core_api.list_namespace()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        pod_counts: dict[str, int] = {}
        for pod in pods.items:
            pod_counts[pod.metadata.namespace] = pod_counts.get(None, 0) + 1

        return [
            NamespaceRaw(
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, 0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_9(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            namespaces = core_api.list_namespace()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        pod_counts: dict[str, int] = {}
        for pod in pods.items:
            pod_counts[pod.metadata.namespace] = pod_counts.get(pod.metadata.namespace, None) + 1

        return [
            NamespaceRaw(
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, 0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_10(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            namespaces = core_api.list_namespace()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        pod_counts: dict[str, int] = {}
        for pod in pods.items:
            pod_counts[pod.metadata.namespace] = pod_counts.get(0) + 1

        return [
            NamespaceRaw(
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, 0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_11(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            namespaces = core_api.list_namespace()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        pod_counts: dict[str, int] = {}
        for pod in pods.items:
            pod_counts[pod.metadata.namespace] = pod_counts.get(pod.metadata.namespace, ) + 1

        return [
            NamespaceRaw(
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, 0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_12(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            namespaces = core_api.list_namespace()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        pod_counts: dict[str, int] = {}
        for pod in pods.items:
            pod_counts[pod.metadata.namespace] = pod_counts.get(pod.metadata.namespace, 1) + 1

        return [
            NamespaceRaw(
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, 0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_13(self) -> list[NamespaceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            namespaces = core_api.list_namespace()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        pod_counts: dict[str, int] = {}
        for pod in pods.items:
            pod_counts[pod.metadata.namespace] = pod_counts.get(pod.metadata.namespace, 0) + 2

        return [
            NamespaceRaw(
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, 0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_14(self) -> list[NamespaceRaw]:
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
                name=None, pod_count=pod_counts.get(namespace.metadata.name, 0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_15(self) -> list[NamespaceRaw]:
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
                name=namespace.metadata.name, pod_count=None
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_16(self) -> list[NamespaceRaw]:
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
                pod_count=pod_counts.get(namespace.metadata.name, 0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_17(self) -> list[NamespaceRaw]:
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
                name=namespace.metadata.name, )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_18(self) -> list[NamespaceRaw]:
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
                name=namespace.metadata.name, pod_count=pod_counts.get(None, 0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_19(self) -> list[NamespaceRaw]:
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
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, None)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_20(self) -> list[NamespaceRaw]:
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
                name=namespace.metadata.name, pod_count=pod_counts.get(0)
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_21(self) -> list[NamespaceRaw]:
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
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, )
            )
            for namespace in namespaces.items
        ]

    def xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_22(self) -> list[NamespaceRaw]:
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
                name=namespace.metadata.name, pod_count=pod_counts.get(namespace.metadata.name, 1)
            )
            for namespace in namespaces.items
        ]

    @_mutmut_mutated(mutants_xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut)
    def list_network_policies(self) -> list[NetworkPolicyRaw]:
        from kubernetes import client as k8s

        networking_api = k8s.NetworkingV1Api()
        try:
            result = networking_api.list_network_policy_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_network_policy_raw(item) for item in result.items]

    def xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_orig(self) -> list[NetworkPolicyRaw]:
        from kubernetes import client as k8s

        networking_api = k8s.NetworkingV1Api()
        try:
            result = networking_api.list_network_policy_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_network_policy_raw(item) for item in result.items]

    def xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_1(self) -> list[NetworkPolicyRaw]:
        from kubernetes import client as k8s

        networking_api = None
        try:
            result = networking_api.list_network_policy_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_network_policy_raw(item) for item in result.items]

    def xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_2(self) -> list[NetworkPolicyRaw]:
        from kubernetes import client as k8s

        networking_api = k8s.NetworkingV1Api()
        try:
            result = None
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_network_policy_raw(item) for item in result.items]

    def xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_3(self) -> list[NetworkPolicyRaw]:
        from kubernetes import client as k8s

        networking_api = k8s.NetworkingV1Api()
        try:
            result = networking_api.list_network_policy_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(None) from exc
        return [_to_network_policy_raw(item) for item in result.items]

    def xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_4(self) -> list[NetworkPolicyRaw]:
        from kubernetes import client as k8s

        networking_api = k8s.NetworkingV1Api()
        try:
            result = networking_api.list_network_policy_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_network_policy_raw(None) for item in result.items]

    @_mutmut_mutated(mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut)
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

    def xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_orig(self) -> bool:
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

    def xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_1(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = None
            raw = crd_api.list_cluster_custom_object(
                group=_CALICO_GROUP,
                version=_CALICO_VERSION,
                plural=_GLOBAL_NETWORK_POLICIES_PLURAL,
            )
        except Exception:
            return False
        return bool(_items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_2(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = None
        except Exception:
            return False
        return bool(_items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_3(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=None,
                version=_CALICO_VERSION,
                plural=_GLOBAL_NETWORK_POLICIES_PLURAL,
            )
        except Exception:
            return False
        return bool(_items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_4(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_CALICO_GROUP,
                version=None,
                plural=_GLOBAL_NETWORK_POLICIES_PLURAL,
            )
        except Exception:
            return False
        return bool(_items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_5(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_CALICO_GROUP,
                version=_CALICO_VERSION,
                plural=None,
            )
        except Exception:
            return False
        return bool(_items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_6(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                version=_CALICO_VERSION,
                plural=_GLOBAL_NETWORK_POLICIES_PLURAL,
            )
        except Exception:
            return False
        return bool(_items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_7(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_CALICO_GROUP,
                plural=_GLOBAL_NETWORK_POLICIES_PLURAL,
            )
        except Exception:
            return False
        return bool(_items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_8(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_CALICO_GROUP,
                version=_CALICO_VERSION,
                )
        except Exception:
            return False
        return bool(_items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_9(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_CALICO_GROUP,
                version=_CALICO_VERSION,
                plural=_GLOBAL_NETWORK_POLICIES_PLURAL,
            )
        except Exception:
            return True
        return bool(_items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_10(self) -> bool:
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
        return bool(None)

    def xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_11(self) -> bool:
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
        return bool(_items(None))

    @_mutmut_mutated(mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut)
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

    def xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_orig(self) -> bool:
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

    def xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_1(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = None
            raw = crd_api.list_cluster_custom_object(
                group=_ISTIO_SECURITY_GROUP,
                version=_ISTIO_SECURITY_VERSION,
                plural=_PEER_AUTHENTICATIONS_PLURAL,
            )
        except Exception:
            return False
        return any(_is_strict_mtls(item) for item in _items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_2(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = None
        except Exception:
            return False
        return any(_is_strict_mtls(item) for item in _items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_3(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=None,
                version=_ISTIO_SECURITY_VERSION,
                plural=_PEER_AUTHENTICATIONS_PLURAL,
            )
        except Exception:
            return False
        return any(_is_strict_mtls(item) for item in _items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_4(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_ISTIO_SECURITY_GROUP,
                version=None,
                plural=_PEER_AUTHENTICATIONS_PLURAL,
            )
        except Exception:
            return False
        return any(_is_strict_mtls(item) for item in _items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_5(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_ISTIO_SECURITY_GROUP,
                version=_ISTIO_SECURITY_VERSION,
                plural=None,
            )
        except Exception:
            return False
        return any(_is_strict_mtls(item) for item in _items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_6(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                version=_ISTIO_SECURITY_VERSION,
                plural=_PEER_AUTHENTICATIONS_PLURAL,
            )
        except Exception:
            return False
        return any(_is_strict_mtls(item) for item in _items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_7(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_ISTIO_SECURITY_GROUP,
                plural=_PEER_AUTHENTICATIONS_PLURAL,
            )
        except Exception:
            return False
        return any(_is_strict_mtls(item) for item in _items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_8(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_ISTIO_SECURITY_GROUP,
                version=_ISTIO_SECURITY_VERSION,
                )
        except Exception:
            return False
        return any(_is_strict_mtls(item) for item in _items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_9(self) -> bool:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_ISTIO_SECURITY_GROUP,
                version=_ISTIO_SECURITY_VERSION,
                plural=_PEER_AUTHENTICATIONS_PLURAL,
            )
        except Exception:
            return True
        return any(_is_strict_mtls(item) for item in _items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_10(self) -> bool:
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
        return any(None)

    def xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_11(self) -> bool:
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
        return any(_is_strict_mtls(None) for item in _items(raw))

    def xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_12(self) -> bool:
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
        return any(_is_strict_mtls(item) for item in _items(None))

mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['_mutmut_orig'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_1'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_2'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_3'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_4'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_5'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_6'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_7'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_8'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_9'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_10'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_11'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_12'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_13'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_14'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_15'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_16'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_17'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_18'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_19'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_20'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_21'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_22'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_namespaces_with_pod_counts__mutmut_22 # type: ignore # mutmut generated

mutants_xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut['_mutmut_orig'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_1'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_2'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_3'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_4'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁlist_network_policies__mutmut_4 # type: ignore # mutmut generated

mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut['_mutmut_orig'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_1'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_2'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_3'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_4'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_5'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_6'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_7'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_8'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_9'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_10'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_11'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_calico_global_network_policies__mutmut_11 # type: ignore # mutmut generated

mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut['_mutmut_orig'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_1'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_2'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_3'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_4'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_5'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_6'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_7'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_8'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_9'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_10'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_11'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut['xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_12'] = KubernetesNetworkPolicyAdapter.xǁKubernetesNetworkPolicyAdapterǁhas_istio_strict_peer_authentication__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_network_policy_raw__mutmut)
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


def x__to_network_policy_raw__mutmut_orig(item: Any) -> NetworkPolicyRaw:
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


def x__to_network_policy_raw__mutmut_1(item: Any) -> NetworkPolicyRaw:
    pod_selector = None
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_2(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = None
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_3(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) and {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_4(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_5(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = None
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_6(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) and []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_7(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_8(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=None,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_9(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=None,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_10(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=None,
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_11(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=None,
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_12(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=None,
    )


def x__to_network_policy_raw__mutmut_13(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_14(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_15(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_16(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        has_empty_pod_selector=not match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_17(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        )


def x__to_network_policy_raw__mutmut_18(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels or not match_expressions,
    )


def x__to_network_policy_raw__mutmut_19(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=match_labels and not match_expressions,
    )


def x__to_network_policy_raw__mutmut_20(item: Any) -> NetworkPolicyRaw:
    pod_selector = item.spec.pod_selector
    match_labels = (pod_selector.match_labels if pod_selector is not None else None) or {}
    match_expressions = (pod_selector.match_expressions if pod_selector is not None else None) or []
    return NetworkPolicyRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        ingress_rule_count=len(item.spec.ingress or []),
        egress_rule_count=len(item.spec.egress or []),
        has_empty_pod_selector=not match_labels and match_expressions,
    )

mutants_x__to_network_policy_raw__mutmut['_mutmut_orig'] = x__to_network_policy_raw__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_1'] = x__to_network_policy_raw__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_2'] = x__to_network_policy_raw__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_3'] = x__to_network_policy_raw__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_4'] = x__to_network_policy_raw__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_5'] = x__to_network_policy_raw__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_6'] = x__to_network_policy_raw__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_7'] = x__to_network_policy_raw__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_8'] = x__to_network_policy_raw__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_9'] = x__to_network_policy_raw__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_10'] = x__to_network_policy_raw__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_11'] = x__to_network_policy_raw__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_12'] = x__to_network_policy_raw__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_13'] = x__to_network_policy_raw__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_14'] = x__to_network_policy_raw__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_15'] = x__to_network_policy_raw__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_16'] = x__to_network_policy_raw__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_17'] = x__to_network_policy_raw__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_18'] = x__to_network_policy_raw__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_19'] = x__to_network_policy_raw__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_network_policy_raw__mutmut['x__to_network_policy_raw__mutmut_20'] = x__to_network_policy_raw__mutmut_20 # type: ignore # mutmut generated
mutants_x__items__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__items__mutmut)
def _items(raw: object) -> list[Any]:
    if not isinstance(raw, dict):
        return []
    items = raw.get("items")
    return items if isinstance(items, list) else []


def x__items__mutmut_orig(raw: object) -> list[Any]:
    if not isinstance(raw, dict):
        return []
    items = raw.get("items")
    return items if isinstance(items, list) else []


def x__items__mutmut_1(raw: object) -> list[Any]:
    if isinstance(raw, dict):
        return []
    items = raw.get("items")
    return items if isinstance(items, list) else []


def x__items__mutmut_2(raw: object) -> list[Any]:
    if not isinstance(raw, dict):
        return []
    items = None
    return items if isinstance(items, list) else []


def x__items__mutmut_3(raw: object) -> list[Any]:
    if not isinstance(raw, dict):
        return []
    items = raw.get(None)
    return items if isinstance(items, list) else []


def x__items__mutmut_4(raw: object) -> list[Any]:
    if not isinstance(raw, dict):
        return []
    items = raw.get("XXitemsXX")
    return items if isinstance(items, list) else []


def x__items__mutmut_5(raw: object) -> list[Any]:
    if not isinstance(raw, dict):
        return []
    items = raw.get("ITEMS")
    return items if isinstance(items, list) else []

mutants_x__items__mutmut['_mutmut_orig'] = x__items__mutmut_orig # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_1'] = x__items__mutmut_1 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_2'] = x__items__mutmut_2 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_3'] = x__items__mutmut_3 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_4'] = x__items__mutmut_4 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_5'] = x__items__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_strict_mtls__mutmut)
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


def x__is_strict_mtls__mutmut_orig(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_1(item: Any) -> bool:
    if isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_2(item: Any) -> bool:
    if not isinstance(item, dict):
        return True
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_3(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = None
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_4(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get(None)
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_5(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("XXspecXX")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_6(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("SPEC")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_7(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_8(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return True
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_9(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = None
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_10(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get(None)
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_11(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("XXmtlsXX")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_12(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("MTLS")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_13(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if isinstance(mtls, dict):
        return False
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_14(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return True
    return mtls.get("mode") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_15(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get(None) == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_16(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("XXmodeXX") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_17(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("MODE") == _STRICT_MTLS_MODE


def x__is_strict_mtls__mutmut_18(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    spec = item.get("spec")
    if not isinstance(spec, dict):
        return False
    mtls = spec.get("mtls")
    if not isinstance(mtls, dict):
        return False
    return mtls.get("mode") != _STRICT_MTLS_MODE

mutants_x__is_strict_mtls__mutmut['_mutmut_orig'] = x__is_strict_mtls__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_1'] = x__is_strict_mtls__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_2'] = x__is_strict_mtls__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_3'] = x__is_strict_mtls__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_4'] = x__is_strict_mtls__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_5'] = x__is_strict_mtls__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_6'] = x__is_strict_mtls__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_7'] = x__is_strict_mtls__mutmut_7 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_8'] = x__is_strict_mtls__mutmut_8 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_9'] = x__is_strict_mtls__mutmut_9 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_10'] = x__is_strict_mtls__mutmut_10 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_11'] = x__is_strict_mtls__mutmut_11 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_12'] = x__is_strict_mtls__mutmut_12 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_13'] = x__is_strict_mtls__mutmut_13 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_14'] = x__is_strict_mtls__mutmut_14 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_15'] = x__is_strict_mtls__mutmut_15 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_16'] = x__is_strict_mtls__mutmut_16 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_17'] = x__is_strict_mtls__mutmut_17 # type: ignore # mutmut generated
mutants_x__is_strict_mtls__mutmut['x__is_strict_mtls__mutmut_18'] = x__is_strict_mtls__mutmut_18 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Namespace/NetworkPolicy info")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Namespace/NetworkPolicy info")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Namespace/NetworkPolicy info")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Namespace/NetworkPolicy info")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Namespace/NetworkPolicy info")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Namespace/NetworkPolicy info")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Namespace/NetworkPolicy info")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Namespace/NetworkPolicy info")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Namespace/NetworkPolicy info")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Namespace/NetworkPolicy info")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Namespace/NetworkPolicy info")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(None)
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("XXRBAC denied access to Namespace/NetworkPolicy infoXX")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("rbac denied access to namespace/networkpolicy info")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC DENIED ACCESS TO NAMESPACE/NETWORKPOLICY INFO")
    return ClusterUnreachableError(f"Cannot list Namespace/NetworkPolicy info: {exc}")


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Namespace/NetworkPolicy info")
    return ClusterUnreachableError(None)

mutants_x__translate_error__mutmut['_mutmut_orig'] = x__translate_error__mutmut_orig # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_1'] = x__translate_error__mutmut_1 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_2'] = x__translate_error__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_3'] = x__translate_error__mutmut_3 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_4'] = x__translate_error__mutmut_4 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_5'] = x__translate_error__mutmut_5 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_6'] = x__translate_error__mutmut_6 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_7'] = x__translate_error__mutmut_7 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_8'] = x__translate_error__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_9'] = x__translate_error__mutmut_9 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_10'] = x__translate_error__mutmut_10 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_11'] = x__translate_error__mutmut_11 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_12'] = x__translate_error__mutmut_12 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_13'] = x__translate_error__mutmut_13 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_14'] = x__translate_error__mutmut_14 # type: ignore # mutmut generated
