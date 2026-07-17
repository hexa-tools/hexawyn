from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.hot_node_analysis_port import HotNodeAnalysisPort


class TestHotNodeAnalysisPort:
    def test_is_abstract(self) -> None:
        assert issubclass(HotNodeAnalysisPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            HotNodeAnalysisPort()  # type: ignore[abstract]
