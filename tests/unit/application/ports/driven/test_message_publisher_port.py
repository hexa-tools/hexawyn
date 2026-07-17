from abc import ABC

import pytest
from hexawyn.application.ports.driven.message_publisher_port import MessagePublisherPort


class TestMessagePublisherPort:
    def test_is_abstract(self) -> None:
        assert issubclass(MessagePublisherPort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            MessagePublisherPort()  # type: ignore[abstract]

    def test_post_message_is_abstract(self) -> None:
        assert getattr(MessagePublisherPort.post_message, "__isabstractmethod__", False)

    def test_concrete_implementation_works(self) -> None:
        class FakePublisher(MessagePublisherPort):
            def post_message(
                self, channel_id: str, text: str, thread_ts: str | None = None
            ) -> str | None:
                return "1234.5678"

            def update_message(self, channel_id: str, message_ts: str, text: str) -> str | None:
                return "1234.9999"

        pub = FakePublisher()
        assert pub.post_message("C123", "hello") == "1234.5678"
        assert pub.post_message("C123", "hello", thread_ts="1234.5678") == "1234.5678"
        assert pub.update_message("C123", "1234.5678", "updated") == "1234.9999"
