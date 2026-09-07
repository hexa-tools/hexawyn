import os

import httpx

_SLACK_API_BASE = "https://slack.com/api"


class SlackHttpClient:
    """Low-level HTTP client for the Slack Web API. Injectable into secondary adapters."""

    def __init__(self, bot_token: str | None = None) -> None:
        self._token = bot_token if bot_token is not None else os.environ.get("SLACK_BOT_TOKEN", "")

    def post(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result
