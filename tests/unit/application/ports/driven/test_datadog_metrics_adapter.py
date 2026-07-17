from unittest.mock import MagicMock, patch

import pytest

pytest.importorskip("datadog_api_client")
from datadog_api_client.exceptions import ApiException  # noqa: E402
from hexawyn.application.ports.driven.cluster_resource_metrics_port import (  # noqa: E402
    ClusterResourceMetricsPort,
)
from hexawyn.domain.errors import (  # noqa: E402
    AdapterTimeoutError,
    InsufficientPermissionsError,
    MetricsUnavailableError,
)


def _series(pointlist: list[list[float]], scope: str = "*") -> MagicMock:
    series = MagicMock()
    series.pointlist = pointlist
    series.scope = scope
    return series


def _response(series: list[MagicMock]) -> MagicMock:
    response = MagicMock()
    response.series = series
    return response


def _adapter(api: MagicMock):
    from hexawyn.adapters.secondary.datadog.datadog_metrics_adapter import (
        DatadogClusterResourceMetricsAdapter,
    )

    return DatadogClusterResourceMetricsAdapter(metrics_api=api)


class TestContract:
    def test_is_a_cluster_resource_metrics_port(self) -> None:
        assert isinstance(_adapter(MagicMock()), ClusterResourceMetricsPort)


class TestGetCurrentUsage:
    def test_converts_nanocores_and_bytes(self) -> None:
        api = MagicMock()
        api.query_metrics.side_effect = [
            _response([_series([[1000.0, 2_000_000_000.0]])]),  # 2 cores
            _response([_series([[1000.0, 2_147_483_648.0]])]),  # 2 GiB
        ]
        adapter = _adapter(api)

        usage = adapter.get_current_usage(timeout_seconds=10.0)

        assert usage["cpu_cores"] == 2.0
        assert usage["memory_gb"] == 2.0

    def test_zero_when_no_series(self) -> None:
        api = MagicMock()
        api.query_metrics.return_value = _response([])
        adapter = _adapter(api)

        usage = adapter.get_current_usage(timeout_seconds=10.0)

        assert usage == {"cpu_cores": 0.0, "memory_gb": 0.0}

    def test_zero_when_all_points_none(self) -> None:
        api = MagicMock()
        api.query_metrics.side_effect = [
            _response([_series([[1000.0, None]])]),
            _response([_series([[1000.0, None]])]),
        ]
        adapter = _adapter(api)

        usage = adapter.get_current_usage(timeout_seconds=10.0)

        assert usage == {"cpu_cores": 0.0, "memory_gb": 0.0}


class TestGetDailyUsage:
    def test_converts_series_values(self) -> None:
        from datetime import UTC, datetime

        api = MagicMock()
        api.query_metrics.side_effect = [
            _response([_series([[1.0, 1_000_000_000.0], [2.0, 2_000_000_000.0]])]),
            _response([_series([[1.0, 1_073_741_824.0], [2.0, 2_147_483_648.0]])]),
        ]
        adapter = _adapter(api)
        start = datetime(2026, 1, 1, tzinfo=UTC)
        end = datetime(2026, 1, 10, tzinfo=UTC)

        daily = adapter.get_daily_usage(start, end, timeout_seconds=10.0)

        assert daily["cpu_daily_cores"] == [1.0, 2.0]
        assert daily["memory_daily_gb"] == [1.0, 2.0]


class TestGetNodeUtilization:
    def test_groups_by_host(self) -> None:
        from datetime import UTC, datetime

        api = MagicMock()
        api.query_metrics.side_effect = [
            _response([_series([[1000.0, 80.0]], scope="host:node-a")]),
            _response([_series([[1000.0, 55.0]], scope="host:node-a")]),
        ]
        adapter = _adapter(api)
        start = datetime(2026, 1, 1, tzinfo=UTC)
        end = datetime(2026, 1, 2, tzinfo=UTC)

        result = adapter.get_node_utilization(start, end, timeout_seconds=10.0)

        assert result["node-a"]["cpu_percent_series"][0][1] == 80.0
        assert result["node-a"]["memory_percent_series"][0][1] == 55.0

    def test_skips_none_points(self) -> None:
        from datetime import UTC, datetime

        api = MagicMock()
        api.query_metrics.side_effect = [
            _response([_series([[], [1000.0, None], [2000.0, 90.0]], scope="host:node-b")]),
            _response([]),
        ]
        adapter = _adapter(api)
        start = datetime(2026, 1, 1, tzinfo=UTC)
        end = datetime(2026, 1, 2, tzinfo=UTC)

        result = adapter.get_node_utilization(start, end, timeout_seconds=10.0)

        assert result["node-b"]["cpu_percent_series"] == [
            (result["node-b"]["cpu_percent_series"][0][0], 90.0)
        ]


class TestErrorTranslation:
    def test_rate_limit_raises_adapter_timeout(self) -> None:
        api = MagicMock()
        api.query_metrics.side_effect = ApiException(status=429)
        adapter = _adapter(api)

        with pytest.raises(AdapterTimeoutError):
            adapter.get_current_usage(timeout_seconds=1.0)

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        api = MagicMock()
        api.query_metrics.side_effect = ApiException(status=403)
        adapter = _adapter(api)

        with pytest.raises(InsufficientPermissionsError) as exc_info:
            adapter.get_current_usage(timeout_seconds=1.0)

        assert "datadog" in str(exc_info.value).lower()

    def test_other_error_raises_metrics_unavailable(self) -> None:
        api = MagicMock()
        api.query_metrics.side_effect = ApiException(status=500)
        adapter = _adapter(api)

        with pytest.raises(MetricsUnavailableError):
            adapter.get_current_usage(timeout_seconds=1.0)


class TestGetDailyUsageEmpty:
    def test_returns_empty_lists_when_no_series(self) -> None:
        from datetime import UTC, datetime

        api = MagicMock()
        api.query_metrics.return_value = _response([])
        adapter = _adapter(api)
        start = datetime(2026, 1, 1, tzinfo=UTC)
        end = datetime(2026, 1, 2, tzinfo=UTC)

        daily = adapter.get_daily_usage(start, end, timeout_seconds=10.0)

        assert daily == {"cpu_daily_cores": [], "memory_daily_gb": []}


class TestHelpers:
    def test_host_from_scope_unknown_fallback(self) -> None:
        from hexawyn.adapters.secondary.datadog.datadog_metrics_adapter import _host_from_scope

        assert _host_from_scope("") == "unknown"

    def test_build_metrics_api_constructs_config(self) -> None:
        from hexawyn.adapters.secondary.datadog.datadog_metrics_adapter import _build_metrics_api

        cfg_data: dict[str, str] = {}
        cfg_mock = MagicMock()
        cfg_mock.api_key = cfg_data
        cfg_mock.server_variables = {}

        with (
            patch("datadog_api_client.Configuration", return_value=cfg_mock),
            patch("datadog_api_client.ApiClient"),
            patch("datadog_api_client.v1.api.metrics_api.MetricsApi"),
        ):
            _build_metrics_api("k", "a", "datadoghq.eu")

        assert cfg_data["apiKeyAuth"] == "k"
        assert cfg_data["appKeyAuth"] == "a"
        assert cfg_mock.server_variables["site"] == "datadoghq.eu"


class TestLazyApiCreation:
    def test_lazily_builds_metrics_api(self) -> None:
        from hexawyn.adapters.secondary.datadog import datadog_metrics_adapter as module
        from hexawyn.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )

        created_api = MagicMock()
        created_api.query_metrics.return_value = _response([])
        adapter = DatadogClusterResourceMetricsAdapter(key="k", app_key="a", site="datadoghq.eu")

        with patch.object(module, "_build_metrics_api", return_value=created_api) as build:
            adapter.get_current_usage(timeout_seconds=1.0)

        build.assert_called_once_with("k", "a", "datadoghq.eu")
