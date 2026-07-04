from __future__ import annotations

from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_command import (
    ClusterCapacityCeilingForecastCommand,
)


class TestClusterCapacityCeilingForecastCommand:
    def test_defaults(self) -> None:
        cmd = ClusterCapacityCeilingForecastCommand()
        assert cmd.window_days == 14

    def test_custom_window_days(self) -> None:
        cmd = ClusterCapacityCeilingForecastCommand(window_days=7)
        assert cmd.window_days == 7
