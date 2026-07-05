from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import TypedDict


class ManagedFieldsEntryRaw(TypedDict):
    manager: str
    operation: str
    time: str
    fields_v1_raw: Mapping[str, object]


class SecretRaw(TypedDict):
    name: str
    namespace: str
    secret_type: str
    data_keys: list[str]
    managed_fields: list[ManagedFieldsEntryRaw]
    creation_timestamp: str
    annotations: dict[str, str]


class SecretReferenceRaw(TypedDict):
    secret_name: str
    namespace: str
    workload_name: str


class SecretRotationAuditPort(ABC):
    """Port for enumerating every Secret across all namespaces (with its
    managedFields history for last-data-change detection), every Deployment/
    standalone-Pod reference to a Secret, and namespace-level rotation
    exemptions."""

    @abstractmethod
    def list_secrets(self) -> list[SecretRaw]:
        """List every Secret across all namespaces, with managedFields."""

    @abstractmethod
    def list_secret_references(self) -> list[SecretReferenceRaw]:
        """List every Deployment/standalone-Pod reference to a Secret (env,
        envFrom, volumes, projected volumes)."""

    @abstractmethod
    def get_namespace_rotation_exemptions(self) -> set[str]:
        """Return the set of namespace names annotated as exempt from the
        rotation policy."""
