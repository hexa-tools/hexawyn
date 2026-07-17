from __future__ import annotations

from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_command import (
    AnalyzeCriticalNamespaceEventsCommand,
)


class TestAnalyzeCriticalNamespaceEventsCommand:
    def test_defaults(self) -> None:
        cmd = AnalyzeCriticalNamespaceEventsCommand(namespace="staging")
        assert cmd.time_window_minutes == 15

    def test_explicit_value(self) -> None:
        cmd = AnalyzeCriticalNamespaceEventsCommand(namespace="staging", time_window_minutes=60)
        assert cmd.time_window_minutes == 60
