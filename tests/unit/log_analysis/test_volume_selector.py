"""Unit tests for select_strategy_by_volume — pure line-count Strategy selection."""

from __future__ import annotations

from hexawyn.domain.services.log_analysis.strategy import (
    HybridStrategy,
    SmartSummaryStrategy,
    StreamingStrategy,
)
from hexawyn.domain.services.log_analysis.strategy_port import LogAnalysisStrategy
from hexawyn.domain.services.log_analysis.volume_selector import select_strategy_by_volume


class TestSelectStrategyByVolume:
    def test_returns_the_abstract_port_type(self) -> None:
        strategy = select_strategy_by_volume(500)
        assert isinstance(strategy, LogAnalysisStrategy)

    def test_smart_for_under_1000_lines(self) -> None:
        assert isinstance(select_strategy_by_volume(500), SmartSummaryStrategy)

    def test_smart_at_upper_boundary_999(self) -> None:
        assert isinstance(select_strategy_by_volume(999), SmartSummaryStrategy)

    def test_hybrid_at_lower_boundary_1000(self) -> None:
        assert isinstance(select_strategy_by_volume(1000), HybridStrategy)

    def test_hybrid_for_mid_range(self) -> None:
        assert isinstance(select_strategy_by_volume(5000), HybridStrategy)

    def test_hybrid_at_upper_boundary_10000(self) -> None:
        assert isinstance(select_strategy_by_volume(10000), HybridStrategy)

    def test_streaming_above_10000(self) -> None:
        assert isinstance(select_strategy_by_volume(10001), StreamingStrategy)

    def test_streaming_for_large_volume(self) -> None:
        assert isinstance(select_strategy_by_volume(15000), StreamingStrategy)

    def test_smart_for_zero_lines(self) -> None:
        assert isinstance(select_strategy_by_volume(0), SmartSummaryStrategy)
