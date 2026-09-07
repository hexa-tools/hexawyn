"""Tests for domain/services/calico/segmentation_service — reachability matrix."""

from __future__ import annotations

from hexawyn.domain.models.calico import (
    CalicoNetworkPolicy,
    CalicoSegmentationAuditResult,
    CalicoSegmentationEdge,
    CalicoWorkload,
)
from hexawyn.domain.services.calico.segmentation_service import (
    _edge_selectors,
    _summary,
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


def _assert_result_full_payload(
    result: CalicoSegmentationAuditResult,
    *,
    tiers: list[str],
    edges: list[CalicoSegmentationEdge],
    summary: str,
) -> None:
    assert result.installed is True
    assert result.not_installed_marker is None
    assert result.view == "calico"
    assert result.tiers == tiers
    assert result.edges == edges
    assert result.gap_count == sum(1 for edge in edges if not edge.restricted)
    assert result.total_paths == len(edges)
    assert result.summary == summary
    assert result.error is None


class TestBuildCalicoSegmentationAudit:
    def test_gap_without_policies_full_payload(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 3), _workload("ns2", 2)],
            policies=[],
            excluded_namespaces=[],
        )
        _assert_result_full_payload(
            result,
            tiers=["ns1", "ns2"],
            edges=[
                CalicoSegmentationEdge(
                    source="ns1",
                    destination="ns2",
                    restricted=False,
                    selectors=[],
                    note=(
                        "Allowed by default (no Calico default-deny on 'ns1' egress or "
                        "'ns2' ingress)"
                    ),
                ),
                CalicoSegmentationEdge(
                    source="ns2",
                    destination="ns1",
                    restricted=False,
                    selectors=[],
                    note=(
                        "Allowed by default (no Calico default-deny on 'ns2' egress or "
                        "'ns1' ingress)"
                    ),
                ),
            ],
            summary="2 of 2 tier-to-tier paths are allowed without a Calico default-deny.",
        )

    def test_fully_segmented_namespaced_default_deny(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 2)],
            policies=[
                _policy(namespace="ns1"),
                _policy(namespace="ns2", name="np2"),
            ],
            excluded_namespaces=[],
        )
        _assert_result_full_payload(
            result,
            tiers=["ns1", "ns2"],
            edges=[
                CalicoSegmentationEdge(
                    source="ns1",
                    destination="ns2",
                    restricted=True,
                    selectors=["app=='web'"],
                    note=None,
                ),
                CalicoSegmentationEdge(
                    source="ns2",
                    destination="ns1",
                    restricted=True,
                    selectors=["app=='web'"],
                    note=None,
                ),
            ],
            summary="No unrestricted tier-to-tier paths out of 2.",
        )

    def test_distinct_destination_selector_included(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 2)],
            policies=[
                _policy(namespace="ns1", selector="app=='web'"),
                _policy(namespace="ns2", name="np2", selector="app=='db'"),
            ],
            excluded_namespaces=[],
        )
        edge = next(edge for edge in result.edges if edge.source == "ns1")
        assert edge.selectors == ["app=='web'", "app=='db'"]

    def test_partial_deny_only_one_tier(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 2)],
            policies=[_policy(namespace="ns1")],
            excluded_namespaces=[],
        )
        edge_out = next(edge for edge in result.edges if edge.source == "ns2")
        edge_in = next(edge for edge in result.edges if edge.source == "ns1")
        assert edge_out.restricted is True  # destination ns1 denies ingress
        assert edge_in.restricted is True  # source ns1 denies egress
        assert result.gap_count == 0

    def test_global_default_deny_covers_all_tiers(self) -> None:
        global_policy = _policy(
            name="g-np",
            namespace="",
            kind="GlobalNetworkPolicy",
            selector="all()",
        )
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 1)],
            policies=[global_policy],
            excluded_namespaces=[],
        )
        assert result.gap_count == 0
        assert all(edge.restricted for edge in result.edges)
        assert result.summary == "No unrestricted tier-to-tier paths out of 2."

    def test_global_policy_not_broad_not_applied(self) -> None:
        global_policy = _policy(
            name="g-np",
            namespace="",
            kind="GlobalNetworkPolicy",
            selector="app=='dns'",
        )
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 1)],
            policies=[global_policy],
            excluded_namespaces=[],
        )
        assert result.gap_count == 2  # noqa: PLR2004

    def test_allow_all_namespace_selectors_in_edge(self) -> None:
        allow_all = _policy(namespace="ns1", action="allow", name="allow-all")
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 2), _workload("ns2", 1)],
            policies=[allow_all],
            excluded_namespaces=[],
        )
        edge = next(edge for edge in result.edges if edge.source == "ns1")
        assert edge.restricted is False
        assert edge.selectors == ["app=='web'"]
        assert edge.note is not None

    def test_no_workloads_empty_matrix_full_payload(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[], policies=[_policy()], excluded_namespaces=[]
        )
        _assert_result_full_payload(
            result,
            tiers=[],
            edges=[],
            summary="No workload tiers to audit.",
        )

    def test_only_system_namespace_uses_default_exclusion(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[_workload("kube-system", 5)],
            policies=[],
        )
        _assert_result_full_payload(
            result,
            tiers=[],
            edges=[],
            summary="No workload tiers to audit.",
        )

    def test_custom_exclusion_replaces_defaults(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[_workload("kube-system", 5), _workload("team-x", 2)],
            policies=[],
            excluded_namespaces=("team-x",),
        )
        assert result.tiers == ["kube-system"]

    def test_zero_pod_tier_skipped(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[_workload("ns1", 0), _workload("ns2", 2)],
            policies=[],
            excluded_namespaces=[],
        )
        assert result.tiers == ["ns2"]

    def test_three_tiers_path_count(self) -> None:
        result = build_calico_segmentation_audit(
            workloads=[_workload("a", 1), _workload("b", 1), _workload("c", 1)],
            policies=[],
            excluded_namespaces=[],
        )
        assert result.total_paths == 6  # noqa: PLR2004
        assert result.gap_count == 6  # noqa: PLR2004


class TestEdgeSelectorsDirect:
    def _policy(self, namespace: str, selector: str) -> CalicoNetworkPolicy:
        return _policy(namespace=namespace, selector=selector)

    def test_source_destination_and_global_combined(self) -> None:
        ns_policies = {
            "ns1": [self._policy("ns1", "a=='1'")],
            "ns2": [self._policy("ns2", "b=='2'")],
        }
        globals_ = [self._policy("", "c=='3'")]
        assert _edge_selectors("ns1", "ns2", ns_policies, globals_) == [
            "a=='1'",
            "b=='2'",
            "c=='3'",
        ]

    def test_destination_missing_policy_skipped(self) -> None:
        ns_policies = {"ns1": [self._policy("ns1", "a=='1'")]}
        assert _edge_selectors("ns1", "ns2", ns_policies, []) == ["a=='1'"]

    def test_duplicate_selector_deduplicated(self) -> None:
        ns_policies = {
            "ns1": [
                _policy(namespace="ns1", selector="a=='1'"),
                _policy(namespace="ns1", selector="a=='1'", name="np2"),
            ]
        }
        assert _edge_selectors("ns1", "ns2", ns_policies, []) == ["a=='1'"]

    def test_empty_selector_skipped(self) -> None:
        ns_policies = {"ns1": [self._policy("ns1", "")]}
        assert _edge_selectors("ns1", "ns2", ns_policies, []) == []

    def test_global_empty_selector_skipped(self) -> None:
        globals_ = [self._policy("", "")]
        assert _edge_selectors("ns1", "ns2", {}, globals_) == []


class TestSummaryDirect:
    def test_zero_gaps(self) -> None:
        assert _summary(0, 4) == "No unrestricted tier-to-tier paths out of 4."

    def test_all_gaps(self) -> None:
        assert (
            _summary(4, 4) == "4 of 4 tier-to-tier paths are allowed without a Calico default-deny."
        )

    def test_partial_gaps(self) -> None:
        assert (
            _summary(2, 6) == "2 of 6 tier-to-tier paths are allowed without a Calico default-deny."
        )
