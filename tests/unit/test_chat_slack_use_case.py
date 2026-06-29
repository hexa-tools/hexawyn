import pytest
from hexawyn.application.use_case.chat_slack.chat_slack_command import ChatSlackCommand
from hexawyn.application.use_case.chat_slack.chat_slack_response import ChatSlackResponse
from hexawyn.application.use_case.chat_slack.chat_slack_use_case import ChatSlackUseCase


class TestChatSlackCommand:
    def test_has_required_fields(self) -> None:
        cmd = ChatSlackCommand(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
            channel_id="C123456",
        )
        assert cmd.query == "why is payments-api crashing?"
        assert cmd.cluster_name == "prod-eu"
        assert cmd.channel_id == "C123456"

    def test_thread_ts_defaults_to_none(self) -> None:
        cmd = ChatSlackCommand(query="test", cluster_name="prod-eu", channel_id="C123")
        assert cmd.thread_ts is None

    def test_thread_ts_can_be_set(self) -> None:
        cmd = ChatSlackCommand(
            query="test", cluster_name="prod-eu", channel_id="C123", thread_ts="1234.5678"
        )
        assert cmd.thread_ts == "1234.5678"

    def test_is_frozen(self) -> None:
        cmd = ChatSlackCommand(query="test", cluster_name="prod", channel_id="C1")
        with pytest.raises(AttributeError):
            cmd.query = "other"  # type: ignore[misc]


class TestChatSlackResponse:
    def test_has_required_fields(self) -> None:
        resp = ChatSlackResponse(
            message="OOM detected",
            quota_display="[23/50 · 27 remaining]",
            suggestions=[],
            is_pro=False,
        )
        assert resp.message == "OOM detected"
        assert resp.quota_display == "[23/50 · 27 remaining]"
        assert resp.suggestions == []
        assert resp.is_pro is False

    def test_with_suggestions(self) -> None:
        resp = ChatSlackResponse(
            message="ok",
            quota_display="[1/50]",
            suggestions=["scale up", "check HPA"],
            is_pro=True,
        )
        assert len(resp.suggestions) == 2
        assert resp.is_pro is True


class TestChatSlackUseCase:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(ChatSlackUseCase, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            ChatSlackUseCase()  # type: ignore[abstract]

    def test_execute_is_abstract(self) -> None:
        assert getattr(ChatSlackUseCase.execute, "__isabstractmethod__", False)
