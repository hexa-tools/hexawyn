"""Unit tests for TokenInputScreen using Textual Pilot."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from textual.widgets import Button, Input, Static


class TestTokenInputScreen:
    @pytest.mark.asyncio
    async def test_compose_renders_without_existing_license(self) -> None:
        with patch("hexawyn.cli.screens.token_input._get_current_plan", return_value=None):
            from hexawyn.cli.screens.token_input import TokenInputScreen
            from hexawyn.cli.tui import HexawynTUI

            app = HexawynTUI(adapter=MagicMock(), demo_mode=True)
            async with app.run_test() as pilot:
                app.push_screen(TokenInputScreen())
                await pilot.pause()

                title = app.query_one("#token-picker-title", Static)
                assert "Activate" in str(title.renderable)
                assert app.query_one("#token-input", Input)
                assert app.query_one("#token-activate", Button)
                assert app.query_one("#token-cancel", Button)

    @pytest.mark.asyncio
    async def test_compose_shows_current_plan_when_license_exists(self) -> None:
        with patch(
            "hexawyn.cli.screens.token_input._get_current_plan",
            return_value="team",
        ):
            from hexawyn.cli.screens.token_input import TokenInputScreen
            from hexawyn.cli.tui import HexawynTUI

            app = HexawynTUI(adapter=MagicMock(), demo_mode=True)
            async with app.run_test() as pilot:
                app.push_screen(TokenInputScreen())
                await pilot.pause()

                help_text = app.query_one("#token-picker-help", Static)
                assert "team" in str(help_text.renderable)
                assert "Currently activated" in str(help_text.renderable)

    @pytest.mark.asyncio
    async def test_cancel_button_dismisses_with_none(self) -> None:
        with patch("hexawyn.cli.screens.token_input._get_current_plan", return_value=None):
            from hexawyn.cli.screens.token_input import TokenInputScreen
            from hexawyn.cli.tui import HexawynTUI

            app = HexawynTUI(adapter=MagicMock(), demo_mode=True)
            async with app.run_test() as pilot:
                app.push_screen(TokenInputScreen())
                await pilot.pause()

                await pilot.click("#token-cancel")
                await pilot.pause()

                assert not app.query(TokenInputScreen)

    @pytest.mark.asyncio
    async def test_activate_with_empty_token_shows_error(self) -> None:
        with patch("hexawyn.cli.screens.token_input._get_current_plan", return_value=None):
            from hexawyn.cli.screens.token_input import TokenInputScreen
            from hexawyn.cli.tui import HexawynTUI

            app = HexawynTUI(adapter=MagicMock(), demo_mode=True)
            async with app.run_test() as pilot:
                app.push_screen(TokenInputScreen())
                await pilot.pause()

                await pilot.click("#token-activate")
                await pilot.pause()

                status = app.query_one("#token-status", Static)
                assert "enter your token" in str(status.renderable).lower()

    @pytest.mark.asyncio
    async def test_activate_with_invalid_token_format_shows_error(self) -> None:
        with patch("hexawyn.cli.screens.token_input._get_current_plan", return_value=None):
            from hexawyn.cli.screens.token_input import TokenInputScreen
            from hexawyn.cli.tui import HexawynTUI

            app = HexawynTUI(adapter=MagicMock(), demo_mode=True)
            async with app.run_test() as pilot:
                app.push_screen(TokenInputScreen())
                await pilot.pause()

                token_input = app.query_one("#token-input", Input)
                token_input.value = "bad_token_format"
                await pilot.click("#token-activate")
                await pilot.pause()

                status = app.query_one("#token-status", Static)
                assert "hxw_" in str(status.renderable).lower()

    @pytest.mark.asyncio
    async def test_activate_successful_flow(self) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "token": "jwt-token",
            "plan": "team",
            "expires_at": "2026-08-17T00:00:00Z",
        }

        fake_client = MagicMock()
        fake_client.__aenter__ = AsyncMock(return_value=fake_client)
        fake_client.__aexit__ = AsyncMock(return_value=None)
        fake_client.post = AsyncMock(return_value=mock_response)

        with (
            patch(
                "hexawyn.cli.screens.token_input._get_current_plan",
                return_value=None,
            ),
            patch("httpx.AsyncClient", return_value=fake_client),
            patch(
                "hexawyn.infrastructure.config.machine_id.get_machine_id",
                return_value="machine-123",
            ),
            patch("pathlib.Path.mkdir"),
            patch("pathlib.Path.write_text"),
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={},
            ),
            patch("hexawyn.infrastructure.config.config_manager.save_config"),
        ):
            from hexawyn.cli.screens.token_input import TokenInputScreen
            from hexawyn.cli.tui import HexawynTUI

            app = HexawynTUI(adapter=MagicMock(), demo_mode=True)
            async with app.run_test() as pilot:
                app.push_screen(TokenInputScreen())
                await pilot.pause()

                token_input = app.query_one("#token-input", Input)
                token_input.value = "hxw_test_valid_token_123"
                await pilot.click("#token-activate")
                await pilot.pause()
                await pilot.pause()

                status = app.query_one("#token-status", Static)
                assert "team" in str(status.renderable)
                assert "License activated" in str(status.renderable)

    @pytest.mark.asyncio
    async def test_activate_connection_error_shows_error(self) -> None:
        import httpx

        fake_client = MagicMock()
        fake_client.__aenter__ = AsyncMock(return_value=fake_client)
        fake_client.__aexit__ = AsyncMock(return_value=None)
        fake_client.post = AsyncMock(side_effect=httpx.ConnectError("refused"))

        with (
            patch(
                "hexawyn.cli.screens.token_input._get_current_plan",
                return_value=None,
            ),
            patch("httpx.AsyncClient", return_value=fake_client),
            patch(
                "hexawyn.infrastructure.config.machine_id.get_machine_id",
                return_value="machine-123",
            ),
        ):
            from hexawyn.cli.screens.token_input import TokenInputScreen
            from hexawyn.cli.tui import HexawynTUI

            app = HexawynTUI(adapter=MagicMock(), demo_mode=True)
            async with app.run_test() as pilot:
                app.push_screen(TokenInputScreen())
                await pilot.pause()

                token_input = app.query_one("#token-input", Input)
                token_input.value = "hxw_test_token"
                await pilot.click("#token-activate")
                await pilot.pause()

                status = app.query_one("#token-status", Static)
                assert "failed" in str(status.renderable).lower()

    @pytest.mark.asyncio
    async def test_activate_401_response_shows_error(self) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.json.return_value = {"detail": "Invalid API key"}

        fake_client = MagicMock()
        fake_client.__aenter__ = AsyncMock(return_value=fake_client)
        fake_client.__aexit__ = AsyncMock(return_value=None)
        fake_client.post = AsyncMock(return_value=mock_response)

        with (
            patch(
                "hexawyn.cli.screens.token_input._get_current_plan",
                return_value=None,
            ),
            patch("httpx.AsyncClient", return_value=fake_client),
            patch(
                "hexawyn.infrastructure.config.machine_id.get_machine_id",
                return_value="machine-123",
            ),
        ):
            from hexawyn.cli.screens.token_input import TokenInputScreen
            from hexawyn.cli.tui import HexawynTUI

            app = HexawynTUI(adapter=MagicMock(), demo_mode=True)
            async with app.run_test() as pilot:
                app.push_screen(TokenInputScreen())
                await pilot.pause()

                token_input = app.query_one("#token-input", Input)
                token_input.value = "hxw_test_token"
                await pilot.click("#token-activate")
                await pilot.pause()

                status = app.query_one("#token-status", Static)
                assert "Invalid API key" in str(status.renderable)

    @pytest.mark.asyncio
    async def test_escape_dismisses_screen(self) -> None:
        with patch("hexawyn.cli.screens.token_input._get_current_plan", return_value=None):
            from hexawyn.cli.screens.token_input import TokenInputScreen
            from hexawyn.cli.tui import HexawynTUI

            app = HexawynTUI(adapter=MagicMock(), demo_mode=True)
            async with app.run_test() as pilot:
                app.push_screen(TokenInputScreen())
                await pilot.pause()

                await pilot.press("escape")
                await pilot.pause()

                assert not app.query(TokenInputScreen)

    def test_get_current_plan_returns_none_when_no_file(self) -> None:
        with patch.object(Path, "exists", return_value=False):
            from hexawyn.cli.screens.token_input import _get_current_plan

            assert _get_current_plan() is None

    def test_get_current_plan_returns_plan_from_valid_jwt(self) -> None:
        import base64
        import json

        payload = {"plan": "scale_up"}
        payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")
        jwt_content = f"header.{payload_b64}.signature"

        with (
            patch.object(Path, "exists", return_value=True),
            patch.object(Path, "read_text", return_value=jwt_content),
        ):
            from hexawyn.cli.screens.token_input import _get_current_plan

            assert _get_current_plan() == "scale_up"

    def test_get_current_plan_returns_none_for_corrupt_jwt(self) -> None:
        with (
            patch.object(Path, "exists", return_value=True),
            patch.object(Path, "read_text", return_value="not.a.valid.jwt"),
        ):
            from hexawyn.cli.screens.token_input import _get_current_plan

            assert _get_current_plan() is None

    def test_get_current_plan_returns_none_for_invalid_base64(self) -> None:
        with (
            patch.object(Path, "exists", return_value=True),
            patch.object(Path, "read_text", return_value="header.!!!invalid!!!.sig"),
        ):
            from hexawyn.cli.screens.token_input import _get_current_plan

            assert _get_current_plan() is None

    def test_get_current_plan_returns_none_for_short_jwt(self) -> None:
        with (
            patch.object(Path, "exists", return_value=True),
            patch.object(Path, "read_text", return_value="only_one_part"),
        ):
            from hexawyn.cli.screens.token_input import _get_current_plan

            assert _get_current_plan() is None
