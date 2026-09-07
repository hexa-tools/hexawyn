"""Unit tests for the Hot Node Analysis domain models — pure dataclasses,
no I/O."""

from __future__ import annotations

from hexawyn.domain.models.hot_node_analysis import (
    ClusterNodeSnapshot,
    HotNodeAnalysisReport,
    HotNodeAnalysisRequest,
    HotNodeResult,
    TopConsumer,
)


class TestTopConsumer:
    def test_fields(self) -> None:
        consumer = TopConsumer(
            pod_name="data-processor-abc",
            namespace="production",
            cpu_usage_cores=0.8,
            memory_usage_gb=1.5,
        )

        assert consumer.pod_name == "data-processor-abc"
        assert consumer.cpu_usage_cores == 0.8  # noqa: PLR2004


class TestClusterNodeSnapshot:
    def test_defaults(self) -> None:
        snapshot = ClusterNodeSnapshot(
            node_name="worker-eu-3",
            cordoned=False,
            allocatable_cpu_cores=8.0,
            allocatable_memory_gb=32.0,
        )

        assert snapshot.cpu_percent_series == []
        assert snapshot.memory_percent_series == []
        assert snapshot.pods == []


class TestHotNodeAnalysisRequest:
    def test_default_window(self) -> None:
        request = HotNodeAnalysisRequest()

        assert request.window_hours == 24  # noqa: PLR2004


class TestHotNodeResult:
    def test_fields(self) -> None:
        result = HotNodeResult(
            node_name="worker-eu-3",
            cpu_avg_percent=88.0,
            memory_avg_percent=65.0,
            cpu_hot=True,
            memory_hot=False,
            hot_hours=21,
            top_consumers=[],
            feasible_redistribution=True,
            target_node="worker-eu-5",
            recommendation="redistribute",
            business_hours_pattern=False,
        )

        assert result.recommendation == "redistribute"
        assert result.target_node == "worker-eu-5"


class TestHotNodeAnalysisReport:
    def test_defaults(self) -> None:
        report = HotNodeAnalysisReport(
            hot_nodes=[],
            healthy_node_count=5,
            excluded_cordoned_nodes=[],
            warnings=[],
            summary="All nodes healthy.",
        )

        assert report.hot_nodes == []
        assert report.healthy_node_count == 5  # noqa: PLR2004
