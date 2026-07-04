from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.headroom_simulation_port import HeadroomSimulationPort


class TestHeadroomSimulationPort:
    def test_is_abstract(self) -> None:
        assert issubclass(HeadroomSimulationPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            HeadroomSimulationPort()  # type: ignore[abstract]
