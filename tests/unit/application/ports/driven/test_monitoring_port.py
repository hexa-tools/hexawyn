import pytest


class TestMonitoringPort:
    def test_monitoring_port_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.monitoring_port import MonitoringPort

        with pytest.raises(TypeError):
            MonitoringPort()  # type: ignore[abstract]

    def test_concrete_implementation_works(self) -> None:
        from hexawyn.application.ports.driven.monitoring_port import MonitoringPort

        class FakeMonitoring(MonitoringPort):
            def get_triggered_monitors(self) -> list[dict[str, str | int | float]]:
                return [{"name": "cpu", "status": "Alert", "value": 95.0}]

            def get_apm_services(self) -> list[dict[str, str | int | float]]:
                return [{"service": "api", "p99_ms": 120, "error_rate": 0.01}]

        adapter = FakeMonitoring()
        assert len(adapter.get_triggered_monitors()) == 1
        assert adapter.get_apm_services()[0]["service"] == "api"
