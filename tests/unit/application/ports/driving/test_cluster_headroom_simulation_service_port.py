from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_service_port import (
    ClusterHeadroomSimulationServicePort,
)


class TestClusterHeadroomSimulationServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(ClusterHeadroomSimulationServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            ClusterHeadroomSimulationServicePort()  # type: ignore[abstract]
