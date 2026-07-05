from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypedDict


class NamespaceRaw(TypedDict):
    name: str
    pod_count: int


class NetworkPolicyRaw(TypedDict):
    name: str
    namespace: str
    ingress_rule_count: int
    egress_rule_count: int
    has_empty_pod_selector: bool


class NetworkPolicyAuditPort(ABC):
    """Port for enumerating every namespace (with its pod count) and every
    NetworkPolicy across the cluster, plus presence checks for Calico
    GlobalNetworkPolicy and Istio strict mTLS PeerAuthentication — both of
    which can provide east-west protection outside vanilla NetworkPolicy
    visibility."""

    @abstractmethod
    def list_namespaces_with_pod_counts(self) -> list[NamespaceRaw]:
        """List every namespace with its live pod count (0 if empty)."""

    @abstractmethod
    def list_network_policies(self) -> list[NetworkPolicyRaw]:
        """List every NetworkPolicy across all namespaces, with ingress/
        egress rule counts and podSelector emptiness."""

    @abstractmethod
    def has_calico_global_network_policies(self) -> bool:
        """True if any Calico GlobalNetworkPolicy CRD exists in the cluster."""

    @abstractmethod
    def has_istio_strict_peer_authentication(self) -> bool:
        """True if any Istio PeerAuthentication with mTLS mode STRICT exists."""
