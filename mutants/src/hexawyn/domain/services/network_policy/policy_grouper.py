from __future__ import annotations

from hexawyn.application.ports.driven.network_policy_audit_port import NetworkPolicyRaw
from hexawyn.domain.models.constants import NetworkPolicyConstants
from hexawyn.domain.models.network_policy import NetworkStatus

_cfg = NetworkPolicyConstants()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_group_policies_by_namespace__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_group_policies_by_namespace__mutmut)
def group_policies_by_namespace(
    policies_raw: list[NetworkPolicyRaw],
) -> dict[str, list[NetworkPolicyRaw]]:
    grouped: dict[str, list[NetworkPolicyRaw]] = {}
    for policy in policies_raw:
        grouped.setdefault(policy["namespace"], []).append(policy)
    return grouped


def x_group_policies_by_namespace__mutmut_orig(
    policies_raw: list[NetworkPolicyRaw],
) -> dict[str, list[NetworkPolicyRaw]]:
    grouped: dict[str, list[NetworkPolicyRaw]] = {}
    for policy in policies_raw:
        grouped.setdefault(policy["namespace"], []).append(policy)
    return grouped


def x_group_policies_by_namespace__mutmut_1(
    policies_raw: list[NetworkPolicyRaw],
) -> dict[str, list[NetworkPolicyRaw]]:
    grouped: dict[str, list[NetworkPolicyRaw]] = None
    for policy in policies_raw:
        grouped.setdefault(policy["namespace"], []).append(policy)
    return grouped


def x_group_policies_by_namespace__mutmut_2(
    policies_raw: list[NetworkPolicyRaw],
) -> dict[str, list[NetworkPolicyRaw]]:
    grouped: dict[str, list[NetworkPolicyRaw]] = {}
    for policy in policies_raw:
        grouped.setdefault(policy["namespace"], []).append(None)
    return grouped


def x_group_policies_by_namespace__mutmut_3(
    policies_raw: list[NetworkPolicyRaw],
) -> dict[str, list[NetworkPolicyRaw]]:
    grouped: dict[str, list[NetworkPolicyRaw]] = {}
    for policy in policies_raw:
        grouped.setdefault(None, []).append(policy)
    return grouped


def x_group_policies_by_namespace__mutmut_4(
    policies_raw: list[NetworkPolicyRaw],
) -> dict[str, list[NetworkPolicyRaw]]:
    grouped: dict[str, list[NetworkPolicyRaw]] = {}
    for policy in policies_raw:
        grouped.setdefault(policy["namespace"], None).append(policy)
    return grouped


def x_group_policies_by_namespace__mutmut_5(
    policies_raw: list[NetworkPolicyRaw],
) -> dict[str, list[NetworkPolicyRaw]]:
    grouped: dict[str, list[NetworkPolicyRaw]] = {}
    for policy in policies_raw:
        grouped.setdefault([]).append(policy)
    return grouped


def x_group_policies_by_namespace__mutmut_6(
    policies_raw: list[NetworkPolicyRaw],
) -> dict[str, list[NetworkPolicyRaw]]:
    grouped: dict[str, list[NetworkPolicyRaw]] = {}
    for policy in policies_raw:
        grouped.setdefault(policy["namespace"], ).append(policy)
    return grouped


def x_group_policies_by_namespace__mutmut_7(
    policies_raw: list[NetworkPolicyRaw],
) -> dict[str, list[NetworkPolicyRaw]]:
    grouped: dict[str, list[NetworkPolicyRaw]] = {}
    for policy in policies_raw:
        grouped.setdefault(policy["XXnamespaceXX"], []).append(policy)
    return grouped


def x_group_policies_by_namespace__mutmut_8(
    policies_raw: list[NetworkPolicyRaw],
) -> dict[str, list[NetworkPolicyRaw]]:
    grouped: dict[str, list[NetworkPolicyRaw]] = {}
    for policy in policies_raw:
        grouped.setdefault(policy["NAMESPACE"], []).append(policy)
    return grouped

mutants_x_group_policies_by_namespace__mutmut['_mutmut_orig'] = x_group_policies_by_namespace__mutmut_orig # type: ignore # mutmut generated
mutants_x_group_policies_by_namespace__mutmut['x_group_policies_by_namespace__mutmut_1'] = x_group_policies_by_namespace__mutmut_1 # type: ignore # mutmut generated
mutants_x_group_policies_by_namespace__mutmut['x_group_policies_by_namespace__mutmut_2'] = x_group_policies_by_namespace__mutmut_2 # type: ignore # mutmut generated
mutants_x_group_policies_by_namespace__mutmut['x_group_policies_by_namespace__mutmut_3'] = x_group_policies_by_namespace__mutmut_3 # type: ignore # mutmut generated
mutants_x_group_policies_by_namespace__mutmut['x_group_policies_by_namespace__mutmut_4'] = x_group_policies_by_namespace__mutmut_4 # type: ignore # mutmut generated
mutants_x_group_policies_by_namespace__mutmut['x_group_policies_by_namespace__mutmut_5'] = x_group_policies_by_namespace__mutmut_5 # type: ignore # mutmut generated
mutants_x_group_policies_by_namespace__mutmut['x_group_policies_by_namespace__mutmut_6'] = x_group_policies_by_namespace__mutmut_6 # type: ignore # mutmut generated
mutants_x_group_policies_by_namespace__mutmut['x_group_policies_by_namespace__mutmut_7'] = x_group_policies_by_namespace__mutmut_7 # type: ignore # mutmut generated
mutants_x_group_policies_by_namespace__mutmut['x_group_policies_by_namespace__mutmut_8'] = x_group_policies_by_namespace__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_note__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_note__mutmut)
def build_note(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_orig(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_1(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = None
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_2(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status == "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_3(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "XXrestrictedXX":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_4(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "RESTRICTED":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_5(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(None)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_6(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(None)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_7(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = None
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_8(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"] or (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_9(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["XXhas_empty_pod_selectorXX"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_10(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["HAS_EMPTY_POD_SELECTOR"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_11(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 and policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_12(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["XXingress_rule_countXX"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_13(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["INGRESS_RULE_COUNT"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_14(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] >= 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_15(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 1 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_16(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["XXegress_rule_countXX"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_17(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["EGRESS_RULE_COUNT"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_18(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] >= 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_19(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 1)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_20(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            None
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_21(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "XX(empty podSelector)XX"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_22(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podselector)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_23(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(EMPTY PODSELECTOR)"
        )

    return "; ".join(notes) if notes else None


def x_build_note__mutmut_24(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(None) if notes else None


def x_build_note__mutmut_25(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "XX; XX".join(notes) if notes else None

mutants_x_build_note__mutmut['_mutmut_orig'] = x_build_note__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_1'] = x_build_note__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_2'] = x_build_note__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_3'] = x_build_note__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_4'] = x_build_note__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_5'] = x_build_note__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_6'] = x_build_note__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_7'] = x_build_note__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_8'] = x_build_note__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_9'] = x_build_note__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_10'] = x_build_note__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_11'] = x_build_note__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_12'] = x_build_note__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_13'] = x_build_note__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_14'] = x_build_note__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_15'] = x_build_note__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_16'] = x_build_note__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_17'] = x_build_note__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_18'] = x_build_note__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_19'] = x_build_note__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_20'] = x_build_note__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_21'] = x_build_note__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_22'] = x_build_note__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_23'] = x_build_note__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_24'] = x_build_note__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_note__mutmut['x_build_note__mutmut_25'] = x_build_note__mutmut_25 # type: ignore # mutmut generated
