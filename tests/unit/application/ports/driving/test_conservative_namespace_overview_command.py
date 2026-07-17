from __future__ import annotations

from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_command import (
    ConservativeNamespaceOverviewCommand,
)


class TestConservativeNamespaceOverviewCommand:
    def test_defaults(self) -> None:
        cmd = ConservativeNamespaceOverviewCommand(namespace="staging")
        assert cmd.max_tokens == 2000

    def test_custom_max_tokens(self) -> None:
        cmd = ConservativeNamespaceOverviewCommand(namespace="staging", max_tokens=500)
        assert cmd.max_tokens == 500
