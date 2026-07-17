from unittest.mock import MagicMock, patch

from hexawyn.adapters.primary.slack.slack_event_server import SlackEventServer
from hexawyn.application.ports.driven.message_publisher_port import MessagePublisherPort
from hexawyn.application.ports.primary.chat_port import ChatPort


def _make_server(
    chat_response: str = "OOM detected in payments-api",
    publisher_ok: bool = True,
) -> tuple[SlackEventServer, MagicMock, MagicMock]:
    chat_adapter = MagicMock(spec=ChatPort)
    chat_adapter.handle_message.return_value = chat_response
    publisher = MagicMock(spec=MessagePublisherPort)
    publisher.post_message.return_value = "1234.0001" if publisher_ok else None
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=publisher)
    return server, chat_adapter, publisher


def _app_mention_event(
    text: str = "<@U123> why is payments-api crashing?",
    channel: str = "C123456",
    ts: str = "1234.5678",
    thread_ts: str | None = None,
) -> dict[str, object]:
    inner: dict[str, object] = {"type": "app_mention", "text": text, "channel": channel, "ts": ts}
    if thread_ts:
        inner["thread_ts"] = thread_ts
    return {"type": "event_callback", "event": inner}


# ── Contract ──────────────────────────────────────────────────────────────────


class TestSlackEventServerContract:
    def test_accepts_chat_adapter_and_publisher(self) -> None:
        server, _, _ = _make_server()
        assert server is not None

    def test_stores_injected_chat_adapter(self) -> None:
        adapter = MagicMock(spec=ChatPort)
        publisher = MagicMock(spec=MessagePublisherPort)
        server = SlackEventServer(chat_adapter=adapter, publisher=publisher)
        assert server._chat_adapter is adapter

    def test_stores_injected_publisher(self) -> None:
        adapter = MagicMock(spec=ChatPort)
        publisher = MagicMock(spec=MessagePublisherPort)
        server = SlackEventServer(chat_adapter=adapter, publisher=publisher)
        assert server._publisher is publisher


# ── url_verification ──────────────────────────────────────────────────────────


class TestHandleEventUrlVerification:
    def test_returns_challenge(self) -> None:
        server, _, _ = _make_server()
        result = server.handle_event({"type": "url_verification", "challenge": "abc123"})
        assert result == {"challenge": "abc123"}

    def test_returns_empty_challenge_when_missing(self) -> None:
        server, _, _ = _make_server()
        result = server.handle_event({"type": "url_verification"})
        assert result["challenge"] == ""

    def test_does_not_call_adapter_for_verification(self) -> None:
        server, adapter, _ = _make_server()
        server.handle_event({"type": "url_verification", "challenge": "abc"})
        adapter.handle_message.assert_not_called()

    def test_does_not_call_publisher_for_verification(self) -> None:
        server, _, publisher = _make_server()
        server.handle_event({"type": "url_verification", "challenge": "abc"})
        publisher.post_message.assert_not_called()


# ── app_mention ───────────────────────────────────────────────────────────────


class TestHandleEventAppMention:
    def setup_method(self) -> None:
        self.server, self.adapter, self.publisher = _make_server()

    def _handle(self, **kwargs: object) -> dict[str, object]:
        with patch(
            "hexawyn.adapters.primary.slack.slack_event_server._get_active_cluster_name",
            return_value="prod-eu",
        ):
            return self.server.handle_event(_app_mention_event(**kwargs))

    def test_returns_ok_true(self) -> None:
        result = self._handle()
        assert result == {"ok": True}

    def test_strips_bot_mention_from_query(self) -> None:
        self._handle(text="<@U123ABC> why is payments-api crashing?")
        query = self.adapter.handle_message.call_args[1]["query"]
        assert "<@" not in query
        assert "why is payments-api crashing?" == query

    def test_passes_channel_id_to_adapter(self) -> None:
        self._handle(channel="C999")
        assert self.adapter.handle_message.call_args[1]["channel_id"] == "C999"

    def test_passes_cluster_name_to_adapter(self) -> None:
        self._handle()
        assert self.adapter.handle_message.call_args[1]["cluster_name"] == "prod-eu"

    def test_passes_ts_as_thread_ts_when_no_thread_ts(self) -> None:
        self._handle(ts="9999.0001", thread_ts=None)
        assert self.adapter.handle_message.call_args[1]["thread_ts"] == "9999.0001"

    def test_prefers_thread_ts_over_ts(self) -> None:
        self._handle(ts="1111.0001", thread_ts="2222.9999")
        assert self.adapter.handle_message.call_args[1]["thread_ts"] == "2222.9999"

    def test_posts_response_to_publisher(self) -> None:
        self._handle()
        self.publisher.post_message.assert_called_once()

    def test_publishes_to_correct_channel(self) -> None:
        self._handle(channel="C777")
        assert self.publisher.post_message.call_args[1]["channel_id"] == "C777"

    def test_publishes_adapter_response_as_text(self) -> None:
        self.adapter.handle_message.return_value = "pods are healthy"
        self._handle()
        assert self.publisher.post_message.call_args[1]["text"] == "pods are healthy"

    def test_publishes_with_thread_ts(self) -> None:
        self._handle(ts="1234.5678")
        assert self.publisher.post_message.call_args[1]["thread_ts"] == "1234.5678"

    def test_ok_true_even_when_publisher_fails(self) -> None:
        self.publisher.post_message.return_value = False
        result = self._handle()
        assert result == {"ok": True}

    def test_handles_mention_with_extra_whitespace(self) -> None:
        self._handle(text="  <@U123>   list pods   ")
        query = self.adapter.handle_message.call_args[1]["query"]
        assert query == "list pods"


# ── Unknown events ────────────────────────────────────────────────────────────


class TestHandleEventUnknown:
    def test_returns_ok_true_for_unknown_type(self) -> None:
        server, _, _ = _make_server()
        result = server.handle_event({"type": "reaction_added"})
        assert result == {"ok": True}

    def test_returns_ok_true_for_event_callback_non_mention(self) -> None:
        server, _, _ = _make_server()
        result = server.handle_event(
            {"type": "event_callback", "event": {"type": "message", "text": "hello"}}
        )
        assert result == {"ok": True}

    def test_returns_ok_true_for_non_dict_inner_event(self) -> None:
        server, _, _ = _make_server()
        result = server.handle_event({"type": "event_callback", "event": "not_a_dict"})
        assert result == {"ok": True}

    def test_does_not_call_adapter_for_unknown(self) -> None:
        server, adapter, _ = _make_server()
        server.handle_event({"type": "reaction_added"})
        adapter.handle_message.assert_not_called()
