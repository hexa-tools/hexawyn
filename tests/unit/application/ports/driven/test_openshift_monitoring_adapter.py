from unittest.mock import MagicMock

from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort

_ROUTE_ENDPOINT = "https://thanos-querier.openshift-monitoring.svc:9091"


class TestPortImplementation:
    def test_is_a_metrics_query_port(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_monitoring_adapter import (
            OpenShiftMonitoringAdapter,
        )

        adapter = OpenShiftMonitoringAdapter(
            endpoint=_ROUTE_ENDPOINT, delegate=MagicMock(spec=MetricsQueryPort)
        )

        assert isinstance(adapter, MetricsQueryPort)

    def test_exposes_endpoint(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_monitoring_adapter import (
            OpenShiftMonitoringAdapter,
        )

        adapter = OpenShiftMonitoringAdapter(
            endpoint=_ROUTE_ENDPOINT, delegate=MagicMock(spec=MetricsQueryPort)
        )

        assert adapter.endpoint == _ROUTE_ENDPOINT


class TestInstantQuery:
    def test_delegates_to_prometheus_port(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_monitoring_adapter import (
            OpenShiftMonitoringAdapter,
        )

        delegate = MagicMock(spec=MetricsQueryPort)
        delegate.instant_query.return_value = [{"metric": {}, "value": 1.0}]
        adapter = OpenShiftMonitoringAdapter(endpoint=_ROUTE_ENDPOINT, delegate=delegate)

        result = adapter.instant_query("up", 5.0)

        delegate.instant_query.assert_called_once_with("up", 5.0)
        assert result[0]["value"] == 1.0


class TestRangeQuery:
    def test_delegates_to_prometheus_port(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_monitoring_adapter import (
            OpenShiftMonitoringAdapter,
        )

        delegate = MagicMock(spec=MetricsQueryPort)
        delegate.range_query.return_value = [{"metric": {}, "values": []}]
        adapter = OpenShiftMonitoringAdapter(endpoint=_ROUTE_ENDPOINT, delegate=delegate)

        result = adapter.range_query("up", "s", "e", "30s", 5.0)

        delegate.range_query.assert_called_once_with("up", "s", "e", "30s", 5.0)
        assert result == [{"metric": {}, "values": []}]


class TestLazyDelegate:
    def test_builds_prometheus_http_adapter_from_endpoint_and_token(self) -> None:
        from unittest.mock import patch

        from hexawyn.adapters.secondary.openshift.openshift_monitoring_adapter import (
            OpenShiftMonitoringAdapter,
        )

        built = MagicMock(spec=MetricsQueryPort)
        built.instant_query.return_value = []
        adapter = OpenShiftMonitoringAdapter(endpoint=_ROUTE_ENDPOINT, token="tok-123")

        with patch(
            "hexawyn.adapters.secondary.gitops.prometheus_http_adapter.PrometheusHTTPAdapter",
            return_value=built,
        ) as adapter_cls:
            result = adapter.instant_query("up", 5.0)

        adapter_cls.assert_called_once_with(_ROUTE_ENDPOINT, token="tok-123")
        assert result == []
