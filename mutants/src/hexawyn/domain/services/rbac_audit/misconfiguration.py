from __future__ import annotations

from typing import Literal

from hexawyn.domain.models.constants import RBACAuditConstants
from hexawyn.domain.models.rbac_audit import PolicyRule

_cfg = RBACAuditConstants()
_CLUSTER_SCOPED_RESOURCES = frozenset(_cfg.cluster_scoped_resources)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_is_misconfigured_binding__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_misconfigured_binding__mutmut)
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


def x_is_misconfigured_binding__mutmut_orig(
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


def x_is_misconfigured_binding__mutmut_1(
    binding_kind: Literal["ClusterRoleBinding", "RoleBinding"],
    effective_rules: list[PolicyRule],
) -> bool:
    if binding_kind == "RoleBinding":
        return False
    return any(
        resource in _CLUSTER_SCOPED_RESOURCES
        for rule in effective_rules
        for resource in rule.resources
    )


def x_is_misconfigured_binding__mutmut_2(
    binding_kind: Literal["ClusterRoleBinding", "RoleBinding"],
    effective_rules: list[PolicyRule],
) -> bool:
    if binding_kind != "XXRoleBindingXX":
        return False
    return any(
        resource in _CLUSTER_SCOPED_RESOURCES
        for rule in effective_rules
        for resource in rule.resources
    )


def x_is_misconfigured_binding__mutmut_3(
    binding_kind: Literal["ClusterRoleBinding", "RoleBinding"],
    effective_rules: list[PolicyRule],
) -> bool:
    if binding_kind != "rolebinding":
        return False
    return any(
        resource in _CLUSTER_SCOPED_RESOURCES
        for rule in effective_rules
        for resource in rule.resources
    )


def x_is_misconfigured_binding__mutmut_4(
    binding_kind: Literal["ClusterRoleBinding", "RoleBinding"],
    effective_rules: list[PolicyRule],
) -> bool:
    if binding_kind != "ROLEBINDING":
        return False
    return any(
        resource in _CLUSTER_SCOPED_RESOURCES
        for rule in effective_rules
        for resource in rule.resources
    )


def x_is_misconfigured_binding__mutmut_5(
    binding_kind: Literal["ClusterRoleBinding", "RoleBinding"],
    effective_rules: list[PolicyRule],
) -> bool:
    if binding_kind != "RoleBinding":
        return True
    return any(
        resource in _CLUSTER_SCOPED_RESOURCES
        for rule in effective_rules
        for resource in rule.resources
    )


def x_is_misconfigured_binding__mutmut_6(
    binding_kind: Literal["ClusterRoleBinding", "RoleBinding"],
    effective_rules: list[PolicyRule],
) -> bool:
    if binding_kind != "RoleBinding":
        return False
    return any(
        None
    )


def x_is_misconfigured_binding__mutmut_7(
    binding_kind: Literal["ClusterRoleBinding", "RoleBinding"],
    effective_rules: list[PolicyRule],
) -> bool:
    if binding_kind != "RoleBinding":
        return False
    return any(
        resource not in _CLUSTER_SCOPED_RESOURCES
        for rule in effective_rules
        for resource in rule.resources
    )

mutants_x_is_misconfigured_binding__mutmut['_mutmut_orig'] = x_is_misconfigured_binding__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_misconfigured_binding__mutmut['x_is_misconfigured_binding__mutmut_1'] = x_is_misconfigured_binding__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_misconfigured_binding__mutmut['x_is_misconfigured_binding__mutmut_2'] = x_is_misconfigured_binding__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_misconfigured_binding__mutmut['x_is_misconfigured_binding__mutmut_3'] = x_is_misconfigured_binding__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_misconfigured_binding__mutmut['x_is_misconfigured_binding__mutmut_4'] = x_is_misconfigured_binding__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_misconfigured_binding__mutmut['x_is_misconfigured_binding__mutmut_5'] = x_is_misconfigured_binding__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_misconfigured_binding__mutmut['x_is_misconfigured_binding__mutmut_6'] = x_is_misconfigured_binding__mutmut_6 # type: ignore # mutmut generated
mutants_x_is_misconfigured_binding__mutmut['x_is_misconfigured_binding__mutmut_7'] = x_is_misconfigured_binding__mutmut_7 # type: ignore # mutmut generated
