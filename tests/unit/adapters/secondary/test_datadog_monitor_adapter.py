from __future__ import annotations

from unittest.mock import Mock

import pytest
from hexawyn.adapters.secondary.datadog.datadog_monitor_adapter import (
    DatadogMonitorAdapter,
)
from hexawyn.domain.errors import MetricsUnavailableError


class MockMonitor:
    def __init__(
        self, name: str, overall_state: str, message: str = "", tags: list[str] | None = None
    ) -> None:
        self.name = name
        self.overall_state = overall_state
        self.message = message
        self.tags = tags or []


class TestDatadogMonitorAdapter:
    def test_get_triggered_monitors(self) -> None:
        api = Mock()
        api.list_monitors.return_value = [
            MockMonitor("alert-1", "Alert", "CPU high", ["env:prod"]),
            MockMonitor("warn-1", "Warn", "disk 80%", []),
            MockMonitor("ok-1", "OK", "", []),
        ]
        adapter = DatadogMonitorAdapter(monitors_api=api)
        result = adapter.get_triggered_monitors()
        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["name"] == "alert-1"
        assert result[1]["name"] == "warn-1"

    def test_get_triggered_monitors_empty(self) -> None:
        api = Mock()
        api.list_monitors.return_value = []
        adapter = DatadogMonitorAdapter(monitors_api=api)
        assert adapter.get_triggered_monitors() == []

    def test_get_triggered_monitors_all_ok(self) -> None:
        api = Mock()
        api.list_monitors.return_value = [MockMonitor("ok", "OK")]
        adapter = DatadogMonitorAdapter(monitors_api=api)
        assert adapter.get_triggered_monitors() == []

    def test_api_error(self) -> None:
        from datadog_api_client.exceptions import ApiException

        api = Mock()
        api.list_monitors.side_effect = ApiException(status=500)
        adapter = DatadogMonitorAdapter(monitors_api=api)
        with pytest.raises(MetricsUnavailableError):
            adapter.get_triggered_monitors()

    def test_get_apm_services_returns_empty(self) -> None:
        adapter = DatadogMonitorAdapter()
        result = adapter.get_apm_services()
        assert result == []
