from unittest.mock import MagicMock

from hexawyn.application.ports.driven.k8s_port import ClusterContext, PodInfo
from hexawyn.application.ports.driven.runtime_port import InvestigationOutput
from hexawyn.application.service.chat_cli_service import (
    ChatCliService,
    _pods_summary,
    _suggested_chips,
    find_pod,
    service_name,
)
from hexawyn.application.use_case.chat_cli.chat_cli_command import ChatCliCommand
from hexawyn.application.use_case.chat_cli.chat_cli_response import ChatCliResponse
from hexawyn.application.use_case.chat_cli.chat_cli_use_case import ChatCliUseCase


def _make_ctx() -> ClusterContext:
    return ClusterContext(name="prod-eu", cluster="k8s", provider="aws", namespace="default")


def _make_output(
    answer: str = "OOM detected",
    status: str = "ok",
    suggestions: list[str] | None = None,
    error: str | None = None,
    cause: str = "",
    solution: str = "",
    embedding: list[float] | None = None,
    usage: dict[str, int | str] | None = None,
) -> InvestigationOutput:
    return InvestigationOutput(
        answer=answer,
        cause=cause,
        solution=solution,
        status=status,
        suggestions=suggestions or [],
        error=error,
        embedding=embedding or [],
        usage=usage or {},
    )


# ── Contract ──────────────────────────────────────────────────────────────────


class TestChatCliServiceContract:
    def test_implements_use_case(self) -> None:
        service = ChatCliService(k8s_port=MagicMock(), runtime=MagicMock())
        assert isinstance(service, ChatCliUseCase)


# ── Empty query ───────────────────────────────────────────────────────────────


class TestChatCliServiceEmptyQuery:
    def test_empty_query_returns_unknown_kind(self) -> None:
        service = ChatCliService(k8s_port=MagicMock(), runtime=MagicMock())
        result = service.execute(ChatCliCommand(query=""))
        assert result.kind == "unknown"

    def test_whitespace_query_returns_unknown_kind(self) -> None:
        service = ChatCliService(k8s_port=MagicMock(), runtime=MagicMock())
        result = service.execute(ChatCliCommand(query="   "))
        assert result.kind == "unknown"

    def test_empty_query_returns_hint_line(self) -> None:
        service = ChatCliService(k8s_port=MagicMock(), runtime=MagicMock())
        result = service.execute(ChatCliCommand(query=""))
        assert len(result.lines) == 1
        assert "type" in result.lines[0][0].lower() or "command" in result.lines[0][0].lower()


# ── Investigation ─────────────────────────────────────────────────────────────


class TestChatCliServiceInvestigation:
    def setup_method(self) -> None:
        self.k8s = MagicMock()
        self.runtime = MagicMock()
        self.k8s.get_cluster_context.return_value = _make_ctx()
        self.service = ChatCliService(k8s_port=self.k8s, runtime=self.runtime)

    def test_execute_returns_chat_cli_response(self) -> None:
        self.runtime.run_investigation.return_value = _make_output()
        result = self.service.execute(ChatCliCommand(query="why is payments-api crashing?"))
        assert isinstance(result, ChatCliResponse)

    def test_result_kind_is_debug(self) -> None:
        self.runtime.run_investigation.return_value = _make_output()
        result = self.service.execute(ChatCliCommand(query="debug payments-api"))
        assert result.kind == "debug"

    def test_answer_appears_in_lines(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(answer="OOM detected")
        result = self.service.execute(ChatCliCommand(query="investigate"))
        texts = [line[0] for line in result.lines]
        assert any("OOM detected" in t for t in texts)

    def test_suggestions_from_output_are_included(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(
            suggestions=["scale up memory", "check HPA"]
        )
        result = self.service.execute(ChatCliCommand(query="investigate"))
        assert "scale up memory" in result.suggestions
        assert "check HPA" in result.suggestions

    def test_suggestions_are_capped_at_four(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(
            suggestions=["a", "b", "c", "d", "e"]
        )
        result = self.service.execute(ChatCliCommand(query="investigate"))
        assert len(result.suggestions) <= 4

    def test_error_message_appears_in_lines(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(answer="", error="timeout")
        result = self.service.execute(ChatCliCommand(query="investigate"))
        texts = [line[0] for line in result.lines]
        assert any("timeout" in t.lower() for t in texts)

    def test_degraded_status_does_not_block_answer(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(
            answer="partial response", status="degraded"
        )
        result = self.service.execute(ChatCliCommand(query="investigate"))
        texts = [line[0] for line in result.lines]
        assert any("partial response" in t for t in texts)

    def test_runtime_is_called_with_query(self) -> None:
        self.runtime.run_investigation.return_value = _make_output()
        self.service.execute(ChatCliCommand(query="show pods"))
        call_args = self.runtime.run_investigation.call_args
        assert call_args[0][0] == "show pods"

    def test_adapter_is_set_on_runtime(self) -> None:
        self.runtime.run_investigation.return_value = _make_output()
        self.service.execute(ChatCliCommand(query="investigate"))
        self.runtime.set_adapter.assert_called_once_with(self.k8s)

    def test_result_has_no_pods_for_investigation(self) -> None:
        self.runtime.run_investigation.return_value = _make_output()
        result = self.service.execute(ChatCliCommand(query="why is api crashing?"))
        assert result.pods is None


# ── Incident memory ───────────────────────────────────────────────────────────


class TestChatCliServiceIncidentMemory:
    def setup_method(self) -> None:
        self.k8s = MagicMock()
        self.runtime = MagicMock()
        self.memory = MagicMock()
        self.k8s.get_cluster_context.return_value = _make_ctx()
        self.service = ChatCliService(
            k8s_port=self.k8s,
            runtime=self.runtime,
            incident_memory_port=self.memory,
        )

    def test_stores_incident_on_successful_investigation_with_embedding(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(
            cause="OOMKilled", solution="raise limit", embedding=[0.1, 0.2]
        )
        self.service.execute(ChatCliCommand(query="why is api down?"))

        self.memory.store_incident.assert_called_once()
        record = self.memory.store_incident.call_args[0][0]
        assert record.cluster_name == "prod-eu"
        assert record.tool_name == "chat_investigation"
        assert record.cause == "OOMKilled"
        assert record.solution == "raise limit"
        assert record.embedding == [0.1, 0.2]

    def test_does_not_store_when_no_embedding(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(embedding=[])
        self.service.execute(ChatCliCommand(query="investigate"))
        self.memory.store_incident.assert_not_called()

    def test_does_not_store_on_error_status(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(
            status="error", error="timeout", embedding=[0.1]
        )
        self.service.execute(ChatCliCommand(query="investigate"))
        self.memory.store_incident.assert_not_called()

    def test_no_memory_port_is_safe(self) -> None:
        service = ChatCliService(k8s_port=self.k8s, runtime=self.runtime)
        self.runtime.run_investigation.return_value = _make_output(embedding=[0.1])
        result = service.execute(ChatCliCommand(query="investigate"))
        assert isinstance(result, ChatCliResponse)


# ── Logs port ─────────────────────────────────────────────────────────────────


class TestChatCliServiceLogs:
    def test_service_accepts_optional_logs_port(self) -> None:
        service = ChatCliService(k8s_port=MagicMock(), runtime=MagicMock(), logs_port=None)
        assert service is not None

    def test_show_logs_returns_unavailable_without_logs_port(self) -> None:
        service = ChatCliService(k8s_port=MagicMock(), runtime=MagicMock(), logs_port=None)
        result = service.show_logs("show logs for payments")
        assert result.kind == "unknown"
        assert any("not available" in line.lower() for line, _ in result.lines)

    def test_show_logs_returns_no_logs_found_when_empty(self) -> None:
        logs_port = MagicMock()
        logs_port.search_logs.return_value = []
        k8s = MagicMock()
        k8s.list_pods.return_value = []
        service = ChatCliService(k8s_port=k8s, runtime=MagicMock(), logs_port=logs_port)
        result = service.show_logs("show logs for payments")
        assert result.kind == "logs"
        assert any("No logs found" in line for line, _ in result.lines)

    def test_show_logs_returns_log_lines(self) -> None:
        logs_port = MagicMock()
        logs_port.search_logs.return_value = [
            {"severity": "ERROR", "timestamp": "2026-06-28T06:00:00Z", "message": "OOM killed"},
        ]
        k8s = MagicMock()
        k8s.list_pods.return_value = []
        service = ChatCliService(k8s_port=k8s, runtime=MagicMock(), logs_port=logs_port)
        result = service.show_logs("show logs for payments")
        assert result.kind == "logs"
        assert any("OOM killed" in line for line, _ in result.lines)


# ── List pods ─────────────────────────────────────────────────────────────────


class TestChatCliServiceListPods:
    def test_list_pods_returns_pods_kind(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            PodInfo(name="api-7f8d9c-xk2lp", namespace="default", status="Running", restarts=0),
        ]
        service = ChatCliService(k8s_port=k8s, runtime=MagicMock())
        result = service.list_pods()
        assert result.kind == "pods"
        assert result.pods is not None
        assert len(result.pods) == 1
        assert result.summary is not None

    def test_list_pods_summary_has_count(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            PodInfo(name="api-abc-123", namespace="default", status="Running", restarts=0),
        ]
        service = ChatCliService(k8s_port=k8s, runtime=MagicMock())
        result = service.list_pods()
        assert "1 pods" in (result.summary or "")


# ── Pending ───────────────────────────────────────────────────────────────────


class TestChatCliServiceExplainPending:
    def test_no_pending_pods_returns_green_message(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            PodInfo(name="api", namespace="default", status="Running", restarts=0),
        ]
        service = ChatCliService(k8s_port=k8s, runtime=MagicMock())
        result = service.explain_pending([])
        assert result.kind == "pending"
        assert any("No pending" in line for line, _ in result.lines)

    def test_lists_pending_pods(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            PodInfo(name="worker-abc12-xyz34", namespace="default", status="Pending", restarts=0),
        ]
        service = ChatCliService(k8s_port=k8s, runtime=MagicMock())
        result = service.explain_pending([])
        assert result.kind == "pending"
        assert any("worker-abc12-xyz34" in line for line, _ in result.lines)

    def test_includes_finding_remediation(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            PodInfo(name="worker-abc12-xyz34", namespace="default", status="Pending", restarts=0),
        ]
        service = ChatCliService(k8s_port=k8s, runtime=MagicMock())
        findings = [
            {
                "severity": "warning",
                "message": "Pod worker is Pending",
                "remediation": "Check node capacity.",
            }
        ]
        result = service.explain_pending(findings)
        assert any("Check node capacity" in line for line, _ in result.lines)


# ── Pure helper functions ─────────────────────────────────────────────────────


class TestServiceName:
    def test_strips_trailing_hash_segments(self) -> None:
        assert service_name("payments-api-7f8d9c-xk2lp") == "payments-api"

    def test_returns_name_unchanged_when_two_parts(self) -> None:
        assert service_name("payments-api") == "payments-api"

    def test_returns_name_unchanged_when_one_part(self) -> None:
        assert service_name("payments") == "payments"

    def test_strips_three_segments(self) -> None:
        assert service_name("airflow-worker-86675-abc12") == "airflow-worker"


class TestFindPod:
    def _pods(self) -> list[PodInfo]:
        return [
            PodInfo(
                name="payments-api-7f8d9c-xk2lp", namespace="default", status="Running", restarts=0
            ),
            PodInfo(
                name="airflow-worker-86675-abc12", namespace="airflow", status="Pending", restarts=0
            ),
        ]

    def test_finds_pod_by_service_name(self) -> None:
        pod = find_pod("debug payments-api", self._pods())
        assert pod is not None
        assert pod["name"] == "payments-api-7f8d9c-xk2lp"

    def test_finds_pod_by_full_name(self) -> None:
        pod = find_pod("payments-api-7f8d9c-xk2lp", self._pods())
        assert pod is not None

    def test_returns_none_when_no_match(self) -> None:
        pod = find_pod("unknown-service", self._pods())
        assert pod is None

    def test_finds_second_pod(self) -> None:
        pod = find_pod("airflow-worker", self._pods())
        assert pod is not None
        assert pod["namespace"] == "airflow"


class TestPodsSummary:
    def test_counts_running_pods(self) -> None:
        pods = [
            PodInfo(name="a", namespace="default", status="Running", restarts=0),
            PodInfo(name="b", namespace="default", status="Running", restarts=0),
        ]
        summary = _pods_summary(pods)
        assert "2 pods" in summary
        assert "2 running" in summary

    def test_includes_crashloop_count(self) -> None:
        pods = [
            PodInfo(name="a", namespace="default", status="Running", restarts=0),
            PodInfo(name="b", namespace="default", status="CrashLoop", restarts=5),
        ]
        summary = _pods_summary(pods)
        assert "1 crashloop" in summary

    def test_includes_pending_count(self) -> None:
        pods = [PodInfo(name="a", namespace="default", status="Pending", restarts=0)]
        summary = _pods_summary(pods)
        assert "1 pending" in summary

    def test_includes_other_count(self) -> None:
        pods = [PodInfo(name="a", namespace="default", status="Terminating", restarts=0)]
        summary = _pods_summary(pods)
        assert "1 other" in summary

    def test_no_optional_parts_when_all_running(self) -> None:
        pods = [PodInfo(name="a", namespace="default", status="Running", restarts=0)]
        summary = _pods_summary(pods)
        assert "crashloop" not in summary
        assert "pending" not in summary


class TestSuggestedChips:
    def test_suggests_debug_for_crashloop(self) -> None:
        pods = [
            PodInfo(
                name="payments-api-7f8d9c-xk2lp",
                namespace="default",
                status="CrashLoop",
                restarts=5,
            )
        ]
        chips = _suggested_chips(pods)
        assert any("debug" in c for c in chips)

    def test_suggests_why_pending_for_pending(self) -> None:
        pods = [
            PodInfo(name="worker-abc12-xyz34", namespace="default", status="Pending", restarts=0)
        ]
        chips = _suggested_chips(pods)
        assert any("pending" in c for c in chips)

    def test_suggests_logs_for_running(self) -> None:
        pods = [PodInfo(name="api-7f8d9c-xk2lp", namespace="default", status="Running", restarts=0)]
        chips = _suggested_chips(pods)
        assert any("logs" in c for c in chips)

    def test_returns_empty_when_no_pods(self) -> None:
        assert _suggested_chips([]) == []


# ── Usage ledger ──────────────────────────────────────────────────────────────


class TestChatCliServiceUsageLedger:
    def setup_method(self) -> None:
        self.k8s = MagicMock()
        self.runtime = MagicMock()
        self.ledger = MagicMock()
        self.k8s.get_cluster_context.return_value = _make_ctx()
        self.service = ChatCliService(
            k8s_port=self.k8s,
            runtime=self.runtime,
            usage_ledger=self.ledger,
        )

    def test_records_usage_after_investigation(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(
            answer="OOM detected",
            status="ok",
            usage={
                "prompt_tokens": 450,
                "completion_tokens": 180,
                "model": "qwen3:8b",
                "provider": "ollama",
            },
        )
        self.service.execute(ChatCliCommand(query="why is payments-api crashing?"))

        self.ledger.record.assert_called_once()
        entry = self.ledger.record.call_args[0][0]
        assert entry["query"] == "why is payments-api crashing?"
        assert entry["cluster_name"] == "prod-eu"
        assert entry["verdict"] == "ok"
        assert entry["duration_ms"] >= 0

    def test_records_usage_with_tool_name_from_usage(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(
            usage={
                "tool_name": "crashloop_detector",
                "prompt_tokens": 100,
                "completion_tokens": 50,
                "model": "qwen3:8b",
                "provider": "ollama",
            },
        )
        self.service.execute(ChatCliCommand(query="debug payments-api"))

        entry = self.ledger.record.call_args[0][0]
        assert entry["tool_name"] == "crashloop_detector"

    def test_no_ledger_is_safe(self) -> None:
        service = ChatCliService(k8s_port=self.k8s, runtime=self.runtime)
        self.runtime.run_investigation.return_value = _make_output()
        result = service.execute(ChatCliCommand(query="investigate"))
        assert isinstance(result, ChatCliResponse)

    def test_ledger_exception_does_not_block_investigation(self) -> None:
        self.ledger.record.side_effect = RuntimeError("disk full")
        self.runtime.run_investigation.return_value = _make_output(answer="OOM detected")

        result = self.service.execute(ChatCliCommand(query="debug"))

        assert isinstance(result, ChatCliResponse)
        assert any("OOM detected" in line[0] for line in result.lines)

    def test_zero_tokens_when_usage_empty(self) -> None:
        self.runtime.run_investigation.return_value = _make_output(usage={})
        self.service.execute(ChatCliCommand(query="list pods"))

        entry = self.ledger.record.call_args[0][0]
        assert entry["prompt_tokens"] == 0
        assert entry["completion_tokens"] == 0
        assert entry["model"] == "-"

    def test_namespace_from_k8s_context(self) -> None:
        self.runtime.run_investigation.return_value = _make_output()
        self.service.execute(ChatCliCommand(query="investigate"))

        entry = self.ledger.record.call_args[0][0]
        assert entry["namespace"] == "default"
