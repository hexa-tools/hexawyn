from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_service_port import (
    HotNodeAnalysisServicePort,
)


class TestHotNodeAnalysisServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(HotNodeAnalysisServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            HotNodeAnalysisServicePort()  # type: ignore[abstract]
