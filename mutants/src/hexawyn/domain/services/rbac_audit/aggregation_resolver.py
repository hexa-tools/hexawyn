from __future__ import annotations

from hexawyn.domain.models.rbac_audit import ClusterRoleCandidate, PolicyRule


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_resolve_effective_rules__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_resolve_effective_rules__mutmut)
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


def x_resolve_effective_rules__mutmut_orig(
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


def x_resolve_effective_rules__mutmut_1(
    own_rules: list[PolicyRule],
    aggregation_selectors: list[dict[str, str]],
    all_cluster_roles: list[ClusterRoleCandidate],
) -> list[PolicyRule]:
    effective_rules = None
    for selector in aggregation_selectors:
        for candidate in all_cluster_roles:
            if _labels_match(selector, candidate.labels):
                effective_rules.extend(candidate.rules)
    return _dedupe(effective_rules)


def x_resolve_effective_rules__mutmut_2(
    own_rules: list[PolicyRule],
    aggregation_selectors: list[dict[str, str]],
    all_cluster_roles: list[ClusterRoleCandidate],
) -> list[PolicyRule]:
    effective_rules = list(None)
    for selector in aggregation_selectors:
        for candidate in all_cluster_roles:
            if _labels_match(selector, candidate.labels):
                effective_rules.extend(candidate.rules)
    return _dedupe(effective_rules)


def x_resolve_effective_rules__mutmut_3(
    own_rules: list[PolicyRule],
    aggregation_selectors: list[dict[str, str]],
    all_cluster_roles: list[ClusterRoleCandidate],
) -> list[PolicyRule]:
    effective_rules = list(own_rules)
    for selector in aggregation_selectors:
        for candidate in all_cluster_roles:
            if _labels_match(None, candidate.labels):
                effective_rules.extend(candidate.rules)
    return _dedupe(effective_rules)


def x_resolve_effective_rules__mutmut_4(
    own_rules: list[PolicyRule],
    aggregation_selectors: list[dict[str, str]],
    all_cluster_roles: list[ClusterRoleCandidate],
) -> list[PolicyRule]:
    effective_rules = list(own_rules)
    for selector in aggregation_selectors:
        for candidate in all_cluster_roles:
            if _labels_match(selector, None):
                effective_rules.extend(candidate.rules)
    return _dedupe(effective_rules)


def x_resolve_effective_rules__mutmut_5(
    own_rules: list[PolicyRule],
    aggregation_selectors: list[dict[str, str]],
    all_cluster_roles: list[ClusterRoleCandidate],
) -> list[PolicyRule]:
    effective_rules = list(own_rules)
    for selector in aggregation_selectors:
        for candidate in all_cluster_roles:
            if _labels_match(candidate.labels):
                effective_rules.extend(candidate.rules)
    return _dedupe(effective_rules)


def x_resolve_effective_rules__mutmut_6(
    own_rules: list[PolicyRule],
    aggregation_selectors: list[dict[str, str]],
    all_cluster_roles: list[ClusterRoleCandidate],
) -> list[PolicyRule]:
    effective_rules = list(own_rules)
    for selector in aggregation_selectors:
        for candidate in all_cluster_roles:
            if _labels_match(selector, ):
                effective_rules.extend(candidate.rules)
    return _dedupe(effective_rules)


def x_resolve_effective_rules__mutmut_7(
    own_rules: list[PolicyRule],
    aggregation_selectors: list[dict[str, str]],
    all_cluster_roles: list[ClusterRoleCandidate],
) -> list[PolicyRule]:
    effective_rules = list(own_rules)
    for selector in aggregation_selectors:
        for candidate in all_cluster_roles:
            if _labels_match(selector, candidate.labels):
                effective_rules.extend(None)
    return _dedupe(effective_rules)


def x_resolve_effective_rules__mutmut_8(
    own_rules: list[PolicyRule],
    aggregation_selectors: list[dict[str, str]],
    all_cluster_roles: list[ClusterRoleCandidate],
) -> list[PolicyRule]:
    effective_rules = list(own_rules)
    for selector in aggregation_selectors:
        for candidate in all_cluster_roles:
            if _labels_match(selector, candidate.labels):
                effective_rules.extend(candidate.rules)
    return _dedupe(None)

mutants_x_resolve_effective_rules__mutmut['_mutmut_orig'] = x_resolve_effective_rules__mutmut_orig # type: ignore # mutmut generated
mutants_x_resolve_effective_rules__mutmut['x_resolve_effective_rules__mutmut_1'] = x_resolve_effective_rules__mutmut_1 # type: ignore # mutmut generated
mutants_x_resolve_effective_rules__mutmut['x_resolve_effective_rules__mutmut_2'] = x_resolve_effective_rules__mutmut_2 # type: ignore # mutmut generated
mutants_x_resolve_effective_rules__mutmut['x_resolve_effective_rules__mutmut_3'] = x_resolve_effective_rules__mutmut_3 # type: ignore # mutmut generated
mutants_x_resolve_effective_rules__mutmut['x_resolve_effective_rules__mutmut_4'] = x_resolve_effective_rules__mutmut_4 # type: ignore # mutmut generated
mutants_x_resolve_effective_rules__mutmut['x_resolve_effective_rules__mutmut_5'] = x_resolve_effective_rules__mutmut_5 # type: ignore # mutmut generated
mutants_x_resolve_effective_rules__mutmut['x_resolve_effective_rules__mutmut_6'] = x_resolve_effective_rules__mutmut_6 # type: ignore # mutmut generated
mutants_x_resolve_effective_rules__mutmut['x_resolve_effective_rules__mutmut_7'] = x_resolve_effective_rules__mutmut_7 # type: ignore # mutmut generated
mutants_x_resolve_effective_rules__mutmut['x_resolve_effective_rules__mutmut_8'] = x_resolve_effective_rules__mutmut_8 # type: ignore # mutmut generated
mutants_x__labels_match__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__labels_match__mutmut)
def _labels_match(selector: dict[str, str], labels: dict[str, str]) -> bool:
    return all(labels.get(key) == value for key, value in selector.items())


def x__labels_match__mutmut_orig(selector: dict[str, str], labels: dict[str, str]) -> bool:
    return all(labels.get(key) == value for key, value in selector.items())


def x__labels_match__mutmut_1(selector: dict[str, str], labels: dict[str, str]) -> bool:
    return all(None)


def x__labels_match__mutmut_2(selector: dict[str, str], labels: dict[str, str]) -> bool:
    return all(labels.get(None) == value for key, value in selector.items())


def x__labels_match__mutmut_3(selector: dict[str, str], labels: dict[str, str]) -> bool:
    return all(labels.get(key) != value for key, value in selector.items())

mutants_x__labels_match__mutmut['_mutmut_orig'] = x__labels_match__mutmut_orig # type: ignore # mutmut generated
mutants_x__labels_match__mutmut['x__labels_match__mutmut_1'] = x__labels_match__mutmut_1 # type: ignore # mutmut generated
mutants_x__labels_match__mutmut['x__labels_match__mutmut_2'] = x__labels_match__mutmut_2 # type: ignore # mutmut generated
mutants_x__labels_match__mutmut['x__labels_match__mutmut_3'] = x__labels_match__mutmut_3 # type: ignore # mutmut generated
mutants_x__dedupe__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__dedupe__mutmut)
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


def x__dedupe__mutmut_orig(rules: list[PolicyRule]) -> list[PolicyRule]:
    seen: set[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = set()
    deduped: list[PolicyRule] = []
    for rule in rules:
        key = (tuple(rule.verbs), tuple(rule.resources), tuple(rule.api_groups))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(rule)
    return deduped


def x__dedupe__mutmut_1(rules: list[PolicyRule]) -> list[PolicyRule]:
    seen: set[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = None
    deduped: list[PolicyRule] = []
    for rule in rules:
        key = (tuple(rule.verbs), tuple(rule.resources), tuple(rule.api_groups))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(rule)
    return deduped


def x__dedupe__mutmut_2(rules: list[PolicyRule]) -> list[PolicyRule]:
    seen: set[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = set()
    deduped: list[PolicyRule] = None
    for rule in rules:
        key = (tuple(rule.verbs), tuple(rule.resources), tuple(rule.api_groups))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(rule)
    return deduped


def x__dedupe__mutmut_3(rules: list[PolicyRule]) -> list[PolicyRule]:
    seen: set[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = set()
    deduped: list[PolicyRule] = []
    for rule in rules:
        key = None
        if key in seen:
            continue
        seen.add(key)
        deduped.append(rule)
    return deduped


def x__dedupe__mutmut_4(rules: list[PolicyRule]) -> list[PolicyRule]:
    seen: set[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = set()
    deduped: list[PolicyRule] = []
    for rule in rules:
        key = (tuple(None), tuple(rule.resources), tuple(rule.api_groups))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(rule)
    return deduped


def x__dedupe__mutmut_5(rules: list[PolicyRule]) -> list[PolicyRule]:
    seen: set[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = set()
    deduped: list[PolicyRule] = []
    for rule in rules:
        key = (tuple(rule.verbs), tuple(None), tuple(rule.api_groups))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(rule)
    return deduped


def x__dedupe__mutmut_6(rules: list[PolicyRule]) -> list[PolicyRule]:
    seen: set[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = set()
    deduped: list[PolicyRule] = []
    for rule in rules:
        key = (tuple(rule.verbs), tuple(rule.resources), tuple(None))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(rule)
    return deduped


def x__dedupe__mutmut_7(rules: list[PolicyRule]) -> list[PolicyRule]:
    seen: set[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = set()
    deduped: list[PolicyRule] = []
    for rule in rules:
        key = (tuple(rule.verbs), tuple(rule.resources), tuple(rule.api_groups))
        if key not in seen:
            continue
        seen.add(key)
        deduped.append(rule)
    return deduped


def x__dedupe__mutmut_8(rules: list[PolicyRule]) -> list[PolicyRule]:
    seen: set[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = set()
    deduped: list[PolicyRule] = []
    for rule in rules:
        key = (tuple(rule.verbs), tuple(rule.resources), tuple(rule.api_groups))
        if key in seen:
            break
        seen.add(key)
        deduped.append(rule)
    return deduped


def x__dedupe__mutmut_9(rules: list[PolicyRule]) -> list[PolicyRule]:
    seen: set[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = set()
    deduped: list[PolicyRule] = []
    for rule in rules:
        key = (tuple(rule.verbs), tuple(rule.resources), tuple(rule.api_groups))
        if key in seen:
            continue
        seen.add(None)
        deduped.append(rule)
    return deduped


def x__dedupe__mutmut_10(rules: list[PolicyRule]) -> list[PolicyRule]:
    seen: set[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = set()
    deduped: list[PolicyRule] = []
    for rule in rules:
        key = (tuple(rule.verbs), tuple(rule.resources), tuple(rule.api_groups))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(None)
    return deduped

mutants_x__dedupe__mutmut['_mutmut_orig'] = x__dedupe__mutmut_orig # type: ignore # mutmut generated
mutants_x__dedupe__mutmut['x__dedupe__mutmut_1'] = x__dedupe__mutmut_1 # type: ignore # mutmut generated
mutants_x__dedupe__mutmut['x__dedupe__mutmut_2'] = x__dedupe__mutmut_2 # type: ignore # mutmut generated
mutants_x__dedupe__mutmut['x__dedupe__mutmut_3'] = x__dedupe__mutmut_3 # type: ignore # mutmut generated
mutants_x__dedupe__mutmut['x__dedupe__mutmut_4'] = x__dedupe__mutmut_4 # type: ignore # mutmut generated
mutants_x__dedupe__mutmut['x__dedupe__mutmut_5'] = x__dedupe__mutmut_5 # type: ignore # mutmut generated
mutants_x__dedupe__mutmut['x__dedupe__mutmut_6'] = x__dedupe__mutmut_6 # type: ignore # mutmut generated
mutants_x__dedupe__mutmut['x__dedupe__mutmut_7'] = x__dedupe__mutmut_7 # type: ignore # mutmut generated
mutants_x__dedupe__mutmut['x__dedupe__mutmut_8'] = x__dedupe__mutmut_8 # type: ignore # mutmut generated
mutants_x__dedupe__mutmut['x__dedupe__mutmut_9'] = x__dedupe__mutmut_9 # type: ignore # mutmut generated
mutants_x__dedupe__mutmut['x__dedupe__mutmut_10'] = x__dedupe__mutmut_10 # type: ignore # mutmut generated
