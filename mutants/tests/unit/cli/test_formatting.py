"""Unit tests for CLI presentation formatting."""

from __future__ import annotations

from hexawyn.cli.presentation.formatting import app_version, compact_project_directory


class TestFormatting:
    def test_app_version_returns_string(self) -> None:
        result = app_version()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_compact_project_directory_returns_string(self) -> None:
        result = compact_project_directory()
        assert isinstance(result, str)
