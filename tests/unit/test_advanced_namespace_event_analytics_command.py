from __future__ import annotations

from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_command import (
    AdvancedNamespaceEventAnalyticsCommand,
)


class TestAdvancedNamespaceEventAnalyticsCommand:
    def test_defaults(self) -> None:
        cmd = AdvancedNamespaceEventAnalyticsCommand(namespace="data-pipeline")
        assert cmd.time_window_minutes == 360

    def test_explicit_value(self) -> None:
        cmd = AdvancedNamespaceEventAnalyticsCommand(
            namespace="data-pipeline", time_window_minutes=120
        )
        assert cmd.time_window_minutes == 120
