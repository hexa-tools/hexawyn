import pytest


class TestDatadogMonitoringPortABC:
    def test_datadog_port_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.datadog_port import DatadogMonitoringPort

        with pytest.raises(TypeError):
            DatadogMonitoringPort()  # type: ignore[abstract]

    def test_concrete_implementation_works(self) -> None:
        from hexawyn.application.ports.driven.datadog_port import DatadogMonitoringPort

        class FakeDatadog(DatadogMonitoringPort):
            def get_triggered_monitors(self) -> list[dict[str, str | int | float]]:
                return [{"name": "cpu", "status": "Alert", "value": 95.0}]

            def get_apm_services(self) -> list[dict[str, str | int | float]]:
                return [{"service": "api", "p99_ms": 120, "error_rate": 0.01}]

        adapter = FakeDatadog()
        assert len(adapter.get_triggered_monitors()) == 1
        assert adapter.get_apm_services()[0]["service"] == "api"
