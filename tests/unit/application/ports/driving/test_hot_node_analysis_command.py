from __future__ import annotations

from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_command import (
    HotNodeAnalysisCommand,
)


class TestHotNodeAnalysisCommand:
    def test_default_window_hours(self) -> None:
        cmd = HotNodeAnalysisCommand()
        assert cmd.window_hours == 24

    def test_custom_window_hours(self) -> None:
        cmd = HotNodeAnalysisCommand(window_hours=12)
        assert cmd.window_hours == 12
