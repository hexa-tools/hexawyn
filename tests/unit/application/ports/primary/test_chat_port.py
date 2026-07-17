import pytest
from hexawyn.application.ports.primary.chat_port import ChatPort


class TestChatPort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(ChatPort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            ChatPort()  # type: ignore[abstract]

    def test_handle_message_is_abstract(self) -> None:
        assert getattr(ChatPort.handle_message, "__isabstractmethod__", False)

    def test_format_response_is_abstract(self) -> None:
        assert getattr(ChatPort.format_response, "__isabstractmethod__", False)
