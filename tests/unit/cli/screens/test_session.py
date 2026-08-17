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
