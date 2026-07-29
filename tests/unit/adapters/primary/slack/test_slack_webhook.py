from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.adapters.primary.slack.slack_webhook import (
    _get_active_cluster_name,
    _handle_app_mention,
    handle_slack_event,
)


class TestHandleSlackEvent:
    def test_url_verification_returns_challenge(self) -> None:
        event: dict[str, object] = {"type": "url_verification", "challenge": "abc123"}
        result = handle_slack_event(event)
        assert result["challenge"] == "abc123"

    def test_url_verification_without_challenge_returns_empty_string(self) -> None:
        event: dict[str, object] = {"type": "url_verification"}
        result = handle_slack_event(event)
        assert result["challenge"] == ""

    def test_event_callback_dispatches_app_mention(self) -> None:
        event: dict[str, object] = {
            "type": "event_callback",
            "event": {
                "type": "app_mention",
                "text": "<@BOT> hello",
                "channel": "C123",
                "ts": "123.456",
            },
        }
        with patch(
            "hexawyn.adapters.primary.slack.slack_webhook._handle_app_mention"
        ) as mock_handler:
            mock_handler.return_value = {"response": "hi there", "channel": "C123"}
            result = handle_slack_event(event)
            assert result["response"] == "hi there"

    def test_event_callback_ignores_non_app_mention_events(self) -> None:
        result = handle_slack_event({"type": "event_callback", "event": {"type": "message"}})
        assert result == {"ok": True}

    def test_event_callback_with_non_dict_inner_returns_ok(self) -> None:
        result = handle_slack_event({"type": "event_callback", "event": "not_a_dict"})
        assert result == {"ok": True}

    def test_event_callback_without_event_key_returns_ok(self) -> None:
        result = handle_slack_event({"type": "event_callback"})
        assert result == {"ok": True}

    def test_unknown_event_type_returns_ok(self) -> None:
        result = handle_slack_event({"type": "unknown_event"})
        assert result == {"ok": True}

    def test_empty_event_returns_ok(self) -> None:
        result = handle_slack_event({})
        assert result == {"ok": True}


class TestHandleAppMention:
    def test_strips_bot_mention_and_calls_adapter(self) -> None:
        inner: dict[str, object] = {
            "text": "<@BOT> why is payments down?",
            "channel": "C123",
            "ts": "123.456",
        }
        with patch(
            "hexawyn.adapters.primary.slack.slack_webhook.SlackChatAdapter"
        ) as mock_adapter_cls:
            with patch(
                "hexawyn.adapters.primary.slack.slack_webhook._get_active_cluster_name"
            ) as mock_cluster:
                mock_cluster.return_value = "prod"
                mock_instance = MagicMock()
                mock_instance.handle_message.return_value = "SLACK QUOTA EXCEEDED response"
                mock_adapter_cls.return_value = mock_instance

                result = _handle_app_mention(inner)

                assert "SLACK QUOTA EXCEEDED response" in str(result["response"])
                assert result["channel"] == "C123"

    def test_passes_thread_ts_when_present(self) -> None:
        inner: dict[str, object] = {
            "text": "<@BOT> hello",
            "channel": "C456",
            "thread_ts": "999.888",
            "ts": "111.222",
        }
        with patch(
            "hexawyn.adapters.primary.slack.slack_webhook.SlackChatAdapter"
        ) as mock_adapter_cls:
            with patch(
                "hexawyn.adapters.primary.slack.slack_webhook._get_active_cluster_name"
            ) as mock_cluster:
                mock_cluster.return_value = "staging"
                mock_instance = MagicMock()
                mock_instance.handle_message.return_value = "response"
                mock_adapter_cls.return_value = mock_instance

                _handle_app_mention(inner)

                mock_instance.handle_message.assert_called_once_with(
                    query="hello",
                    cluster_name="staging",
                    channel_id="C456",
                    thread_ts="999.888",
                )

    def test_falls_back_to_ts_for_thread(self) -> None:
        inner: dict[str, object] = {
            "text": "<@BOT> test",
            "channel": "C789",
            "ts": "555.555",
        }
        with patch(
            "hexawyn.adapters.primary.slack.slack_webhook.SlackChatAdapter"
        ) as mock_adapter_cls:
            with patch(
                "hexawyn.adapters.primary.slack.slack_webhook._get_active_cluster_name"
            ) as mock_cluster:
                mock_cluster.return_value = "dev"
                mock_instance = MagicMock()
                mock_instance.handle_message.return_value = "ok"
                mock_adapter_cls.return_value = mock_instance

                _handle_app_mention(inner)

                mock_instance.handle_message.assert_called_once_with(
                    query="test",
                    cluster_name="dev",
                    channel_id="C789",
                    thread_ts="555.555",
                )

    def test_handles_empty_text(self) -> None:
        inner: dict[str, object] = {
            "text": "",
            "channel": "C000",
            "ts": "000.000",
        }
        with patch(
            "hexawyn.adapters.primary.slack.slack_webhook.SlackChatAdapter"
        ) as mock_adapter_cls:
            with patch(
                "hexawyn.adapters.primary.slack.slack_webhook._get_active_cluster_name"
            ) as mock_cluster:
                mock_cluster.return_value = "prod"
                mock_instance = MagicMock()
                mock_instance.handle_message.return_value = "empty query handled"
                mock_adapter_cls.return_value = mock_instance

                result = _handle_app_mention(inner)

                mock_instance.handle_message.assert_called_once_with(
                    query="",
                    cluster_name="prod",
                    channel_id="C000",
                    thread_ts="000.000",
                )
                assert "empty query handled" in str(result["response"])


class TestGetActiveClusterName:
    def test_returns_from_kubeconfig_reader(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.kubeconfig_reader.get_active_context"
        ) as mock_ctx:
            mock_ctx.return_value = {"name": "prod-eu", "cluster": {"server": "https://..."}}
            result = _get_active_cluster_name()
            assert result == "prod-eu"

    def test_returns_none_name_falls_back_to_kubectl(self) -> None:
        with (
            patch("hexawyn.infrastructure.config.kubeconfig_reader.get_active_context") as mock_ctx,
            patch("subprocess.run") as mock_run,
        ):
            mock_ctx.return_value = None
            mock_run.return_value = MagicMock(stdout="minikube\n", returncode=0)
            result = _get_active_cluster_name()
            assert result == "minikube"

    def test_kubeconfig_exception_falls_back_to_kubectl(self) -> None:
        with (
            patch("hexawyn.infrastructure.config.kubeconfig_reader.get_active_context") as mock_ctx,
            patch("subprocess.run") as mock_run,
        ):
            mock_ctx.side_effect = Exception("no kubeconfig")
            mock_run.return_value = MagicMock(stdout="aks-cluster\n", returncode=0)
            result = _get_active_cluster_name()
            assert result == "aks-cluster"

    def test_kubectl_non_zero_returncode_returns_unknown(self) -> None:
        with (
            patch("hexawyn.infrastructure.config.kubeconfig_reader.get_active_context") as mock_ctx,
            patch("subprocess.run") as mock_run,
        ):
            mock_ctx.side_effect = Exception("no kubeconfig")
            mock_run.return_value = MagicMock(stdout="", returncode=1)
            result = _get_active_cluster_name()
            assert result == "unknown"

    def test_kubectl_empty_stdout_returns_unknown(self) -> None:
        with (
            patch("hexawyn.infrastructure.config.kubeconfig_reader.get_active_context") as mock_ctx,
            patch("subprocess.run") as mock_run,
        ):
            mock_ctx.side_effect = Exception("no kubeconfig")
            mock_run.return_value = MagicMock(stdout="\n", returncode=0)
            result = _get_active_cluster_name()
            assert result == "unknown"

    def test_both_sources_fail_returns_unknown(self) -> None:
        with (
            patch("hexawyn.infrastructure.config.kubeconfig_reader.get_active_context") as mock_ctx,
            patch("subprocess.run") as mock_run,
        ):
            mock_ctx.side_effect = Exception("no kubeconfig")
            mock_run.side_effect = Exception("no kubectl")
            result = _get_active_cluster_name()
            assert result == "unknown"
