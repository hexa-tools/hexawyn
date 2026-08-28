from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.domain.models.cilium import (
    CiliumDetectionResult,
    CiliumEncryptionStatusResult,
    CiliumIdentitiesResult,
    CiliumNetworkPoliciesResult,
    CiliumNetworkPolicyDetail,
    CiliumPolicyAuditResult,
    CiliumSegmentationAuditResult,
    CiliumStatusResult,
)


class CiliumPort(ABC):
    """Outbound port to observe a Cilium installation — read-only."""

    @abstractmethod
    def detect(self) -> CiliumDetectionResult: ...

    @abstractmethod
    def status(self) -> CiliumStatusResult: ...

    @abstractmethod
    def list_network_policies(self) -> CiliumNetworkPoliciesResult: ...

    @abstractmethod
    def get_network_policy(self, name: str, namespace: str | None) -> CiliumNetworkPolicyDetail: ...

    @abstractmethod
    def audit_policies(self) -> CiliumPolicyAuditResult: ...

    @abstractmethod
    def list_identities(self) -> CiliumIdentitiesResult: ...

    @abstractmethod
    def segmentation_audit(self) -> CiliumSegmentationAuditResult: ...

    @abstractmethod
    def encryption_status(self) -> CiliumEncryptionStatusResult: ...
