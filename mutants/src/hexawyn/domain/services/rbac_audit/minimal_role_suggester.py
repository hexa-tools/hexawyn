from __future__ import annotations

from hexawyn.domain.models.rbac_audit import PolicyRule, RiskLevel, SuggestedRole

_READ_ONLY_VERBS = ("get", "list", "watch")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_suggest_minimal_role__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_suggest_minimal_role__mutmut)
def suggest_minimal_role(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_orig(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_1(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind=None,
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_2(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=None,
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_3(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis=None,
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_4(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_5(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_6(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_7(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="XXRoleXX",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_8(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_9(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="ROLE",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_10(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(None),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_11(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="XXaudit_logXX",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_12(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="AUDIT_LOG",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_13(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind=None, rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_14(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=None, basis="estimated"
    )


def x_suggest_minimal_role__mutmut_15(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis=None
    )


def x_suggest_minimal_role__mutmut_16(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_17(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", basis="estimated"
    )


def x_suggest_minimal_role__mutmut_18(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), )


def x_suggest_minimal_role__mutmut_19(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="XXRoleXX", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_20(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="role", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_21(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="ROLE", rules=_narrow_to_read_only(effective_rules), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_22(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(None), basis="estimated"
    )


def x_suggest_minimal_role__mutmut_23(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="XXestimatedXX"
    )


def x_suggest_minimal_role__mutmut_24(
    effective_rules: list[PolicyRule],
    api_usage_available: bool,
    observed_verb_resource_pairs: list[tuple[str, str]],
) -> SuggestedRole:
    if api_usage_available:
        return SuggestedRole(
            kind="Role",
            rules=_rules_from_observed_pairs(observed_verb_resource_pairs),
            basis="audit_log",
        )
    return SuggestedRole(
        kind="Role", rules=_narrow_to_read_only(effective_rules), basis="ESTIMATED"
    )

mutants_x_suggest_minimal_role__mutmut['_mutmut_orig'] = x_suggest_minimal_role__mutmut_orig # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_1'] = x_suggest_minimal_role__mutmut_1 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_2'] = x_suggest_minimal_role__mutmut_2 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_3'] = x_suggest_minimal_role__mutmut_3 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_4'] = x_suggest_minimal_role__mutmut_4 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_5'] = x_suggest_minimal_role__mutmut_5 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_6'] = x_suggest_minimal_role__mutmut_6 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_7'] = x_suggest_minimal_role__mutmut_7 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_8'] = x_suggest_minimal_role__mutmut_8 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_9'] = x_suggest_minimal_role__mutmut_9 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_10'] = x_suggest_minimal_role__mutmut_10 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_11'] = x_suggest_minimal_role__mutmut_11 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_12'] = x_suggest_minimal_role__mutmut_12 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_13'] = x_suggest_minimal_role__mutmut_13 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_14'] = x_suggest_minimal_role__mutmut_14 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_15'] = x_suggest_minimal_role__mutmut_15 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_16'] = x_suggest_minimal_role__mutmut_16 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_17'] = x_suggest_minimal_role__mutmut_17 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_18'] = x_suggest_minimal_role__mutmut_18 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_19'] = x_suggest_minimal_role__mutmut_19 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_20'] = x_suggest_minimal_role__mutmut_20 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_21'] = x_suggest_minimal_role__mutmut_21 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_22'] = x_suggest_minimal_role__mutmut_22 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_23'] = x_suggest_minimal_role__mutmut_23 # type: ignore # mutmut generated
mutants_x_suggest_minimal_role__mutmut['x_suggest_minimal_role__mutmut_24'] = x_suggest_minimal_role__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_recommendation__mutmut)
def build_recommendation(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_orig(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_1(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = None
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_2(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules or suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_3(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_4(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis != "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_5(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "XXaudit_logXX"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_6(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "AUDIT_LOG"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_7(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "XXNo API usage observed in the audit window — recommend you remove all permissions for this service account.XX"  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_8(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "no api usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_9(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "NO API USAGE OBSERVED IN THE AUDIT WINDOW — RECOMMEND YOU REMOVE ALL PERMISSIONS FOR THIS SERVICE ACCOUNT."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_10(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level != "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_11(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "XXlowXX":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_12(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "LOW":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_13(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "XXCurrent permissions are minimal — no action needed.XX"
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_14(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_15(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "CURRENT PERMISSIONS ARE MINIMAL — NO ACTION NEEDED."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_16(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_17(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "XXNo API usage observed in the audit window — recommend you remove all permissions for this service account.XX"  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_18(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "no api usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_19(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "NO API USAGE OBSERVED IN THE AUDIT WINDOW — RECOMMEND YOU REMOVE ALL PERMISSIONS FOR THIS SERVICE ACCOUNT."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_20(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = None
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_21(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        None
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_22(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "XX; XX".join(
        f"{'/'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_23(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(None)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_24(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'XX/XX'.join(rule.verbs)} {', '.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_25(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {', '.join(None)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."


def x_build_recommendation__mutmut_26(
    risk_level: RiskLevel, namespace: str, suggested_role: SuggestedRole
) -> str:
    no_usage_confirmed = not suggested_role.rules and suggested_role.basis == "audit_log"
    if no_usage_confirmed:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    if risk_level == "low":
        return "Current permissions are minimal — no action needed."
    if not suggested_role.rules:
        return "No API usage observed in the audit window — recommend you remove all permissions for this service account."  # noqa: E501
    described = "; ".join(
        f"{'/'.join(rule.verbs)} {'XX, XX'.join(rule.resources)}" for rule in suggested_role.rules
    )
    return f"Replace with a Role limited to: {described} in the {namespace} namespace."

mutants_x_build_recommendation__mutmut['_mutmut_orig'] = x_build_recommendation__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_1'] = x_build_recommendation__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_2'] = x_build_recommendation__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_3'] = x_build_recommendation__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_4'] = x_build_recommendation__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_5'] = x_build_recommendation__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_6'] = x_build_recommendation__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_7'] = x_build_recommendation__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_8'] = x_build_recommendation__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_9'] = x_build_recommendation__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_10'] = x_build_recommendation__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_11'] = x_build_recommendation__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_12'] = x_build_recommendation__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_13'] = x_build_recommendation__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_14'] = x_build_recommendation__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_15'] = x_build_recommendation__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_16'] = x_build_recommendation__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_17'] = x_build_recommendation__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_18'] = x_build_recommendation__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_19'] = x_build_recommendation__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_20'] = x_build_recommendation__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_21'] = x_build_recommendation__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_22'] = x_build_recommendation__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_23'] = x_build_recommendation__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_24'] = x_build_recommendation__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_25'] = x_build_recommendation__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_26'] = x_build_recommendation__mutmut_26 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__rules_from_observed_pairs__mutmut)
def _rules_from_observed_pairs(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, set()).add(verb)
    return [
        PolicyRule(verbs=sorted(verbs), resources=[resource], api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_orig(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, set()).add(verb)
    return [
        PolicyRule(verbs=sorted(verbs), resources=[resource], api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_1(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = None
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, set()).add(verb)
    return [
        PolicyRule(verbs=sorted(verbs), resources=[resource], api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_2(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, set()).add(None)
    return [
        PolicyRule(verbs=sorted(verbs), resources=[resource], api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_3(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(None, set()).add(verb)
    return [
        PolicyRule(verbs=sorted(verbs), resources=[resource], api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_4(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, None).add(verb)
    return [
        PolicyRule(verbs=sorted(verbs), resources=[resource], api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_5(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(set()).add(verb)
    return [
        PolicyRule(verbs=sorted(verbs), resources=[resource], api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_6(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, ).add(verb)
    return [
        PolicyRule(verbs=sorted(verbs), resources=[resource], api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_7(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, set()).add(verb)
    return [
        PolicyRule(verbs=None, resources=[resource], api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_8(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, set()).add(verb)
    return [
        PolicyRule(verbs=sorted(verbs), resources=None, api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_9(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, set()).add(verb)
    return [
        PolicyRule(verbs=sorted(verbs), resources=[resource], api_groups=None)
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_10(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, set()).add(verb)
    return [
        PolicyRule(resources=[resource], api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_11(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, set()).add(verb)
    return [
        PolicyRule(verbs=sorted(verbs), api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_12(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, set()).add(verb)
    return [
        PolicyRule(verbs=sorted(verbs), resources=[resource], )
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_13(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, set()).add(verb)
    return [
        PolicyRule(verbs=sorted(None), resources=[resource], api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


def x__rules_from_observed_pairs__mutmut_14(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, set()).add(verb)
    return [
        PolicyRule(verbs=sorted(verbs), resources=[resource], api_groups=["XXXX"])
        for resource, verbs in verbs_by_resource.items()
    ]

mutants_x__rules_from_observed_pairs__mutmut['_mutmut_orig'] = x__rules_from_observed_pairs__mutmut_orig # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_1'] = x__rules_from_observed_pairs__mutmut_1 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_2'] = x__rules_from_observed_pairs__mutmut_2 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_3'] = x__rules_from_observed_pairs__mutmut_3 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_4'] = x__rules_from_observed_pairs__mutmut_4 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_5'] = x__rules_from_observed_pairs__mutmut_5 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_6'] = x__rules_from_observed_pairs__mutmut_6 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_7'] = x__rules_from_observed_pairs__mutmut_7 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_8'] = x__rules_from_observed_pairs__mutmut_8 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_9'] = x__rules_from_observed_pairs__mutmut_9 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_10'] = x__rules_from_observed_pairs__mutmut_10 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_11'] = x__rules_from_observed_pairs__mutmut_11 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_12'] = x__rules_from_observed_pairs__mutmut_12 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_13'] = x__rules_from_observed_pairs__mutmut_13 # type: ignore # mutmut generated
mutants_x__rules_from_observed_pairs__mutmut['x__rules_from_observed_pairs__mutmut_14'] = x__rules_from_observed_pairs__mutmut_14 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__narrow_to_read_only__mutmut)
def _narrow_to_read_only(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=read_verbs,
                    resources=rule.resources,
                    api_groups=rule.api_groups,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_orig(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=read_verbs,
                    resources=rule.resources,
                    api_groups=rule.api_groups,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_1(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = None
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=read_verbs,
                    resources=rule.resources,
                    api_groups=rule.api_groups,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_2(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "XX*XX" in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=read_verbs,
                    resources=rule.resources,
                    api_groups=rule.api_groups,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_3(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" not in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=read_verbs,
                    resources=rule.resources,
                    api_groups=rule.api_groups,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_4(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = None
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=read_verbs,
                    resources=rule.resources,
                    api_groups=rule.api_groups,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_5(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = list(None)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=read_verbs,
                    resources=rule.resources,
                    api_groups=rule.api_groups,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_6(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = None
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=read_verbs,
                    resources=rule.resources,
                    api_groups=rule.api_groups,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_7(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb not in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=read_verbs,
                    resources=rule.resources,
                    api_groups=rule.api_groups,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_8(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                None
            )
    return narrowed


def x__narrow_to_read_only__mutmut_9(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=None,
                    resources=rule.resources,
                    api_groups=rule.api_groups,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_10(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=read_verbs,
                    resources=None,
                    api_groups=rule.api_groups,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_11(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=read_verbs,
                    resources=rule.resources,
                    api_groups=None,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_12(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    resources=rule.resources,
                    api_groups=rule.api_groups,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_13(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=read_verbs,
                    api_groups=rule.api_groups,
                )
            )
    return narrowed


def x__narrow_to_read_only__mutmut_14(rules: list[PolicyRule]) -> list[PolicyRule]:
    narrowed: list[PolicyRule] = []
    for rule in rules:
        if "*" in rule.verbs:
            read_verbs = list(_READ_ONLY_VERBS)
        else:
            read_verbs = [verb for verb in _READ_ONLY_VERBS if verb in rule.verbs]
        if read_verbs:
            narrowed.append(
                PolicyRule(
                    verbs=read_verbs,
                    resources=rule.resources,
                    )
            )
    return narrowed

mutants_x__narrow_to_read_only__mutmut['_mutmut_orig'] = x__narrow_to_read_only__mutmut_orig # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_1'] = x__narrow_to_read_only__mutmut_1 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_2'] = x__narrow_to_read_only__mutmut_2 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_3'] = x__narrow_to_read_only__mutmut_3 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_4'] = x__narrow_to_read_only__mutmut_4 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_5'] = x__narrow_to_read_only__mutmut_5 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_6'] = x__narrow_to_read_only__mutmut_6 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_7'] = x__narrow_to_read_only__mutmut_7 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_8'] = x__narrow_to_read_only__mutmut_8 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_9'] = x__narrow_to_read_only__mutmut_9 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_10'] = x__narrow_to_read_only__mutmut_10 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_11'] = x__narrow_to_read_only__mutmut_11 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_12'] = x__narrow_to_read_only__mutmut_12 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_13'] = x__narrow_to_read_only__mutmut_13 # type: ignore # mutmut generated
mutants_x__narrow_to_read_only__mutmut['x__narrow_to_read_only__mutmut_14'] = x__narrow_to_read_only__mutmut_14 # type: ignore # mutmut generated
