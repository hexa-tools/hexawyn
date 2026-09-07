from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from hexawyn.application.ports.driven.gitops_drift_audit_port import (
    AuditEventRaw,
    AuditLogFetchResult,
    GitOpsDriftAuditPort,
    LiveConfigResourceRaw,
    ManagedFieldsEntryRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403
_AUDIT_LOG_PATH_ENV_VAR = "K8S_AUDIT_LOG_PATH"
_DEFAULT_AUDIT_LOG_PATH = "/var/log/kubernetes/audit.log"
_RESOURCE_KIND_BY_PLURAL = {"configmaps": "ConfigMap", "secrets": "Secret"}


class KubernetesAuditLogAdapter(GitOpsDriftAuditPort):
    """Secondary adapter — enumerates ConfigMap/Secret managedFields (always
    available via the K8s API) and, if configured, reads a local k8s audit
    log file used purely to enrich actor identity."""

    def list_live_config_resources(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def fetch_audit_log_events(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)


def _to_resource(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = metadata.managed_fields or []
    return LiveConfigResourceRaw(
        kind=kind,
        name=metadata.name,
        namespace=metadata.namespace,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
    )


def _to_managed_fields_entry(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = entry.fields_v1
    fields_v1_raw = fields_v1 if isinstance(fields_v1, dict) else {}
    return ManagedFieldsEntryRaw(
        manager=entry.manager,
        operation=entry.operation,
        time=entry.time.isoformat(),
        fields_v1_raw=fields_v1_raw,
    )


def _parse_audit_line(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ConfigMap/Secret info")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")
