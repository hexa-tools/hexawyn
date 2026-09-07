"""Unit tests for cli/commands/update_command.py — hexa update and hexa version."""

from __future__ import annotations

from unittest.mock import patch

from click.testing import CliRunner
from hexawyn.cli.commands.update_command import update, update_check, version


class TestVersionCommand:
    def test_prints_installed_version(self) -> None:
        result = CliRunner().invoke(version)

        assert result.exit_code == 0
        assert "hexawyn 0.1.0b20" in result.output


class TestResolveInstallIndex:
    def test_prod_index_needs_no_args(self) -> None:
        from hexawyn.cli.commands.update_command import resolve_install_index

        with patch(
            "hexawyn.cli.commands.update_command._resolve_index_url",
            return_value="https://pypi.org",
        ):
            assert resolve_install_index() == {"index_args": []}

    def test_testpypi_index_adds_index_and_extra_index(self) -> None:
        from hexawyn.cli.commands.update_command import resolve_install_index

        with patch(
            "hexawyn.cli.commands.update_command._resolve_index_url",
            return_value="https://test.pypi.org",
        ):
            result = resolve_install_index()
            assert "--index-url" in result["index_args"]
            assert "https://test.pypi.org/simple/" in result["index_args"]
            assert "--extra-index-url" in result["index_args"]
            assert "https://pypi.org/simple/" in result["index_args"]


class TestUpdateCheckCommand:
    def test_update_check_up_to_date(self) -> None:
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
        ):
            mock_check.return_value.status = "up_to_date"
            mock_check.return_value.current_version = "0.1.0b17"
            mock_check.return_value.latest_version = "0.1.0b17"

            result = CliRunner().invoke(update_check)

        assert result.exit_code == 0
        assert "up to date" in result.output

    def test_update_check_unknown(self) -> None:
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
        ):
            mock_check.return_value.status = "unknown"
            mock_check.return_value.error = "network unavailable"

            result = CliRunner().invoke(update_check)

        assert result.exit_code == 0
        assert "network unavailable" in result.output

    def test_update_check_available_prints_command(self) -> None:
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
            patch(
                "hexawyn.cli.commands.update_command._detect_installer",
                return_value="pipx",
            ),
            patch(
                "hexawyn.cli.commands.update_command.resolve_install_index",
                return_value={"index_args": []},
            ),
        ):
            mock_check.return_value.status = "update_available"
            mock_check.return_value.current_version = "0.1.0b9"
            mock_check.return_value.latest_version = "0.1.0b17"

            result = CliRunner().invoke(update_check)

        assert result.exit_code == 0
        assert "0.1.0b17" in result.output
        assert "pipx install" in result.output


class TestUpdateCommand:
    def test_update_available_shows_upgrade_hint(self) -> None:
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
            patch(
                "hexawyn.cli.commands.update_command._detect_installer",
                return_value="pipx",
            ),
            patch(
                "hexawyn.cli.commands.update_command.resolve_install_index",
                return_value={"index_args": []},
            ),
            patch("subprocess.run") as mock_run,
        ):
            mock_check.return_value.status = "update_available"
            mock_check.return_value.current_version = "0.1.0b9"
            mock_check.return_value.latest_version = "0.1.0b17"
            mock_run.return_value.returncode = 0

            result = CliRunner().invoke(update, input="y\n")

        assert result.exit_code == 0
        assert "0.1.0b17" in result.output
        assert "Update available" in result.output

    def test_up_to_date_shows_message(self) -> None:
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
        ):
            mock_check.return_value.status = "up_to_date"
            mock_check.return_value.current_version = "0.1.0b17"
            mock_check.return_value.latest_version = "0.1.0b17"

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

    def test_update_confirmed_pipx_installs(self) -> None:
        """Confirming install runs pipx with the right index args."""
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
            patch(
                "hexawyn.cli.commands.update_command._detect_installer",
                return_value="pipx",
            ),
            patch(
                "hexawyn.cli.commands.update_command.resolve_install_index",
                return_value={
                    "index_args": [
                        "--index-url",
                        "https://test.pypi.org/simple/",
                        "--extra-index-url",
                        "https://pypi.org/simple/",
                    ]
                },
            ),
            patch("subprocess.run") as mock_run,
        ):
            mock_check.return_value.status = "update_available"
            mock_check.return_value.current_version = "0.1.0b9"
            mock_check.return_value.latest_version = "0.1.0b17"
            mock_run.return_value.returncode = 0

            result = CliRunner().invoke(update, input="y\n")

        assert result.exit_code == 0
        assert mock_run.call_count == 1
        cmd = mock_run.call_args.args[0]
        assert cmd[0:3] == ["pipx", "install", "--force"]
        assert "--pip-args" in cmd
        assert any("https://test.pypi.org/simple/" in part for part in cmd)

    def test_update_declined_prints_command_not_run(self) -> None:
        """Declining shows the upgrade command but does not run it."""
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
            patch(
                "hexawyn.cli.commands.update_command._detect_installer",
                return_value="pipx",
            ),
            patch(
                "hexawyn.cli.commands.update_command.resolve_install_index",
                return_value={"index_args": []},
            ),
            patch("subprocess.run") as mock_run,
        ):
            mock_check.return_value.status = "update_available"
            mock_check.return_value.current_version = "0.1.0b9"
            mock_check.return_value.latest_version = "0.1.0b17"
            mock_run.return_value.returncode = 0

            result = CliRunner().invoke(update, input="n\n")

        assert result.exit_code == 0
        mock_run.assert_not_called()
        assert "pipx" in result.output

    def test_update_check_prints_command_without_running(self) -> None:
        """update-check always prints the command without executing it."""
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
            patch(
                "hexawyn.cli.commands.update_command._detect_installer",
                return_value="pipx",
            ),
            patch(
                "hexawyn.cli.commands.update_command.resolve_install_index",
                return_value={"index_args": []},
            ),
            patch("subprocess.run") as mock_run,
        ):
            mock_check.return_value.status = "update_available"
            mock_check.return_value.current_version = "0.1.0b9"
            mock_check.return_value.latest_version = "0.1.0b17"
            mock_run.return_value.returncode = 0

            result = CliRunner().invoke(update_check)

        assert result.exit_code == 0
        mock_run.assert_not_called()
        assert "pipx install" in result.output

    def test_update_install_failure_exits_nonzero(self) -> None:
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
            patch(
                "hexawyn.cli.commands.update_command._detect_installer",
                return_value="pipx",
            ),
            patch(
                "hexawyn.cli.commands.update_command.resolve_install_index",
                return_value={"index_args": []},
            ),
            patch("subprocess.run") as mock_run,
        ):
            mock_check.return_value.status = "update_available"
            mock_check.return_value.current_version = "0.1.0b9"
            mock_check.return_value.latest_version = "0.1.0b17"
            mock_run.return_value.returncode = 1

            result = CliRunner().invoke(update, input="y\n")

        assert result.exit_code == 1

    def test_pip_install_command_uses_force_and_yes(self) -> None:
        """pip installs with --force-reinstall; pipx path used the force flag."""
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
            patch(
                "hexawyn.cli.commands.update_command._detect_installer",
                return_value="pip",
            ),
            patch(
                "hexawyn.cli.commands.update_command.resolve_install_index",
                return_value={"index_args": []},
            ),
            patch("subprocess.run") as mock_run,
        ):
            mock_check.return_value.status = "update_available"
            mock_check.return_value.current_version = "0.1.0b9"
            mock_check.return_value.latest_version = "0.1.0b17"
            mock_run.return_value.returncode = 0

            result = CliRunner().invoke(update, input="y\n")

        assert result.exit_code == 0
        assert mock_run.call_count == 1
        cmd = mock_run.call_args.args[0]
        assert cmd[0:4] == ["pip", "install", "--upgrade", "--force-reinstall"]

    def test_update_installer_missing_fails_gracefully(self) -> None:
        with (
            patch("hexawyn.cli.commands.update_command.check_for_update") as mock_check,
            patch("hexawyn.cli.commands.update_command.PyPIVersionAdapter"),
            patch(
                "hexawyn.cli.commands.update_command._detect_installer",
                return_value="pipx",
            ),
            patch(
                "hexawyn.cli.commands.update_command.resolve_install_index",
                return_value={"index_args": []},
            ),
            patch("subprocess.run", side_effect=FileNotFoundError("pipx not found")),
        ):
            mock_check.return_value.status = "update_available"
            mock_check.return_value.current_version = "0.1.0b9"
            mock_check.return_value.latest_version = "0.1.0b17"

            result = CliRunner().invoke(update, input="y\n")

        assert result.exit_code == 1
