"""Unit tests for analyze_hot_nodes — pure orchestration of hot detection,
top-consumer selection, redistribution feasibility, and recommendation."""

from __future__ import annotations

from hexawyn.domain.models.hot_node_analysis import (
    ClusterNodeSnapshot,
    HotNodeAnalysisRequest,
    TopConsumer,
)
from hexawyn.domain.services.hot_node_analysis.node_analysis_builder import analyze_hot_nodes


def _consumer(name: str, cpu: float, memory: float = 1.0) -> TopConsumer:
    return TopConsumer(
        pod_name=name, namespace="production", cpu_usage_cores=cpu, memory_usage_gb=memory
    )


def _hourly_series(value: float, hours: int = 24) -> list[tuple[str, float]]:
    return [(f"2026-06-17T{h % 24:02d}:00:00Z", value) for h in range(hours)]


def _hot_cpu_series(
    hot_hours: int = 20, hot_value: float = 92.0, cool_value: float = 50.0
) -> list[tuple[str, float]]:
    return _hourly_series(hot_value, hot_hours) + _hourly_series(cool_value, 24 - hot_hours)


def _node(  # noqa: PLR0913
    name: str,
    cordoned: bool = False,
    allocatable_cpu: float = 8.0,
    allocatable_memory: float = 32.0,
    cpu_series: list[tuple[str, float]] | None = None,
    memory_series: list[tuple[str, float]] | None = None,
    pods: list[TopConsumer] | None = None,
) -> ClusterNodeSnapshot:
    return ClusterNodeSnapshot(
        node_name=name,
        cordoned=cordoned,
        allocatable_cpu_cores=allocatable_cpu,
        allocatable_memory_gb=allocatable_memory,
        cpu_percent_series=cpu_series if cpu_series is not None else _hourly_series(50.0),
        memory_percent_series=memory_series if memory_series is not None else _hourly_series(50.0),
        pods=pods or [],
    )


class TestHotNodeDetectionAndRedistribution:
    def test_tc1_hot_node_triggers_redistribution_check(self) -> None:
        """TC1: worker-1 CPU 92% for 20/24h → hot, redistribution triggered."""
        worker1 = _node("worker-1", cpu_series=_hot_cpu_series())
        worker3 = _node("worker-3")

        report = analyze_hot_nodes(HotNodeAnalysisRequest(), [worker1, worker3])

        assert len(report.hot_nodes) == 1
        assert report.hot_nodes[0].node_name == "worker-1"
        assert report.hot_nodes[0].cpu_hot is True

    def test_tc2_partial_redistribution_is_recommended(self) -> None:
        """TC2: worker-1 has 3 large pods, worker-3 has capacity for 2 →
        redistribute recommended."""
        worker1_pods = [_consumer("pod-a", 1.0), _consumer("pod-b", 1.0), _consumer("pod-c", 1.0)]
        worker1 = _node("worker-1", cpu_series=_hot_cpu_series(), pods=worker1_pods)
        worker3 = _node(
            "worker-3",
            allocatable_cpu=10.0,
            pods=[_consumer("worker-3-existing", 8.0)],
        )

        report = analyze_hot_nodes(HotNodeAnalysisRequest(), [worker1, worker3])

        hot = report.hot_nodes[0]
        assert hot.recommendation == "redistribute"
        assert hot.feasible_redistribution is True
        assert hot.target_node == "worker-3"

    def test_tc3_all_nodes_hot_recommends_add_node(self) -> None:
        """TC3: all nodes above 80% → add node, redistribution not feasible."""
        pods = [_consumer("pod-a", 1.0), _consumer("pod-b", 1.0)]
        worker1 = _node("worker-1", cpu_series=_hot_cpu_series(), pods=pods)
        worker2 = _node("worker-2", cpu_series=_hot_cpu_series(), pods=pods)

        report = analyze_hot_nodes(HotNodeAnalysisRequest(), [worker1, worker2])

        assert len(report.hot_nodes) == 2  # noqa: PLR2004
        for hot in report.hot_nodes:
            assert hot.feasible_redistribution is False
            assert hot.recommendation == "add_node"

    def test_tc4_no_hot_nodes_is_all_healthy(self) -> None:
        """TC4: no hot nodes → all nodes healthy summary."""
        worker1 = _node("worker-1")
        worker2 = _node("worker-2")

        report = analyze_hot_nodes(HotNodeAnalysisRequest(), [worker1, worker2])

        assert report.hot_nodes == []
        assert report.healthy_node_count == 2  # noqa: PLR2004
        assert "healthy" in report.summary.lower()

    def test_tc5_cpu_hot_memory_fine_is_disclosed_independently(self) -> None:
        """TC5: 85% CPU but 30% memory → CPU-hot, memory fine."""
        worker1 = _node(
            "worker-1",
            cpu_series=_hourly_series(85.0),
            memory_series=_hourly_series(30.0),
        )
        worker2 = _node("worker-2")

        report = analyze_hot_nodes(HotNodeAnalysisRequest(), [worker1, worker2])

        hot = report.hot_nodes[0]
        assert hot.cpu_hot is True
        assert hot.memory_hot is False


class TestCordonedNodeExclusion:
    def test_cordoned_node_excluded_from_analysis(self) -> None:
        cordoned = _node("worker-maintenance", cordoned=True, cpu_series=_hot_cpu_series())
        healthy = _node("worker-2")

        report = analyze_hot_nodes(HotNodeAnalysisRequest(), [cordoned, healthy])

        assert report.excluded_cordoned_nodes == ["worker-maintenance"]
        assert report.hot_nodes == []
        assert report.healthy_node_count == 1


class TestMissingMetricsExclusion:
    def test_node_with_no_series_excluded_with_warning(self) -> None:
        missing_metrics = _node("worker-kubelet-issue", cpu_series=[], memory_series=[])
        healthy = _node("worker-2")

        report = analyze_hot_nodes(HotNodeAnalysisRequest(), [missing_metrics, healthy])

        assert report.hot_nodes == []
        assert report.healthy_node_count == 1
        assert any("worker-kubelet-issue" in warning for warning in report.warnings)

    def test_summary_mentions_warnings_alongside_hot_nodes(self) -> None:
        missing_metrics = _node("worker-kubelet-issue", cpu_series=[], memory_series=[])
        hot = _node("worker-1", cpu_series=_hot_cpu_series())

        report = analyze_hot_nodes(HotNodeAnalysisRequest(), [missing_metrics, hot])

        assert len(report.hot_nodes) == 1
        assert "excluded due to missing metrics" in report.summary


class TestZeroTotalPodUsage:
    def test_zero_total_cpu_usage_is_not_a_dominant_pod(self) -> None:
        """Edge case: pods present but reporting zero CPU usage (e.g. idle) —
        must not be treated as a single-dominant-pod pattern."""
        idle_pods = [_consumer("idle-a", 0.0), _consumer("idle-b", 0.0)]
        worker1 = _node("worker-1", cpu_series=_hot_cpu_series(), pods=idle_pods)
        worker2 = _node("worker-2", cpu_series=_hot_cpu_series())

        report = analyze_hot_nodes(HotNodeAnalysisRequest(), [worker1, worker2])

        hot = report.hot_nodes[0]
        assert hot.recommendation == "add_node"


class TestDaemonSetOnlyNode:
    def test_hot_node_with_no_redistribution_candidates_falls_through(self) -> None:
        """Edge case: DaemonSet-only node — pods already filtered to empty
        upstream, so redistribution has nothing to move and no single
        dominant pod to scale, falling through to add_node."""
        worker1 = _node("worker-1", cpu_series=_hot_cpu_series(), pods=[])
        worker2 = _node("worker-2")

        report = analyze_hot_nodes(HotNodeAnalysisRequest(), [worker1, worker2])

        hot = report.hot_nodes[0]
        assert hot.top_consumers == []
        assert hot.feasible_redistribution is False
        assert hot.recommendation == "add_node"


class TestSingleDominantPod:
    def test_single_large_pod_recommends_scale_vertically(self) -> None:
        """Edge case: node with a single very large pod → vertical scale."""
        dominant_pod = [_consumer("huge-pod", 7.0), _consumer("tiny-pod", 0.1)]
        worker1 = _node(
            "worker-1", allocatable_cpu=8.0, cpu_series=_hot_cpu_series(), pods=dominant_pod
        )
        worker2 = _node("worker-2", allocatable_cpu=8.0, pods=[_consumer("worker-2-existing", 7.9)])

        report = analyze_hot_nodes(HotNodeAnalysisRequest(), [worker1, worker2])

        hot = report.hot_nodes[0]
        assert hot.feasible_redistribution is False
        assert hot.recommendation == "scale_vertically"
