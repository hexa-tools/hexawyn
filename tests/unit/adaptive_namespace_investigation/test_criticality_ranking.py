"""Unit tests for select_top_critical / detect_node_pressure_context — pure
criticality ranking and selection logic."""

from __future__ import annotations

from hexawyn.domain.models.adaptive_namespace_investigation import (
    RankedFailingResource,
    UnhealthyResourceRef,
)
from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
    detect_node_pressure_context,
    select_top_critical,
)


class TestSelectTopCritical:
    def test_skips_pending_even_with_depth_to_spare(self) -> None:
        """TC1: 2 pods CrashLoopBackOff, 1 pending, default depth=3 → drills
        into the 2 CrashLoop pods, skips pending."""
        unhealthy = [
            UnhealthyResourceRef(name="pod-a", kind="Pod", reason="CrashLoopBackOff"),
            UnhealthyResourceRef(name="pod-b", kind="Pod", reason="CrashLoopBackOff"),
            UnhealthyResourceRef(name="pod-c", kind="Pod", reason="Pending"),
        ]
        restart_counts = {"pod-a": 10, "pod-b": 5, "pod-c": 0}

        ranked, has_more, remaining = select_top_critical(unhealthy, restart_counts, depth=3)

        assert [r.name for r in ranked] == ["pod-a", "pod-b"]
        assert has_more is False
        assert remaining == 0

    def test_no_failing_resources_returns_empty(self) -> None:
        """TC2: no failing resources → no drill-down."""
        ranked, has_more, remaining = select_top_critical([], {}, depth=3)

        assert ranked == []
        assert has_more is False
        assert remaining == 0

    def test_depth_one_limits_to_top_resource(self) -> None:
        """TC3: depth=1 → only the top-ranked resource investigated."""
        unhealthy = [
            UnhealthyResourceRef(name="pod-a", kind="Pod", reason="CrashLoopBackOff"),
            UnhealthyResourceRef(name="pod-b", kind="Pod", reason="CrashLoopBackOff"),
        ]
        restart_counts = {"pod-a": 45, "pod-b": 12}

        ranked, has_more, remaining = select_top_critical(unhealthy, restart_counts, depth=1)

        assert len(ranked) == 1
        assert ranked[0].name == "pod-a"
        assert has_more is True
        assert remaining == 1

    def test_ranks_by_restart_count_descending(self) -> None:
        """Checker edge case: CrashLoop (45 restarts) must outrank OOMKilled
        (12 restarts)."""
        unhealthy = [
            UnhealthyResourceRef(name="auth-pod-xyz", kind="Pod", reason="OOMKilled"),
            UnhealthyResourceRef(name="payment-pod-abc", kind="Pod", reason="CrashLoopBackOff"),
        ]
        restart_counts = {"auth-pod-xyz": 12, "payment-pod-abc": 45}

        ranked, _, _ = select_top_critical(unhealthy, restart_counts, depth=3)

        assert [r.name for r in ranked] == ["payment-pod-abc", "auth-pod-xyz"]
        assert ranked[0].restart_count == 45
        assert ranked[1].restart_count == 12

    def test_deployment_ranked_before_pod(self) -> None:
        unhealthy = [
            UnhealthyResourceRef(name="pod-a", kind="Pod", reason="CrashLoopBackOff"),
            UnhealthyResourceRef(
                name="checkout-deploy", kind="Deployment", reason="0/2 replicas ready"
            ),
        ]
        restart_counts = {"pod-a": 100}

        ranked, _, _ = select_top_critical(unhealthy, restart_counts, depth=3)

        assert ranked[0].name == "checkout-deploy"
        assert ranked[0].restart_count == 0

    def test_fifty_failing_pods_capped_to_depth_default(self) -> None:
        """TC5: 50 failing pods, depth=3 → only top 3 investigated."""
        unhealthy = [
            UnhealthyResourceRef(name=f"pod-{i}", kind="Pod", reason="CrashLoopBackOff")
            for i in range(50)
        ]
        restart_counts = {f"pod-{i}": i for i in range(50)}

        ranked, has_more, remaining = select_top_critical(unhealthy, restart_counts, depth=3)

        assert len(ranked) == 3
        assert has_more is True
        assert remaining == 47
        assert ranked[0].name == "pod-49"

    def test_terminating_and_unknown_pods_excluded(self) -> None:
        unhealthy = [
            UnhealthyResourceRef(name="pod-a", kind="Pod", reason="Terminating"),
            UnhealthyResourceRef(name="pod-b", kind="Pod", reason="Unknown"),
        ]

        ranked, _, _ = select_top_critical(unhealthy, {}, depth=3)

        assert ranked == []


class TestDetectNodePressureContext:
    def test_all_pending_flags_node_pressure(self) -> None:
        unhealthy = [
            UnhealthyResourceRef(name="pod-a", kind="Pod", reason="Pending"),
            UnhealthyResourceRef(name="pod-b", kind="Pod", reason="Pending"),
        ]

        context = detect_node_pressure_context(unhealthy, [])

        assert context is not None
        assert "2" in context

    def test_no_context_when_resources_were_drilled(self) -> None:
        unhealthy = [UnhealthyResourceRef(name="pod-a", kind="Pod", reason="Pending")]
        ranked = [
            RankedFailingResource(
                name="pod-b", kind="Pod", reason="CrashLoopBackOff", restart_count=5, rank=0
            )
        ]

        context = detect_node_pressure_context(unhealthy, ranked)

        assert context is None

    def test_no_context_when_nothing_pending(self) -> None:
        context = detect_node_pressure_context([], [])

        assert context is None
