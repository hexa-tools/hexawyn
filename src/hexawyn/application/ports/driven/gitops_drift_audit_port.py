from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import TypedDict


class ManagedFieldsEntryRaw(TypedDict):
    manager: str
    operation: str
    time: str
    fields_v1_raw: Mapping[str, object]


class LiveConfigResourceRaw(TypedDict):
    kind: str
    name: str
    namespace: str
    managed_fields: list[ManagedFieldsEntryRaw]


class AuditEventRaw(TypedDict):
    kind: str
    name: str
    namespace: str
    actor: str
    verb: str
    timestamp: str


class AuditLogFetchResult(TypedDict):
    available: bool
    events: list[AuditEventRaw]
    earliest_timestamp: str | None


class GitOpsDriftAuditPort(ABC):
    """Port for reading ConfigMap/Secret managedFields plus an optional
    k8s audit-log source, used to detect manual changes outside GitOps."""

    @abstractmethod
    def list_live_config_resources(self, namespace: str) -> list[LiveConfigResourceRaw]:
        """List ConfigMaps and Secrets in the namespace, with managedFields."""

    @abstractmethod
    def fetch_audit_log_events(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        """Fetch k8s audit log events for ConfigMap/Secret writes, if configured."""
