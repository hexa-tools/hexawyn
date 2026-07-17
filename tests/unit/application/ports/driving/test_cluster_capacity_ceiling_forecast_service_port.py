from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_service_port import (
    ClusterCapacityCeilingForecastServicePort,
)


class TestClusterCapacityCeilingForecastServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(ClusterCapacityCeilingForecastServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            ClusterCapacityCeilingForecastServicePort()  # type: ignore[abstract]
