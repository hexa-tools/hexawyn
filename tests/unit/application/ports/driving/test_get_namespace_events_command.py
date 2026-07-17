from __future__ import annotations

from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_command import (
    GetNamespaceEventsCommand,
)


class TestGetNamespaceEventsCommand:
    def test_defaults(self) -> None:
        cmd = GetNamespaceEventsCommand(namespace="production")
        assert cmd.time_window_minutes == 15
        assert cmd.top_n == 20

    def test_explicit_values(self) -> None:
        cmd = GetNamespaceEventsCommand(namespace="production", time_window_minutes=30, top_n=10)
        assert cmd.time_window_minutes == 30
        assert cmd.top_n == 10
