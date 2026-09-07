from __future__ import annotations

from hexawyn.domain.models.constants import RBACAuditConstants
from hexawyn.domain.models.rbac_audit import PolicyRule

_cfg = RBACAuditConstants()
_SECRETS_RESOURCE = "secrets"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_has_wildcard_verb__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_has_wildcard_verb__mutmut)
def has_wildcard_verb(rule: PolicyRule) -> bool:
    return _cfg.wildcard in rule.verbs


def x_has_wildcard_verb__mutmut_orig(rule: PolicyRule) -> bool:
    return _cfg.wildcard in rule.verbs


def x_has_wildcard_verb__mutmut_1(rule: PolicyRule) -> bool:
    return _cfg.wildcard not in rule.verbs

mutants_x_has_wildcard_verb__mutmut['_mutmut_orig'] = x_has_wildcard_verb__mutmut_orig # type: ignore # mutmut generated
mutants_x_has_wildcard_verb__mutmut['x_has_wildcard_verb__mutmut_1'] = x_has_wildcard_verb__mutmut_1 # type: ignore # mutmut generated
mutants_x_has_wildcard_resource__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_has_wildcard_resource__mutmut)
def has_wildcard_resource(rule: PolicyRule) -> bool:
    return _cfg.wildcard in rule.resources


def x_has_wildcard_resource__mutmut_orig(rule: PolicyRule) -> bool:
    return _cfg.wildcard in rule.resources


def x_has_wildcard_resource__mutmut_1(rule: PolicyRule) -> bool:
    return _cfg.wildcard not in rule.resources

mutants_x_has_wildcard_resource__mutmut['_mutmut_orig'] = x_has_wildcard_resource__mutmut_orig # type: ignore # mutmut generated
mutants_x_has_wildcard_resource__mutmut['x_has_wildcard_resource__mutmut_1'] = x_has_wildcard_resource__mutmut_1 # type: ignore # mutmut generated
mutants_x_targets_secrets__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_targets_secrets__mutmut)
def targets_secrets(rule: PolicyRule) -> bool:
    return _SECRETS_RESOURCE in rule.resources


def x_targets_secrets__mutmut_orig(rule: PolicyRule) -> bool:
    return _SECRETS_RESOURCE in rule.resources


def x_targets_secrets__mutmut_1(rule: PolicyRule) -> bool:
    return _SECRETS_RESOURCE not in rule.resources

mutants_x_targets_secrets__mutmut['_mutmut_orig'] = x_targets_secrets__mutmut_orig # type: ignore # mutmut generated
mutants_x_targets_secrets__mutmut['x_targets_secrets__mutmut_1'] = x_targets_secrets__mutmut_1 # type: ignore # mutmut generated
