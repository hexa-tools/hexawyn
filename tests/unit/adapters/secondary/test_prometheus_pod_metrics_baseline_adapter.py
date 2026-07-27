"""Unit tests for PrometheusPodMetricsBaselineAdapter (mocks MetricsQueryPort + K8sPort)."""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.adapters.secondary.gitops.prometheus_pod_metrics_baseline_adapter import (
    PrometheusPodMetricsBaselineAdapter,
)
from hexawyn.application.ports.driven.pod_metrics_baseline_port import PodMetricsBaselinePort


def _pod_info(name: str, age: str) -> dict:
    return {
        "name": name,
        "namespace": "production",
        "status": "Running",
        "restarts": 0,
        "age": age,
        "node": "n1",
    }


def _range_sample(pod: str, values: list[tuple[str, float]]) -> dict:
    return {"metric": {"pod": pod}, "values": values}


class TestImplementsPort:
    def test_implements_pod_metrics_baseline_port(self) -> None:
        adapter = PrometheusPodMetricsBaselineAdapter(
            metrics_query_port=MagicMock(), k8s_port=MagicMock()
        )
        assert isinstance(adapter, PodMetricsBaselinePort)


class TestQueryConstruction:
    def test_runs_exactly_three_range_queries_scoped_to_namespace(self) -> None:
        metrics_query_port = MagicMock()
        metrics_query_port.range_query.return_value = []
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = []

        adapter = PrometheusPodMetricsBaselineAdapter(
            metrics_query_port=metrics_query_port, k8s_port=k8s_port
        )
        adapter.get_all_pod_metrics_data(namespace="production", window_days=7)

        assert metrics_query_port.range_query.call_count == 3  # noqa: PLR2004
        for call in metrics_query_port.range_query.call_args_list:
            assert 'namespace="production"' in call.args[0]
            assert call.kwargs["step"] == "1h"


class TestSeriesToPodMatching:
    def test_last_point_is_current_rest_is_baseline(self) -> None:
        metrics_query_port = MagicMock()
        metrics_query_port.range_query.side_effect = [
            [_range_sample("payment-api", [("t0", 200.0), ("t1", 205.0), ("t2", 850.0)])],
            [],
            [],
        ]
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [_pod_info("payment-api", "30d")]

        adapter = PrometheusPodMetricsBaselineAdapter(
            metrics_query_port=metrics_query_port, k8s_port=k8s_port
        )
        result = adapter.get_all_pod_metrics_data(namespace="production", window_days=7)

        assert len(result) == 1
        pod = result[0]
        assert pod["pod_name"] == "payment-api"
        assert pod["cpu_current_millicores"] == 850.0  # noqa: PLR2004
        assert pod["cpu_baseline_millicores"] == [200.0, 205.0]

    def test_pod_with_no_matching_series_gets_empty_baseline(self) -> None:
        metrics_query_port = MagicMock()
        metrics_query_port.range_query.return_value = []
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [_pod_info("orphan-pod", "30d")]

        adapter = PrometheusPodMetricsBaselineAdapter(
            metrics_query_port=metrics_query_port, k8s_port=k8s_port
        )
        result = adapter.get_all_pod_metrics_data(namespace="production", window_days=7)

        assert result[0]["cpu_baseline_millicores"] == []
        assert result[0]["cpu_current_millicores"] == 0.0


class TestPodAgeParsing:
    def test_hours_parsed_directly(self) -> None:
        metrics_query_port = MagicMock()
        metrics_query_port.range_query.return_value = []
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [_pod_info("pod-a", "2h")]

        adapter = PrometheusPodMetricsBaselineAdapter(
            metrics_query_port=metrics_query_port, k8s_port=k8s_port
        )
        result = adapter.get_all_pod_metrics_data(namespace="production", window_days=7)

        assert result[0]["pod_age_hours"] == 2.0  # noqa: PLR2004

    def test_days_converted_to_hours(self) -> None:
        metrics_query_port = MagicMock()
        metrics_query_port.range_query.return_value = []
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [_pod_info("pod-b", "3d")]

        adapter = PrometheusPodMetricsBaselineAdapter(
            metrics_query_port=metrics_query_port, k8s_port=k8s_port
        )
        result = adapter.get_all_pod_metrics_data(namespace="production", window_days=7)

        assert result[0]["pod_age_hours"] == 72.0  # noqa: PLR2004

    def test_minutes_converted_to_hours(self) -> None:
        metrics_query_port = MagicMock()
        metrics_query_port.range_query.return_value = []
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [_pod_info("pod-c", "45m")]

        adapter = PrometheusPodMetricsBaselineAdapter(
            metrics_query_port=metrics_query_port, k8s_port=k8s_port
        )
        result = adapter.get_all_pod_metrics_data(namespace="production", window_days=7)

        assert result[0]["pod_age_hours"] == 0.75  # noqa: PLR2004


class TestHonestDefaults:
    """Neither restart timing nor batch-job labeling is derivable from the
    current K8sPort/MetricsQueryPort surface — the adapter must not fake them."""

    def test_hours_since_last_restart_is_none(self) -> None:
        metrics_query_port = MagicMock()
        metrics_query_port.range_query.return_value = []
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [_pod_info("pod-a", "30d")]

        adapter = PrometheusPodMetricsBaselineAdapter(
            metrics_query_port=metrics_query_port, k8s_port=k8s_port
        )
        result = adapter.get_all_pod_metrics_data(namespace="production", window_days=7)

        assert result[0]["hours_since_last_restart"] is None

    def test_is_scheduled_batch_job_is_false(self) -> None:
        metrics_query_port = MagicMock()
        metrics_query_port.range_query.return_value = []
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [_pod_info("pod-a", "30d")]

        adapter = PrometheusPodMetricsBaselineAdapter(
            metrics_query_port=metrics_query_port, k8s_port=k8s_port
        )
        result = adapter.get_all_pod_metrics_data(namespace="production", window_days=7)

        assert result[0]["is_scheduled_batch_job"] is False


class TestPodAgeParsingEdgeCases:
    def test_empty_age_string_returns_zero(self) -> None:
        metrics_query_port = MagicMock()
        metrics_query_port.range_query.return_value = []
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [_pod_info("pod-a", "")]

        adapter = PrometheusPodMetricsBaselineAdapter(
            metrics_query_port=metrics_query_port, k8s_port=k8s_port
        )
        result = adapter.get_all_pod_metrics_data(namespace="production", window_days=7)

        assert result[0]["pod_age_hours"] == 0.0

    def test_non_numeric_age_returns_zero(self) -> None:
        metrics_query_port = MagicMock()
        metrics_query_port.range_query.return_value = []
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [_pod_info("pod-a", "unknown")]

        adapter = PrometheusPodMetricsBaselineAdapter(
            metrics_query_port=metrics_query_port, k8s_port=k8s_port
        )
        result = adapter.get_all_pod_metrics_data(namespace="production", window_days=7)

        assert result[0]["pod_age_hours"] == 0.0

    def test_unknown_unit_returns_zero(self) -> None:
        metrics_query_port = MagicMock()
        metrics_query_port.range_query.return_value = []
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [_pod_info("pod-a", "5w")]

        adapter = PrometheusPodMetricsBaselineAdapter(
            metrics_query_port=metrics_query_port, k8s_port=k8s_port
        )
        result = adapter.get_all_pod_metrics_data(namespace="production", window_days=7)

        assert result[0]["pod_age_hours"] == 0.0
