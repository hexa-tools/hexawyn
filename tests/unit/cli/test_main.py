from __future__ import annotations

from click.testing import CliRunner


class TestAppGroup:
    def test_app_group_help(self) -> None:
        from hexawyn.cli.main import app

        runner = CliRunner()
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0

    def test_subcommands_registered(self) -> None:
        from hexawyn.cli.main import app

        command_names = [cmd.name for cmd in app.commands.values()]
        assert "start" in command_names
        assert "setup" in command_names

    def test_start_option_help(self) -> None:
        from hexawyn.cli.main import app

        runner = CliRunner()
        result = runner.invoke(app, ["start", "--help"])
        assert result.exit_code == 0
        assert "--demo" in result.output
        assert "--expert" in result.output
        assert "--scenario" in result.output
