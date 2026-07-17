from unittest.mock import MagicMock, patch

import pytest

pytest.importorskip("datadog_api_client")
from datadog_api_client.exceptions import ApiException  # noqa: E402
from hexawyn.application.ports.driven.monitoring_port import MonitoringPort  # noqa: E402
from hexawyn.domain.errors import MetricsUnavailableError  # noqa: E402


def _monitor(
    name: str = "CPU high",
    state: str = "Alert",
    msg: str = "cpu > 90%",
    tags: list[str] | None = None,
) -> MagicMock:
    m = MagicMock()
    m.name = name
    m.overall_state = state
    m.message = msg
    m.tags = tags or []
    return m


def _adapter(api: MagicMock):
    from hexawyn.adapters.secondary.datadog.datadog_monitor_adapter import (
        DatadogMonitorAdapter,
    )

    return DatadogMonitorAdapter(monitors_api=api)


class TestContract:
    def test_is_a_monitoring_port(self) -> None:
        assert isinstance(_adapter(MagicMock()), MonitoringPort)


class TestGetTriggeredMonitors:
    def test_returns_alert_warn_no_data_only(self) -> None:
        api = MagicMock()
        api.list_monitors.return_value = [
            _monitor("alert-1", "Alert"),
            _monitor("warn-1", "Warn"),
            _monitor("no-data", "No Data"),
            _monitor("ok-1", "OK"),
        ]
        adapter = _adapter(api)

        triggered = adapter.get_triggered_monitors()

        names = {m["name"] for m in triggered}
        assert names == {"alert-1", "warn-1", "no-data"}
        assert len(triggered) == 3

    def test_maps_monitor_fields(self) -> None:
        api = MagicMock()
        api.list_monitors.return_value = [
            _monitor("disk full", "Alert", "disk > 85%", ["env:prod"])
        ]
        adapter = _adapter(api)

        triggered = adapter.get_triggered_monitors()

        m = triggered[0]
        assert m["name"] == "disk full"
        assert m["status"] == "Alert"
        assert m["message"] == "disk > 85%"
        assert m["tags"] == "env:prod"

    def test_empty_when_none_triggered(self) -> None:
        api = MagicMock()
        api.list_monitors.return_value = [_monitor("ok", "OK")]
        adapter = _adapter(api)

        assert adapter.get_triggered_monitors() == []


class TestGetAPMServices:
    def test_raises_not_implemented(self) -> None:
        adapter = _adapter(MagicMock())

        with pytest.raises(NotImplementedError):
            adapter.get_apm_services()


class TestErrorTranslation:
    def test_api_error_raises_metrics_unavailable(self) -> None:
        api = MagicMock()
        api.list_monitors.side_effect = ApiException(status=500)
        adapter = _adapter(api)

        with pytest.raises(MetricsUnavailableError):
            adapter.get_triggered_monitors()


class TestHelpers:
    def test_build_monitors_api_constructs_config(self) -> None:
        from hexawyn.adapters.secondary.datadog.datadog_monitor_adapter import (
            _build_monitors_api,
        )

        cfg_data: dict[str, str] = {}
        cfg_mock = MagicMock()
        cfg_mock.api_key = cfg_data
        cfg_mock.server_variables = {}

        with (
            patch("datadog_api_client.Configuration", return_value=cfg_mock),
            patch("datadog_api_client.ApiClient"),
            patch("datadog_api_client.v1.api.monitors_api.MonitorsApi"),
        ):
            _build_monitors_api("k", "a", "datadoghq.eu")

        assert cfg_data["apiKeyAuth"] == "k"
        assert cfg_data["appKeyAuth"] == "a"
        assert cfg_mock.server_variables["site"] == "datadoghq.eu"


class TestLazyApiCreation:
    def test_lazily_builds_monitors_api(self) -> None:
        from hexawyn.adapters.secondary.datadog import datadog_monitor_adapter as module
        from hexawyn.adapters.secondary.datadog.datadog_monitor_adapter import (
            DatadogMonitorAdapter,
        )

        created_api = MagicMock()
        created_api.list_monitors.return_value = []
        adapter = DatadogMonitorAdapter(key="k", app_key="a", site="datadoghq.com")

        with patch.object(module, "_build_monitors_api", return_value=created_api) as build:
            adapter.get_triggered_monitors()

        build.assert_called_once_with("k", "a", "datadoghq.com")
