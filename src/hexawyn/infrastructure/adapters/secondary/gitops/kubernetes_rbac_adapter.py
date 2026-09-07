from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from hexawyn.application.ports.driven.rbac_security_audit_port import (
    ApiUsageEventRaw,
    ApiUsageFetchResult,
    PodOwnerRaw,
    PolicyRuleRaw,
    RBACSecurityAuditPort,
    RoleBindingRaw,
    RoleRaw,
    RoleRefRaw,
    ServiceAccountRaw,
    SubjectRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403
_AUDIT_LOG_PATH_ENV_VAR = "K8S_AUDIT_LOG_PATH"
_DEFAULT_AUDIT_LOG_PATH = "/var/log/kubernetes/audit.log"
_SERVICE_ACCOUNT_USERNAME_PREFIX = "system:serviceaccount:"
_DEFAULT_SERVICE_ACCOUNT_NAME = "default"


class KubernetesRBACAdapter(RBACSecurityAuditPort):
    """Secondary adapter — enumerates ServiceAccounts, RoleBindings/
    ClusterRoleBindings, Role/ClusterRole rules (with raw aggregationRule
    label-selector data) and owning Pods via the K8s API, and, if configured,
    reads a local k8s audit log file to compute actual per-service-account
    API usage."""

    def list_service_accounts(self) -> list[ServiceAccountRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_service_account_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            ServiceAccountRaw(name=item.metadata.name, namespace=item.metadata.namespace)
            for item in result.items
        ]

    def list_role_bindings(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def list_roles(self) -> list[RoleRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_roles = rbac_api.list_cluster_role()
            namespaced_roles = rbac_api.list_role_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        roles = [_to_cluster_role(item) for item in cluster_roles.items]
        roles += [_to_namespaced_role(item) for item in namespaced_roles.items]
        return roles

    def list_pods_by_service_account(self) -> list[PodOwnerRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            PodOwnerRaw(
                pod_name=item.metadata.name,
                namespace=item.metadata.namespace,
                service_account_name=item.spec.service_account_name
                or _DEFAULT_SERVICE_ACCOUNT_NAME,
            )
            for item in result.items
        ]

    def fetch_api_usage(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)


def _to_binding(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def _to_subject(subject: Any) -> SubjectRaw:
    return SubjectRaw(kind=subject.kind, name=subject.name, namespace=subject.namespace)


def _to_cluster_role(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def _to_namespaced_role(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def _to_rule(rule: Any) -> PolicyRuleRaw:
    return PolicyRuleRaw(
        verbs=rule.verbs or [],
        resources=rule.resources or [],
        api_groups=rule.api_groups or [],
    )


def _to_aggregation_selectors(aggregation_rule: Any) -> list[dict[str, str]]:
    if aggregation_rule is None or not aggregation_rule.cluster_role_selectors:
        return []
    return [selector.match_labels or {} for selector in aggregation_rule.cluster_role_selectors]


def _parse_audit_line(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ServiceAccount/RBAC info")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")
