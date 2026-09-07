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
        assert "v0.1.0b20" in result.output

    def test_subcommands_registered(self) -> None:
        from hexawyn.cli.main import app

        command_names = [cmd.name for cmd in app.commands.values()]
        assert "start" in command_names
        assert "auth" in command_names
        assert "claude" in command_names
        assert "codex" in command_names
        assert "opencode" in command_names
        assert "cursor" in command_names
        assert "gemini" in command_names
        assert "uninstall" in command_names
        assert "update-check" in command_names
        assert "login" not in command_names
        assert "setup" not in command_names

    def test_start_option_help(self) -> None:
        from hexawyn.cli.main import app

        runner = CliRunner()
        result = runner.invoke(app, ["start", "--help"])
        assert result.exit_code == 0
        assert "--demo" in result.output
        assert "--expert" in result.output
        assert "--scenario" in result.output
        assert "--no-cloud" in result.output


class TestStartCommand:
    def _invoke(self, args: tuple[str, ...]) -> tuple[int, str, dict[str, str | None]]:
        import os as _os
        from unittest.mock import patch

        from hexawyn.cli.main import app

        runner = CliRunner()
        with patch.dict(_os.environ, {}, clear=True):
            result = runner.invoke(app, list(args))
            snapshot = {
                k: _os.environ.get(k)
                for k in ("HEXAWYN_RUNTIME_MODE", "HEXAWYN_DEMO_MODE", "HEXAWYN_DEMO_SCENARIO")
            }
        return result.exit_code, result.output, snapshot

    def test_no_cloud_skips_auth_and_opens(self) -> None:
        from unittest.mock import patch

        with (
            patch("hexawyn.cli.main._cloud_auth_ready") as auth,
            patch("hexawyn.cli.app.HexawynApp") as cli_app,
        ):
            code, _, env = self._invoke(("start", "--no-cloud"))

        auth.assert_not_called()
        cli_app.assert_called_once_with(expert_mode=False)
        cli_app.return_value.run.assert_called_once()
        assert env["HEXAWYN_RUNTIME_MODE"] == "embedded"

    def test_valid_token_keeps_cloud_mode(self) -> None:
        from unittest.mock import patch

        with (
            patch("hexawyn.cli.main._cloud_auth_ready", return_value=True) as auth,
            patch("hexawyn.cli.app.HexawynApp") as cli_app,
        ):
            code, _, env = self._invoke(("start",))

        auth.assert_called_once()
        cli_app.return_value.run.assert_called_once()
        assert code == 0
        assert env["HEXAWYN_RUNTIME_MODE"] is None

    def test_invalid_token_falls_back_to_embedded(self) -> None:
        from unittest.mock import patch

        with (
            patch("hexawyn.cli.main._cloud_auth_ready", return_value=False) as auth,
            patch("hexawyn.cli.app.HexawynApp") as cli_app,
        ):
            code, _, env = self._invoke(("start",))

        auth.assert_called_once()
        cli_app.return_value.run.assert_called_once()
        assert env["HEXAWYN_RUNTIME_MODE"] == "embedded"

    def test_demo_bypasses_auth(self) -> None:
        from unittest.mock import patch

        with (
            patch("hexawyn.cli.main._cloud_auth_ready") as auth,
            patch("hexawyn.cli.app.HexawynApp") as cli_app,
        ):
            code, _, env = self._invoke(("start", "--demo"))

        auth.assert_not_called()
        cli_app.return_value.run.assert_called_once()
        assert env["HEXAWYN_DEMO_MODE"] == "true"


class TestStartInternals:
    def test_cloud_auth_ready_true_on_valid(self, monkeypatch) -> None:
        from hexawyn.cli import main
        from hexawyn.domain.models.auth import LoginOutcome

        class _FakeService:
            def __init__(self, *args: object, **kwargs: object) -> None:
                pass

            def authenticate(self) -> LoginOutcome:
                return LoginOutcome.AUTHENTICATED

        monkeypatch.setattr("hexawyn.application.service.login_service.LoginService", _FakeService)
        assert main._cloud_auth_ready() is True

    def test_cloud_auth_ready_false_on_invalid(self, monkeypatch) -> None:
        from hexawyn.cli import main
        from hexawyn.domain.models.auth import LoginOutcome

        class _FakeService:
            def __init__(self, *args: object, **kwargs: object) -> None:
                pass

            def authenticate(self) -> LoginOutcome:
                return LoginOutcome.INVALID_TOKEN

        monkeypatch.setattr("hexawyn.application.service.login_service.LoginService", _FakeService)
        assert main._cloud_auth_ready() is False

    def test_prompt_token_returns_value(self) -> None:
        from unittest.mock import patch

        from hexawyn.cli.main import _prompt_token

        with patch("hexawyn.cli.main.click.prompt", return_value="hxw_x"):
            assert _prompt_token() == "hxw_x"

    def test_prompt_token_returns_none_on_abort(self) -> None:
        from unittest.mock import patch

        import click
        from hexawyn.cli.main import _prompt_token

        with patch("hexawyn.cli.main.click.prompt", side_effect=click.Abort()):
            assert _prompt_token() is None

    def test_prompt_token_returns_none_on_keyboard_interrupt(self) -> None:
        # A real TTY raises KeyboardInterrupt (not click.Abort) from the raw
        # getpass read — Ctrl+C must still fall through to local/BYOK mode.
        from unittest.mock import patch

        from hexawyn.cli.main import _prompt_token

        with patch("hexawyn.cli.main.click.prompt", side_effect=KeyboardInterrupt()):
            assert _prompt_token() is None
