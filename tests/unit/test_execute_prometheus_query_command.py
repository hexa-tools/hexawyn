from __future__ import annotations

from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_command import (
    ExecutePrometheusQueryCommand,
)


class TestExecutePrometheusQueryCommand:
    def test_defaults(self) -> None:
        cmd = ExecutePrometheusQueryCommand(promql="up")
        assert cmd.query_type == "instant"
        assert cmd.start is None
        assert cmd.end is None
        assert cmd.step == "15s"
        assert cmd.unit_hint == "raw"
        assert cmd.timeout_seconds == 15.0

    def test_range_query_values(self) -> None:
        cmd = ExecutePrometheusQueryCommand(
            promql="rate(container_cpu_usage_seconds_total[5m])",
            query_type="range",
            start="2024-06-01T14:00:00Z",
            end="2024-06-01T14:05:00Z",
            step="30s",
            unit_hint="cores",
            timeout_seconds=30.0,
        )
        assert cmd.query_type == "range"
        assert cmd.start == "2024-06-01T14:00:00Z"
        assert cmd.unit_hint == "cores"
        assert cmd.timeout_seconds == 30.0
