from __future__ import annotations

from hexawyn.application.ports.driven.rbac_security_audit_port import (
    PodOwnerRaw,
    PolicyRuleRaw,
    RoleBindingRaw,
    RoleRaw,
)
from hexawyn.application.use_case.security.audit_rbac_permissions.response import (
    AuditRbacPermissionsResponse,
    PolicyRuleDict,
    RBACFindingDict,
    SuggestedRoleDict,
    UnusedServiceAccountDict,
)
from hexawyn.domain.models.rbac_audit import (
    ClusterRoleCandidate,
    PolicyRule,
    RBACAuditReport,
    RBACFinding,
    SuggestedRole,
)

_ServiceAccountKey = tuple[str, str]
_RoleKey = tuple[str | None, str]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_to_policy_rule__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_policy_rule__mutmut)
def to_policy_rule(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=raw["verbs"],
        resources=raw["resources"],
        api_groups=raw["api_groups"],
    )


def x_to_policy_rule__mutmut_orig(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=raw["verbs"],
        resources=raw["resources"],
        api_groups=raw["api_groups"],
    )


def x_to_policy_rule__mutmut_1(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=None,
        resources=raw["resources"],
        api_groups=raw["api_groups"],
    )


def x_to_policy_rule__mutmut_2(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=raw["verbs"],
        resources=None,
        api_groups=raw["api_groups"],
    )


def x_to_policy_rule__mutmut_3(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=raw["verbs"],
        resources=raw["resources"],
        api_groups=None,
    )


def x_to_policy_rule__mutmut_4(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        resources=raw["resources"],
        api_groups=raw["api_groups"],
    )


def x_to_policy_rule__mutmut_5(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=raw["verbs"],
        api_groups=raw["api_groups"],
    )


def x_to_policy_rule__mutmut_6(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=raw["verbs"],
        resources=raw["resources"],
        )


def x_to_policy_rule__mutmut_7(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=raw["XXverbsXX"],
        resources=raw["resources"],
        api_groups=raw["api_groups"],
    )


def x_to_policy_rule__mutmut_8(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=raw["VERBS"],
        resources=raw["resources"],
        api_groups=raw["api_groups"],
    )


def x_to_policy_rule__mutmut_9(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=raw["verbs"],
        resources=raw["XXresourcesXX"],
        api_groups=raw["api_groups"],
    )


def x_to_policy_rule__mutmut_10(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=raw["verbs"],
        resources=raw["RESOURCES"],
        api_groups=raw["api_groups"],
    )


def x_to_policy_rule__mutmut_11(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=raw["verbs"],
        resources=raw["resources"],
        api_groups=raw["XXapi_groupsXX"],
    )


def x_to_policy_rule__mutmut_12(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=raw["verbs"],
        resources=raw["resources"],
        api_groups=raw["API_GROUPS"],
    )

mutants_x_to_policy_rule__mutmut['_mutmut_orig'] = x_to_policy_rule__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_policy_rule__mutmut['x_to_policy_rule__mutmut_1'] = x_to_policy_rule__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_policy_rule__mutmut['x_to_policy_rule__mutmut_2'] = x_to_policy_rule__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_policy_rule__mutmut['x_to_policy_rule__mutmut_3'] = x_to_policy_rule__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_policy_rule__mutmut['x_to_policy_rule__mutmut_4'] = x_to_policy_rule__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_policy_rule__mutmut['x_to_policy_rule__mutmut_5'] = x_to_policy_rule__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_policy_rule__mutmut['x_to_policy_rule__mutmut_6'] = x_to_policy_rule__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_policy_rule__mutmut['x_to_policy_rule__mutmut_7'] = x_to_policy_rule__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_policy_rule__mutmut['x_to_policy_rule__mutmut_8'] = x_to_policy_rule__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_policy_rule__mutmut['x_to_policy_rule__mutmut_9'] = x_to_policy_rule__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_policy_rule__mutmut['x_to_policy_rule__mutmut_10'] = x_to_policy_rule__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_policy_rule__mutmut['x_to_policy_rule__mutmut_11'] = x_to_policy_rule__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_policy_rule__mutmut['x_to_policy_rule__mutmut_12'] = x_to_policy_rule__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_candidate__mutmut)
def to_candidate(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        labels=role["labels"],
        rules=[to_policy_rule(rule) for rule in role["rules"]],
    )


def x_to_candidate__mutmut_orig(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        labels=role["labels"],
        rules=[to_policy_rule(rule) for rule in role["rules"]],
    )


def x_to_candidate__mutmut_1(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=None,
        labels=role["labels"],
        rules=[to_policy_rule(rule) for rule in role["rules"]],
    )


def x_to_candidate__mutmut_2(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        labels=None,
        rules=[to_policy_rule(rule) for rule in role["rules"]],
    )


def x_to_candidate__mutmut_3(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        labels=role["labels"],
        rules=None,
    )


def x_to_candidate__mutmut_4(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        labels=role["labels"],
        rules=[to_policy_rule(rule) for rule in role["rules"]],
    )


def x_to_candidate__mutmut_5(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        rules=[to_policy_rule(rule) for rule in role["rules"]],
    )


def x_to_candidate__mutmut_6(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        labels=role["labels"],
        )


def x_to_candidate__mutmut_7(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["XXnameXX"],
        labels=role["labels"],
        rules=[to_policy_rule(rule) for rule in role["rules"]],
    )


def x_to_candidate__mutmut_8(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["NAME"],
        labels=role["labels"],
        rules=[to_policy_rule(rule) for rule in role["rules"]],
    )


def x_to_candidate__mutmut_9(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        labels=role["XXlabelsXX"],
        rules=[to_policy_rule(rule) for rule in role["rules"]],
    )


def x_to_candidate__mutmut_10(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        labels=role["LABELS"],
        rules=[to_policy_rule(rule) for rule in role["rules"]],
    )


def x_to_candidate__mutmut_11(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        labels=role["labels"],
        rules=[to_policy_rule(None) for rule in role["rules"]],
    )


def x_to_candidate__mutmut_12(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        labels=role["labels"],
        rules=[to_policy_rule(rule) for rule in role["XXrulesXX"]],
    )


def x_to_candidate__mutmut_13(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        labels=role["labels"],
        rules=[to_policy_rule(rule) for rule in role["RULES"]],
    )

mutants_x_to_candidate__mutmut['_mutmut_orig'] = x_to_candidate__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut['x_to_candidate__mutmut_1'] = x_to_candidate__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut['x_to_candidate__mutmut_2'] = x_to_candidate__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut['x_to_candidate__mutmut_3'] = x_to_candidate__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut['x_to_candidate__mutmut_4'] = x_to_candidate__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut['x_to_candidate__mutmut_5'] = x_to_candidate__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut['x_to_candidate__mutmut_6'] = x_to_candidate__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut['x_to_candidate__mutmut_7'] = x_to_candidate__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut['x_to_candidate__mutmut_8'] = x_to_candidate__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut['x_to_candidate__mutmut_9'] = x_to_candidate__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut['x_to_candidate__mutmut_10'] = x_to_candidate__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut['x_to_candidate__mutmut_11'] = x_to_candidate__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut['x_to_candidate__mutmut_12'] = x_to_candidate__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_candidate__mutmut['x_to_candidate__mutmut_13'] = x_to_candidate__mutmut_13 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_index_bindings_by_service_account__mutmut)
def index_bindings_by_service_account(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_orig(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_1(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = None
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_2(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["XXsubjectsXX"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_3(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["SUBJECTS"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_4(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["XXkindXX"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_5(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["KIND"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_6(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] == "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_7(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "XXServiceAccountXX":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_8(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "serviceaccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_9(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "SERVICEACCOUNT":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_10(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                break
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_11(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = None
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_12(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] and binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_13(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["XXnamespaceXX"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_14(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["NAMESPACE"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_15(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["XXnamespaceXX"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_16(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["NAMESPACE"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_17(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is not None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_18(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                break
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_19(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = None
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_20(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["XXnameXX"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_21(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["NAME"])
            index.setdefault(key, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_22(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(None)
    return index


def x_index_bindings_by_service_account__mutmut_23(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(None, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_24(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, None).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_25(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault([]).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_26(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, ).append(binding)
    return index

mutants_x_index_bindings_by_service_account__mutmut['_mutmut_orig'] = x_index_bindings_by_service_account__mutmut_orig # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_1'] = x_index_bindings_by_service_account__mutmut_1 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_2'] = x_index_bindings_by_service_account__mutmut_2 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_3'] = x_index_bindings_by_service_account__mutmut_3 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_4'] = x_index_bindings_by_service_account__mutmut_4 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_5'] = x_index_bindings_by_service_account__mutmut_5 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_6'] = x_index_bindings_by_service_account__mutmut_6 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_7'] = x_index_bindings_by_service_account__mutmut_7 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_8'] = x_index_bindings_by_service_account__mutmut_8 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_9'] = x_index_bindings_by_service_account__mutmut_9 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_10'] = x_index_bindings_by_service_account__mutmut_10 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_11'] = x_index_bindings_by_service_account__mutmut_11 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_12'] = x_index_bindings_by_service_account__mutmut_12 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_13'] = x_index_bindings_by_service_account__mutmut_13 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_14'] = x_index_bindings_by_service_account__mutmut_14 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_15'] = x_index_bindings_by_service_account__mutmut_15 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_16'] = x_index_bindings_by_service_account__mutmut_16 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_17'] = x_index_bindings_by_service_account__mutmut_17 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_18'] = x_index_bindings_by_service_account__mutmut_18 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_19'] = x_index_bindings_by_service_account__mutmut_19 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_20'] = x_index_bindings_by_service_account__mutmut_20 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_21'] = x_index_bindings_by_service_account__mutmut_21 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_22'] = x_index_bindings_by_service_account__mutmut_22 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_23'] = x_index_bindings_by_service_account__mutmut_23 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_24'] = x_index_bindings_by_service_account__mutmut_24 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_25'] = x_index_bindings_by_service_account__mutmut_25 # type: ignore # mutmut generated
mutants_x_index_bindings_by_service_account__mutmut['x_index_bindings_by_service_account__mutmut_26'] = x_index_bindings_by_service_account__mutmut_26 # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_index_pods_by_service_account__mutmut)
def index_pods_by_service_account(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_orig(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_1(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = None
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_2(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = None
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_3(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["XXnamespaceXX"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_4(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["NAMESPACE"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_5(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["namespace"], pod["XXservice_account_nameXX"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_6(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["namespace"], pod["SERVICE_ACCOUNT_NAME"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_7(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(None)
    return index


def x_index_pods_by_service_account__mutmut_8(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["namespace"], pod["service_account_name"])
        index.setdefault(None, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_9(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, None).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_10(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["namespace"], pod["service_account_name"])
        index.setdefault([]).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_11(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, ).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_12(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["XXpod_nameXX"])
    return index


def x_index_pods_by_service_account__mutmut_13(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["POD_NAME"])
    return index

mutants_x_index_pods_by_service_account__mutmut['_mutmut_orig'] = x_index_pods_by_service_account__mutmut_orig # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut['x_index_pods_by_service_account__mutmut_1'] = x_index_pods_by_service_account__mutmut_1 # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut['x_index_pods_by_service_account__mutmut_2'] = x_index_pods_by_service_account__mutmut_2 # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut['x_index_pods_by_service_account__mutmut_3'] = x_index_pods_by_service_account__mutmut_3 # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut['x_index_pods_by_service_account__mutmut_4'] = x_index_pods_by_service_account__mutmut_4 # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut['x_index_pods_by_service_account__mutmut_5'] = x_index_pods_by_service_account__mutmut_5 # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut['x_index_pods_by_service_account__mutmut_6'] = x_index_pods_by_service_account__mutmut_6 # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut['x_index_pods_by_service_account__mutmut_7'] = x_index_pods_by_service_account__mutmut_7 # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut['x_index_pods_by_service_account__mutmut_8'] = x_index_pods_by_service_account__mutmut_8 # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut['x_index_pods_by_service_account__mutmut_9'] = x_index_pods_by_service_account__mutmut_9 # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut['x_index_pods_by_service_account__mutmut_10'] = x_index_pods_by_service_account__mutmut_10 # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut['x_index_pods_by_service_account__mutmut_11'] = x_index_pods_by_service_account__mutmut_11 # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut['x_index_pods_by_service_account__mutmut_12'] = x_index_pods_by_service_account__mutmut_12 # type: ignore # mutmut generated
mutants_x_index_pods_by_service_account__mutmut['x_index_pods_by_service_account__mutmut_13'] = x_index_pods_by_service_account__mutmut_13 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_resolve_role__mutmut)
def resolve_role(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["name"]),  # type: ignore
    )


def x_resolve_role__mutmut_orig(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["name"]),  # type: ignore
    )


def x_resolve_role__mutmut_1(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["XXkindXX"] == "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["name"]),  # type: ignore
    )


def x_resolve_role__mutmut_2(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["KIND"] == "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["name"]),  # type: ignore
    )


def x_resolve_role__mutmut_3(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] != "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["name"]),  # type: ignore
    )


def x_resolve_role__mutmut_4(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "XXClusterRoleXX":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["name"]),  # type: ignore
    )


def x_resolve_role__mutmut_5(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "clusterrole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["name"]),  # type: ignore
    )


def x_resolve_role__mutmut_6(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "CLUSTERROLE":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["name"]),  # type: ignore
    )


def x_resolve_role__mutmut_7(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(None)  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["name"]),  # type: ignore
    )


def x_resolve_role__mutmut_8(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["XXnameXX"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["name"]),  # type: ignore
    )


def x_resolve_role__mutmut_9(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["NAME"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["name"]),  # type: ignore
    )


def x_resolve_role__mutmut_10(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        None,  # type: ignore
    )


def x_resolve_role__mutmut_11(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["XXnamespaceXX"], role_ref["name"]),  # type: ignore
    )


def x_resolve_role__mutmut_12(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["NAMESPACE"], role_ref["name"]),  # type: ignore
    )


def x_resolve_role__mutmut_13(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["XXnameXX"]),  # type: ignore
    )


def x_resolve_role__mutmut_14(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["NAME"]),  # type: ignore
    )

mutants_x_resolve_role__mutmut['_mutmut_orig'] = x_resolve_role__mutmut_orig # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_1'] = x_resolve_role__mutmut_1 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_2'] = x_resolve_role__mutmut_2 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_3'] = x_resolve_role__mutmut_3 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_4'] = x_resolve_role__mutmut_4 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_5'] = x_resolve_role__mutmut_5 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_6'] = x_resolve_role__mutmut_6 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_7'] = x_resolve_role__mutmut_7 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_8'] = x_resolve_role__mutmut_8 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_9'] = x_resolve_role__mutmut_9 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_10'] = x_resolve_role__mutmut_10 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_11'] = x_resolve_role__mutmut_11 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_12'] = x_resolve_role__mutmut_12 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_13'] = x_resolve_role__mutmut_13 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut['x_resolve_role__mutmut_14'] = x_resolve_role__mutmut_14 # type: ignore # mutmut generated
mutants_x_to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_response__mutmut)
def to_response(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_orig(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_1(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=None,
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_2(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=None,
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_3(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=None,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_4(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=None,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_5(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=None,
        error=None,
    )


def x_to_response__mutmut_6(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_7(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_8(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_9(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_10(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        error=None,
    )


def x_to_response__mutmut_11(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        )


def x_to_response__mutmut_12(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(None) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_13(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=None, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_14(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=None)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_15(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_16(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, )
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )

mutants_x_to_response__mutmut['_mutmut_orig'] = x_to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_1'] = x_to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_2'] = x_to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_3'] = x_to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_4'] = x_to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_5'] = x_to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_6'] = x_to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_7'] = x_to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_8'] = x_to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_9'] = x_to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_10'] = x_to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_11'] = x_to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_12'] = x_to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_13'] = x_to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_14'] = x_to_response__mutmut_14 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_15'] = x_to_response__mutmut_15 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_16'] = x_to_response__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_finding_dict__mutmut)
def _to_finding_dict(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_orig(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_1(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=None,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_2(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=None,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_3(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=None,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_4(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=None,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_5(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=None,
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_6(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=None,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_7(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=None,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_8(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=None,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_9(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=None,
    )


def x__to_finding_dict__mutmut_10(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_11(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_12(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_13(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_14(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_15(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_16(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_17(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_18(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        )


def x__to_finding_dict__mutmut_19(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(None) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def x__to_finding_dict__mutmut_20(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(None),
    )

mutants_x__to_finding_dict__mutmut['_mutmut_orig'] = x__to_finding_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_1'] = x__to_finding_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_2'] = x__to_finding_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_3'] = x__to_finding_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_4'] = x__to_finding_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_5'] = x__to_finding_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_6'] = x__to_finding_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_7'] = x__to_finding_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_8'] = x__to_finding_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_9'] = x__to_finding_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_10'] = x__to_finding_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_11'] = x__to_finding_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_12'] = x__to_finding_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_13'] = x__to_finding_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_14'] = x__to_finding_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_15'] = x__to_finding_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_16'] = x__to_finding_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_17'] = x__to_finding_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_18'] = x__to_finding_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_19'] = x__to_finding_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_20'] = x__to_finding_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_rule_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_rule_dict__mutmut)
def _to_rule_dict(rule: PolicyRule) -> PolicyRuleDict:
    return PolicyRuleDict(
        verbs=rule.verbs,
        resources=rule.resources,
        api_groups=rule.api_groups,
    )


def x__to_rule_dict__mutmut_orig(rule: PolicyRule) -> PolicyRuleDict:
    return PolicyRuleDict(
        verbs=rule.verbs,
        resources=rule.resources,
        api_groups=rule.api_groups,
    )


def x__to_rule_dict__mutmut_1(rule: PolicyRule) -> PolicyRuleDict:
    return PolicyRuleDict(
        verbs=None,
        resources=rule.resources,
        api_groups=rule.api_groups,
    )


def x__to_rule_dict__mutmut_2(rule: PolicyRule) -> PolicyRuleDict:
    return PolicyRuleDict(
        verbs=rule.verbs,
        resources=None,
        api_groups=rule.api_groups,
    )


def x__to_rule_dict__mutmut_3(rule: PolicyRule) -> PolicyRuleDict:
    return PolicyRuleDict(
        verbs=rule.verbs,
        resources=rule.resources,
        api_groups=None,
    )


def x__to_rule_dict__mutmut_4(rule: PolicyRule) -> PolicyRuleDict:
    return PolicyRuleDict(
        resources=rule.resources,
        api_groups=rule.api_groups,
    )


def x__to_rule_dict__mutmut_5(rule: PolicyRule) -> PolicyRuleDict:
    return PolicyRuleDict(
        verbs=rule.verbs,
        api_groups=rule.api_groups,
    )


def x__to_rule_dict__mutmut_6(rule: PolicyRule) -> PolicyRuleDict:
    return PolicyRuleDict(
        verbs=rule.verbs,
        resources=rule.resources,
        )

mutants_x__to_rule_dict__mutmut['_mutmut_orig'] = x__to_rule_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_rule_dict__mutmut['x__to_rule_dict__mutmut_1'] = x__to_rule_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_rule_dict__mutmut['x__to_rule_dict__mutmut_2'] = x__to_rule_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_rule_dict__mutmut['x__to_rule_dict__mutmut_3'] = x__to_rule_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_rule_dict__mutmut['x__to_rule_dict__mutmut_4'] = x__to_rule_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_rule_dict__mutmut['x__to_rule_dict__mutmut_5'] = x__to_rule_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_rule_dict__mutmut['x__to_rule_dict__mutmut_6'] = x__to_rule_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_suggested_role_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_suggested_role_dict__mutmut)
def _to_suggested_role_dict(
    suggested_role: SuggestedRole,
) -> SuggestedRoleDict:
    return SuggestedRoleDict(
        kind=suggested_role.kind,
        rules=[_to_rule_dict(rule) for rule in suggested_role.rules],
        basis=suggested_role.basis,
    )


def x__to_suggested_role_dict__mutmut_orig(
    suggested_role: SuggestedRole,
) -> SuggestedRoleDict:
    return SuggestedRoleDict(
        kind=suggested_role.kind,
        rules=[_to_rule_dict(rule) for rule in suggested_role.rules],
        basis=suggested_role.basis,
    )


def x__to_suggested_role_dict__mutmut_1(
    suggested_role: SuggestedRole,
) -> SuggestedRoleDict:
    return SuggestedRoleDict(
        kind=None,
        rules=[_to_rule_dict(rule) for rule in suggested_role.rules],
        basis=suggested_role.basis,
    )


def x__to_suggested_role_dict__mutmut_2(
    suggested_role: SuggestedRole,
) -> SuggestedRoleDict:
    return SuggestedRoleDict(
        kind=suggested_role.kind,
        rules=None,
        basis=suggested_role.basis,
    )


def x__to_suggested_role_dict__mutmut_3(
    suggested_role: SuggestedRole,
) -> SuggestedRoleDict:
    return SuggestedRoleDict(
        kind=suggested_role.kind,
        rules=[_to_rule_dict(rule) for rule in suggested_role.rules],
        basis=None,
    )


def x__to_suggested_role_dict__mutmut_4(
    suggested_role: SuggestedRole,
) -> SuggestedRoleDict:
    return SuggestedRoleDict(
        rules=[_to_rule_dict(rule) for rule in suggested_role.rules],
        basis=suggested_role.basis,
    )


def x__to_suggested_role_dict__mutmut_5(
    suggested_role: SuggestedRole,
) -> SuggestedRoleDict:
    return SuggestedRoleDict(
        kind=suggested_role.kind,
        basis=suggested_role.basis,
    )


def x__to_suggested_role_dict__mutmut_6(
    suggested_role: SuggestedRole,
) -> SuggestedRoleDict:
    return SuggestedRoleDict(
        kind=suggested_role.kind,
        rules=[_to_rule_dict(rule) for rule in suggested_role.rules],
        )


def x__to_suggested_role_dict__mutmut_7(
    suggested_role: SuggestedRole,
) -> SuggestedRoleDict:
    return SuggestedRoleDict(
        kind=suggested_role.kind,
        rules=[_to_rule_dict(None) for rule in suggested_role.rules],
        basis=suggested_role.basis,
    )

mutants_x__to_suggested_role_dict__mutmut['_mutmut_orig'] = x__to_suggested_role_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_suggested_role_dict__mutmut['x__to_suggested_role_dict__mutmut_1'] = x__to_suggested_role_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_suggested_role_dict__mutmut['x__to_suggested_role_dict__mutmut_2'] = x__to_suggested_role_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_suggested_role_dict__mutmut['x__to_suggested_role_dict__mutmut_3'] = x__to_suggested_role_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_suggested_role_dict__mutmut['x__to_suggested_role_dict__mutmut_4'] = x__to_suggested_role_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_suggested_role_dict__mutmut['x__to_suggested_role_dict__mutmut_5'] = x__to_suggested_role_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_suggested_role_dict__mutmut['x__to_suggested_role_dict__mutmut_6'] = x__to_suggested_role_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_suggested_role_dict__mutmut['x__to_suggested_role_dict__mutmut_7'] = x__to_suggested_role_dict__mutmut_7 # type: ignore # mutmut generated
