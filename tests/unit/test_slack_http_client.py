from unittest.mock import patch

from hexawyn.adapters.secondary.slack.slack_http_client import SlackHttpClient


class TestSlackHttpClientInit:
    def test_accepts_explicit_token(self) -> None:
        client = SlackHttpClient(bot_token="xoxb-test-token")
        assert client._token == "xoxb-test-token"

    def test_reads_token_from_env_when_none(self) -> None:
        with patch.dict("os.environ", {"SLACK_BOT_TOKEN": "xoxb-env-token"}):
            client = SlackHttpClient()
        assert client._token == "xoxb-env-token"

    def test_empty_token_when_no_env(self) -> None:
        with patch.dict("os.environ", {}, clear=True):
            with patch(
                "hexawyn.adapters.secondary.slack.slack_http_client.os.environ.get",
                return_value="",
            ):
                client = SlackHttpClient()
        assert client._token == ""


class TestSlackHttpClientPost:
    def setup_method(self) -> None:
        self.client = SlackHttpClient(bot_token="xoxb-test-token")

    def test_posts_to_correct_slack_endpoint(self) -> None:
        with patch("httpx.post") as mock_post:
            mock_post.return_value.json.return_value = {"ok": True}
            self.client.post("chat.postMessage", {"channel": "C123", "text": "hello"})
        url = mock_post.call_args[0][0]
        assert "slack.com/api/chat.postMessage" in url

    def test_sends_bearer_token_in_header(self) -> None:
        with patch("httpx.post") as mock_post:
            mock_post.return_value.json.return_value = {"ok": True}
            self.client.post("chat.postMessage", {"channel": "C123", "text": "hello"})
        headers = mock_post.call_args[1]["headers"]
        assert headers["Authorization"] == "Bearer xoxb-test-token"

    def test_sends_payload_as_json(self) -> None:
        with patch("httpx.post") as mock_post:
            mock_post.return_value.json.return_value = {"ok": True}
            self.client.post("chat.postMessage", {"channel": "C123", "text": "hello"})
        json_body = mock_post.call_args[1]["json"]
        assert json_body["channel"] == "C123"
        assert json_body["text"] == "hello"

    def test_returns_parsed_json_response(self) -> None:
        with patch("httpx.post") as mock_post:
            mock_post.return_value.json.return_value = {"ok": True, "ts": "1234.5678"}
            result = self.client.post("chat.postMessage", {"channel": "C123", "text": "hi"})
        assert result["ok"] is True
        assert result["ts"] == "1234.5678"

    def test_raises_on_network_error(self) -> None:
        import pytest

        with patch("httpx.post", side_effect=Exception("connection refused")):
            with pytest.raises(Exception, match="connection refused"):
                self.client.post("chat.postMessage", {"channel": "C123", "text": "hi"})
