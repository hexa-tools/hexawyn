from unittest.mock import MagicMock

from hexawyn.application.use_case.chat_cli.chat_cli_response import ChatCliResponse


class TestResponseRenderer:
    def test_render_lines_writes_each_line(self) -> None:
        from hexawyn.cli.presentation.response_renderer import render_lines

        mock_log = MagicMock()
        lines = [("hello", "bold"), ("world", "dim")]

        render_lines(mock_log, lines)

        assert mock_log.write.call_count == 2

    def test_render_result_pods_renders_table(self) -> None:
        from hexawyn.cli.presentation.response_renderer import render_result

        mock_log = MagicMock()
        result = ChatCliResponse(
            kind="pods",
            pods=[{"name": "test-pod", "namespace": "default", "status": "Running", "restarts": 0}],
            lines=[],
            summary="3 pods found",
        )

        render_result(mock_log, result)

        assert mock_log.write.call_count >= 2

    def test_render_result_non_pods_delegates_to_lines(self) -> None:
        from hexawyn.cli.presentation.response_renderer import render_result

        mock_log = MagicMock()
        result = ChatCliResponse(
            kind="text",
            pods=None,
            lines=[("some text", "dim")],
            summary="",
        )

        render_result(mock_log, result)

        assert mock_log.write.call_count == 1
        assert "[dim]some text[/dim]" in str(mock_log.write.call_args_list[0][0][0])
