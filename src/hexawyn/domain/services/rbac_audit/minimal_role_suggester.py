from __future__ import annotations

from hexawyn.domain.models.rbac_audit import PolicyRule, RiskLevel, SuggestedRole

_READ_ONLY_VERBS = ("get", "list", "watch")


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


def _rules_from_observed_pairs(pairs: list[tuple[str, str]]) -> list[PolicyRule]:
    verbs_by_resource: dict[str, set[str]] = {}
    for verb, resource in pairs:
        verbs_by_resource.setdefault(resource, set()).add(verb)
    return [
        PolicyRule(verbs=sorted(verbs), resources=[resource], api_groups=[""])
        for resource, verbs in verbs_by_resource.items()
    ]


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
