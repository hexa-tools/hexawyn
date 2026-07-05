from __future__ import annotations

from hexawyn.domain.models.constants import RBACAuditConstants
from hexawyn.domain.models.rbac_audit import PolicyRule, RiskLevel
from hexawyn.domain.services.rbac_audit.wildcard_detection import (
    has_wildcard_resource,
    has_wildcard_verb,
    targets_secrets,
)

_cfg = RBACAuditConstants()
_NARROW_BREADTH_THRESHOLD = _cfg.narrow_breadth_verb_limit * _cfg.narrow_breadth_resource_limit


def classify_risk_level(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def build_risk_reasons(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("grants access to all resources (*)")
    if any(has_wildcard_verb(rule) and targets_secrets(rule) for rule in effective_rules):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def compute_permission_breadth(effective_rules: list[PolicyRule]) -> int:
    distinct_verbs: set[str] = set()
    distinct_resources: set[str] = set()
    for rule in effective_rules:
        distinct_verbs.update(rule.verbs)
        distinct_resources.update(rule.resources)
    return len(distinct_verbs) * len(distinct_resources)
