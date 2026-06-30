from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypedDict


class TlsSecretData(TypedDict):
    secret_name: str
    namespace: str
    cert_pem: str
    cert_manager_managed: bool
    cert_manager_auto_renewing: bool


class IngressRef(TypedDict):
    ingress_name: str
    namespace: str
    secret_name: str
    host: str


class ClusterCertificateHealthPort(ABC):
    """Outbound port — reads TLS secrets and ingresses from a Kubernetes cluster."""

    @abstractmethod
    def list_namespaces(self) -> list[str]: ...

    @abstractmethod
    def list_tls_secrets(self, namespace: str) -> list[TlsSecretData]: ...

    @abstractmethod
    def list_ingresses(self, namespace: str) -> list[IngressRef]: ...
