from __future__ import annotations

from hexawyn.domain.models.constants import RBACAuditConstants
from hexawyn.domain.models.rbac_audit import PolicyRule

_cfg = RBACAuditConstants()
_SECRETS_RESOURCE = "secrets"


def has_wildcard_verb(rule: PolicyRule) -> bool:
    return _cfg.wildcard in rule.verbs


def has_wildcard_resource(rule: PolicyRule) -> bool:
    return _cfg.wildcard in rule.resources


def targets_secrets(rule: PolicyRule) -> bool:
    return _SECRETS_RESOURCE in rule.resources
