from __future__ import annotations


class TestManualChangeOutsideGitOpsCommand:
    def test_defaults_window_days_to_seven(self) -> None:
        from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_command import (
            ManualChangeOutsideGitOpsCommand,
        )

        command = ManualChangeOutsideGitOpsCommand(namespace="production")

        assert command.namespace == "production"
        assert command.window_days == 7

    def test_accepts_custom_window_days(self) -> None:
        from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_command import (
            ManualChangeOutsideGitOpsCommand,
        )

        command = ManualChangeOutsideGitOpsCommand(namespace="production", window_days=3)

        assert command.window_days == 3
