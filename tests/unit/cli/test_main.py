from __future__ import annotations

from click.testing import CliRunner


class TestAppGroup:
    def test_app_group_help(self) -> None:
        from hexawyn.cli.main import app

        runner = CliRunner()
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0

    def test_bare_invoke_shows_logo_header(self) -> None:
        from hexawyn.cli.main import app

        runner = CliRunner()
        result = runner.invoke(app, [])

        assert result.exit_code == 0
        assert "█" in result.output
        assert "v0.1.0b17" in result.output

    def test_subcommands_registered(self) -> None:
        from hexawyn.cli.main import app

        command_names = [cmd.name for cmd in app.commands.values()]
        assert "start" in command_names
        assert "setup" in command_names
        assert "claude" in command_names
        assert "codex" in command_names
        assert "opencode" in command_names
        assert "cursor" in command_names
        assert "gemini" in command_names
        assert "uninstall" in command_names
        assert "update-check" in command_names

    def test_start_option_help(self) -> None:
        from hexawyn.cli.main import app

        runner = CliRunner()
        result = runner.invoke(app, ["start", "--help"])
        assert result.exit_code == 0
        assert "--demo" in result.output
        assert "--expert" in result.output
        assert "--scenario" in result.output
