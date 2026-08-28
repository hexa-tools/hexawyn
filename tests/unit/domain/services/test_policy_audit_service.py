"""Tests for domain/services/calico/policy_audit_service — coverage gaps."""

from __future__ import annotations

from hexawyn.domain.models.calico import (
    CalicoNetworkPolicy,
    CalicoWorkload,
)
from hexawyn.domain.services.calico.policy_audit_service import (
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


def _workload(namespace: str, pods: int) -> CalicoWorkload:
    return CalicoWorkload(namespace=namespace, pod_count=pods)


class TestBuildCalicoPolicyAudit:
    def test_gap_when_no_policy(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 3)],
            policies=[],
            excluded_namespaces=[],
        )
        assert result.installed is True
        assert result.total_namespaces_checked == 1  # noqa: PLR2004
        assert result.gap_count == 1  # noqa: PLR2004
        gap = result.findings[0]
        assert gap.namespace == "ns1"
        assert gap.issue == "no_policy"
        assert gap.network_status == "open"
        assert gap.risk_level == "critical"
        assert gap.selectors == []

    def test_fully_covered_no_gap(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2)],
            policies=[_namespaced_policy(namespace="ns1")],
            excluded_namespaces=[],
        )
        assert result.gap_count == 0
        assert result.findings == []

    def test_l7_gap_when_restricted_without_l7(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2)],
            policies=[_namespaced_policy(namespace="ns1", has_l7_rule=False)],
            excluded_namespaces=[],
        )
        assert result.gap_count == 1  # noqa: PLR2004
        assert result.findings[0].issue == "l7_gap"
        assert result.findings[0].network_status == "restricted"

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
        gap = result.findings[0]
        assert gap.issue == "no_default_deny"
        assert gap.network_status == "partially_restricted"
        assert gap.risk_level == "medium"

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
        global_policy = CalicoNetworkPolicy(
            name="g-np",
            namespace="",
            kind="GlobalNetworkPolicy",
            selector="all()",
            action="deny",
            ingress_rules=("deny",),
            egress_rules=("deny",),
            ingress_rule_count=1,
            egress_rule_count=1,
            order=10.0,
            apply_on_forward=False,
            has_l7_rule=True,
        )
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 1)],
            policies=[global_policy],
            excluded_namespaces=[],
        )
        assert result.gap_count == 0

    def test_system_namespaces_excluded(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("kube-system", 5)],
            policies=[],
            excluded_namespaces=("kube-system",),
        )
        assert result.total_namespaces_checked == 0
        assert result.gap_count == 0

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
        medium = CalicoNetworkPolicy(
            name="np",
            namespace="nsM",
            kind="CalicoNetworkPolicy",
            selector="app=='web'",
            action="allow",
            ingress_rules=("allow tcp",),
            egress_rules=(),
            ingress_rule_count=1,
            egress_rule_count=0,
            order=10.0,
            apply_on_forward=False,
            has_l7_rule=False,
        )
        result = build_calico_policy_audit(
            workloads=[_workload("nsC", 1), _workload("nsM", 4)],
            policies=[medium],
            excluded_namespaces=[],
        )
        order = [gap.namespace for gap in result.findings]
        assert order == ["nsC", "nsM"]  # critical (no policy) before medium (no default deny)

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

    def test_summary_reflects_gaps(self) -> None:
        result = build_calico_policy_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 1)],
            policies=[_namespaced_policy(namespace="ns1")],
            excluded_namespaces=[],
        )
        assert result.summary is not None
        assert "1" in result.summary
