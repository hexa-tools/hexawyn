from __future__ import annotations

from hexawyn.domain.models.configuration_drift import DriftSeverity

_FIELD_SEVERITY: dict[str, DriftSeverity] = {
    "image": "critical",
    "replicas": "warning",
    "resource_limits": "warning",
    "env_vars": "warning",
    "configmap_data": "warning",
    "labels": "info",
}
_DEFAULT_SEVERITY: DriftSeverity = "warning"

_ALWAYS_CRITICAL_KINDS = frozenset(
    {"Role", "ClusterRole", "RoleBinding", "ClusterRoleBinding", "Secret"}
)


def classify_severity(field_name: str, resource_kind: str) -> DriftSeverity:
    """RBAC/Secret kinds are always critical regardless of which field
    drifted; otherwise severity is determined by which kind of field it is."""
    if resource_kind in _ALWAYS_CRITICAL_KINDS:
        return "critical"
    return _FIELD_SEVERITY.get(field_name, _DEFAULT_SEVERITY)
