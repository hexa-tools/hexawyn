from hexawyn.adapters.secondary.slack.slack_http_client import SlackHttpClient
from hexawyn.application.ports.driven.message_publisher_port import MessagePublisherPort


class SlackHttpPublisher(MessagePublisherPort):
    """
    Posts messages to Slack via chat.postMessage using SLACK_BOT_TOKEN.
    SlackHttpClient is injected — never instantiated internally.
    Never raises — delivery failures return None.
    """

    def __init__(self, http_client: SlackHttpClient) -> None:
        self._client = http_client

    def post_message(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def update_message(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None
