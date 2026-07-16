from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.runtime_port import InvestigationOutput, QuotaCheckResult
from hexawyn.application.service.chat_slack_service import ChatSlackService
from hexawyn.application.use_case.chat_slack.chat_slack_command import ChatSlackCommand
from hexawyn.application.use_case.chat_slack.chat_slack_response import ChatSlackResponse
from hexawyn.application.use_case.chat_slack.chat_slack_use_case import ChatSlackUseCase
from hexawyn.domain.errors import QuotaExceededError
from hexawyn.domain.models.cluster import ClusterContext


def _make_command(
    query: str = "why is payments-api crashing?",
    cluster_name: str = "prod-eu",
    thread_ts: str | None = None,
) -> ChatSlackCommand:
    return ChatSlackCommand(
        query=query,
        cluster_name=cluster_name,
        channel_id="C123456",
        thread_ts=thread_ts,
    )


def _make_output(
    answer: str = "OOM detected",
    suggestions: list[str] | None = None,
    error: str | None = None,
    status: str = "complete",
) -> InvestigationOutput:
    return InvestigationOutput(
        answer=answer,
        cause="",
        solution="",
        status=status,
        suggestions=suggestions or [],
        error=error,
        embedding=[],
        usage={},
    )


def _make_runtime(answer: str = "OOM detected", suggestions: list[str] | None = None) -> MagicMock:
    runtime = MagicMock()
    runtime.run_investigation.return_value = _make_output(answer=answer, suggestions=suggestions)
    runtime.check_quota.return_value = QuotaCheckResult(
        allowed=True, used=23, limit=50, remaining=27
    )
    return runtime


# ── Contract ──────────────────────────────────────────────────────────────────


class TestChatSlackServiceContract:
    def test_implements_use_case(self) -> None:
        service = ChatSlackService(runtime=MagicMock())
        assert isinstance(service, ChatSlackUseCase)

    def test_accepts_runtime_port(self) -> None:
        from hexawyn.application.ports.driven.runtime_port import RuntimePort

        runtime = MagicMock(spec=RuntimePort)
        service = ChatSlackService(runtime=runtime)
        assert service is not None

    def test_defaults_to_get_runtime_when_none(self) -> None:
        mock_runtime = MagicMock()
        with patch(
            "hexawyn.application.service.chat_slack_service.get_runtime",
            return_value=mock_runtime,
        ):
            service = ChatSlackService()
        assert service._runtime is mock_runtime


# ── Investigation ─────────────────────────────────────────────────────────────


class TestChatSlackServiceInvestigation:
    def setup_method(self) -> None:
        self.runtime = _make_runtime()
        self.service = ChatSlackService(runtime=self.runtime)

    def _execute(self, **kwargs: object) -> ChatSlackResponse:
        with patch(
            "hexawyn.application.service.chat_slack_service.get_quota_display",
            return_value="[23/50 · 27 remaining]",
        ):
            with patch(
                "hexawyn.application.service.chat_slack_service.is_pro",
                return_value=False,
            ):
                return self.service.execute(_make_command(**kwargs))

    def test_execute_returns_chat_slack_response(self) -> None:
        result = self._execute()
        assert isinstance(result, ChatSlackResponse)

    def test_execute_returns_answer_from_runtime(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(answer="OOM detected in pod")
        result = self._execute()
        assert result.message == "OOM detected in pod"

    def test_execute_calls_runtime_with_query(self) -> None:
        self._execute(query="why is payments-api crashing?")
        call_args = self.runtime.run_investigation.call_args
        assert call_args[0][0] == "why is payments-api crashing?"

    def test_execute_calls_runtime_with_cluster_context(self) -> None:
        self._execute(cluster_name="staging-eu")
        call_args = self.runtime.run_investigation.call_args
        ctx: ClusterContext = call_args[0][1]
        assert ctx.name == "staging-eu"

    def test_execute_includes_suggestions_from_runtime(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(
            suggestions=["scale up memory", "check HPA"]
        )
        result = self._execute()
        assert "scale up memory" in result.suggestions
        assert "check HPA" in result.suggestions

    def test_execute_includes_quota_display(self) -> None:
        result = self._execute()
        assert result.quota_display == "[23/50 · 27 remaining]"

    def test_execute_includes_is_pro(self) -> None:
        with patch(
            "hexawyn.application.service.chat_slack_service.get_quota_display",
            return_value="[⭐ Pro]",
        ):
            with patch("hexawyn.application.service.chat_slack_service.is_pro", return_value=True):
                result = self.service.execute(_make_command())
        assert result.is_pro is True

    def test_execute_with_thread_ts_passes_correctly(self) -> None:
        result = self._execute(thread_ts="1234.5678")
        assert isinstance(result, ChatSlackResponse)

    def test_runtime_not_called_when_quota_exceeded(self) -> None:
        self.runtime.check_quota.return_value = QuotaCheckResult(
            allowed=False, used=50, limit=50, remaining=0
        )
        with pytest.raises(QuotaExceededError):
            self.service.execute(_make_command())
        self.runtime.run_investigation.assert_not_called()

    def test_does_not_call_set_adapter(self) -> None:
        self._execute()
        self.runtime.set_adapter.assert_not_called()

    def test_suggestions_capped_at_four(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(
            suggestions=["a", "b", "c", "d", "e"]
        )
        result = self._execute()
        assert len(result.suggestions) <= 4


# ── Quota ─────────────────────────────────────────────────────────────────────


class TestChatSlackServiceQuota:
    def test_quota_checked_before_investigation(self) -> None:
        runtime = _make_runtime()
        runtime.check_quota.return_value = QuotaCheckResult(
            allowed=False, used=50, limit=50, remaining=0
        )
        service = ChatSlackService(runtime=runtime)
        with pytest.raises(QuotaExceededError):
            service.execute(_make_command())
        runtime.check_quota.assert_called_once()
        runtime.run_investigation.assert_not_called()

    def test_execute_raises_quota_exceeded_when_limit_reached(self) -> None:
        runtime = _make_runtime()
        runtime.check_quota.return_value = QuotaCheckResult(
            allowed=False, used=50, limit=50, remaining=0
        )
        service = ChatSlackService(runtime=runtime)
        with pytest.raises(QuotaExceededError):
            service.execute(_make_command())

    def test_execute_does_not_catch_exceptions(self) -> None:
        runtime = _make_runtime()
        runtime.check_quota.side_effect = RuntimeError("unexpected")
        service = ChatSlackService(runtime=runtime)
        with pytest.raises(RuntimeError):
            service.execute(_make_command())
