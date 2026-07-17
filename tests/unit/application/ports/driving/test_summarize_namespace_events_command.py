from __future__ import annotations

from hexawyn.application.ports.driving.summarize_namespace_events.summarize_namespace_events_command import (
    SummarizeNamespaceEventsCommand,
)


class TestSummarizeNamespaceEventsCommand:
    def test_defaults(self) -> None:
        cmd = SummarizeNamespaceEventsCommand(namespace="staging")
        assert cmd.time_window_minutes == 15

    def test_explicit_value(self) -> None:
        cmd = SummarizeNamespaceEventsCommand(namespace="staging", time_window_minutes=60)
        assert cmd.time_window_minutes == 60
