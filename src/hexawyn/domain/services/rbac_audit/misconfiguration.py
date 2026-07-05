from __future__ import annotations

from typing import Literal

from hexawyn.domain.models.constants import RBACAuditConstants
from hexawyn.domain.models.rbac_audit import PolicyRule

_cfg = RBACAuditConstants()
_CLUSTER_SCOPED_RESOURCES = frozenset(_cfg.cluster_scoped_resources)


def is_misconfigured_binding(
    binding_kind: Literal["ClusterRoleBinding", "RoleBinding"],
    effective_rules: list[PolicyRule],
) -> bool:
    if binding_kind != "RoleBinding":
        return False
    return any(
        resource in _CLUSTER_SCOPED_RESOURCES
        for rule in effective_rules
        for resource in rule.resources
    )
