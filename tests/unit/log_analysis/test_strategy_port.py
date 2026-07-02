"""Unit tests for the LogAnalysisStrategy interface (ILogAnalysisStrategy port)."""

from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.domain.services.log_analysis.strategy_port import LogAnalysisStrategy


class TestLogAnalysisStrategyPort:
    def test_is_abc(self) -> None:
        assert issubclass(LogAnalysisStrategy, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            LogAnalysisStrategy()  # type: ignore[abstract]

    def test_declares_analyze_and_supports(self) -> None:
        assert "analyze" in LogAnalysisStrategy.__abstractmethods__
        assert "supports" in LogAnalysisStrategy.__abstractmethods__

    def test_reexported_from_strategy_module(self) -> None:
        from hexawyn.domain.services.log_analysis.strategy import (
            LogAnalysisStrategy as ReExported,
        )

        assert ReExported is LogAnalysisStrategy
