from __future__ import annotations


class TestMarkdownLog:
    def test_imports_and_subclass(self) -> None:
        from hexawyn.cli.widgets.markdown_log import MarkdownLog
        from textual.widgets import Markdown

        assert issubclass(MarkdownLog, Markdown)

    def test_write_plain_text(self) -> None:
        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write("Hello world")

        assert "Hello world" in log._markdown

    def test_write_multiple_appends(self) -> None:
        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write("first line")
        log.write("second line")

        assert "first line" in log._markdown
        assert "second line" in log._markdown

    def test_write_initializes_markdown(self) -> None:
        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write("single")

        assert "single" in log._markdown

    def test_write_lines_tuple_list(self) -> None:
        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write_lines([("some text", "bold"), ("", "dim"), ("more", "green")])

        assert "some text" in log._markdown
        assert "more" in log._markdown

    def test_lines_strip_markup_styles(self) -> None:
        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write_lines([("important", "bold red")])

        assert "important" in log._markdown
        assert "[bold" not in log._markdown

    def test_plain_text_buffer_for_selection(self) -> None:
        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write("line one")
        log.write("line two")

        assert log.plain_text == "line one\nline two"

    def test_write_empty_string_noop(self) -> None:
        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write("")

        assert log._markdown == ""

    def test_write_code_block_fences_content(self) -> None:
        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write_code_block("╔═ logo ═╗")

        assert "```text" in log._markdown
        assert "╔═ logo ═╗" in log._markdown
        assert "```" in log._markdown

    def test_write_code_block_strips_rich_markup(self) -> None:
        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write_code_block("[dim]logo text[/dim]")

        assert "logo text" in log._markdown
        assert "[dim]" not in log._markdown

    def test_selection_updated_copies_selected_text(self) -> None:
        from unittest.mock import MagicMock, PropertyMock, patch

        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write("hello selected world")
        log.notify = MagicMock()  # type: ignore[method-assign]
        mock_screen = MagicMock()
        mock_screen.get_selected_text.return_value = "selected"

        with (
            patch.object(log, "_copy_to_clipboard") as mock_copy,
            patch(
                "hexawyn.cli.widgets.markdown_log.MarkdownLog.screen",
                new_callable=PropertyMock,
                return_value=mock_screen,
            ),
        ):
            log.selection_updated(object())  # type: ignore[arg-type]

        mock_copy.assert_called_once_with("selected")
        log.notify.assert_called_once()

    def test_selection_updated_noop_without_selection(self) -> None:
        from unittest.mock import MagicMock, PropertyMock, patch

        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write("some text")
        log.notify = MagicMock()  # type: ignore[method-assign]
        mock_screen = MagicMock()
        mock_screen.get_selected_text.return_value = None

        with (
            patch.object(log, "_copy_to_clipboard") as mock_copy,
            patch(
                "hexawyn.cli.widgets.markdown_log.MarkdownLog.screen",
                new_callable=PropertyMock,
                return_value=mock_screen,
            ),
        ):
            log.selection_updated(None)

        mock_copy.assert_not_called()
        log.notify.assert_not_called()

    def test_selection_updated_skips_empty_text(self) -> None:
        from unittest.mock import MagicMock, PropertyMock, patch

        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write("some text")
        log.notify = MagicMock()  # type: ignore[method-assign]
        mock_screen = MagicMock()
        mock_screen.get_selected_text.return_value = ""

        with (
            patch.object(log, "_copy_to_clipboard") as mock_copy,
            patch(
                "hexawyn.cli.widgets.markdown_log.MarkdownLog.screen",
                new_callable=PropertyMock,
                return_value=mock_screen,
            ),
        ):
            log.selection_updated(object())  # type: ignore[arg-type]

        mock_copy.assert_not_called()
        log.notify.assert_not_called()

    def test_repeated_selection_not_copied_twice(self) -> None:
        from unittest.mock import MagicMock, PropertyMock, patch

        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write("some text")
        log.notify = MagicMock()  # type: ignore[method-assign]
        mock_screen = MagicMock()
        mock_screen.get_selected_text.return_value = "some"

        with (
            patch.object(log, "_copy_to_clipboard") as mock_copy,
            patch(
                "hexawyn.cli.widgets.markdown_log.MarkdownLog.screen",
                new_callable=PropertyMock,
                return_value=mock_screen,
            ),
        ):
            log.selection_updated(object())  # type: ignore[arg-type]
            log.selection_updated(object())  # type: ignore[arg-type]

        mock_copy.assert_called_once_with("some")

    def test_on_mouse_up_copies_current_selection(self) -> None:
        import asyncio
        from unittest.mock import MagicMock, patch

        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write("selected text")
        event = MagicMock()

        async def run() -> None:
            with (
                patch.object(log, "_copy_current_selection") as mock_copy,
                patch("hexawyn.cli.widgets.markdown_log.Markdown._on_mouse_up") as mock_super,
            ):
                await log._on_mouse_up(event)
                mock_super.assert_awaited_once_with(event)
                mock_copy.assert_called_once()

        asyncio.run(run())

    def test_copy_current_selection_screen_error_returns(self) -> None:
        from unittest.mock import MagicMock, PropertyMock, patch

        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.notify = MagicMock()  # type: ignore[method-assign]
        mock_screen = MagicMock()
        mock_screen.get_selected_text.side_effect = RuntimeError("no screen")

        with (
            patch.object(log, "_copy_to_clipboard") as mock_copy,
            patch(
                "hexawyn.cli.widgets.markdown_log.MarkdownLog.screen",
                new_callable=PropertyMock,
                return_value=mock_screen,
            ),
        ):
            log.selection_updated(None)

        mock_copy.assert_not_called()
        log.notify.assert_not_called()

    def test_copy_to_clipboard_darwin(self) -> None:
        from unittest.mock import patch

        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        with (
            patch("platform.system", return_value="Darwin"),
            patch("subprocess.run") as mock_run,
        ):
            log._copy_to_clipboard("secret")

        mock_run.assert_called_once_with(["pbcopy"], input=b"secret", check=True)

    def test_copy_to_clipboard_linux_wl_copy(self) -> None:
        from unittest.mock import patch

        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        with (
            patch("platform.system", return_value="Linux"),
            patch("subprocess.run") as mock_run,
        ):
            log._copy_to_clipboard("secret")

        assert mock_run.call_count == 1

    def test_copy_to_clipboard_linux_falls_back_to_xclip(self) -> None:
        from unittest.mock import MagicMock, patch

        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()

        def fake_run(cmd, **kwargs):  # type: ignore[no-untyped-def]
            if cmd == ["wl-copy"]:
                raise FileNotFoundError("wl-copy missing")
            return MagicMock()

        with (
            patch("platform.system", return_value="Linux"),
            patch("subprocess.run", side_effect=fake_run),
        ):
            log._copy_to_clipboard("secret")

    def test_copy_to_clipboard_linux_both_tools_fail(self) -> None:
        from unittest.mock import patch

        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        with (
            patch("platform.system", return_value="Linux"),
            patch("subprocess.run", side_effect=FileNotFoundError("missing")),
        ):
            log._copy_to_clipboard("secret")

    def test_copy_to_clipboard_unknown_system(self) -> None:
        from unittest.mock import patch

        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        with (
            patch("platform.system", return_value="Windows"),
            patch("subprocess.run") as mock_run,
        ):
            log._copy_to_clipboard("secret")

        mock_run.assert_not_called()

    def test_copy_to_clipboard_generic_exception(self) -> None:
        from unittest.mock import patch

        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        with (
            patch("platform.system", return_value="Darwin"),
            patch("subprocess.run", side_effect=OSError("denied")),
        ):
            log._copy_to_clipboard("secret")

    def test_write_list_append(self) -> None:
        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write([("a", "bold"), ("b", "dim")])

        assert "a\nb" in log._markdown

    def test_write_non_string_object(self) -> None:
        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        log = MarkdownLog()
        log.write(42)

        assert "42" in log._markdown

    def test_strip_rich_markup_fallback_on_error(self) -> None:
        from unittest.mock import patch

        from hexawyn.cli.widgets.markdown_log import MarkdownLog

        with patch(
            "hexawyn.cli.widgets.markdown_log.Text.from_markup",
            side_effect=ValueError("bad markup"),
        ):
            result = MarkdownLog._strip_rich_markup("[broken")

        assert result == "[broken"
