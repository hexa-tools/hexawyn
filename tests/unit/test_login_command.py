"""Unit tests for the hexa login command."""

from __future__ import annotations

from unittest.mock import patch

import click
from click.testing import CliRunner
from hexawyn.cli.commands.login_command import login
from hexawyn.domain.models.auth import LoginOutcome


class _FakeService:
    def __init__(self, outcome: LoginOutcome) -> None:
        self.outcome = outcome
        self.calls = 0

    def authenticate(self) -> LoginOutcome:
        self.calls += 1
        return self.outcome


class TestLoginCommand:
    def _invoke(self, outcome: LoginOutcome) -> tuple[int, _FakeService]:
        fake = _FakeService(outcome)
        with patch("hexawyn.cli.commands.login_command._build_service", return_value=fake):
            result = CliRunner().invoke(login)
        return result.exit_code, fake

    def test_command_exists_and_named_login(self) -> None:
        assert login.name == "login"

    def test_success_exit_zero(self) -> None:
        code, fake = self._invoke(LoginOutcome.AUTHENTICATED)
        assert code == 0
        assert fake.calls == 1

    def test_existing_valid_exit_zero(self) -> None:
        code, _ = self._invoke(LoginOutcome.STARTED_WITH_EXISTING)
        assert code == 0

    def test_cancelled_exit_zero(self) -> None:
        code, _ = self._invoke(LoginOutcome.CANCELLED)
        assert code == 0

    def test_invalid_token_exit_one(self) -> None:
        code, _ = self._invoke(LoginOutcome.INVALID_TOKEN)
        assert code == 1

    def test_unavailable_exit_one(self) -> None:
        code, _ = self._invoke(LoginOutcome.UNAVAILABLE)
        assert code == 1


class TestLoginRegistered:
    def test_login_is_registered_on_main_app(self) -> None:
        from hexawyn.cli.main import app

        assert "login" in app.commands


class TestLoginCommandWiring:
    def test_build_service_wires_cloud_auth_port(self) -> None:
        from hexawyn.application.ports.driven.cloud_auth_port import CloudAuthPort
        from hexawyn.application.service.login_service import LoginService
        from hexawyn.cli.commands.login_command import _build_service

        service = _build_service()
        assert isinstance(service, LoginService)
        assert isinstance(service._auth, CloudAuthPort)

    def test_prompt_token_returns_value(self) -> None:
        from hexawyn.cli.commands.login_command import _prompt_token

        with patch("hexawyn.cli.commands.login_command.click.prompt", return_value="hxw_x"):
            assert _prompt_token() == "hxw_x"

    def test_prompt_token_returns_none_on_abort(self) -> None:
        from hexawyn.cli.commands.login_command import _prompt_token

        with patch("hexawyn.cli.commands.login_command.click.prompt", side_effect=click.Abort()):
            assert _prompt_token() is None
