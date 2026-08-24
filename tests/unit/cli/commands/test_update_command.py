"""Unit tests for cli/commands/update_command.py — hexa update and hexa version."""

from __future__ import annotations

from unittest.mock import patch

from click.testing import CliRunner
from hexawyn.cli.commands.update_command import update, version


class TestVersionCommand:
    def test_prints_installed_version(self) -> None:
        result = CliRunner().invoke(version)

        assert result.exit_code == 0
        assert "hexawyn 0.1.0b8" in result.output


class TestUpdateCommand:
    def test_update_available_shows_upgrade_hint(self) -> None:
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
        ):
            mock_check.return_value.status = "update_available"
            mock_check.return_value.current_version = "0.1.0b3"
            mock_check.return_value.latest_version = "0.1.0b4"

            result = CliRunner().invoke(update)

        assert result.exit_code == 0
        assert "0.1.0b4" in result.output
        assert "Update available" in result.output

    def test_up_to_date_shows_message(self) -> None:
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
        ):
            mock_check.return_value.status = "up_to_date"
            mock_check.return_value.current_version = "0.1.0b4"
            mock_check.return_value.latest_version = "0.1.0b4"

            result = CliRunner().invoke(update)

        assert result.exit_code == 0
        assert "up to date" in result.output

    def test_unknown_shows_error_message(self) -> None:
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
        ):
            mock_check.return_value.status = "unknown"
            mock_check.return_value.error = "network unavailable"

            result = CliRunner().invoke(update)

        assert result.exit_code == 0
        assert "network unavailable" in result.output
