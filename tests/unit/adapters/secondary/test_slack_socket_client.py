import asyncio
import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from hexawyn.adapters.secondary.slack.slack_http_client import SlackHttpClient
from hexawyn.application.ports.driven.message_publisher_port import MessagePublisherPort
from hexawyn.application.ports.primary.chat_port import ChatPort


def _make_client(
    chat_response: str = "OOM detected in payments-api",
    app_token: str = "xapp-test-token",
) -> tuple[MagicMock, MagicMock, MagicMock, MagicMock]:
    from hexawyn.adapters.primary.slack.slack_socket_client import SlackSocketClient

    chat_adapter = MagicMock(spec=ChatPort)
    chat_adapter.handle_message.return_value = chat_response
    publisher = MagicMock(spec=MessagePublisherPort)
    publisher.post_message.return_value = "1234.0001"
    publisher.update_message.return_value = "1234.0001"
    http_client = MagicMock(spec=SlackHttpClient)
    http_client.post.return_value = {"ok": True, "url": "wss://fake.slack.com/link/?ticket=xxx"}
    client = SlackSocketClient(
        chat_adapter=chat_adapter,
        publisher=publisher,
        http_client=http_client,
        app_token=app_token,
    )
    return client, chat_adapter, publisher, http_client


# ── Contract ──────────────────────────────────────────────────────────────────


class TestSlackSocketClientContract:
    def test_accepts_chat_adapter_publisher_http_client_and_token(self) -> None:
        from hexawyn.adapters.primary.slack.slack_socket_client import SlackSocketClient

        chat = MagicMock(spec=ChatPort)
        pub = MagicMock(spec=MessagePublisherPort)
        http = MagicMock(spec=SlackHttpClient)
        client = SlackSocketClient(
            chat_adapter=chat,
            publisher=pub,
            http_client=http,
            app_token="xapp-test",
        )
        assert client is not None

    def test_stores_app_token(self) -> None:
        from hexawyn.adapters.primary.slack.slack_socket_client import SlackSocketClient

        chat = MagicMock(spec=ChatPort)
        pub = MagicMock(spec=MessagePublisherPort)
        http = MagicMock(spec=SlackHttpClient)
        client = SlackSocketClient(
            chat_adapter=chat,
            publisher=pub,
            http_client=http,
            app_token="xapp-secret-123",
        )
        assert client._app_token == "xapp-secret-123"

    def test_stores_injected_dependencies(self) -> None:
        from hexawyn.adapters.primary.slack.slack_socket_client import SlackSocketClient

        chat = MagicMock(spec=ChatPort)
        pub = MagicMock(spec=MessagePublisherPort)
        http = MagicMock(spec=SlackHttpClient)
        client = SlackSocketClient(
            chat_adapter=chat,
            publisher=pub,
            http_client=http,
            app_token="xapp-1",
        )
        assert client._chat_adapter is chat
        assert client._publisher is pub
        assert client._http_client is http


# ── Open Connection ───────────────────────────────────────────────────────────


class TestOpenConnection:
    def test_calls_apps_connections_open(self) -> None:
        client, _, _, _ = _make_client()
        with patch("httpx.post") as mock_post:
            mock_response = MagicMock()
            mock_response.json.return_value = {"ok": True, "url": "wss://fake.slack.com/link"}
            mock_post.return_value = mock_response
            client._open_connection()
            mock_post.assert_called_once()
            call_args = mock_post.call_args
            assert call_args[0][0] == "https://slack.com/api/apps.connections.open"
            headers = call_args[1]["headers"]
            assert headers["Authorization"] == "Bearer xapp-test-token"

    def test_returns_websocket_url(self) -> None:
        client, _, _, _ = _make_client()
        with patch("httpx.post") as mock_post:
            mock_response = MagicMock()
            mock_response.json.return_value = {
                "ok": True,
                "url": "wss://wss-primary.slack.com/link/?ticket=abc",
            }
            mock_post.return_value = mock_response
            result = client._open_connection()
        assert result == "wss://wss-primary.slack.com/link/?ticket=abc"

    def test_returns_empty_string_when_not_ok(self) -> None:
        client, _, _, _ = _make_client()
        with patch("httpx.post") as mock_post:
            mock_response = MagicMock()
            mock_response.json.return_value = {"ok": False, "error": "invalid_auth"}
            mock_post.return_value = mock_response
            result = client._open_connection()
        assert result == ""

    def test_returns_empty_string_when_no_url(self) -> None:
        client, _, _, _ = _make_client()
        with patch("httpx.post") as mock_post:
            mock_response = MagicMock()
            mock_response.json.return_value = {"ok": True}
            mock_post.return_value = mock_response
            result = client._open_connection()
        assert result == ""

    def test_returns_empty_string_on_network_error(self) -> None:
        client, _, _, _ = _make_client()
        with patch("httpx.post") as mock_post:
            mock_post.side_effect = ConnectionError("refused")
            result = client._open_connection()
        assert result == ""


# ── Handle Socket Message ─────────────────────────────────────────────────────


class TestHandleSocketMessage:
    def _make_event(
        self, event_type: str, text: str = "<@U123> why is payments-api crashing?"
    ) -> dict[str, object]:
        return {
            "envelope_id": "env-001",
            "type": "events_api",
            "payload": {
                "type": "event_callback",
                "event": {"type": event_type, "text": text, "channel": "C123", "ts": "1234.5678"},
            },
        }

    @pytest.mark.asyncio
    async def test_handles_url_verification(self) -> None:
        client, adapter, publisher, _ = _make_client()
        verif_msg: dict[str, object] = {
            "envelope_id": "env-002",
            "type": "events_api",
            "payload": {"type": "url_verification", "challenge": "challenge-abc"},
        }
        mock_ws = MagicMock()
        mock_ws.send = AsyncMock()
        await client._handle_socket_message(mock_ws, json.dumps(verif_msg))
        adapter.handle_message.assert_not_called()
        publisher.post_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_handles_app_mention(self) -> None:
        client, adapter, publisher, _ = _make_client()
        msg = self._make_event("app_mention")
        mock_ws = MagicMock()
        mock_ws.send = AsyncMock()

        with patch(
            "hexawyn.adapters.primary.slack.slack_socket_client._get_active_cluster_name",
            return_value="prod-eu",
        ):
            await client._handle_socket_message(mock_ws, json.dumps(msg))

        adapter.handle_message.assert_called_once()
        publisher.post_message.assert_called_once()  # thinking message
        publisher.update_message.assert_called_once()  # result replaces thinking

    @pytest.mark.asyncio
    async def test_ignores_non_events_api_messages(self) -> None:
        client, adapter, publisher, _ = _make_client()
        msg: dict[str, object] = {"type": "hello", "envelope_id": "env-003"}
        mock_ws = MagicMock()
        mock_ws.send = AsyncMock()
        await client._handle_socket_message(mock_ws, json.dumps(msg))
        adapter.handle_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_ignores_non_dict_inner_event(self) -> None:
        client, adapter, publisher, _ = _make_client()
        msg: dict[str, object] = {
            "envelope_id": "env-004",
            "type": "events_api",
            "payload": {"type": "event_callback", "event": "not_a_dict"},
        }
        mock_ws = MagicMock()
        mock_ws.send = AsyncMock()
        await client._handle_socket_message(mock_ws, json.dumps(msg))
        adapter.handle_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_ignores_non_app_mention_event(self) -> None:
        client, adapter, publisher, _ = _make_client()
        msg = self._make_event("message")
        mock_ws = MagicMock()
        mock_ws.send = AsyncMock()
        await client._handle_socket_message(mock_ws, json.dumps(msg))
        adapter.handle_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_strips_bot_mention_from_query(self) -> None:
        client, adapter, _, _ = _make_client()
        msg = self._make_event("app_mention", text="<@U123ABC> list pods in payments-api")
        mock_ws = MagicMock()
        mock_ws.send = AsyncMock()

        with patch(
            "hexawyn.adapters.primary.slack.slack_socket_client._get_active_cluster_name",
            return_value="prod-eu",
        ):
            await client._handle_socket_message(mock_ws, json.dumps(msg))

        query = adapter.handle_message.call_args[1]["query"]
        assert "<@" not in query
        assert query == "list pods in payments-api"

    @pytest.mark.asyncio
    async def test_passes_channel_to_adapter(self) -> None:
        client, adapter, _, _ = _make_client()
        inner: dict[str, object] = {
            "envelope_id": "env-005",
            "type": "events_api",
            "payload": {
                "type": "event_callback",
                "event": {
                    "type": "app_mention",
                    "text": "<@U123> test",
                    "channel": "C999",
                    "ts": "1.0",
                },
            },
        }
        mock_ws = MagicMock()
        mock_ws.send = AsyncMock()

        with patch(
            "hexawyn.adapters.primary.slack.slack_socket_client._get_active_cluster_name",
            return_value="prod-eu",
        ):
            await client._handle_socket_message(mock_ws, json.dumps(inner))

        assert adapter.handle_message.call_args[1]["channel_id"] == "C999"

    @pytest.mark.asyncio
    async def test_posts_response_via_publisher(self) -> None:
        client, adapter, publisher, _ = _make_client()
        adapter.handle_message.return_value = "pods are healthy"
        msg = self._make_event("app_mention")
        mock_ws = MagicMock()
        mock_ws.send = AsyncMock()

        with patch(
            "hexawyn.adapters.primary.slack.slack_socket_client._get_active_cluster_name",
            return_value="prod-eu",
        ):
            await client._handle_socket_message(mock_ws, json.dumps(msg))

        assert publisher.update_message.call_args[1]["text"] == "pods are healthy"

    @pytest.mark.asyncio
    async def test_continues_when_thinking_message_fails(self) -> None:
        client, adapter, publisher, _ = _make_client()
        publisher.post_message.return_value = None  # thinking failed
        msg = self._make_event("app_mention")
        mock_ws = MagicMock()
        mock_ws.send = AsyncMock()

        with patch(
            "hexawyn.adapters.primary.slack.slack_socket_client._get_active_cluster_name",
            return_value="prod-eu",
        ):
            await client._handle_socket_message(mock_ws, json.dumps(msg))

        adapter.handle_message.assert_called_once()
        publisher.update_message.assert_not_called()
        assert publisher.post_message.call_count == 2  # thinking + fallback result  # noqa: PLR2004

    @pytest.mark.asyncio
    async def test_handles_invalid_json_gracefully(self) -> None:
        client, adapter, _, _ = _make_client()
        mock_ws = MagicMock()
        mock_ws.send = AsyncMock()
        await client._handle_socket_message(mock_ws, "not valid json {{{")
        adapter.handle_message.assert_not_called()


# ── Run (async main loop) ─────────────────────────────────────────────────────


class TestRun:
    @pytest.mark.asyncio
    async def test_stops_when_running_is_false(self) -> None:
        client, _, _, _ = _make_client()
        client._running = False
        await client.run()

    @pytest.mark.asyncio
    async def test_sleeps_when_open_connection_returns_empty(self) -> None:
        client, _, _, _ = _make_client()

        with patch.object(client, "_open_connection", return_value=""):
            with patch("asyncio.sleep", new_callable=AsyncMock) as mock_sleep:
                client._running = True
                run_task = asyncio.ensure_future(client.run())
                await asyncio.sleep(0.05)
                client._running = False
                await run_task

            assert mock_sleep.call_count >= 1

    @pytest.mark.asyncio
    async def test_sleeps_on_websocket_connection_error(self) -> None:
        client, _, _, _ = _make_client()

        mock_connect = AsyncMock()
        mock_connect.__aenter__.side_effect = ConnectionError("refused")
        mock_connect.__aexit__.return_value = None

        with patch.object(client, "_open_connection", return_value="wss://fake.slack.com/link"):
            with patch("websockets.connect", return_value=mock_connect):
                with patch("asyncio.sleep", new_callable=AsyncMock) as mock_sleep:
                    client._running = True
                    run_task = asyncio.ensure_future(client.run())
                    await asyncio.sleep(0.05)
                    client._running = False
                    await run_task

            assert mock_sleep.call_count >= 1

    @pytest.mark.asyncio
    async def test_handles_connection_closed(self) -> None:
        from websockets.exceptions import ConnectionClosed
        from websockets.frames import Close

        client, _, _, _ = _make_client()

        mock_ws = MagicMock()
        mock_ws.__aiter__.side_effect = ConnectionClosed(
            rcvd=Close(1000, "ok"), sent=Close(1000, "ok"), rcvd_then_sent=False
        )

        async def _ctx_manager() -> MagicMock:
            return mock_ws

        mock_connect = MagicMock()
        mock_connect.__aenter__ = _ctx_manager

        with patch.object(client, "_open_connection", return_value="wss://fake.slack.com/link"):
            with patch("websockets.connect", return_value=mock_connect):
                with patch("asyncio.sleep", new_callable=AsyncMock) as mock_sleep:
                    client._running = True
                    run_task = asyncio.ensure_future(client.run())
                    await asyncio.sleep(0.05)
                    client._running = False
                    await run_task

            assert mock_sleep.call_count >= 1
