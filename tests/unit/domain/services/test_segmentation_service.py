"""Tests for domain/services/calico/segmentation_service — reachability matrix."""

from __future__ import annotations

from hexawyn.domain.models.calico import CalicoNetworkPolicy, CalicoWorkload
from hexawyn.domain.services.calico.segmentation_service import (
    build_calico_segmentation_audit,
)


def _policy(**overrides: object) -> CalicoNetworkPolicy:
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


class TestBuildCalicoSegmentationAudit:
    def test_gap_found_without_policies(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 3), _workload("ns2", 2)],
            policies=[],
            excluded_namespaces=[],
        )
        assert result.installed is True
        assert result.view == "calico"
        assert result.tiers == ["ns1", "ns2"]
        assert result.total_paths == 2  # noqa: PLR2004
        assert result.gap_count == 2  # noqa: PLR2004
        assert all(not edge.restricted for edge in result.edges)

    def test_fully_segmented_namespaced_default_deny_each_side(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 2)],
            policies=[
                _policy(namespace="ns1"),
                _policy(namespace="ns2", name="np2"),
            ],
            excluded_namespaces=[],
        )
        assert result.gap_count == 0
        assert all(edge.restricted for edge in result.edges)

    def test_global_default_deny_covers_all_tiers(self) -> None:
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
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 1)],
            policies=[global_policy],
            excluded_namespaces=[],
        )
        assert result.gap_count == 0
        assert all(edge.restricted for edge in result.edges)

    def test_partial_allow_all_in_namespace_flagged_as_broad(self) -> None:
        allow_all = _policy(namespace="ns1", action="allow", name="allow-all")
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 1)],
            policies=[allow_all],
            excluded_namespaces=[],
        )
        assert result.gap_count == 2  # noqa: PLR2004
        edge = next(e for e in result.edges if e.source == "ns1")
        assert edge.restricted is False
        assert "app=='web'" in edge.selectors

    def test_no_workloads_empty_matrix(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[], policies=[_policy()], excluded_namespaces=[]
        )
        assert result.tiers == []
        assert result.edges == []
        assert result.gap_count == 0
        assert result.total_paths == 0

    def test_system_namespaces_excluded(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[_workload("kube-system", 5), _workload("ns1", 2)],
            policies=[],
            excluded_namespaces=("kube-system",),
        )
        assert result.tiers == ["ns1"]

    def test_overlapping_selectors_not_duplicated(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 1)],
            policies=[_policy(namespace="ns2"), _policy(namespace="ns2", name="np2")],
            excluded_namespaces=[],
        )
        assert result.gap_count == 0
        sources = [edge.source for edge in result.edges]
        assert len(sources) == len(set(sources))

    def test_malformed_selector_reported_raw(self) -> None:
        broken = _policy(namespace="ns1", selector="--- broken")
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 1)],
            policies=[broken],
            excluded_namespaces=[],
        )
        assert all("--- broken" in edge.selectors for edge in result.edges if edge.source == "ns1")

    def test_summary_reflects_gaps(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 1)],
            policies=[],
            excluded_namespaces=[],
        )
        assert result.summary is not None
        assert "2" in result.summary
