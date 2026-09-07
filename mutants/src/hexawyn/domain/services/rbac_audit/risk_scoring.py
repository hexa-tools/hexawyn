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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_risk_level__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_risk_level__mutmut)
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


def x_classify_risk_level__mutmut_orig(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def x_classify_risk_level__mutmut_1(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "XXcriticalXX"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def x_classify_risk_level__mutmut_2(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "CRITICAL"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def x_classify_risk_level__mutmut_3(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(None):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def x_classify_risk_level__mutmut_4(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(None) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def x_classify_risk_level__mutmut_5(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "XXcriticalXX"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def x_classify_risk_level__mutmut_6(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "CRITICAL"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def x_classify_risk_level__mutmut_7(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(None):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def x_classify_risk_level__mutmut_8(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(None) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def x_classify_risk_level__mutmut_9(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "XXhighXX"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def x_classify_risk_level__mutmut_10(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "HIGH"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def x_classify_risk_level__mutmut_11(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(None) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def x_classify_risk_level__mutmut_12(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) < _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "medium"


def x_classify_risk_level__mutmut_13(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "XXlowXX"
    return "medium"


def x_classify_risk_level__mutmut_14(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "LOW"
    return "medium"


def x_classify_risk_level__mutmut_15(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "XXmediumXX"


def x_classify_risk_level__mutmut_16(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> RiskLevel:
    if is_cluster_admin:
        return "critical"
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        return "critical"
    if any(has_wildcard_verb(rule) for rule in effective_rules):
        return "high"
    if compute_permission_breadth(effective_rules) <= _NARROW_BREADTH_THRESHOLD:
        return "low"
    return "MEDIUM"

mutants_x_classify_risk_level__mutmut['_mutmut_orig'] = x_classify_risk_level__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_1'] = x_classify_risk_level__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_2'] = x_classify_risk_level__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_3'] = x_classify_risk_level__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_4'] = x_classify_risk_level__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_5'] = x_classify_risk_level__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_6'] = x_classify_risk_level__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_7'] = x_classify_risk_level__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_8'] = x_classify_risk_level__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_9'] = x_classify_risk_level__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_10'] = x_classify_risk_level__mutmut_10 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_11'] = x_classify_risk_level__mutmut_11 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_12'] = x_classify_risk_level__mutmut_12 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_13'] = x_classify_risk_level__mutmut_13 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_14'] = x_classify_risk_level__mutmut_14 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_15'] = x_classify_risk_level__mutmut_15 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_16'] = x_classify_risk_level__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_risk_reasons__mutmut)
def build_risk_reasons(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("grants access to all resources (*)")
    if any(has_wildcard_verb(rule) and targets_secrets(rule) for rule in effective_rules):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def x_build_risk_reasons__mutmut_orig(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("grants access to all resources (*)")
    if any(has_wildcard_verb(rule) and targets_secrets(rule) for rule in effective_rules):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def x_build_risk_reasons__mutmut_1(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = None
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("grants access to all resources (*)")
    if any(has_wildcard_verb(rule) and targets_secrets(rule) for rule in effective_rules):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def x_build_risk_reasons__mutmut_2(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(None)
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("grants access to all resources (*)")
    if any(has_wildcard_verb(rule) and targets_secrets(rule) for rule in effective_rules):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def x_build_risk_reasons__mutmut_3(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(None):
        reasons.append("grants access to all resources (*)")
    if any(has_wildcard_verb(rule) and targets_secrets(rule) for rule in effective_rules):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def x_build_risk_reasons__mutmut_4(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(None) for rule in effective_rules):
        reasons.append("grants access to all resources (*)")
    if any(has_wildcard_verb(rule) and targets_secrets(rule) for rule in effective_rules):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def x_build_risk_reasons__mutmut_5(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append(None)
    if any(has_wildcard_verb(rule) and targets_secrets(rule) for rule in effective_rules):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def x_build_risk_reasons__mutmut_6(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("XXgrants access to all resources (*)XX")
    if any(has_wildcard_verb(rule) and targets_secrets(rule) for rule in effective_rules):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def x_build_risk_reasons__mutmut_7(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("GRANTS ACCESS TO ALL RESOURCES (*)")
    if any(has_wildcard_verb(rule) and targets_secrets(rule) for rule in effective_rules):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def x_build_risk_reasons__mutmut_8(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("grants access to all resources (*)")
    if any(None):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def x_build_risk_reasons__mutmut_9(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("grants access to all resources (*)")
    if any(has_wildcard_verb(rule) or targets_secrets(rule) for rule in effective_rules):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def x_build_risk_reasons__mutmut_10(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("grants access to all resources (*)")
    if any(has_wildcard_verb(None) and targets_secrets(rule) for rule in effective_rules):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def x_build_risk_reasons__mutmut_11(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("grants access to all resources (*)")
    if any(has_wildcard_verb(rule) and targets_secrets(None) for rule in effective_rules):
        reasons.append("wildcard verb grants full access to secrets")
    return reasons


def x_build_risk_reasons__mutmut_12(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("grants access to all resources (*)")
    if any(has_wildcard_verb(rule) and targets_secrets(rule) for rule in effective_rules):
        reasons.append(None)
    return reasons


def x_build_risk_reasons__mutmut_13(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("grants access to all resources (*)")
    if any(has_wildcard_verb(rule) and targets_secrets(rule) for rule in effective_rules):
        reasons.append("XXwildcard verb grants full access to secretsXX")
    return reasons


def x_build_risk_reasons__mutmut_14(is_cluster_admin: bool, effective_rules: list[PolicyRule]) -> list[str]:
    reasons: list[str] = []
    if is_cluster_admin:
        reasons.append(f"bound to {_cfg.cluster_admin_role_name}")
    if any(has_wildcard_resource(rule) for rule in effective_rules):
        reasons.append("grants access to all resources (*)")
    if any(has_wildcard_verb(rule) and targets_secrets(rule) for rule in effective_rules):
        reasons.append("WILDCARD VERB GRANTS FULL ACCESS TO SECRETS")
    return reasons

mutants_x_build_risk_reasons__mutmut['_mutmut_orig'] = x_build_risk_reasons__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_1'] = x_build_risk_reasons__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_2'] = x_build_risk_reasons__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_3'] = x_build_risk_reasons__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_4'] = x_build_risk_reasons__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_5'] = x_build_risk_reasons__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_6'] = x_build_risk_reasons__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_7'] = x_build_risk_reasons__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_8'] = x_build_risk_reasons__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_9'] = x_build_risk_reasons__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_10'] = x_build_risk_reasons__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_11'] = x_build_risk_reasons__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_12'] = x_build_risk_reasons__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_13'] = x_build_risk_reasons__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_risk_reasons__mutmut['x_build_risk_reasons__mutmut_14'] = x_build_risk_reasons__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_permission_breadth__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_permission_breadth__mutmut)
def compute_permission_breadth(effective_rules: list[PolicyRule]) -> int:
    distinct_verbs: set[str] = set()
    distinct_resources: set[str] = set()
    for rule in effective_rules:
        distinct_verbs.update(rule.verbs)
        distinct_resources.update(rule.resources)
    return len(distinct_verbs) * len(distinct_resources)


def x_compute_permission_breadth__mutmut_orig(effective_rules: list[PolicyRule]) -> int:
    distinct_verbs: set[str] = set()
    distinct_resources: set[str] = set()
    for rule in effective_rules:
        distinct_verbs.update(rule.verbs)
        distinct_resources.update(rule.resources)
    return len(distinct_verbs) * len(distinct_resources)


def x_compute_permission_breadth__mutmut_1(effective_rules: list[PolicyRule]) -> int:
    distinct_verbs: set[str] = None
    distinct_resources: set[str] = set()
    for rule in effective_rules:
        distinct_verbs.update(rule.verbs)
        distinct_resources.update(rule.resources)
    return len(distinct_verbs) * len(distinct_resources)


def x_compute_permission_breadth__mutmut_2(effective_rules: list[PolicyRule]) -> int:
    distinct_verbs: set[str] = set()
    distinct_resources: set[str] = None
    for rule in effective_rules:
        distinct_verbs.update(rule.verbs)
        distinct_resources.update(rule.resources)
    return len(distinct_verbs) * len(distinct_resources)


def x_compute_permission_breadth__mutmut_3(effective_rules: list[PolicyRule]) -> int:
    distinct_verbs: set[str] = set()
    distinct_resources: set[str] = set()
    for rule in effective_rules:
        distinct_verbs.update(None)
        distinct_resources.update(rule.resources)
    return len(distinct_verbs) * len(distinct_resources)


def x_compute_permission_breadth__mutmut_4(effective_rules: list[PolicyRule]) -> int:
    distinct_verbs: set[str] = set()
    distinct_resources: set[str] = set()
    for rule in effective_rules:
        distinct_verbs.update(rule.verbs)
        distinct_resources.update(None)
    return len(distinct_verbs) * len(distinct_resources)


def x_compute_permission_breadth__mutmut_5(effective_rules: list[PolicyRule]) -> int:
    distinct_verbs: set[str] = set()
    distinct_resources: set[str] = set()
    for rule in effective_rules:
        distinct_verbs.update(rule.verbs)
        distinct_resources.update(rule.resources)
    return len(distinct_verbs) / len(distinct_resources)

mutants_x_compute_permission_breadth__mutmut['_mutmut_orig'] = x_compute_permission_breadth__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_permission_breadth__mutmut['x_compute_permission_breadth__mutmut_1'] = x_compute_permission_breadth__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_permission_breadth__mutmut['x_compute_permission_breadth__mutmut_2'] = x_compute_permission_breadth__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_permission_breadth__mutmut['x_compute_permission_breadth__mutmut_3'] = x_compute_permission_breadth__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_permission_breadth__mutmut['x_compute_permission_breadth__mutmut_4'] = x_compute_permission_breadth__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_permission_breadth__mutmut['x_compute_permission_breadth__mutmut_5'] = x_compute_permission_breadth__mutmut_5 # type: ignore # mutmut generated
