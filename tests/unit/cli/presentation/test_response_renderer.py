from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import ChatCliResponse


class TestResponseRenderer:
    def test_render_lines_combines_into_one_write(self) -> None:
        from hexawyn.cli.presentation.response_renderer import render_lines

        mock_log = MagicMock()
        lines = [("hello", "bold"), ("", "dim"), ("world", "green")]

        render_lines(mock_log, lines)

        mock_log.write.assert_called_once()

    def test_render_result_pods_renders_table(self) -> None:
        from hexawyn.cli.presentation.response_renderer import render_result

        mock_log = MagicMock()
        result = ChatCliResponse(
            kind="pods",
            pods=[{"name": "test-pod", "namespace": "ns", "status": "Running", "restarts": 0}],
            lines=[],
            summary="3 pods found",
        )
        render_result(mock_log, result)
        assert mock_log.write.call_count >= 2  # noqa: PLR2004

    def test_render_result_non_pods_delegates_to_lines(self) -> None:
        from hexawyn.cli.presentation.response_renderer import render_result

        mock_log = MagicMock()
        result = ChatCliResponse(kind="text", pods=None, lines=[("some text", "dim")], summary="")
        render_result(mock_log, result)
        assert mock_log.write.call_count >= 1

    def test_render_result_debug_renders_markdown_lines(self) -> None:
        from hexawyn.cli.presentation.response_renderer import render_result

        mock_log = MagicMock()
        result = ChatCliResponse(
            kind="debug",
            pods=None,
            lines=[("answer paragraph", "white"), ("", "dim"), ("second", "green")],
            summary="",
        )
        render_result(mock_log, result)
        assert mock_log.write.call_count == 3  # noqa: PLR2004  # initial "" + two non-empty

    def test_render_result_debug_with_suggestions(self) -> None:
        from hexawyn.cli.presentation.response_renderer import render_result

        mock_log = MagicMock()
        result = ChatCliResponse(
            kind="debug",
            pods=None,
            lines=[("answer", "white")],
            summary="",
            suggestions=["Check pod logs", "Increase memory"],
        )
        render_result(mock_log, result)

        write_args = [str(c) for c in mock_log.write.call_args_list]
        assert any("Suggestions" in arg for arg in write_args)
        assert any("Check pod logs" in arg for arg in write_args)
