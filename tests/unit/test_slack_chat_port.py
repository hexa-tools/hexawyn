import pytest
from hexawyn.application.ports.primary.slack_chat_port import SlackChatPort


class TestSlackChatPort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(SlackChatPort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            SlackChatPort()  # type: ignore[abstract]

    def test_handle_message_is_abstract(self) -> None:
        assert getattr(SlackChatPort.handle_message, "__isabstractmethod__", False)

    def test_format_response_is_abstract(self) -> None:
        assert getattr(SlackChatPort.format_response, "__isabstractmethod__", False)
