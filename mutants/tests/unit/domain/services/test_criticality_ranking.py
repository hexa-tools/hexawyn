from __future__ import annotations

from hexawyn.domain.models.adaptive_namespace_investigation import (
    RankedFailingResource,
    UnhealthyResourceRef,
)


class TestSelectTopCritical:
    def test_happy_path_selects_top_by_priority_and_restarts(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            select_top_critical,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name="deploy-1", kind="Deployment", reason="CrashLoopBackOff"),
            UnhealthyResourceRef(name="pod-1", kind="Pod", reason="OOMKilled"),
        ]
        restarts = {"pod-1": 10, "deploy-1": 0}
        depth = 5

        ranked, has_more, remaining = select_top_critical(unhealthy, restarts, depth)

        assert len(ranked) == 2  # noqa: PLR2004
        assert ranked[0].name == "deploy-1"
        assert ranked[1].name == "pod-1"
        assert has_more is False
        assert remaining == 0

    def test_empty_unhealthy_returns_empty(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            select_top_critical,
        )

        ranked, has_more, remaining = select_top_critical([], {}, 5)

        assert ranked == []
        assert has_more is False
        assert remaining == 0

    def test_pending_pods_excluded_from_ranking(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            select_top_critical,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name="pending-pod", kind="Pod", reason="Pending"),
            UnhealthyResourceRef(name="good-deploy", kind="Deployment", reason="CrashLoopBackOff"),
        ]
        restarts: dict[str, int] = {}

        ranked, has_more, remaining = select_top_critical(unhealthy, restarts, 5)

        assert len(ranked) == 1
        assert ranked[0].name == "good-deploy"

    def test_terminating_pods_excluded(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            select_top_critical,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name="terminating-pod", kind="Pod", reason="Terminating"),
        ]
        restarts: dict[str, int] = {}

        ranked, has_more, remaining = select_top_critical(unhealthy, restarts, 5)

        assert ranked == []

    def test_unknown_pods_excluded(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            select_top_critical,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name="unknown-pod", kind="Pod", reason="Unknown"),
        ]
        restarts: dict[str, int] = {}

        ranked, has_more, remaining = select_top_critical(unhealthy, restarts, 5)

        assert ranked == []

    def test_depth_limits_results(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            select_top_critical,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name=f"deploy-{i}", kind="Deployment", reason="Error")
            for i in range(10)
        ]
        restarts: dict[str, int] = {}

        ranked, has_more, remaining = select_top_critical(unhealthy, restarts, 3)

        assert len(ranked) == 3  # noqa: PLR2004
        assert has_more is True
        assert remaining == 7  # noqa: PLR2004

    def test_has_more_false_when_exactly_at_depth(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            select_top_critical,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name=f"deploy-{i}", kind="Deployment", reason="Error")
            for i in range(3)
        ]
        restarts: dict[str, int] = {}

        ranked, has_more, remaining = select_top_critical(unhealthy, restarts, 3)

        assert has_more is False
        assert remaining == 0

    def test_deployments_have_priority_over_pods(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            select_top_critical,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name="pod-a", kind="Pod", reason="OOMKilled"),
            UnhealthyResourceRef(name="deploy-a", kind="Deployment", reason="CrashLoopBackOff"),
        ]
        restarts = {"pod-a": 100}

        ranked, _, _ = select_top_critical(unhealthy, restarts, 5)

        assert ranked[0].name == "deploy-a"
        assert ranked[1].name == "pod-a"

    def test_pods_sorted_by_restart_count_descending(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            select_top_critical,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name="pod-low", kind="Pod", reason="OOMKilled"),
            UnhealthyResourceRef(name="pod-high", kind="Pod", reason="OOMKilled"),
        ]
        restarts = {"pod-low": 3, "pod-high": 50}

        ranked, _, _ = select_top_critical(unhealthy, restarts, 5)

        assert ranked[0].name == "pod-high"
        assert ranked[1].name == "pod-low"

    def test_pod_with_missing_restart_count_defaults_to_zero(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            select_top_critical,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name="pod-no-restarts", kind="Pod", reason="OOMKilled"),
        ]
        restarts: dict[str, int] = {}

        ranked, _, _ = select_top_critical(unhealthy, restarts, 5)

        assert ranked[0].restart_count == 0

    def test_rank_assigned_correctly(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            select_top_critical,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name=f"deploy-{i}", kind="Deployment", reason="Error")
            for i in range(5)
        ]
        restarts: dict[str, int] = {}

        ranked, _, _ = select_top_critical(unhealthy, restarts, 5)

        for i, item in enumerate(ranked):
            assert item.rank == i

    def test_same_priority_sorted_by_name(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            select_top_critical,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name="zzz", kind="Deployment", reason="Error"),
            UnhealthyResourceRef(name="aaa", kind="Deployment", reason="Error"),
        ]
        restarts: dict[str, int] = {}

        ranked, _, _ = select_top_critical(unhealthy, restarts, 5)

        assert ranked[0].name == "aaa"
        assert ranked[1].name == "zzz"


class TestDetectNodePressureContext:
    def test_ranked_resources_present_returns_none(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            detect_node_pressure_context,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name="pending-1", kind="Pod", reason="Pending"),
        ]
        ranked = [
            RankedFailingResource(
                name="deploy-1",
                kind="Deployment",
                reason="Error",
                restart_count=0,
                rank=0,
            ),
        ]

        result = detect_node_pressure_context(unhealthy, ranked)

        assert result is None

    def test_no_ranked_with_pending_pods_returns_pressure_note(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            detect_node_pressure_context,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name="pending-1", kind="Pod", reason="Pending"),
            UnhealthyResourceRef(name="pending-2", kind="Pod", reason="Pending"),
            UnhealthyResourceRef(name="ok-deploy", kind="Deployment", reason="Error"),
        ]
        ranked: list[RankedFailingResource] = []

        result = detect_node_pressure_context(unhealthy, ranked)

        assert result is not None
        assert "2 pod(s) pending" in result
        assert "node capacity" in result

    def test_no_ranked_no_pending_returns_none(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            detect_node_pressure_context,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name="all-drilled", kind="Deployment", reason="Error"),
        ]
        ranked: list[RankedFailingResource] = []

        result = detect_node_pressure_context(unhealthy, ranked)

        assert result is None

    def test_empty_unhealthy_and_empty_ranked_returns_none(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            detect_node_pressure_context,
        )

        result = detect_node_pressure_context([], [])

        assert result is None

    def test_only_terminating_pending_unknown_excluded(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
            detect_node_pressure_context,
        )

        unhealthy: list[UnhealthyResourceRef] = [
            UnhealthyResourceRef(name="t1", kind="Pod", reason="Terminating"),
            UnhealthyResourceRef(name="u1", kind="Pod", reason="Unknown"),
        ]
        ranked: list[RankedFailingResource] = []

        result = detect_node_pressure_context(unhealthy, ranked)

        assert result is None
