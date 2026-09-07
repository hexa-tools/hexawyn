from __future__ import annotations

from hexawyn.application.ports.driven.rbac_security_audit_port import (
    ApiUsageFetchResult,
    PolicyRuleRaw,
    RoleBindingRaw,
    RoleRaw,
    RoleRefRaw,
    ServiceAccountRaw,
)
from hexawyn.domain.models.constants import RBACAuditConstants
from hexawyn.domain.models.rbac_audit import (
    ClusterRoleCandidate,
    PolicyRule,
    RBACFinding,
    RoleKey,
    ServiceAccountKey,
)
from hexawyn.domain.services.rbac_audit.aggregation_resolver import (
    resolve_effective_rules,
)
from hexawyn.domain.services.rbac_audit.minimal_role_suggester import (
    build_recommendation,
    suggest_minimal_role,
)
from hexawyn.domain.services.rbac_audit.misconfiguration import is_misconfigured_binding
from hexawyn.domain.services.rbac_audit.risk_scoring import (
    build_risk_reasons,
    classify_risk_level,
)

_cfg = RBACAuditConstants()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_finding__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_finding__mutmut)
def build_finding(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_orig(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_1(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = None
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_2(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = True
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_3(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = None
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_4(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = True
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_5(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = None

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_6(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = None
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_7(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            None, binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_8(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], None, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_9(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, None, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_10(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, None
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_11(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_12(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_13(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_14(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_15(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["XXrole_refXX"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_16(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["ROLE_REF"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_17(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is not None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_18(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            break
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_19(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole" or binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_20(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["XXrole_refXX"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_21(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["ROLE_REF"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_22(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["XXkindXX"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_23(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["KIND"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_24(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] != "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_25(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "XXClusterRoleXX"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_26(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "clusterrole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_27(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "CLUSTERROLE"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_28(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["XXrole_refXX"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_29(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["ROLE_REF"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_30(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["XXnameXX"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_31(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["NAME"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_32(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] != _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_33(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = None

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_34(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = False

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_35(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = None
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_36(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(None) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_37(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["XXrulesXX"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_38(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["RULES"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_39(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["XXkindXX"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_40(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["KIND"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_41(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] != "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_42(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "XXClusterRoleXX":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_43(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "clusterrole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_44(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "CLUSTERROLE":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_45(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = None
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_46(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                None, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_47(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, None, cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_48(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], None
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_49(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_50(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_51(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_52(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["XXaggregation_selectorsXX"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_53(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["AGGREGATION_SELECTORS"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_54(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = None
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_55(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(None)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_56(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(None, binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_57(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], None):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_58(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_59(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], ):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_60(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["XXbinding_kindXX"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_61(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["BINDING_KIND"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_62(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = None

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_63(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = False

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_64(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = None
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_65(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(None, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_66(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, None)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_67(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_68(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, )
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_69(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = None
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_70(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(None, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_71(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, None)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_72(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_73(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, )
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_74(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            None  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_75(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "XXRoleBinding grants cluster-scoped resource access that has no effect within a namespaceXX"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_76(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "rolebinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_77(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "ROLEBINDING GRANTS CLUSTER-SCOPED RESOURCE ACCESS THAT HAS NO EFFECT WITHIN A NAMESPACE"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_78(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = None
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_79(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["XXverbXX"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_80(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["VERB"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_81(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["XXresourceXX"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_82(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["RESOURCE"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_83(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["XXeventsXX"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_84(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["EVENTS"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_85(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"] or event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_86(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["XXservice_accountXX"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_87(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["SERVICE_ACCOUNT"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_88(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] != service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_89(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["XXnameXX"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_90(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["NAME"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_91(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["XXnamespaceXX"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_92(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["NAMESPACE"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_93(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] != service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_94(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["XXnamespaceXX"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_95(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["NAMESPACE"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_96(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = None
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_97(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(None, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_98(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, None, observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_99(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], None)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_100(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_101(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_102(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], )
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_103(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["XXavailableXX"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_104(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["AVAILABLE"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_105(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = None

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_106(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(None, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_107(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, None, suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_108(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], None)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_109(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_110(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_111(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], )

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_112(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["XXnamespaceXX"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_113(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["NAMESPACE"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_114(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=None,
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_115(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=None,
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_116(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=None,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_117(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=None,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_118(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=None,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_119(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=None,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_120(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=None,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_121(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=None,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_122(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=None,
    )


def x_build_finding__mutmut_123(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_124(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_125(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_126(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_127(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_128(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_129(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_130(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_131(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        )


def x_build_finding__mutmut_132(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["XXnameXX"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_133(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["NAME"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_134(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["XXnamespaceXX"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def x_build_finding__mutmut_135(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["NAMESPACE"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )

mutants_x_build_finding__mutmut['_mutmut_orig'] = x_build_finding__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_1'] = x_build_finding__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_2'] = x_build_finding__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_3'] = x_build_finding__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_4'] = x_build_finding__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_5'] = x_build_finding__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_6'] = x_build_finding__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_7'] = x_build_finding__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_8'] = x_build_finding__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_9'] = x_build_finding__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_10'] = x_build_finding__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_11'] = x_build_finding__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_12'] = x_build_finding__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_13'] = x_build_finding__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_14'] = x_build_finding__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_15'] = x_build_finding__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_16'] = x_build_finding__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_17'] = x_build_finding__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_18'] = x_build_finding__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_19'] = x_build_finding__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_20'] = x_build_finding__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_21'] = x_build_finding__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_22'] = x_build_finding__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_23'] = x_build_finding__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_24'] = x_build_finding__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_25'] = x_build_finding__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_26'] = x_build_finding__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_27'] = x_build_finding__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_28'] = x_build_finding__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_29'] = x_build_finding__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_30'] = x_build_finding__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_31'] = x_build_finding__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_32'] = x_build_finding__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_33'] = x_build_finding__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_34'] = x_build_finding__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_35'] = x_build_finding__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_36'] = x_build_finding__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_37'] = x_build_finding__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_38'] = x_build_finding__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_39'] = x_build_finding__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_40'] = x_build_finding__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_41'] = x_build_finding__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_42'] = x_build_finding__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_43'] = x_build_finding__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_44'] = x_build_finding__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_45'] = x_build_finding__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_46'] = x_build_finding__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_47'] = x_build_finding__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_48'] = x_build_finding__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_49'] = x_build_finding__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_50'] = x_build_finding__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_51'] = x_build_finding__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_52'] = x_build_finding__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_53'] = x_build_finding__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_54'] = x_build_finding__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_55'] = x_build_finding__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_56'] = x_build_finding__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_57'] = x_build_finding__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_58'] = x_build_finding__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_59'] = x_build_finding__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_60'] = x_build_finding__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_61'] = x_build_finding__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_62'] = x_build_finding__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_63'] = x_build_finding__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_64'] = x_build_finding__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_65'] = x_build_finding__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_66'] = x_build_finding__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_67'] = x_build_finding__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_68'] = x_build_finding__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_69'] = x_build_finding__mutmut_69 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_70'] = x_build_finding__mutmut_70 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_71'] = x_build_finding__mutmut_71 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_72'] = x_build_finding__mutmut_72 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_73'] = x_build_finding__mutmut_73 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_74'] = x_build_finding__mutmut_74 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_75'] = x_build_finding__mutmut_75 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_76'] = x_build_finding__mutmut_76 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_77'] = x_build_finding__mutmut_77 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_78'] = x_build_finding__mutmut_78 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_79'] = x_build_finding__mutmut_79 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_80'] = x_build_finding__mutmut_80 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_81'] = x_build_finding__mutmut_81 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_82'] = x_build_finding__mutmut_82 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_83'] = x_build_finding__mutmut_83 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_84'] = x_build_finding__mutmut_84 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_85'] = x_build_finding__mutmut_85 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_86'] = x_build_finding__mutmut_86 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_87'] = x_build_finding__mutmut_87 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_88'] = x_build_finding__mutmut_88 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_89'] = x_build_finding__mutmut_89 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_90'] = x_build_finding__mutmut_90 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_91'] = x_build_finding__mutmut_91 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_92'] = x_build_finding__mutmut_92 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_93'] = x_build_finding__mutmut_93 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_94'] = x_build_finding__mutmut_94 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_95'] = x_build_finding__mutmut_95 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_96'] = x_build_finding__mutmut_96 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_97'] = x_build_finding__mutmut_97 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_98'] = x_build_finding__mutmut_98 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_99'] = x_build_finding__mutmut_99 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_100'] = x_build_finding__mutmut_100 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_101'] = x_build_finding__mutmut_101 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_102'] = x_build_finding__mutmut_102 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_103'] = x_build_finding__mutmut_103 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_104'] = x_build_finding__mutmut_104 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_105'] = x_build_finding__mutmut_105 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_106'] = x_build_finding__mutmut_106 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_107'] = x_build_finding__mutmut_107 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_108'] = x_build_finding__mutmut_108 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_109'] = x_build_finding__mutmut_109 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_110'] = x_build_finding__mutmut_110 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_111'] = x_build_finding__mutmut_111 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_112'] = x_build_finding__mutmut_112 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_113'] = x_build_finding__mutmut_113 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_114'] = x_build_finding__mutmut_114 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_115'] = x_build_finding__mutmut_115 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_116'] = x_build_finding__mutmut_116 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_117'] = x_build_finding__mutmut_117 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_118'] = x_build_finding__mutmut_118 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_119'] = x_build_finding__mutmut_119 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_120'] = x_build_finding__mutmut_120 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_121'] = x_build_finding__mutmut_121 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_122'] = x_build_finding__mutmut_122 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_123'] = x_build_finding__mutmut_123 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_124'] = x_build_finding__mutmut_124 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_125'] = x_build_finding__mutmut_125 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_126'] = x_build_finding__mutmut_126 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_127'] = x_build_finding__mutmut_127 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_128'] = x_build_finding__mutmut_128 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_129'] = x_build_finding__mutmut_129 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_130'] = x_build_finding__mutmut_130 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_131'] = x_build_finding__mutmut_131 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_132'] = x_build_finding__mutmut_132 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_133'] = x_build_finding__mutmut_133 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_134'] = x_build_finding__mutmut_134 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_135'] = x_build_finding__mutmut_135 # type: ignore # mutmut generated
mutants_x_resolve_role__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_resolve_role__mutmut)
def resolve_role(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["name"]))


def x_resolve_role__mutmut_orig(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["name"]))


def x_resolve_role__mutmut_1(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["XXkindXX"] == "ClusterRole":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["name"]))


def x_resolve_role__mutmut_2(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["KIND"] == "ClusterRole":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["name"]))


def x_resolve_role__mutmut_3(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] != "ClusterRole":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["name"]))


def x_resolve_role__mutmut_4(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "XXClusterRoleXX":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["name"]))


def x_resolve_role__mutmut_5(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "clusterrole":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["name"]))


def x_resolve_role__mutmut_6(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "CLUSTERROLE":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["name"]))


def x_resolve_role__mutmut_7(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":
        return cluster_roles_by_name.get(None)
    return roles_by_namespace_name.get((binding["namespace"], role_ref["name"]))


def x_resolve_role__mutmut_8(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":
        return cluster_roles_by_name.get(role_ref["XXnameXX"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["name"]))


def x_resolve_role__mutmut_9(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":
        return cluster_roles_by_name.get(role_ref["NAME"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["name"]))


def x_resolve_role__mutmut_10(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get(None)


def x_resolve_role__mutmut_11(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["XXnamespaceXX"], role_ref["name"]))


def x_resolve_role__mutmut_12(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["NAMESPACE"], role_ref["name"]))


def x_resolve_role__mutmut_13(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["XXnameXX"]))


def x_resolve_role__mutmut_14(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["NAME"]))

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
mutants_x_index_bindings_by_service_account__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_index_bindings_by_service_account__mutmut)
def index_bindings_by_service_account(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_orig(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_1(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = None
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_2(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["XXsubjectsXX"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_3(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["SUBJECTS"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_4(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["XXkindXX"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_5(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["KIND"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_6(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] == "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_7(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "XXServiceAccountXX":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_8(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "serviceaccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_9(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "SERVICEACCOUNT":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_10(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                break
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_11(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = None
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_12(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] and binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_13(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["XXnamespaceXX"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_14(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["NAMESPACE"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_15(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["XXnamespaceXX"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_16(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["NAMESPACE"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_17(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is not None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_18(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                break
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_19(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(None)
    return index


def x_index_bindings_by_service_account__mutmut_20(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault(None, []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_21(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), None).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_22(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault([]).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_23(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), ).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_24(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["XXnameXX"]), []).append(binding)
    return index


def x_index_bindings_by_service_account__mutmut_25(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["NAME"]), []).append(binding)
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
mutants_x_index_pods_by_service_account__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_index_pods_by_service_account__mutmut)
def index_pods_by_service_account(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_orig(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_1(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = None
    for pod in pod_owners:
        key: tuple[str, str] = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_2(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = None
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_3(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["XXnamespaceXX"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_4(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["NAMESPACE"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_5(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["namespace"], pod["XXservice_account_nameXX"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_6(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["namespace"], pod["SERVICE_ACCOUNT_NAME"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_7(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(None)
    return index


def x_index_pods_by_service_account__mutmut_8(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["namespace"], pod["service_account_name"])
        index.setdefault(None, []).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_9(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, None).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_10(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["namespace"], pod["service_account_name"])
        index.setdefault([]).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_11(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, ).append(pod["pod_name"])
    return index


def x_index_pods_by_service_account__mutmut_12(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["XXpod_nameXX"])
    return index


def x_index_pods_by_service_account__mutmut_13(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["namespace"], pod["service_account_name"])
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
mutants_x_to_policy_rule__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_policy_rule__mutmut)
def to_policy_rule(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["verbs"], resources=raw["resources"], api_groups=raw["api_groups"])


def x_to_policy_rule__mutmut_orig(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["verbs"], resources=raw["resources"], api_groups=raw["api_groups"])


def x_to_policy_rule__mutmut_1(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=None, resources=raw["resources"], api_groups=raw["api_groups"])


def x_to_policy_rule__mutmut_2(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["verbs"], resources=None, api_groups=raw["api_groups"])


def x_to_policy_rule__mutmut_3(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["verbs"], resources=raw["resources"], api_groups=None)


def x_to_policy_rule__mutmut_4(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(resources=raw["resources"], api_groups=raw["api_groups"])


def x_to_policy_rule__mutmut_5(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["verbs"], api_groups=raw["api_groups"])


def x_to_policy_rule__mutmut_6(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["verbs"], resources=raw["resources"], )


def x_to_policy_rule__mutmut_7(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["XXverbsXX"], resources=raw["resources"], api_groups=raw["api_groups"])


def x_to_policy_rule__mutmut_8(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["VERBS"], resources=raw["resources"], api_groups=raw["api_groups"])


def x_to_policy_rule__mutmut_9(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["verbs"], resources=raw["XXresourcesXX"], api_groups=raw["api_groups"])


def x_to_policy_rule__mutmut_10(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["verbs"], resources=raw["RESOURCES"], api_groups=raw["api_groups"])


def x_to_policy_rule__mutmut_11(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["verbs"], resources=raw["resources"], api_groups=raw["XXapi_groupsXX"])


def x_to_policy_rule__mutmut_12(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["verbs"], resources=raw["resources"], api_groups=raw["API_GROUPS"])

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
