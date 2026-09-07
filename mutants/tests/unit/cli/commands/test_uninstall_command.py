"""Unit tests for cli/commands/uninstall_command.py — hexa uninstall."""

from __future__ import annotations

from unittest.mock import patch

from click.testing import CliRunner
from hexawyn.cli.commands.uninstall_command import _detect_installer, uninstall


class TestDetectInstaller:
    def test_pipx_when_executable_in_pipx_venv(self) -> None:
        with (
            patch("shutil.which", return_value="/usr/bin/pipx"),
            patch("sys.executable", "/home/djepeno/.local/share/pipx/venvs/hexawyn/bin/python"),
        ):
            assert _detect_installer() == "pipx"

    def test_pipx_when_executable_contains_pipx_venvs(self) -> None:
        with (
            patch("shutil.which", return_value="/usr/bin/pipx"),
            patch("sys.executable", "/opt/pipx/venvs/hexawyn/bin/python"),
        ):
            assert _detect_installer() == "pipx"

    def test_pip_when_pipx_not_installed(self) -> None:
        with (
            patch("shutil.which", return_value=None),
            patch("sys.executable", "/home/user/venv/bin/python"),
        ):
            assert _detect_installer() == "pip"

    def test_pip_when_not_in_pipx_venv(self) -> None:
        with (
            patch("shutil.which", return_value="/usr/bin/pipx"),
            patch("sys.executable", "/home/user/venv/bin/python"),
        ):
            assert _detect_installer() == "pip"


class TestUninstallCommand:
    def test_uninstall_via_pipx(self) -> None:
        """When installed via pipx, run `pipx uninstall hexawyn` on stdout."""
        with (
            patch(
                "hexawyn.cli.commands.uninstall_command._detect_installer",
                return_value="pipx",
            ),
            patch("subprocess.run") as mock_run,
        ):
            mock_run.return_value.returncode = 0
            result = CliRunner().invoke(uninstall)

        assert result.exit_code == 0
        mock_run.assert_called_once()
        assert mock_run.call_args.args[0] == ["pipx", "uninstall", "hexawyn"]

    def test_uninstall_via_pip(self) -> None:
        """When installed via pip, run `pip uninstall -y hexawyn` on stdout."""
        with (
            patch(
                "hexawyn.cli.commands.uninstall_command._detect_installer",
                return_value="pip",
            ),
            patch("subprocess.run") as mock_run,
        ):
            mock_run.return_value.returncode = 0
            result = CliRunner().invoke(uninstall)

        assert result.exit_code == 0
        mock_run.assert_called_once()
        assert mock_run.call_args.args[0] == ["pip", "uninstall", "-y", "hexawyn"]

    def test_uninstall_exit_code_passthrough(self) -> None:
        """A failing subprocess propagates a non-zero exit code."""
        with (
            patch(
                "hexawyn.cli.commands.uninstall_command._detect_installer",
                return_value="pipx",
            ),
            patch("subprocess.run") as mock_run,
        ):
            mock_run.return_value.returncode = 1
            result = CliRunner().invoke(uninstall)

        assert result.exit_code == 1

    def test_uninstall_missing_installer(self) -> None:
        """A missing pipx/pip binary fails gracefully with exit code 1."""
        with (
            patch(
                "hexawyn.cli.commands.uninstall_command._detect_installer",
                return_value="pipx",
            ),
            patch("subprocess.run", side_effect=FileNotFoundError("pipx not found")),
        ):
            result = CliRunner().invoke(uninstall)

        assert result.exit_code == 1
