import json
import re
from http.server import BaseHTTPRequestHandler, HTTPServer

from hexawyn.application.ports.driven.message_publisher_port import MessagePublisherPort
from hexawyn.application.ports.primary.chat_port import ChatPort


class SlackEventServer:
    """
    Primary adapter — HTTP server that receives Slack Events API webhooks.

    Handles:
    - url_verification: responds with Slack challenge (one-time app setup)
    - app_mention: runs investigation via ChatPort, posts result via MessagePublisherPort

    Both ChatPort and MessagePublisherPort are injected — no platform coupling.
    """

    def __init__(
        self,
        chat_adapter: ChatPort,
        publisher: MessagePublisherPort,
    ) -> None:
        self._chat_adapter = chat_adapter
        self._publisher = publisher

    def handle_event(self, body: dict[str, object]) -> dict[str, object]:
        """Route a Slack event. Pure function — testable without HTTP."""
        event_type = body.get("type")

        if event_type == "url_verification":
            return {"challenge": body.get("challenge", "")}

        if event_type == "event_callback":
            inner = body.get("event", {})
            if isinstance(inner, dict) and inner.get("type") == "app_mention":
                return self._handle_app_mention(inner)

        return {"ok": True}

    def _handle_app_mention(self, inner: dict[str, object]) -> dict[str, object]:
        text = str(inner.get("text", ""))
        query = re.sub(r"<@[A-Z0-9]+>", "", text).strip()
        channel_id = str(inner.get("channel", ""))
        thread_ts = inner.get("thread_ts") or inner.get("ts")
        thread_ts_str = str(thread_ts) if thread_ts else None
        cluster_name = _get_active_cluster_name()

        response = self._chat_adapter.handle_message(
            query=query,
            cluster_name=cluster_name,
            channel_id=channel_id,
            thread_ts=thread_ts_str,
        )
        self._publisher.post_message(
            channel_id=channel_id,
            text=response,
            thread_ts=thread_ts_str,
        )
        return {"ok": True}

    def start(self, port: int = 8080) -> None:
        """Start the HTTP server. Blocking — run from a dedicated process."""
        _self = self

        class _Handler(BaseHTTPRequestHandler):
            def do_POST(self) -> None:  # noqa: N802
                length = int(self.headers.get("Content-Length", 0))
                raw = self.rfile.read(length)
                try:
                    body = json.loads(raw)
                except json.JSONDecodeError:
                    self.send_response(400)
                    self.end_headers()
                    return
                result = _self.handle_event(body)
                payload = json.dumps(result).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, format: str, *args: object) -> None:
                pass  # silence stdlib access logs

        with HTTPServer(("", port), _Handler) as httpd:
            httpd.serve_forever()


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
