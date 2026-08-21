from abc import ABC, abstractmethod
from typing import TypedDict


class IngressInfo(TypedDict):
    name: str
    namespace: str
    host: str
    target_service: str
    tls_enabled: bool


class IngressPort(ABC):
    """Driven port — reads vanilla Kubernetes Ingress resources.

    Standard networking.k8s.io/v1 Ingresses expose hosts through
    spec.rules and optionally TLS through spec.tls. This is the vanilla
    Kubernetes counterpart of the OpenShift-specific Routes.
    """

    @abstractmethod
    def list_ingresses(self, namespace: str) -> list[IngressInfo]:
        """List Ingresses in *namespace*.

        Raises InsufficientPermissionsError on RBAC 403.
        Raises ClusterUnreachableError on other API failures.
        """
