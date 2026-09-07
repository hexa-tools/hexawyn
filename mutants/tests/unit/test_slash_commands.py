"""Unit tests for slash-command detection in the TUI."""

from __future__ import annotations

from hexawyn.cli.presentation.slash_commands import is_cloud_providers_command


class TestIsCloudProvidersCommand:
    def test_providers(self) -> None:
        assert is_cloud_providers_command("/providers") is True

    def test_not_providers(self) -> None:
        assert is_cloud_providers_command("/context") is False
        assert is_cloud_providers_command("/token") is False
