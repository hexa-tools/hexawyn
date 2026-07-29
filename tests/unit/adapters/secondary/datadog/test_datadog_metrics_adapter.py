from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import Mock, patch

import pytest
from hexawyn.adapters.secondary.datadog.datadog_metrics_adapter import (
    DatadogClusterResourceMetricsAdapter,
    _host_from_scope,
    _latest_value,
    _series_by_host,
    _translate_error,
    _ts_to_iso,
    _values,
)
from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
)
from hexawyn.domain.errors import (
    AdapterTimeoutError,
    InsufficientPermissionsError,
    MetricsUnavailableError,
)


def _series_mock(scope: str, pointlist: list[list[float | None]]) -> Mock:
    series = Mock()
    series.scope = scope
    series.pointlist = pointlist
    return series


def _api_mock(series_list: list[Mock] | None = None) -> Mock:
    api = Mock()
    response = Mock()
    response.series = series_list or []
    api.query_metrics.return_value = response
    return api


class TestDatadogClusterResourceMetricsAdapter:
    def test_implements_port(self) -> None:
        adapter = DatadogClusterResourceMetricsAdapter(metrics_api=Mock())
        assert isinstance(adapter, ClusterResourceMetricsPort)

    # ── get_current_usage ───────────────────────────────────

    def test_get_current_usage_returns_cpu_and_memory(self) -> None:
        api = Mock()
        response_cpu = Mock()
        response_cpu.series = [_series_mock("", [[1680000000, 100.0], [1680000300, 2500000000.0]])]
        response_memory = Mock()
        response_memory.series = [
            _series_mock("", [[1680000000, 500.0], [1680000300, 2147483648.0]])
        ]
        api.query_metrics.side_effect = [response_cpu, response_memory]

        adapter = DatadogClusterResourceMetricsAdapter(metrics_api=api)
        result = adapter.get_current_usage(timeout_seconds=15.0)

        assert isinstance(result["cpu_cores"], float)
        assert isinstance(result["memory_gb"], float)
        assert result["cpu_cores"] == pytest.approx(2.5)
        assert result["memory_gb"] == pytest.approx(2.0)

    def test_get_current_usage_empty_series_returns_zeros(self) -> None:
        api = _api_mock([])
        adapter = DatadogClusterResourceMetricsAdapter(metrics_api=api)
        result = adapter.get_current_usage(timeout_seconds=15.0)
        assert result["cpu_cores"] == 0.0
        assert result["memory_gb"] == 0.0

    def test_get_current_usage_null_values_in_series(self) -> None:
        api = Mock()
        null_series = _series_mock("", [[1680000000, None], [1680000300, None]])
        api.query_metrics.return_value = Mock(series=[null_series])

        adapter = DatadogClusterResourceMetricsAdapter(metrics_api=api)
        result = adapter.get_current_usage(timeout_seconds=15.0)

        assert result["cpu_cores"] == 0.0
        assert result["memory_gb"] == 0.0

    # ── get_daily_usage ─────────────────────────────────────

    def test_get_daily_usage_returns_series(self) -> None:
        cpu_series = _series_mock("", [[1680000000, 1000000000.0], [1680086400, 1500000000.0]])
        mem_series = _series_mock("", [[1680000000, 1073741824.0], [1680086400, 2147483648.0]])
        api = _api_mock([cpu_series, mem_series])
        response_cpu = Mock(series=[cpu_series])
        response_mem = Mock(series=[mem_series])
        api.query_metrics.side_effect = [response_cpu, response_mem]

        adapter = DatadogClusterResourceMetricsAdapter(metrics_api=api)
        start = datetime(2024, 1, 1, tzinfo=UTC)
        end = datetime(2024, 1, 3, tzinfo=UTC)

        result = adapter.get_daily_usage(start=start, end=end, timeout_seconds=15.0)

        assert result["cpu_daily_cores"] == [1.0, 1.5]
        assert result["memory_daily_gb"] == [1.0, 2.0]

    def test_get_daily_usage_empty_series_returns_empty_lists(self) -> None:
        api = _api_mock([])
        adapter = DatadogClusterResourceMetricsAdapter(metrics_api=api)
        start = datetime(2024, 1, 1, tzinfo=UTC)
        end = datetime(2024, 1, 3, tzinfo=UTC)

        result = adapter.get_daily_usage(start=start, end=end, timeout_seconds=15.0)

        assert result["cpu_daily_cores"] == []
        assert result["memory_daily_gb"] == []

    # ── get_node_utilization ────────────────────────────────

    def test_get_node_utilization_returns_per_node_data(self) -> None:
        cpu_series = _series_mock(
            "host:node-1,env:prod",
            [[1680000000000, 45.0], [1680000060000, 55.0]],
        )
        mem_series = _series_mock(
            "host:node-1,env:prod",
            [[1680000000000, 60.0], [1680000060000, 70.0]],
        )
        api = Mock()
        api.query_metrics.side_effect = [
            Mock(series=[cpu_series]),
            Mock(series=[mem_series]),
        ]

        adapter = DatadogClusterResourceMetricsAdapter(metrics_api=api)
        start = datetime(2024, 1, 1, tzinfo=UTC)
        end = datetime(2024, 1, 2, tzinfo=UTC)

        result = adapter.get_node_utilization(start=start, end=end, timeout_seconds=15.0)

        assert "node-1" in result
        assert len(result["node-1"]["cpu_percent_series"]) == 2  # noqa: PLR2004
        assert len(result["node-1"]["memory_percent_series"]) == 2  # noqa: PLR2004

    def test_get_node_utilization_empty_series_returns_empty_dict(self) -> None:
        api = _api_mock([])
        adapter = DatadogClusterResourceMetricsAdapter(metrics_api=api)
        start = datetime(2024, 1, 1, tzinfo=UTC)
        end = datetime(2024, 1, 2, tzinfo=UTC)

        result = adapter.get_node_utilization(start=start, end=end, timeout_seconds=15.0)

        assert result == {}

    # ── error translation ───────────────────────────────────

    def test_api_error_rate_limit_raises_adapter_timeout(self) -> None:
        from datadog_api_client.exceptions import ApiException

        api = Mock()
        api.query_metrics.side_effect = ApiException(status=429)
        adapter = DatadogClusterResourceMetricsAdapter(metrics_api=api)

        with pytest.raises(AdapterTimeoutError):
            adapter.get_current_usage(timeout_seconds=15.0)

    def test_api_error_401_raises_insufficient_permissions(self) -> None:
        from datadog_api_client.exceptions import ApiException

        api = Mock()
        api.query_metrics.side_effect = ApiException(status=401)
        adapter = DatadogClusterResourceMetricsAdapter(metrics_api=api)

        with pytest.raises(InsufficientPermissionsError):
            adapter.get_current_usage(timeout_seconds=15.0)

    def test_api_error_403_raises_insufficient_permissions(self) -> None:
        from datadog_api_client.exceptions import ApiException

        api = Mock()
        api.query_metrics.side_effect = ApiException(status=403)
        adapter = DatadogClusterResourceMetricsAdapter(metrics_api=api)

        with pytest.raises(InsufficientPermissionsError):
            adapter.get_current_usage(timeout_seconds=15.0)

    def test_api_error_generic_raises_metrics_unavailable(self) -> None:
        from datadog_api_client.exceptions import ApiException

        api = Mock()
        api.query_metrics.side_effect = ApiException(status=500)
        adapter = DatadogClusterResourceMetricsAdapter(metrics_api=api)

        with pytest.raises(MetricsUnavailableError):
            adapter.get_current_usage(timeout_seconds=15.0)

    # ── lazy API construction ───────────────────────────────

    def test_lazy_api_construction_when_metrics_api_is_none(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.datadog.datadog_metrics_adapter._build_metrics_api"
        ) as mock_build:
            mock_build.return_value = _api_mock([_series_mock("", [])])
            adapter = DatadogClusterResourceMetricsAdapter(key="k", app_key="a", site="s")
            adapter.get_current_usage(timeout_seconds=15.0)
            mock_build.assert_called_once_with("k", "a", "s")


class TestHelpers:
    def test_latest_value_returns_last_non_null(self) -> None:
        series = _series_mock("", [[0, 10.0], [1, None], [2, 30.0]])
        assert _latest_value([series]) == 30.0  # noqa: PLR2004

    def test_latest_value_empty_series_returns_zero(self) -> None:
        assert _latest_value([]) == 0.0

    def test_latest_value_all_nulls_returns_zero(self) -> None:
        series = _series_mock("", [[0, None], [1, None]])
        assert _latest_value([series]) == 0.0

    def test_values_returns_all_non_null(self) -> None:
        series = _series_mock("", [[0, 10.0], [1, None], [2, 30.0]])
        assert _values([series]) == [10.0, 30.0]

    def test_values_empty_series_returns_empty_list(self) -> None:
        assert _values([]) == []

    def test_series_by_host_groups_by_host_tag(self) -> None:
        s1 = _series_mock("host:node-a,key:val", [[1680000000000, 10.0]])
        s2 = _series_mock("host:node-b", [[1680000000000, 20.0]])
        result = _series_by_host([s1, s2])
        assert "node-a" in result
        assert "node-b" in result
        assert len(result["node-a"]) == 1
        assert result["node-a"][0][1] == 10.0  # noqa: PLR2004

    def test_series_by_host_empty_returns_empty_dict(self) -> None:
        assert _series_by_host([]) == {}

    def test_host_from_scope_extracts_host_tag(self) -> None:
        assert _host_from_scope("host:my-node,env:prod,region:us") == "my-node"

    def test_host_from_scope_no_host_tag_returns_unknown(self) -> None:
        assert _host_from_scope("env:prod,region:us") == "unknown"

    def test_host_from_scope_empty_string_returns_unknown(self) -> None:
        assert _host_from_scope("") == "unknown"

    def test_ts_to_iso_converts_epoch_millis(self) -> None:
        result = _ts_to_iso(1700000000000.0)
        assert result.endswith("Z")
        assert "2023-11-" in result

    def test_translate_error_rate_limit(self) -> None:
        from datadog_api_client.exceptions import ApiException

        exc = ApiException(status=429)
        result = _translate_error(exc)
        assert isinstance(result, AdapterTimeoutError)

    def test_translate_error_401(self) -> None:
        from datadog_api_client.exceptions import ApiException

        exc = ApiException(status=401)
        result = _translate_error(exc)
        assert isinstance(result, InsufficientPermissionsError)

    def test_translate_error_403(self) -> None:
        from datadog_api_client.exceptions import ApiException

        exc = ApiException(status=403)
        result = _translate_error(exc)
        assert isinstance(result, InsufficientPermissionsError)

    def test_translate_error_unknown(self) -> None:
        from datadog_api_client.exceptions import ApiException

        exc = ApiException(status=502)
        result = _translate_error(exc)
        assert isinstance(result, MetricsUnavailableError)
