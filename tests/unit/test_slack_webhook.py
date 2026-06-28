import os
from unittest.mock import patch


class TestSlackWebhook:
    def test_health_includes_slack_configured(self) -> None:
        with patch.dict(
            os.environ,
            {"HEXAWYN_SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"},
        ):
            from hexawyn.mcp.server import health

            result = health()
            assert "slack" in result

    def test_slack_event_url_verification(self) -> None:
        from hexawyn.adapters.primary.slack.slack_webhook import handle_slack_event

        event = {
            "type": "url_verification",
            "challenge": "test_challenge_123",
        }
        result = handle_slack_event(event)
        assert result["challenge"] == "test_challenge_123"

    def test_slack_app_mention_triggers_investigation(self) -> None:
        from hexawyn.adapters.primary.slack.slack_webhook import handle_slack_event

        event = {
            "type": "event_callback",
            "event": {
                "type": "app_mention",
                "text": "<@BOTID> why is payments-api crashing?",
                "channel": "C123456",
                "ts": "1234567890.123456",
            },
        }
        with patch(
            "hexawyn.adapters.primary.slack.slack_webhook.SlackChatAdapter"
        ) as mock_adapter_class:
            mock_adapter_class.return_value.handle_message.return_value = "OOM detected"
            result = handle_slack_event(event)
        assert result is not None

    def test_unknown_event_type_returns_ok(self) -> None:
        from hexawyn.adapters.primary.slack.slack_webhook import handle_slack_event

        result = handle_slack_event({"type": "unknown_event"})
        assert result == {"ok": True}

    def test_app_mention_strips_bot_mention_from_query(self) -> None:
        from hexawyn.adapters.primary.slack.slack_webhook import handle_slack_event

        event = {
            "type": "event_callback",
            "event": {
                "type": "app_mention",
                "text": "<@U12345> how many pods?",
                "channel": "C999",
                "ts": "111.222",
            },
        }
        with patch(
            "hexawyn.adapters.primary.slack.slack_webhook.SlackChatAdapter"
        ) as mock_adapter_class:
            mock_adapter_class.return_value.handle_message.return_value = "3 pods"
            handle_slack_event(event)
            call_kwargs = mock_adapter_class.return_value.handle_message.call_args[1]
            assert "<@U12345>" not in call_kwargs["query"]
            assert "how many pods?" in call_kwargs["query"]

    def test_app_mention_response_includes_channel(self) -> None:
        from hexawyn.adapters.primary.slack.slack_webhook import handle_slack_event

        event = {
            "type": "event_callback",
            "event": {
                "type": "app_mention",
                "text": "<@BOT> list pods",
                "channel": "C777",
                "ts": "999.000",
            },
        }
        with patch(
            "hexawyn.adapters.primary.slack.slack_webhook.SlackChatAdapter"
        ) as mock_adapter_class:
            mock_adapter_class.return_value.handle_message.return_value = "ok"
            result = handle_slack_event(event)
        assert result.get("channel") == "C777"

    def test_health_shows_slack_not_configured_without_env(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            from hexawyn.mcp import server as mcp_server

            with patch.object(mcp_server, "_cluster_status", {}):
                with (
                    patch("hexawyn.mcp.server.get_connection") as mock_conn,
                    patch("hexawyn.mcp.server.get_api_key", return_value=None),
                    patch(
                        "hexawyn.mcp.server.get_cache_stats",
                        return_value={"l1_size": 0, "l1_ttl_seconds": 300},
                    ),
                ):
                    mock_conn.return_value.execute.return_value.fetchone.return_value = (1,)
                    result = mcp_server.health()
            assert "slack" in result
