from __future__ import annotations

from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_command import (
    AdaptiveNamespaceInvestigationCommand,
)


class TestAdaptiveNamespaceInvestigationCommand:
    def test_defaults(self) -> None:
        cmd = AdaptiveNamespaceInvestigationCommand(namespace="production")
        assert cmd.depth == 3

    def test_custom_depth(self) -> None:
        cmd = AdaptiveNamespaceInvestigationCommand(namespace="production", depth=1)
        assert cmd.depth == 1
