from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.slo_breach_prediction_port import (
    SLOBreachPredictionPort,
)


class TestSLOBreachPredictionPort:
    def test_is_abstract(self) -> None:
        assert issubclass(SLOBreachPredictionPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            SLOBreachPredictionPort()  # type: ignore[abstract]
