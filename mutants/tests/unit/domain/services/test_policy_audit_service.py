"""Tests for domain/services/calico/policy_audit_service — coverage gaps."""

from __future__ import annotations

from hexawyn.domain.models.calico import (
    CalicoCoverageGap,
    CalicoNetworkPolicy,
    CalicoWorkload,
)
from hexawyn.domain.services.calico.policy_audit_service import (
    _build_note,
    _is_default_deny,
    _rank_key,
    _status,
    build_calico_policy_audit,
)


def _namespaced_policy(**overrides: object) -> CalicoNetworkPolicy:
    base: dict[str, object] = {
        "name": "np",
        "namespace": "ns1",
        "kind": "CalicoNetworkPolicy",
        "selector": "app=='web'",
        "action": "deny",
        "ingress_rules": ("deny tcp",),
        "egress_rules": (),
        "ingress_rule_count": 1,
        "egress_rule_count": 1,
        "order": 10.0,
        "apply_on_forward": False,
        "has_l7_rule": True,
    }
    base.update(overrides)
    return CalicoNetworkPolicy(**base)  # type: ignore[arg-type]


def _global_policy(**overrides: object) -> CalicoNetworkPolicy:
    base: dict[str, object] = {
        "name": "g-np",
        "namespace": "",
        "kind": "GlobalNetworkPolicy",
        "selector": "all()",
        "action": "deny",
        "ingress_rules": ("deny",),
        "egress_rules": ("deny",),
        "ingress_rule_count": 1,
        "egress_rule_count": 1,
        "order": 10.0,
        "apply_on_forward": False,
        "has_l7_rule": True,
    }
    base.update(overrides)
    return CalicoNetworkPolicy(**base)  # type: ignore[arg-type]


def _workload(namespace: str, pods: int) -> CalicoWorkload:
    return CalicoWorkload(namespace=namespace, pod_count=pods)


def _expected_gap(  # noqa: PLR0913
    *,
    namespace: str,
    workload_count: int,
    policy_count: int,
    issue: str,
    network_status: str,
    risk_level: str,
    selectors: list[str],
    note: str,
) -> CalicoCoverageGap:
    return CalicoCoverageGap(
        namespace=namespace,
        workload_count=workload_count,
        policy_count=policy_count,
        issue=issue,
        network_status=network_status,
        risk_level=risk_level,
        selectors=selectors,
        note=note,
    )


class TestBuildCalicoPolicyAudit:
    def test_gap_when_no_policy_full_payload(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 3)],
            policies=[],
            excluded_namespaces=[],
        )
        assert result.installed is True
        assert result.not_installed_marker is None
        assert result.total_namespaces_checked == 1  # noqa: PLR2004
        assert result.gap_count == 1  # noqa: PLR2004
        assert result.summary == "1 namespace(s) have Calico L3/L4 coverage gaps out of 1 checked."
        assert result.error is None
        assert result.findings[0] == _expected_gap(
            namespace="ns1",
            workload_count=3,
            policy_count=0,
            issue="no_policy",
            network_status="open",
            risk_level="critical",
            selectors=[],
            note="No Calico policy restricts 3 workload(s) in namespace 'ns1'",
        )

    def test_fully_covered_no_gap(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2)],
            policies=[_namespaced_policy(namespace="ns1")],
            excluded_namespaces=[],
        )
        assert result.gap_count == 0
        assert result.findings == []
        assert result.summary == "No Calico L3/L4 coverage gaps out of 1 namespace(s) checked."

    def test_l7_gap_when_restricted_without_l7(self) -> None:
        policy = _namespaced_policy(namespace="ns1", has_l7_rule=False)
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2)],
            policies=[policy],
            excluded_namespaces=[],
        )
        assert result.gap_count == 1  # noqa: PLR2004
        assert result.summary == "1 namespace(s) have Calico L3/L4 coverage gaps out of 1 checked."
        assert result.findings[0] == _expected_gap(
            namespace="ns1",
            workload_count=2,
            policy_count=1,
            issue="l7_gap",
            network_status="restricted",
            risk_level="low",
            selectors=["app=='web'"],
            note="L3/L4 default-deny present but no L7 (HTTP/TLS) rule for 2 workload(s)",
        )

    def test_no_default_deny_partially_restricted(self) -> None:
        policy = _namespaced_policy(
            namespace="ns1", action="allow", egress_rule_count=0, has_l7_rule=False
        )
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2)],
            policies=[policy],
            excluded_namespaces=[],
        )
        assert result.gap_count == 1  # noqa: PLR2004
        assert result.findings[0] == _expected_gap(
            namespace="ns1",
            workload_count=2,
            policy_count=1,
            issue="no_default_deny",
            network_status="partially_restricted",
            risk_level="medium",
            selectors=["app=='web'"],
            note=("Partial L3/L4 coverage; no default-deny (deny rule) present for 2 workload(s)"),
        )

    def test_egress_only_policy_is_partially_restricted(self) -> None:
        policy = _namespaced_policy(
            namespace="ns1",
            action="allow",
            ingress_rule_count=0,
            ingress_rules=(),
            egress_rule_count=1,
            egress_rules=("allow egress",),
            has_l7_rule=False,
        )
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2)],
            policies=[policy],
            excluded_namespaces=[],
        )
        assert result.gap_count == 1  # noqa: PLR2004
        assert result.findings[0].network_status == "partially_restricted"
        assert result.findings[0].issue == "no_default_deny"

    def test_ingress_only_policy_is_partially_restricted(self) -> None:
        policy = _namespaced_policy(
            namespace="ns1",
            action="allow",
            ingress_rule_count=1,
            ingress_rules=("allow tcp",),
            egress_rule_count=0,
            egress_rules=(),
            has_l7_rule=False,
        )
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2)],
            policies=[policy],
            excluded_namespaces=[],
        )
        assert result.findings[0].network_status == "partially_restricted"

    def test_allow_policy_single_rule_is_open(self) -> None:
        policy = _namespaced_policy(
            namespace="ns1",
            action="allow",
            ingress_rule_count=0,
            ingress_rules=(),
            egress_rule_count=0,
            egress_rules=(),
            has_l7_rule=False,
        )
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2)],
            policies=[policy],
            excluded_namespaces=[],
        )
        assert result.gap_count == 1  # noqa: PLR2004
        assert result.findings[0].network_status == "open"
        assert result.findings[0].risk_level == "critical"

    def test_policy_without_rules_is_open_gap(self) -> None:
        policy = _namespaced_policy(
            namespace="ns1",
            action="allow",
            ingress_rule_count=0,
            egress_rule_count=0,
            has_l7_rule=False,
        )
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2)],
            policies=[policy],
            excluded_namespaces=[],
        )
        assert result.gap_count == 1  # noqa: PLR2004
        gap = result.findings[0]
        assert gap.network_status == "open"
        assert gap.issue == "no_default_deny"
        assert gap.risk_level == "critical"

    def test_broad_global_default_deny_covers_all(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 1)],
            policies=[_global_policy()],
            excluded_namespaces=[],
        )
        assert result.gap_count == 0

    def test_mixed_action_global_counts_as_default_deny(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2)],
            policies=[_global_policy(action="mixed")],
            excluded_namespaces=[],
        )
        assert result.gap_count == 0

    def test_non_broad_global_not_applied(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2)],
            policies=[_global_policy(selector="app=='kube-dns'")],
            excluded_namespaces=[],
        )
        assert result.gap_count == 1  # noqa: PLR2004
        assert result.findings[0].issue == "no_policy"

    def test_system_namespaces_excluded_by_default(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("kube-system", 5), _workload("ns1", 2)],
            policies=[],
        )
        assert result.total_namespaces_checked == 1  # noqa: PLR2004
        assert result.findings[0].namespace == "ns1"

    def test_custom_exclusion_replaces_not_adds_to_defaults(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("kube-system", 5), _workload("team-x", 2)],
            policies=[],
            excluded_namespaces=("team-x",),
        )
        assert result.total_namespaces_checked == 1  # noqa: PLR2004
        assert result.findings[0].namespace == "kube-system"

    def test_empty_workloads(self) -> None:
        result = build_calico_policy_audit(
            workloads=[], policies=[_namespaced_policy()], excluded_namespaces=[]
        )
        assert result.gap_count == 0
        assert result.findings == []

    def test_zero_pod_namespace_skipped(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 0)], policies=[], excluded_namespaces=[]
        )
        assert result.total_namespaces_checked == 0
        assert result.gap_count == 0

    def test_ranking_critical_before_medium(self) -> None:
        medium = _namespaced_policy(
            namespace="nsM",
            action="allow",
            ingress_rule_count=1,
            ingress_rules=("allow tcp",),
            egress_rule_count=0,
            egress_rules=(),
            has_l7_rule=False,
        )
        result = build_calico_policy_audit(
            workloads=[_workload("nsC", 1), _workload("nsM", 4)],
            policies=[medium],
            excluded_namespaces=[],
        )
        order = [gap.namespace for gap in result.findings]
        assert order == ["nsC", "nsM"]

    def test_ranking_by_workload_count_within_risk(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("small", 1), _workload("large", 9)],
            policies=[],
            excluded_namespaces=[],
        )
        assert result.findings[0].namespace == "large"
        assert result.findings[0].workload_count == 9  # noqa: PLR2004

    def test_overlapping_selectors_not_duplicated(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2)],
            policies=[
                _namespaced_policy(namespace="ns1"),
                _namespaced_policy(namespace="ns1", name="np2"),
            ],
            excluded_namespaces=[],
        )
        assert result.gap_count == 0


class TestStatusDirect:
    def test_no_applicable_open(self) -> None:
        assert _status([], has_default_deny=False, has_ingress=False, has_egress=False) == "open"

    def test_default_deny_restricted(self) -> None:
        assert _status([_namespaced_policy()], True, True, True) == "restricted"

    def test_default_deny_restricted_even_without_rules(self) -> None:
        assert _status([_namespaced_policy()], True, False, False) == "restricted"

    def test_ingress_only_partially_restricted(self) -> None:
        assert _status([_namespaced_policy()], False, True, False) == "partially_restricted"

    def test_egress_only_partially_restricted(self) -> None:
        assert _status([_namespaced_policy()], False, False, True) == "partially_restricted"

    def test_no_rules_open(self) -> None:
        assert _status([_namespaced_policy()], False, False, False) == "open"


class TestIsDefaultDenyDirect:
    def test_deny_true(self) -> None:
        assert _is_default_deny(_namespaced_policy(action="deny")) is True

    def test_mixed_true(self) -> None:
        assert _is_default_deny(_namespaced_policy(action="mixed")) is True

    def test_allow_false(self) -> None:
        assert _is_default_deny(_namespaced_policy(action="allow")) is False

    def test_none_action_false(self) -> None:
        assert _is_default_deny(_namespaced_policy(action=None)) is False


class TestBuildNoteDirect:
    def test_no_policy_note(self) -> None:
        note = _build_note("no_policy", "ns1", 3)
        assert note == "No Calico policy restricts 3 workload(s) in namespace 'ns1'"

    def test_no_default_deny_note(self) -> None:
        note = _build_note("no_default_deny", "ns1", 2)
        assert (
            note == "Partial L3/L4 coverage; no default-deny (deny rule) present for 2 workload(s)"
        )

    def test_l7_gap_note(self) -> None:
        note = _build_note("l7_gap", "ns1", 4)
        assert note == "L3/L4 default-deny present but no L7 (HTTP/TLS) rule for 4 workload(s)"

    def test_unknown_issue_falls_back_l7_note(self) -> None:
        note = _build_note("whatever", "ns1", 1)
        assert note == "L3/L4 default-deny present but no L7 (HTTP/TLS) rule for 1 workload(s)"


class TestRankKeyDirect:
    def _gap(self, risk: str, workload_count: int) -> CalicoCoverageGap:
        return CalicoCoverageGap(
            namespace="ns",
            workload_count=workload_count,
            policy_count=1,
            issue="no_policy",
            network_status="open",
            risk_level=risk,
            selectors=[],
            note=None,
        )

    def test_critical_first(self) -> None:
        assert _rank_key(self._gap("critical", 1)) == (0, -1)

    def test_medium_second(self) -> None:
        assert _rank_key(self._gap("medium", 2)) == (1, -2)

    def test_low_third(self) -> None:
        assert _rank_key(self._gap("low", 3)) == (2, -3)

    def test_unknown_risk_defaults_to_low(self) -> None:
        assert _rank_key(self._gap("unknown", 4)) == (2, -4)
