from __future__ import annotations

from hexawyn.domain.models.rbac_audit import ClusterRoleCandidate, PolicyRule


def resolve_effective_rules(
    own_rules: list[PolicyRule],
    aggregation_selectors: list[dict[str, str]],
    all_cluster_roles: list[ClusterRoleCandidate],
) -> list[PolicyRule]:
    effective_rules = list(own_rules)
    for selector in aggregation_selectors:
        for candidate in all_cluster_roles:
            if _labels_match(selector, candidate.labels):
                effective_rules.extend(candidate.rules)
    return _dedupe(effective_rules)


def _labels_match(selector: dict[str, str], labels: dict[str, str]) -> bool:
    return all(labels.get(key) == value for key, value in selector.items())


def _dedupe(rules: list[PolicyRule]) -> list[PolicyRule]:
    seen: set[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = set()
    deduped: list[PolicyRule] = []
    for rule in rules:
        key = (tuple(rule.verbs), tuple(rule.resources), tuple(rule.api_groups))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(rule)
    return deduped
