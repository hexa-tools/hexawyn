from abc import ABC, abstractmethod

from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort


class CloudProvider(ABC):
    """Contract that every cloud adapter must fulfill."""

    @classmethod
    @abstractmethod
    def supports(cls, context: ClusterContext) -> bool:
        """Does this provider support the given cluster?"""

    @classmethod
    @abstractmethod
    def build(cls, context: ClusterContext) -> K8sPort:
        """Build the adapter bundle for this cluster."""

    @classmethod
    @abstractmethod
    def provider_name(cls) -> str:
        """Display name: 'AWS EKS', 'Azure AKS', etc."""

    @classmethod
    @abstractmethod
    def provider_badge(cls) -> str:
        """CLI badge: '☁ AWS', '☁ Azure', etc."""
