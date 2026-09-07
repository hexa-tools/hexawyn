"""Unit tests for the /providers CloudProvidersScreen (TUI) via Textual run_test."""

from __future__ import annotations

import asyncio
from types import SimpleNamespace
from unittest.mock import patch

from hexawyn.cli.screens.cloud_providers import CloudProvidersScreen
from textual.app import App
from textual.widgets import Input, Static


class _HostApp(App[None]):
    """Minimal host that pushes the CloudProvidersScreen."""

    def __init__(self) -> None:
        super().__init__()
        self.provider_screen = CloudProvidersScreen()

    def on_mount(self) -> None:
        self.push_screen(self.provider_screen)


def _run(coro: object) -> None:
    asyncio.run(coro)  # type: ignore[arg-type]


async def _press(screen: CloudProvidersScreen, button_id: str) -> None:
    await screen.on_button_pressed(
        SimpleNamespace(button=SimpleNamespace(id=button_id))  # type: ignore[arg-type]
    )


def test_composes_and_renders_aws_fields() -> None:
    async def _go() -> None:
        app = _HostApp()
        async with app.run_test() as pilot:
            await pilot.pause()
            ids = {i.id for i in app.provider_screen.query("Input")}
            assert {"field-access_key", "field-secret_key", "field-region"} <= ids

    _run(_go())


def test_save_stores_values() -> None:
    async def _go() -> None:
        app = _HostApp()
        with (
            patch("hexawyn.cli.screens.cloud_providers.set_provider_credentials") as save,
            patch("hexawyn.cli.screens.cloud_providers.apply_provider_env") as apply_env,
        ):
            async with app.run_test() as pilot:
                await pilot.pause()
                await _press(app.provider_screen, "provider-gcp")
                await pilot.pause()
                assert {"field-credentials_file"} <= {
                    i.id for i in app.provider_screen.query("Input")
                }

                await _press(app.provider_screen, "provider-aws")
                await pilot.pause()
                app.provider_screen.query_one("#field-access_key", Input).value = "AKIA"
                app.provider_screen.query_one("#field-secret_key", Input).value = "s3cr3t"
                app.provider_screen._save()

        save.assert_called_once_with("aws", {"access_key": "AKIA", "secret_key": "s3cr3t"})
        apply_env.assert_called_once_with("aws")

    _run(_go())


def test_clear_revokes_provider() -> None:
    async def _go() -> None:
        app = _HostApp()
        with patch("hexawyn.cli.screens.cloud_providers.clear_provider_credentials") as clear:
            async with app.run_test() as pilot:
                await pilot.pause()
                await _press(app.provider_screen, "providers-clear")

        clear.assert_called_once_with("aws")

    _run(_go())


def test_lists_providers_with_status() -> None:
    async def _go() -> None:
        app = _HostApp()
        with patch(
            "hexawyn.cli.screens.cloud_providers.get_provider_credentials",
            return_value={"aws": {"access_key": "AKIA"}, "gcp": {}},
        ):
            async with app.run_test() as pilot:
                await pilot.pause()
                lines = [str(line.render()) for line in app.provider_screen.query(".provider-btn")]

        joined = "\n".join(lines)
        assert "aws" in joined
        assert "gcp" in joined
        assert "✔" in joined  # aws marked as creds set


def test_arrow_keys_step_through_providers() -> None:
    async def _go() -> None:
        app = _HostApp()
        async with app.run_test() as pilot:
            await pilot.pause()
            assert app.provider_screen._selected == "aws"
            await app.provider_screen.action_next_provider()
            assert app.provider_screen._selected == "gcp"
            await app.provider_screen.action_next_provider()
            assert app.provider_screen._selected == "azure"
            await app.provider_screen.action_prev_provider()
            assert app.provider_screen._selected == "gcp"
            await app.provider_screen.action_next_provider()
            assert app.provider_screen._selected == "azure"
            await app.provider_screen.action_next_provider()
            assert app.provider_screen._selected == "datadog"
            await app.provider_screen.action_next_provider()
            assert app.provider_screen._selected == "aws"  # wraps

    _run(_go())


def test_cancel_button_and_action_dismiss() -> None:
    async def _go() -> None:
        app = _HostApp()
        with patch.object(app.provider_screen, "dismiss") as dismiss:
            async with app.run_test() as pilot:
                await pilot.pause()
                app.provider_screen.action_cancel()
                dismiss.assert_called_once_with(None)
                dismiss.reset_mock()
                await _press(app.provider_screen, "providers-cancel")
                dismiss.assert_called_once_with(None)

    _run(_go())


def test_save_with_empty_fields_shows_prompt() -> None:
    async def _go() -> None:
        app = _HostApp()
        with patch("hexawyn.cli.screens.cloud_providers.set_provider_credentials") as save:
            async with app.run_test() as pilot:
                await pilot.pause()
                await _press(app.provider_screen, "providers-save")
                status = app.provider_screen.query_one("#providers-status", Static).render()
                assert "Enter at least one" in str(status)
                save.assert_not_called()

    _run(_go())


def test_render_fields_unknown_provider_shows_fallback() -> None:
    async def _go() -> None:
        app = _HostApp()
        async with app.run_test() as pilot:
            await pilot.pause()
            await app.provider_screen._render_fields("unknown")
            texts = [str(s.render()) for s in app.provider_screen.query(".provider-label")]
            assert any("no credentials" in t for t in texts)

    _run(_go())


def test_focus_provider_handles_missing_widget() -> None:
    async def _go() -> None:
        app = _HostApp()
        async with app.run_test() as pilot:
            await pilot.pause()
            app.provider_screen._focus_provider("nonexistent")  # must not raise

    _run(_go())


def test_render_status_shows_creds_when_set() -> None:
    async def _go() -> None:
        app = _HostApp()
        with patch(
            "hexawyn.cli.screens.cloud_providers.get_provider_credentials",
            return_value={"aws": {"access_key": "AKIA"}},
        ):
            async with app.run_test() as pilot:
                await pilot.pause()
                status = app.provider_screen.query_one("#providers-status", Static).render()
                assert "creds set" in str(status)

    _run(_go())
