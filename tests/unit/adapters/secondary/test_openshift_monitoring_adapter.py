from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.openshift.openshift_monitoring_adapter import (
    OpenShiftMonitoringAdapter,
)
from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort


class TestOpenShiftMonitoringAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OpenShiftMonitoringAdapter("http://localhost"), MetricsQueryPort)

    def test_endpoint_property(self) -> None:
        adapter = OpenShiftMonitoringAdapter("http://thanos:9090")
        assert adapter.endpoint == "http://thanos:9090"

    def test_delegates_instant_query(self) -> None:
        delegate = Mock(spec=MetricsQueryPort)
        delegate.instant_query.return_value = []
        adapter = OpenShiftMonitoringAdapter("http://localhost", delegate=delegate)
        result = adapter.instant_query("up", 10.0)
        assert result == []
        delegate.instant_query.assert_called_once_with("up", 10.0)

    def test_delegates_range_query(self) -> None:
        delegate = Mock(spec=MetricsQueryPort)
        delegate.range_query.return_value = []
        adapter = OpenShiftMonitoringAdapter("http://localhost", delegate=delegate)
        result = adapter.range_query(
            "up", "2024-01-01T00:00:00Z", "2024-01-01T01:00:00Z", "1m", 10.0
        )
        assert result == []
        delegate.range_query.assert_called_once_with(
            "up", "2024-01-01T00:00:00Z", "2024-01-01T01:00:00Z", "1m", 10.0
        )
