from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.cli.screens.session import SessionScreen


class TestSessionScreen:
    @staticmethod
    def _create_screen(initial_command: str | None = None) -> SessionScreen:
        with patch("hexawyn.cli.screens.session.Screen.__init__", return_value=None):
            return SessionScreen(initial_command=initial_command)

    @staticmethod
    def _mock_tui(screen: SessionScreen, **attrs: object) -> MagicMock:
        mock_app = MagicMock()
        for k, v in attrs.items():
            setattr(mock_app, k, v)
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        return mock_app

    def test_init(self) -> None:
        screen = self._create_screen()
        assert screen.initial_command is None
        assert screen._history == []

    def test_init_with_initial_command(self) -> None:
        screen = self._create_screen(initial_command="/help")
        assert screen.initial_command == "/help"

    def test_tui_app_returns_app(self) -> None:
        screen = self._create_screen()
        from hexawyn.cli.tui import HexawynTUI

        mock_app = MagicMock(spec=HexawynTUI)
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        result = screen._tui_app()
        assert result is mock_app

    def test_aside_lines(self) -> None:
        screen = self._create_screen()
        mock_app = MagicMock()
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        with patch(
            "hexawyn.cli.screens.session.build_aside_lines", return_value=["line1", "line2"]
        ):
            result = screen._aside_lines()
            assert result == ["line1", "line2"]

    def test_action_manage_subscription_with_token(self) -> None:
        screen = self._create_screen()
        screen.notify = MagicMock()  # type: ignore[method-assign]
        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "hxw_abc"},
            ),
            patch("webbrowser.open") as mock_wb,
        ):
            screen.action_manage_subscription()
            mock_wb.assert_called_once()
            assert "hxw_abc" in mock_wb.call_args[0][0]

    def test_action_manage_subscription_without_token(self) -> None:
        screen = self._create_screen()
        screen.notify = MagicMock()  # type: ignore[method-assign]
        with (
            patch("hexawyn.infrastructure.config.config_manager.load_config", return_value={}),
            patch("webbrowser.open") as mock_wb,
        ):
            screen.action_manage_subscription()
            mock_wb.assert_called_once_with("https://hexawyn.com/account/manage")

    def test_on_unmount_cancels_refresh_task(self) -> None:
        screen = self._create_screen()
        mock_task = MagicMock()
        screen._refresh_task = mock_task
        screen.on_unmount()
        mock_task.cancel.assert_called_once()

    def test_on_unmount_no_task(self) -> None:
        screen = self._create_screen()
        screen._refresh_task = None
        screen.on_unmount()

    def test_on_input_changed_noop(self) -> None:
        screen = self._create_screen()
        screen.on_input_changed(MagicMock())

    def test_license_aside_lines(self) -> None:
        screen = self._create_screen()
        with patch("hexawyn.cli.screens.session.format_license_aside_lines", return_value=["lic1"]):
            result = screen._license_aside_lines()
            assert result == ["lic1"]

    def test_requested_context_name_delegates(self) -> None:
        screen = self._create_screen()
        with patch("hexawyn.cli.screens.session.extract_requested_context", return_value="prod"):
            result = screen._requested_context_name("/context prod")
            assert result == "prod"

    def test_available_contexts_with_service(self) -> None:
        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.context_service = MagicMock()
        mock_app.context_service.discover.return_value = [MagicMock()]
        mock_app.startup_status = None
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        result = screen._available_contexts()
        assert len(result) == 1

    def test_available_contexts_with_startup_status(self) -> None:
        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.context_service = None
        mock_app.startup_status = MagicMock()
        mock_app.startup_status.contexts = [MagicMock()]
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        result = screen._available_contexts()
        assert len(result) == 1

    def test_available_contexts_empty(self) -> None:
        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.context_service = None
        mock_app.startup_status = None
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        result = screen._available_contexts()
        assert result == []

    def test_switch_context_no_service(self) -> None:
        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.context_service = None
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        mock_log = MagicMock()
        screen.query_one = MagicMock(return_value=mock_log)  # type: ignore[method-assign]
        with patch("hexawyn.cli.screens.session.render_lines") as mock_render:
            screen._switch_context("prod")
            mock_render.assert_called_once()

    def test_switch_context_success(self) -> None:
        screen = self._create_screen()
        mock_svc = MagicMock()
        mock_switch = MagicMock()
        mock_switch.switched = True
        mock_switch.current_context = MagicMock()
        mock_switch.current_context.name = "prod"
        mock_switch.contexts = []
        mock_svc.switch_context.return_value = mock_switch
        mock_app = MagicMock()
        mock_app.context_service = mock_svc
        mock_app.adapter_builder = MagicMock()
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        mock_log = MagicMock()
        screen.query_one = MagicMock(return_value=mock_log)  # type: ignore[method-assign]
        with (
            patch("hexawyn.cli.screens.session.startup_status_from_switch"),
            patch("hexawyn.cli.screens.session.format_context_switch_lines", return_value=[]),
        ):
            screen._switch_context("prod")
            mock_app.adapter_builder.assert_called_once()

    def test_switch_context_failed_switch(self) -> None:
        screen = self._create_screen()
        mock_svc = MagicMock()
        mock_switch = MagicMock()
        mock_switch.switched = False
        mock_switch.current_context = None
        mock_switch.contexts = []
        mock_svc.switch_context.return_value = mock_switch
        mock_app = MagicMock()
        mock_app.context_service = mock_svc
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        mock_log = MagicMock()
        screen.query_one = MagicMock(return_value=mock_log)  # type: ignore[method-assign]
        with patch(
            "hexawyn.cli.screens.session.missing_context_lines", return_value=[("missing", "red")]
        ):
            screen._switch_context("prod")

    def test_switch_context_none_context_name(self) -> None:
        screen = self._create_screen()
        screen._switch_context(None)

    def test_handle_stack_command(self) -> None:
        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.cluster_name = "prod"
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        mock_log = MagicMock()
        with (
            patch("hexawyn.cli.presentation.stack_view.run_stack_command", return_value=["output"]),
            patch("hexawyn.cli.screens.session.render_lines") as mock_render,
        ):
            screen._handle_stack_command("/stack", mock_log)
            mock_render.assert_called_once()

    def test_refresh_footer(self) -> None:
        screen = self._create_screen()
        mock_footer = MagicMock()
        screen.query_one = MagicMock(return_value=mock_footer)  # type: ignore[method-assign]
        with (
            patch("hexawyn.infrastructure.license.license_reader.read_license_state") as mock_read,
            patch(
                "hexawyn.cli.screens.session.format_license_footer_hint",
                return_value="Ctrl+B manage",
            ),
        ):
            mock_read.return_value = MagicMock(state="active")
            screen._refresh_footer()
            mock_footer.update.assert_called_once()

    def test_start_background_license_refresh_creates_task(self) -> None:
        screen = self._create_screen()
        with patch("hexawyn.cli.screens.session.asyncio.create_task") as mock_create:
            screen._start_background_license_refresh()
            mock_create.assert_called_once()
            assert screen._refresh_task is not None

    def test_handle_context_command_no_service(self) -> None:
        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.context_service = None
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        mock_log = MagicMock()
        with patch("hexawyn.cli.screens.session.render_lines") as mock_render:
            import asyncio

            asyncio.run(screen._handle_context_command("/context", mock_log))
            mock_render.assert_called_once()

    def test_handle_context_command_with_name(self) -> None:
        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.context_service = MagicMock()
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        screen._switch_context = MagicMock()  # type: ignore[method-assign]
        mock_log = MagicMock()
        with patch("hexawyn.cli.screens.session.extract_requested_context", return_value="prod"):
            import asyncio

            asyncio.run(screen._handle_context_command("/context prod", mock_log))
            screen._switch_context.assert_called_once_with("prod")

    def test_open_context_picker(self) -> None:
        screen = self._create_screen()
        mock_app = MagicMock()
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        screen._available_contexts = MagicMock(return_value=[])  # type: ignore[method-assign]
        with patch("hexawyn.cli.screens.session.ContextPickerScreen") as mock_picker:
            import asyncio

            asyncio.run(screen._open_context_picker())
            mock_picker.assert_called_once()
            mock_app.push_screen.assert_called_once()

    def test_duration_rendered_in_status_bar_not_log(self) -> None:
        """The response duration is a transient status, not persistent log content."""
        import asyncio

        from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import (
            ChatCliResponse,
        )

        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.expert_mode = False
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        screen._refresh_aside = MagicMock()  # type: ignore[method-assign]

        mock_log = MagicMock()
        mock_status = MagicMock()
        screen.query_one = MagicMock(
            side_effect=lambda _id, _cls=None: mock_log if _id == "#conversation" else mock_status
        )  # type: ignore[method-assign]  # noqa: E501

        result = ChatCliResponse(kind="debug", lines=[("answer", "white")], duration_ms=25000)
        mock_route = MagicMock(return_value=result)

        with (
            patch("hexawyn.cli.screens.session.route_command", mock_route),
            patch("hexawyn.cli.screens.session.render_result"),
            patch("hexawyn.cli.screens.session.safe_findings", return_value=[]),
        ):
            asyncio.run(screen._handle_command("how many pods?"))

        calls = [str(c) for c in mock_log.write.call_args_list]
        assert not any("25.0s" in c for c in calls), "duration must not persist in log"
        status_calls = [str(c) for c in mock_status.update.call_args_list]
        assert any("25.0s" in c for c in status_calls), "duration must appear in status bar"

    def test_agentic_steps_rendered_in_normal_mode(self) -> None:
        """Agentic steps are shown during execution in normal mode too."""
        import asyncio
        from unittest.mock import PropertyMock

        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.expert_mode = False
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        screen._refresh_aside = MagicMock()  # type: ignore[method-assign]

        mock_log = MagicMock()
        mock_status = MagicMock()
        screen.query_one = MagicMock(
            side_effect=lambda _id, _cls=None: mock_log if _id == "#conversation" else mock_status
        )  # type: ignore[method-assign]  # noqa: E501

        from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import (
            ChatCliResponse,
        )

        result = ChatCliResponse(kind="debug", lines=[("answer", "white")], duration_ms=0)

        def fake_route(_text, _adapter, _history, on_progress=None):  # type: ignore[no-untyped-def]
            if on_progress:
                on_progress("plan", "Plan")
            return result

        with (
            patch("hexawyn.cli.screens.session.route_command", side_effect=fake_route),
            patch("hexawyn.cli.screens.session.render_result"),
            patch("hexawyn.cli.screens.session.safe_findings", return_value=[]),
            patch(
                "hexawyn.cli.screens.session.SessionScreen.app",
                new_callable=PropertyMock,
                return_value=MagicMock(),
            ) as mock_app_prop,
        ):
            mock_app_prop.return_value.call_from_thread = lambda fn, *args: fn(*args)
            asyncio.run(screen._handle_command("how many pods?"))

        status_calls = [str(c) for c in mock_status.update.call_args_list]
        assert any("Plan" in c for c in status_calls), "agentic steps must be visible"

    def test_agentic_steps_rendered_in_expert_mode(self) -> None:
        """Expert/debug mode keeps exposing the agentic steps."""
        import asyncio
        from unittest.mock import PropertyMock

        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.expert_mode = True
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        screen._refresh_aside = MagicMock()  # type: ignore[method-assign]

        mock_log = MagicMock()
        mock_status = MagicMock()
        screen.query_one = MagicMock(
            side_effect=lambda _id, _cls=None: mock_log if _id == "#conversation" else mock_status
        )  # type: ignore[method-assign]  # noqa: E501

        from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import (
            ChatCliResponse,
        )

        result = ChatCliResponse(kind="debug", lines=[("answer", "white")], duration_ms=0)

        def fake_route(_text, _adapter, _history, on_progress=None):  # type: ignore[no-untyped-def]
            if on_progress:
                on_progress("plan", "Plan")
                on_progress("execute", "Execute")
            return result

        with (
            patch("hexawyn.cli.screens.session.route_command", side_effect=fake_route),
            patch("hexawyn.cli.screens.session.render_result"),
            patch("hexawyn.cli.screens.session.safe_findings", return_value=[]),
            patch(
                "hexawyn.cli.screens.session.SessionScreen.app",
                new_callable=PropertyMock,
                return_value=MagicMock(),
            ) as mock_app_prop,
        ):
            mock_app_prop.return_value.call_from_thread = lambda fn, *args: fn(*args)
            asyncio.run(screen._handle_command("how many pods?"))

        status_calls = [str(c) for c in mock_status.update.call_args_list]
        assert any(
            "Plan" in c and "Execute" in c for c in status_calls
        ), "expert mode must show steps"  # noqa: E501

    def test_copy_to_clipboard_darwin(self) -> None:
        screen = self._create_screen()
        with (
            patch("platform.system", return_value="Darwin"),
            patch("subprocess.run") as mock_run,
        ):
            result = screen._copy_to_clipboard("hello")

        assert result == "✓ Copied to clipboard"
        mock_run.assert_called_once_with(["pbcopy"], input=b"hello", check=True)

    def test_copy_to_clipboard_linux_wl_copy(self) -> None:
        screen = self._create_screen()
        with (
            patch("platform.system", return_value="Linux"),
            patch("subprocess.run") as mock_run,
        ):
            result = screen._copy_to_clipboard("hello")

        assert result == "✓ Copied to clipboard"
        mock_run.assert_called_once_with(["wl-copy"], input=b"hello", check=True)

    def test_copy_to_clipboard_linux_falls_back_to_xclip(self) -> None:
        screen = self._create_screen()

        def fake_run(cmd, **kwargs):  # type: ignore[no-untyped-def]
            if cmd == ["wl-copy"]:
                raise FileNotFoundError("wl-copy missing")
            return MagicMock()

        with (
            patch("platform.system", return_value="Linux"),
            patch("subprocess.run", side_effect=fake_run),
        ):
            result = screen._copy_to_clipboard("hello")

        assert result == "✓ Copied to clipboard"

    def test_copy_to_clipboard_linux_no_tool(self) -> None:
        screen = self._create_screen()
        with (
            patch("platform.system", return_value="Linux"),
            patch("subprocess.run", side_effect=FileNotFoundError("missing")),
        ):
            result = screen._copy_to_clipboard("hello")

        assert "xclip or wl-clipboard" in result

    def test_copy_to_clipboard_unsupported_system(self) -> None:
        screen = self._create_screen()
        with patch("platform.system", return_value="Windows"):
            result = screen._copy_to_clipboard("hello")

        assert "not supported" in result

    def test_copy_to_clipboard_exception(self) -> None:
        screen = self._create_screen()
        with (
            patch("platform.system", return_value="Darwin"),
            patch("subprocess.run", side_effect=OSError("denied")),
        ):
            result = screen._copy_to_clipboard("hello")

        assert "Copy failed" in result

    def test_action_copy_response_without_response(self) -> None:
        screen = self._create_screen()
        screen._last_response = ""
        mock_status = MagicMock()
        screen.query_one = MagicMock(return_value=mock_status)  # type: ignore[method-assign]
        screen.action_copy_response()
        assert "Nothing to copy" in str(mock_status.update.call_args)

    def test_action_copy_response_with_response(self) -> None:
        screen = self._create_screen()
        screen._last_response = "the answer"
        mock_status = MagicMock()
        screen.query_one = MagicMock(return_value=mock_status)  # type: ignore[method-assign]
        with patch.object(screen, "_copy_to_clipboard", return_value="✓ Copied") as mock_copy:
            screen.action_copy_response()

        mock_copy.assert_called_once_with("the answer")
        mock_status.update.assert_called_once()

    def test_action_export_response_without_response(self) -> None:
        screen = self._create_screen()
        screen._last_response = ""
        mock_status = MagicMock()
        screen.query_one = MagicMock(return_value=mock_status)  # type: ignore[method-assign]
        screen.action_export_response()
        assert "Nothing to export" in str(mock_status.update.call_args)

    def test_action_export_response_darwin(self) -> None:
        screen = self._create_screen()
        screen._last_response = "the answer"
        mock_status = MagicMock()
        screen.query_one = MagicMock(return_value=mock_status)  # type: ignore[method-assign]
        with (
            patch("platform.system", return_value="Darwin"),
            patch("subprocess.Popen") as mock_popen,
            patch("tempfile.NamedTemporaryFile") as mock_tmp,
        ):
            mock_file = MagicMock()
            mock_tmp.return_value.__enter__.return_value = mock_file
            mock_file.name = "/tmp/answer.txt"
            screen.action_export_response()

        mock_popen.assert_called_once_with(["open", "/tmp/answer.txt"])
        mock_status.update.assert_called_once()

    def test_action_export_response_linux(self) -> None:
        screen = self._create_screen()
        screen._last_response = "the answer"
        mock_status = MagicMock()
        screen.query_one = MagicMock(return_value=mock_status)  # type: ignore[method-assign]
        with (
            patch("platform.system", return_value="Linux"),
            patch("subprocess.Popen") as mock_popen,
            patch("tempfile.NamedTemporaryFile") as mock_tmp,
        ):
            mock_file = MagicMock()
            mock_tmp.return_value.__enter__.return_value = mock_file
            mock_file.name = "/tmp/answer.txt"
            screen.action_export_response()

        mock_popen.assert_called_once_with(["xdg-open", "/tmp/answer.txt"])

    def test_action_export_response_exception(self) -> None:
        screen = self._create_screen()
        screen._last_response = "the answer"
        mock_status = MagicMock()
        screen.query_one = MagicMock(return_value=mock_status)  # type: ignore[method-assign]
        with (
            patch("platform.system", return_value="Linux"),
            patch("subprocess.Popen", side_effect=OSError("no opener")),
            patch("tempfile.NamedTemporaryFile") as mock_tmp,
        ):
            mock_file = MagicMock()
            mock_tmp.return_value.__enter__.return_value = mock_file
            mock_file.name = "/tmp/answer.txt"
            screen.action_export_response()

        assert "Export failed" in str(mock_status.update.call_args)

    def test_action_clear_input_with_value(self) -> None:
        screen = self._create_screen()
        mock_input = MagicMock()
        mock_input.value = "some text"
        screen.query_one = MagicMock(return_value=mock_input)  # type: ignore[method-assign]
        screen.action_clear_input()
        assert mock_input.value == ""

    def test_action_clear_input_exits_app(self) -> None:
        from unittest.mock import PropertyMock

        screen = self._create_screen()
        mock_input = MagicMock()
        mock_input.value = ""
        screen.query_one = MagicMock(return_value=mock_input)  # type: ignore[method-assign]
        with patch(
            "hexawyn.cli.screens.session.SessionScreen.app",
            new_callable=PropertyMock,
            return_value=MagicMock(),
        ) as mock_app_prop:
            screen.action_clear_input()
            mock_app_prop.return_value.exit.assert_called_once()

    def test_on_input_changed_is_noop(self) -> None:
        import asyncio

        screen = self._create_screen()
        asyncio.run(screen.on_input_changed(MagicMock()))

    def test_on_input_submitted_empty_text(self) -> None:
        import asyncio

        screen = self._create_screen()
        event = MagicMock()
        event.value = "   "
        event.input = MagicMock()
        asyncio.run(screen.on_input_submitted(event))
        event.input.remember.assert_not_called()

    def test_on_input_submitted_with_text(self) -> None:
        import asyncio

        screen = self._create_screen()
        event = MagicMock()
        event.value = "  hello  "
        event.input = MagicMock()
        screen._handle_command = MagicMock()  # type: ignore[method-assign]

        async def run() -> None:
            await screen.on_input_submitted(event)

        with patch("hexawyn.cli.screens.session.asyncio.create_task") as mock_create:
            asyncio.run(run())
            mock_create.assert_called_once()
            assert event.input.remember.call_count >= 1

    def test_show_spinner_renders_stages(self) -> None:
        import asyncio

        screen = self._create_screen()
        mock_status = MagicMock()
        screen.query_one = MagicMock(return_value=mock_status)  # type: ignore[method-assign]
        log = MagicMock()

        async def run() -> None:
            await screen._show_spinner(log, ["Thinking", "Executing"])

        with patch("hexawyn.cli.screens.session.asyncio.sleep", new=asyncio.sleep):
            asyncio.run(run())

        assert mock_status.update.call_count > 0

    def test_show_spinner_cancelled(self) -> None:
        import asyncio

        screen = self._create_screen()
        mock_status = MagicMock()
        screen.query_one = MagicMock(return_value=mock_status)  # type: ignore[method-assign]
        log = MagicMock()

        async def run() -> None:
            task = asyncio.create_task(screen._show_spinner(log, ["Thinking"]))
            await asyncio.sleep(0)
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

        asyncio.run(run())
        assert mock_status.update.call_count > 0

    def test_handle_command_setup_branch(self) -> None:
        import asyncio

        screen = self._create_screen()
        screen._tui_app = MagicMock(return_value=MagicMock())  # type: ignore[method-assign]
        mock_log = MagicMock()
        screen.query_one = MagicMock(return_value=mock_log)  # type: ignore[method-assign]
        with (
            patch("hexawyn.cli.screens.session._is_setup_command", return_value=True),
            patch("hexawyn.cli.screens.session.render_setup_info") as mock_render,
        ):
            asyncio.run(screen._handle_command("/setup"))
            mock_render.assert_called_once_with(mock_log)

    def test_handle_command_token_branch(self) -> None:
        import asyncio
        from unittest.mock import AsyncMock

        screen = self._create_screen()
        screen._tui_app = MagicMock(return_value=MagicMock())  # type: ignore[method-assign]
        mock_log = MagicMock()
        screen.query_one = MagicMock(return_value=mock_log)  # type: ignore[method-assign]
        screen._open_token_input = AsyncMock()  # type: ignore[method-assign]
        with patch("hexawyn.cli.screens.session._is_token_command", return_value=True):
            asyncio.run(screen._handle_command("/token"))
            screen._open_token_input.assert_awaited_once()

    def test_handle_command_context_branch(self) -> None:
        import asyncio
        from unittest.mock import AsyncMock

        screen = self._create_screen()
        screen._tui_app = MagicMock(return_value=MagicMock())  # type: ignore[method-assign]
        mock_log = MagicMock()
        screen.query_one = MagicMock(return_value=mock_log)  # type: ignore[method-assign]
        screen._handle_context_command = AsyncMock()  # type: ignore[method-assign]
        with patch("hexawyn.cli.screens.session._is_context_command", return_value=True):
            asyncio.run(screen._handle_command("/context"))
            screen._handle_context_command.assert_awaited_once_with("/context", mock_log)

    def test_handle_command_stack_branch(self) -> None:
        import asyncio

        screen = self._create_screen()
        screen._tui_app = MagicMock(return_value=MagicMock())  # type: ignore[method-assign]
        mock_log = MagicMock()
        screen.query_one = MagicMock(return_value=mock_log)  # type: ignore[method-assign]
        screen._handle_stack_command = MagicMock()  # type: ignore[method-assign]
        with patch("hexawyn.cli.screens.session._is_stack_command", return_value=True):
            asyncio.run(screen._handle_command("/stack"))
            screen._handle_stack_command.assert_called_once_with("/stack", mock_log)

    def test_handle_command_refresh_branch_success(self) -> None:
        import asyncio

        screen = self._create_screen()
        screen._tui_app = MagicMock(return_value=MagicMock())  # type: ignore[method-assign]
        mock_log = MagicMock()
        screen.query_one = MagicMock(return_value=mock_log)  # type: ignore[method-assign]
        screen._refresh_aside = MagicMock()  # type: ignore[method-assign]
        with (
            patch(
                "hexawyn.infrastructure.license.license_reader.refresh_license",
                return_value=True,
            ),
            patch("hexawyn.cli.screens.session._is_setup_command", return_value=False),
            patch("hexawyn.cli.screens.session._is_token_command", return_value=False),
            patch("hexawyn.cli.screens.session._is_context_command", return_value=False),
            patch("hexawyn.cli.screens.session._is_stack_command", return_value=False),
        ):
            asyncio.run(screen._handle_command("/refresh"))
            assert mock_log.write.call_count >= 1

    def test_handle_command_refresh_branch_failure(self) -> None:
        import asyncio

        screen = self._create_screen()
        screen._tui_app = MagicMock(return_value=MagicMock())  # type: ignore[method-assign]
        mock_log = MagicMock()
        screen.query_one = MagicMock(return_value=mock_log)  # type: ignore[method-assign]
        screen._refresh_aside = MagicMock()  # type: ignore[method-assign]
        with (
            patch(
                "hexawyn.infrastructure.license.license_reader.refresh_license",
                return_value=False,
            ),
            patch("hexawyn.cli.screens.session._is_setup_command", return_value=False),
            patch("hexawyn.cli.screens.session._is_token_command", return_value=False),
            patch("hexawyn.cli.screens.session._is_context_command", return_value=False),
            patch("hexawyn.cli.screens.session._is_stack_command", return_value=False),
        ):
            asyncio.run(screen._handle_command("/refresh"))
            assert "re-activate" in str(mock_log.write.call_args_list[-1])

    def test_handle_context_command_without_name_opens_picker(self) -> None:
        import asyncio
        from unittest.mock import AsyncMock

        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.context_service = MagicMock()
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        mock_log = MagicMock()
        screen.query_one = MagicMock(return_value=mock_log)  # type: ignore[method-assign]
        screen._open_context_picker = AsyncMock()  # type: ignore[method-assign]
        with patch("hexawyn.cli.screens.session.extract_requested_context", return_value=None):
            asyncio.run(screen._handle_context_command("/context", mock_log))
            screen._open_context_picker.assert_awaited_once()

    def test_open_context_picker_callback_switches(self) -> None:
        import asyncio

        screen = self._create_screen()
        mock_app = MagicMock()
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        screen._available_contexts = MagicMock(return_value=[])  # type: ignore[method-assign]
        screen._switch_context = MagicMock()  # type: ignore[method-assign]
        with patch("hexawyn.cli.screens.session.ContextPickerScreen"):
            asyncio.run(screen._open_context_picker())
            callback = mock_app.push_screen.call_args.kwargs["callback"]
            callback("prod")
            screen._switch_context.assert_called_once_with("prod")

    def test_on_input_submitted_remember_missing(self) -> None:
        import asyncio

        screen = self._create_screen()
        event = MagicMock()
        event.value = "hello"
        event.input = MagicMock()
        del event.input.remember  # simulate input without `remember`
        event.input.action_delete_left_all = MagicMock()
        screen._handle_command = MagicMock()  # type: ignore[method-assign]

        async def run() -> None:
            await screen.on_input_submitted(event)

        with patch("hexawyn.cli.screens.session.asyncio.create_task") as mock_create:
            asyncio.run(run())
            mock_create.assert_called_once()

    def test_compose_and_mount_build_ui(self) -> None:
        import asyncio

        from hexawyn.cli.screens.session import SessionScreen
        from textual.app import App, ComposeResult

        class _SessionApp(App[None]):
            def compose(self) -> ComposeResult:
                yield SessionScreen()

        mock_app_attrs = {
            "cluster_name": "prod",
            "run_startup_scan": False,
            "expert_mode": False,
            "adapter": MagicMock(),
            "context_service": None,
            "startup_status": None,
            "adapter_builder": MagicMock(),
            "run_worker": MagicMock(),
            "call_from_thread": lambda fn, *args: fn(*args),
        }
        mock_tui = MagicMock()
        for k, v in mock_app_attrs.items():
            setattr(mock_tui, k, v)

        async def run() -> None:
            with (
                patch.object(SessionScreen, "_tui_app", return_value=mock_tui),
                patch.object(SessionScreen, "_refresh_aside"),
                patch.object(SessionScreen, "_refresh_footer"),
                patch.object(SessionScreen, "_start_background_license_refresh"),
            ):
                app = _SessionApp()
                async with app.run_test() as _pilot:
                    screen = app.screen
                    assert screen.query("#cmd-input")
                    assert screen.query("#conversation")
                    assert screen.query("#aside-body")
                    assert screen.query("#status-bar")
                    assert screen.query("#footer-hints")

        asyncio.run(run())

    def test_tui_app_returns_real_hexawyn_app(self) -> None:
        from unittest.mock import PropertyMock

        from hexawyn.cli.tui import HexawynTUI

        mock_app = MagicMock(spec=HexawynTUI)
        screen = self._create_screen()
        with patch(
            "hexawyn.cli.screens.session.SessionScreen.app",
            new_callable=PropertyMock,
            return_value=mock_app,
        ):
            result = screen._tui_app()

        assert result is mock_app

    def test_on_mount_with_startup_scan_and_initial_command(self) -> None:
        import asyncio

        from hexawyn.cli.screens.session import SessionScreen
        from textual.app import App, ComposeResult

        class _SessionApp(App[None]):
            def compose(self) -> ComposeResult:
                yield SessionScreen(initial_command="/context prod")

        mock_app_attrs = {
            "cluster_name": "prod",
            "run_startup_scan": True,
            "expert_mode": False,
            "adapter": MagicMock(),
            "context_service": MagicMock(),
            "startup_status": None,
            "adapter_builder": MagicMock(),
            "run_worker": MagicMock(),
            "call_from_thread": lambda fn, *args: fn(*args),
        }
        mock_tui = MagicMock()
        for k, v in mock_app_attrs.items():
            setattr(mock_tui, k, v)
        mock_tui.context_service.switch_context.return_value = MagicMock(
            switched=True,
            current_context=MagicMock(name="prod"),
            contexts=[],
        )

        async def run() -> None:
            with (
                patch.object(SessionScreen, "_tui_app", return_value=mock_tui),
                patch.object(SessionScreen, "_refresh_aside"),
                patch.object(SessionScreen, "_refresh_footer"),
                patch.object(SessionScreen, "_start_background_license_refresh"),
                patch(
                    "hexawyn.cli.screens.session.startup_status_from_switch",
                    return_value=MagicMock(),
                ),
                patch(
                    "hexawyn.cli.screens.session.format_context_switch_lines",
                    return_value=[("switched", "green")],
                ),
            ):
                app = _SessionApp()
                async with app.run_test() as _pilot:
                    assert app.screen.query("#conversation")

        asyncio.run(run())

    def test_background_license_refresh_runs_periodically(self) -> None:
        import asyncio

        screen = self._create_screen()
        screen._refresh_aside = MagicMock()  # type: ignore[method-assign]
        screen._refresh_footer = MagicMock()  # type: ignore[method-assign]

        orig_sleep = asyncio.sleep

        async def fake_sleep(_seconds: float) -> None:
            await orig_sleep(0.001)

        async def run() -> None:
            with (
                patch("hexawyn.cli.screens.session.asyncio.sleep", side_effect=fake_sleep),
                patch(
                    "hexawyn.infrastructure.license.license_reader.refresh_license",
                    return_value=True,
                ),
            ):
                screen._start_background_license_refresh()
                task = screen._refresh_task
                assert task is not None
                for _ in range(10):
                    await orig_sleep(0.005)
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass

        asyncio.run(run())
        assert screen._refresh_aside.call_count > 0  # type: ignore[attr-defined]

    def test_background_license_refresh_cancelled_during_initial_sleep(self) -> None:
        import asyncio

        screen = self._create_screen()
        screen._refresh_aside = MagicMock()  # type: ignore[method-assign]
        screen._refresh_footer = MagicMock()  # type: ignore[method-assign]

        orig_sleep = asyncio.sleep

        async def fake_sleep(_seconds: float) -> None:
            await orig_sleep(5)

        async def run() -> None:
            with patch("hexawyn.cli.screens.session.asyncio.sleep", side_effect=fake_sleep):
                screen._start_background_license_refresh()
                task = screen._refresh_task
                assert task is not None
                await orig_sleep(0.01)
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass

        asyncio.run(run())
        assert screen._refresh_aside.call_count == 0  # type: ignore[attr-defined]

    def test_handle_command_spinner_cancel_raises_cancelled(self) -> None:
        import asyncio

        class _CancelledAwaitable:
            def cancel(self) -> None:
                return None

            def __await__(self):  # type: ignore[no-untyped-def]
                raise asyncio.CancelledError()
                yield  # pragma: no cover

        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.expert_mode = False
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        screen._refresh_aside = MagicMock()  # type: ignore[method-assign]
        mock_log = MagicMock()
        mock_status = MagicMock()
        screen.query_one = MagicMock(
            side_effect=lambda _id, _cls=None: mock_log if _id == "#conversation" else mock_status
        )  # type: ignore[method-assign]  # noqa: E501

        from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import (
            ChatCliResponse,
        )

        result = ChatCliResponse(kind="debug", lines=[("answer", "white")], duration_ms=0)

        with (
            patch("hexawyn.cli.screens.session.route_command", return_value=result),
            patch("hexawyn.cli.screens.session.render_result"),
            patch("hexawyn.cli.screens.session.safe_findings", return_value=[]),
            patch(
                "hexawyn.cli.screens.session.asyncio.create_task",
                return_value=_CancelledAwaitable(),
            ),
        ):
            asyncio.run(screen._handle_command("hello"))

        assert mock_status.update.call_count > 0

    def test_handle_command_findings_inserted_into_history(self) -> None:
        import asyncio
        from unittest.mock import PropertyMock

        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.expert_mode = False
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        screen._refresh_aside = MagicMock()  # type: ignore[method-assign]
        mock_log = MagicMock()
        mock_status = MagicMock()
        screen.query_one = MagicMock(
            side_effect=lambda _id, _cls=None: mock_log if _id == "#conversation" else mock_status
        )  # type: ignore[method-assign]  # noqa: E501

        from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import (
            ChatCliResponse,
        )

        result = ChatCliResponse(kind="debug", lines=[("answer", "white")], duration_ms=0)

        captured: dict[str, object] = {}

        def fake_route(_text, _adapter, history, on_progress=None):  # type: ignore[no-untyped-def]
            captured["history"] = history
            return result

        with (
            patch("hexawyn.cli.screens.session.route_command", side_effect=fake_route),
            patch("hexawyn.cli.screens.session.render_result"),
            patch(
                "hexawyn.cli.screens.session.safe_findings",
                return_value=[
                    {
                        "type": "issue",
                        "resource": "pod-x",
                        "namespace": "ns",
                        "message": "down",
                    }
                ],
            ),
            patch(
                "hexawyn.cli.screens.session.SessionScreen.app",
                new_callable=PropertyMock,
                return_value=MagicMock(),
            ) as mock_app_prop,
        ):
            mock_app_prop.return_value.call_from_thread = lambda fn, *args: fn(*args)
            asyncio.run(screen._handle_command("what is wrong?"))

        history = captured["history"]
        assert isinstance(history, list)
        assert history[0]["role"] == "system"
        assert "pod-x" in history[0]["content"]
        assert "investigate" in history[0]["content"]

    def test_handle_command_stores_history_and_last_response(self) -> None:
        import asyncio

        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.expert_mode = False
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        screen._refresh_aside = MagicMock()  # type: ignore[method-assign]
        mock_log = MagicMock()
        mock_status = MagicMock()
        screen.query_one = MagicMock(
            side_effect=lambda _id, _cls=None: mock_log if _id == "#conversation" else mock_status
        )  # type: ignore[method-assign]  # noqa: E501

        from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import (
            ChatCliResponse,
        )

        result = ChatCliResponse(kind="debug", lines=[("the answer text", "white")], duration_ms=0)

        with (
            patch("hexawyn.cli.screens.session.route_command", return_value=result),
            patch("hexawyn.cli.screens.session.render_result"),
            patch("hexawyn.cli.screens.session.safe_findings", return_value=[]),
        ):
            asyncio.run(screen._handle_command("hello"))

        assert screen._last_response == "the answer text"
        assert screen._history[-1]["role"] == "assistant"
        assert screen._history[-1]["content"] == "the answer text"

    def test_open_token_input(self) -> None:
        import asyncio

        screen = self._create_screen()
        mock_app = MagicMock()
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        mock_log = MagicMock()
        screen.query_one = MagicMock(return_value=mock_log)  # type: ignore[method-assign]
        screen._refresh_aside = MagicMock()  # type: ignore[method-assign]

        with (
            patch("hexawyn.cli.screens.token_input.TokenInputScreen"),
        ):
            asyncio.run(screen._open_token_input())
            mock_app.push_screen.assert_called_once()
            callback = mock_app.push_screen.call_args.kwargs["callback"]
            callback("hxw_")

        assert mock_log.write.call_count >= 1

    def test_refresh_quota_bar_success(self) -> None:
        screen = self._create_screen()
        mock_app = MagicMock()
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        screen._refresh_footer = MagicMock()  # type: ignore[method-assign]
        mock_quota_bar = MagicMock()
        screen.query_one = MagicMock(return_value=mock_quota_bar)  # type: ignore[method-assign]

        class _Quota:
            state = type("S", (), {"value": "limited"})()

        class _Response:
            quotas = [_Quota(), _Quota()]

        with (
            patch(
                "hexawyn.application.service.runtime_adapter.get_runtime",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.application.use_case.cluster.get_quota_usage.get_quota_usage_use_case.GetQuotaUsageUseCase"  # noqa: E501
            ) as mock_uc,
            patch("hexawyn.cli.widgets.quota_bar._quota_bar", return_value="bar"),
        ):
            mock_uc.return_value.execute.return_value = _Response()
            screen._refresh_quota_bar()

        assert mock_quota_bar.update.call_count >= 1

    def test_refresh_quota_bar_failure(self) -> None:
        screen = self._create_screen()
        mock_app = MagicMock()
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        screen._refresh_footer = MagicMock()  # type: ignore[method-assign]
        mock_quota_bar = MagicMock()
        screen.query_one = MagicMock(return_value=mock_quota_bar)  # type: ignore[method-assign]

        with (
            patch(
                "hexawyn.application.service.runtime_adapter.get_runtime",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.application.use_case.cluster.get_quota_usage.get_quota_usage_use_case.GetQuotaUsageUseCase",  # noqa: E501
                side_effect=RuntimeError("boom"),
            ),
        ):
            screen._refresh_quota_bar()

        assert "Quota unavailable" in str(mock_quota_bar.update.call_args)

    def test_run_startup_scan_success(self) -> None:
        import asyncio
        from unittest.mock import PropertyMock

        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.cluster_name = "prod"
        mock_app.startup_result = None
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        mock_log = MagicMock()
        screen.query_one = MagicMock(return_value=mock_log)  # type: ignore[method-assign]

        from hexawyn.application.ports.driven.runtime_port import StartupScanResult

        mock_runtime = MagicMock()
        mock_runtime.run_startup_scan.return_value = StartupScanResult(health_score=85)

        with (
            patch(
                "hexawyn.application.service.runtime_adapter.get_runtime",
                return_value=mock_runtime,
            ),
            patch("hexawyn.cli.screens.session.is_valid_startup_result", return_value=True),
            patch(
                "hexawyn.cli.screens.session.SessionScreen.app",
                new_callable=PropertyMock,
                return_value=MagicMock(),
            ) as mock_app_prop,
        ):
            mock_app_prop.return_value.call_from_thread = lambda fn, *args: fn(*args)
            asyncio.run(screen._run_startup_scan())

        assert mock_app.startup_result is not None
        assert mock_app.startup_result["health_score"] == 85  # noqa: PLR2004

    def test_run_startup_scan_failure(self) -> None:
        import asyncio
        from unittest.mock import PropertyMock

        screen = self._create_screen()
        mock_app = MagicMock()
        mock_app.cluster_name = "prod"
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]
        mock_log = MagicMock()
        screen.query_one = MagicMock(return_value=mock_log)  # type: ignore[method-assign]

        mock_runtime = MagicMock()
        mock_runtime.run_startup_scan.side_effect = RuntimeError("control plane down")

        with (
            patch(
                "hexawyn.application.service.runtime_adapter.get_runtime",
                return_value=mock_runtime,
            ),
            patch(
                "hexawyn.cli.screens.session.SessionScreen.app",
                new_callable=PropertyMock,
                return_value=MagicMock(),
            ) as mock_app_prop,
        ):
            mock_app_prop.return_value.call_from_thread = lambda fn, *args: fn(*args)
            asyncio.run(screen._run_startup_scan())

        assert mock_log.write.call_count >= 1
