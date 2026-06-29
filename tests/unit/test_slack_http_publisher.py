from unittest.mock import MagicMock

from hexawyn.adapters.secondary.slack.slack_http_publisher import SlackHttpPublisher
from hexawyn.application.ports.driven.message_publisher_port import MessagePublisherPort


def _make_client(ok: bool = True, ts: str | None = "1234.0001") -> MagicMock:
    client = MagicMock()
    response: dict[str, object] = {"ok": ok}
    if ts:
        response["ts"] = ts
    client.post.return_value = response
    return client


class TestSlackHttpPublisherContract:
    def test_implements_message_publisher_port(self) -> None:
        publisher = SlackHttpPublisher(http_client=MagicMock())
        assert isinstance(publisher, MessagePublisherPort)

    def test_accepts_injected_http_client(self) -> None:
        client = MagicMock()
        publisher = SlackHttpPublisher(http_client=client)
        assert publisher._client is client


class TestSlackHttpPublisherPostMessage:
    def setup_method(self) -> None:
        self.client = _make_client(ok=True)
        self.publisher = SlackHttpPublisher(http_client=self.client)

    def test_returns_ts_on_success(self) -> None:
        result = self.publisher.post_message("C123456", "hello")
        assert result == "1234.0001"

    def test_returns_none_when_slack_returns_ok_false(self) -> None:
        self.client.post.return_value = {"ok": False, "error": "channel_not_found"}
        result = self.publisher.post_message("C_BAD", "hello")
        assert result is None

    def test_calls_chat_post_message_endpoint(self) -> None:
        self.publisher.post_message("C123456", "hello")
        method = self.client.post.call_args[0][0]
        assert method == "chat.postMessage"

    def test_sends_channel_id_in_payload(self) -> None:
        self.publisher.post_message("C999", "hello")
        payload = self.client.post.call_args[0][1]
        assert payload["channel"] == "C999"

    def test_sends_text_in_payload(self) -> None:
        self.publisher.post_message("C123", "OOM detected in payments-api")
        payload = self.client.post.call_args[0][1]
        assert payload["text"] == "OOM detected in payments-api"

    def test_includes_thread_ts_when_provided(self) -> None:
        self.publisher.post_message("C123", "reply", thread_ts="1234.5678")
        payload = self.client.post.call_args[0][1]
        assert payload["thread_ts"] == "1234.5678"

    def test_omits_thread_ts_when_none(self) -> None:
        self.publisher.post_message("C123", "hello", thread_ts=None)
        payload = self.client.post.call_args[0][1]
        assert "thread_ts" not in payload

    def test_never_raises_on_network_error(self) -> None:
        self.client.post.side_effect = Exception("connection refused")
        result = self.publisher.post_message("C123", "hello")
        assert result is None

    def test_never_raises_on_unexpected_error(self) -> None:
        self.client.post.side_effect = RuntimeError("unexpected")
        result = self.publisher.post_message("C123", "hello")
        assert result is None

    def test_post_message_without_thread_ts_returns_ts(self) -> None:
        result = self.publisher.post_message("C123", "test message")
        assert result == "1234.0001"


class TestSlackHttpPublisherUpdateMessage:
    def setup_method(self) -> None:
        self.client = _make_client(ok=True)
        self.publisher = SlackHttpPublisher(http_client=self.client)

    def test_calls_chat_update_endpoint(self) -> None:
        self.publisher.update_message("C123", "1234.0001", "updated text")
        method = self.client.post.call_args[0][0]
        assert method == "chat.update"

    def test_sends_channel_ts_and_text(self) -> None:
        self.publisher.update_message("C999", "9876.5432", "new content")
        payload = self.client.post.call_args[0][1]
        assert payload["channel"] == "C999"
        assert payload["ts"] == "9876.5432"
        assert payload["text"] == "new content"

    def test_returns_ts_on_success(self) -> None:
        result = self.publisher.update_message("C123", "ts", "hello")
        assert result == "1234.0001"

    def test_returns_none_on_failure(self) -> None:
        self.client.post.return_value = {"ok": False}
        result = self.publisher.update_message("C123", "ts", "hello")
        assert result is None

    def test_never_raises_on_network_error(self) -> None:
        self.client.post.side_effect = Exception("connection refused")
        result = self.publisher.update_message("C123", "ts", "hello")
        assert result is None
