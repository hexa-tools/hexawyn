from __future__ import annotations

import asyncio
import json
import os
import re

import httpx
import websockets
from websockets.exceptions import ConnectionClosed

from hexawyn.adapters.secondary.slack.slack_http_client import SlackHttpClient
from hexawyn.application.ports.driven.message_publisher_port import MessagePublisherPort
from hexawyn.application.ports.primary.chat_port import ChatPort
from hexawyn.utils.logger import get_logger

_log = get_logger("slack.socket")


class SlackSocketClient:
    """
    Primary adapter — Slack Socket Mode client using WebSocket.

    Receives Slack events via WebSocket (no public URL needed),
    delegates investigations to ChatPort, posts responses via MessagePublisherPort.

    Requires SLACK_APP_TOKEN (xapp-...) for Socket Mode authentication.
    SLACK_BOT_TOKEN (xoxb-...) is used via SlackHttpClient for API calls.
    """

    def __init__(
        self,
        chat_adapter: ChatPort,
        publisher: MessagePublisherPort,
        http_client: SlackHttpClient | None = None,
        app_token: str | None = None,
        cluster_name: str | None = None,
    ) -> None:
        self._chat_adapter = chat_adapter
        self._publisher = publisher
        self._http_client = http_client or SlackHttpClient()
        self._app_token = app_token or os.environ.get("SLACK_APP_TOKEN", "")
        self._cluster_name = cluster_name
        self._running = False

    def _open_connection(self) -> str:
        try:
            response = httpx.post(
                "https://slack.com/api/apps.connections.open",
                headers={
                    "Authorization": f"Bearer {self._app_token}",
                    "Content-Type": "application/json",
                },
                json={},
                timeout=10.0,
            )
            result: dict[str, object] = response.json()
            if not isinstance(result, dict):
                _log.warning("apps.connections.open returned non-dict")
                return ""
            ok = result.get("ok")
            url = result.get("url")
            if ok is True and isinstance(url, str):
                _log.info("WebSocket URL obtained")
                return url
            _log.error("apps.connections.open failed: %s", result.get("error", "unknown"))
            return ""
        except Exception:
            _log.exception("apps.connections.open error")
            return ""

    async def _handle_socket_message(
        self,
        ws: websockets.ClientConnection,
        raw_message: str,
    ) -> None:
        try:
            message: dict[str, object] = json.loads(raw_message)
        except json.JSONDecodeError:
            return

        envelope_id = message.get("envelope_id")
        if isinstance(envelope_id, str):
            await self._send_ack(ws, envelope_id)

        msg_type = message.get("type")
        if msg_type != "events_api":
            _log.debug("ignoring message type: %s", msg_type)
            return

        payload = message.get("payload")
        if not isinstance(payload, dict):
            return

        event_type = payload.get("type")
        if event_type != "event_callback":
            _log.debug("ignoring payload type: %s", event_type)
            return

        inner = payload.get("event")
        if not isinstance(inner, dict):
            return

        if inner.get("type") != "app_mention":
            _log.debug("ignoring event type: %s", inner.get("type"))
            return

        text = str(inner.get("text", ""))
        query = re.sub(r"<@[A-Z0-9]+>", "", text).strip()
        channel_id = str(inner.get("channel", ""))
        thread_ts = inner.get("thread_ts") or inner.get("ts")
        thread_ts_str = str(thread_ts) if thread_ts else None
        cluster_name = self._cluster_name or _get_active_cluster_name()

        _log.info("app_mention: query=%r channel=%s cluster=%s", query, channel_id, cluster_name)

        thinking_ts = self._publisher.post_message(
            channel_id=channel_id,
            text=":mag: hexawyn is investigating...",
            thread_ts=thread_ts_str,
        )

        response = self._chat_adapter.handle_message(
            query=query,
            cluster_name=cluster_name,
            channel_id=channel_id,
            thread_ts=thread_ts_str,
        )
        _log.info("investigation response (first 120 chars): %s", response[:120])

        if thinking_ts is not None:
            self._publisher.update_message(
                channel_id=channel_id,
                message_ts=thinking_ts,
                text=response,
            )
        else:
            self._publisher.post_message(
                channel_id=channel_id,
                text=response,
                thread_ts=thread_ts_str,
            )

    async def _send_ack(
        self,
        ws: websockets.ClientConnection,
        envelope_id: str,
    ) -> None:
        try:
            ack = json.dumps({"envelope_id": envelope_id})
            await ws.send(ack)
        except Exception:
            pass

    async def run(self) -> None:
        while self._running:
            ws_url = self._open_connection()
            if not ws_url:
                _log.warning("no WebSocket URL, retrying in 5s...")
                await asyncio.sleep(5)
                continue
            try:
                _log.info("connecting to Slack Socket Mode...")
                async with websockets.connect(ws_url) as ws:
                    _log.info("connected, listening for events")
                    async for raw in ws:
                        if not self._running:
                            break
                        if isinstance(raw, str):
                            await self._handle_socket_message(ws, raw)
            except ConnectionClosed:
                _log.warning("WebSocket connection closed, reconnecting...")
            except Exception:
                _log.exception("WebSocket error, reconnecting...")
            await asyncio.sleep(5)


def _get_active_cluster_name() -> str:
    try:
        from hexawyn.infrastructure.config.kubeconfig_reader import get_active_context

        ctx = get_active_context()
        if ctx is not None and ctx.get("name"):
            return str(ctx.get("name"))
    except Exception:
        pass

    try:
        import subprocess

        result = subprocess.run(
            ["kubectl", "config", "current-context"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass

    return "unknown"
