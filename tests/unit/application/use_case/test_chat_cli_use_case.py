import pytest
from hexawyn.application.use_case.chat_cli.chat_cli_command import ChatCliCommand
from hexawyn.application.use_case.chat_cli.chat_cli_response import ChatCliResponse
from hexawyn.application.use_case.chat_cli.chat_cli_use_case import ChatCliUseCase


class TestChatCliCommand:
    def test_has_query_field(self) -> None:
        cmd = ChatCliCommand(query="why is payments-api crashing?")
        assert cmd.query == "why is payments-api crashing?"

    def test_is_frozen(self) -> None:
        cmd = ChatCliCommand(query="test")
        with pytest.raises(AttributeError):
            cmd.query = "other"  # type: ignore[misc]

    def test_empty_query_is_valid(self) -> None:
        cmd = ChatCliCommand(query="")
        assert cmd.query == ""


class TestChatCliResponse:
    def test_kind_is_required(self) -> None:
        resp = ChatCliResponse(kind="debug")
        assert resp.kind == "debug"

    def test_default_lines_is_empty(self) -> None:
        resp = ChatCliResponse(kind="debug")
        assert resp.lines == []

    def test_default_pods_is_none(self) -> None:
        resp = ChatCliResponse(kind="pods")
        assert resp.pods is None

    def test_default_summary_is_none(self) -> None:
        resp = ChatCliResponse(kind="pods")
        assert resp.summary is None

    def test_default_suggestions_is_empty(self) -> None:
        resp = ChatCliResponse(kind="debug")
        assert resp.suggestions == []

    def test_with_lines(self) -> None:
        resp = ChatCliResponse(kind="debug", lines=[("OOM detected", "white")])
        assert resp.lines == [("OOM detected", "white")]

    def test_with_suggestions(self) -> None:
        resp = ChatCliResponse(kind="debug", suggestions=["scale up", "check HPA"])
        assert len(resp.suggestions) == 2


class TestChatCliUseCase:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(ChatCliUseCase, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            ChatCliUseCase()  # type: ignore[abstract]

    def test_execute_is_abstract(self) -> None:
        assert getattr(ChatCliUseCase.execute, "__isabstractmethod__", False)
