from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.capacity_forecast_port import CapacityForecastPort


class TestCapacityForecastPort:
    def test_is_abstract(self) -> None:
        assert issubclass(CapacityForecastPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            CapacityForecastPort()  # type: ignore[abstract]
