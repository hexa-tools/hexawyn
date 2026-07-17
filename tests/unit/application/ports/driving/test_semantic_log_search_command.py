from __future__ import annotations

from hexawyn.application.ports.driving.semantic_log_search.semantic_log_search_command import (
    SemanticLogSearchCommand,
)


class TestSemanticLogSearchCommand:
    def test_defaults(self) -> None:
        cmd = SemanticLogSearchCommand(pattern="connection refused to postgres")
        assert cmd.is_regex is False
        assert cmd.namespace is None
        assert cmd.time_window_minutes == 60

    def test_explicit_values(self) -> None:
        cmd = SemanticLogSearchCommand(
            pattern="foo.*bar", is_regex=True, namespace="production", time_window_minutes=15
        )
        assert cmd.is_regex is True
        assert cmd.namespace == "production"
        assert cmd.time_window_minutes == 15
