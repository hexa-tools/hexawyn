"""Calico driven port (ABC) — the shared contract for the whole Calico series.

Read-only by design. Every method degrades honestly: when Calico is absent it
returns an empty ``NOT_INSTALLED``-aware result / empty list / None rather than
raising an untranslated exception.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.domain.models.calico import (
    CalicoBgpConfiguration,
    CalicoBgpPeer,
    CalicoDetectionResult,
    CalicoHostEndpoint,
    CalicoIPPool,
    CalicoNetworkPolicy,
    CalicoWorkload,
)


class CalicoPort(ABC):
    """Outbound contract for Calico introspection — never triggers mutation."""

    @abstractmethod
    def detect(self) -> CalicoDetectionResult:
        """Return whether Calico is installed, its version/mode and agent health."""

    @abstractmethod
    def status(self) -> CalicoDetectionResult:
        """Alias of ``detect`` returning the same truthful detection snapshot."""

    @abstractmethod
    def list_network_policies(self, namespace: str | None = None) -> list[CalicoNetworkPolicy]:
        """List Calico NetworkPolicies / GlobalNetworkPolicies (empty when absent)."""

    @abstractmethod
    def get_network_policy(self, name: str, namespace: str) -> CalicoNetworkPolicy | None:
        """Fetch one policy, or None when Calico is absent / policy missing."""

    @abstractmethod
    def list_workloads(self, namespace: str | None = None) -> list[CalicoWorkload]:
        """List workload namespaces with their pod counts (for audit coverage)."""

    @abstractmethod
    def audit_policies(self) -> dict[str, object]:
        """Return a policy audit summary (honest empty/False when absent)."""

    @abstractmethod
    def list_ip_pools(self) -> list[CalicoIPPool]:
        """List Calico IPPools (empty when absent)."""

    @abstractmethod
    def list_host_endpoints(self) -> list[CalicoHostEndpoint]:
        """List Calico HostEndpoints (empty when absent)."""

    @abstractmethod
    def list_bgp_configurations(self) -> list[CalicoBgpConfiguration]:
        """List Calico BGPConfigurations (empty when absent)."""

    @abstractmethod
    def list_bgp_peers(self) -> list[CalicoBgpPeer]:
        """List Calico BGPPeers (empty when absent)."""

    @abstractmethod
    def bgp_audit(self) -> dict[str, object]:
        """Return a BGP node-to-node mesh audit (empty when absent)."""

    @abstractmethod
    def encryption_status(self) -> dict[str, object]:
        """Return wireguard/encryption state (empty when absent)."""

    @abstractmethod
    def felix_metrics(self) -> dict[str, object]:
        """Return Felix metrics via the metrics source (unavailable flag otherwise)."""

    @abstractmethod
    def felix_policy_counters(self) -> dict[str, object]:
        """Return per-policy allow/deny counters (available flag otherwise)."""

    @abstractmethod
    def connectivity_health(self) -> dict[str, object]:
        """Return dataplane connectivity health (unavailable flag otherwise)."""
