from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_command import (
    ChatCliCommand,
)
from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import (
    ChatCliResponse,
)
from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_use_case import (
    ChatCliUseCase,
    find_pod,
    service_name,
)


class TestChatCliUseCase:
    def test_execute_returns_response(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []
        k8s.get_cluster_context.return_value = {
            "name": "test",
            "cluster": "test-cluster",
            "provider": "vanilla",
            "namespace": "default",
        }
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "status": "ok",
            "answer": "test response",
            "suggestions": [],
            "usage": {},
            "embedding": [],
            "cause": "",
            "solution": "",
            "error": None,
            "predicted_intents": [],
        }

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        result = use_case.execute(ChatCliCommand(query="test query"))

        assert isinstance(result, ChatCliResponse)

    def test_execute_forwards_on_progress(self) -> None:
        """execute() exposes on_progress publicly (no private _execute call)."""
        k8s = MagicMock()
        k8s.get_cluster_context.return_value = {
            "name": "test",
            "cluster": "test-cluster",
            "provider": "vanilla",
            "namespace": "default",
        }
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "status": "ok",
            "answer": "test response",
            "suggestions": [],
            "usage": {},
            "embedding": [],
            "cause": "",
            "solution": "",
            "error": None,
            "predicted_intents": [],
        }
        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        captured: list[tuple[str, str]] = []

        def on_progress(node: str, label: str) -> None:
            captured.append((node, label))

        result = use_case.execute(ChatCliCommand(query="test query"), on_progress=on_progress)

        assert isinstance(result, ChatCliResponse)
        runtime.run_investigation.assert_called()
        assert (
            captured or runtime.run_investigation.call_args.kwargs.get("on_progress") is on_progress
        )

    def test_list_pods_returns_response(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []
        runtime = MagicMock()

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        result = use_case.list_pods()

        assert isinstance(result, ChatCliResponse)
        assert result.kind == "pods"

    def test_execute_with_empty_query(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []
        runtime = MagicMock()

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        result = use_case.execute(ChatCliCommand(query=""))

        assert isinstance(result, ChatCliResponse)
        assert result.kind == "unknown"

    def test_execute_whitespace_only_query(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []
        runtime = MagicMock()

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        result = use_case.execute(ChatCliCommand(query="   "))

        assert isinstance(result, ChatCliResponse)
        assert result.kind == "unknown"

    def test_show_logs_without_logs_port(self) -> None:
        k8s = MagicMock()
        runtime = MagicMock()

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        result = use_case.show_logs("test-service")

        assert result.kind == "unknown"
        assert any("not available" in line[0].lower() for line in result.lines)

    def test_show_logs_with_logs_port_no_results(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []
        runtime = MagicMock()
        logs = MagicMock()
        logs.search_logs.return_value = []

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime, logs_port=logs)
        result = use_case.show_logs("test-service")

        assert result.kind == "logs"
        assert any("No logs found" in line[0] for line in result.lines)

    def test_show_logs_with_pod_match(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            {
                "name": "payment-service-abc-def",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "age": "2d",
                "node": "node-1",
                "cpu_request_millicores": 100,
                "memory_request_mib": 256,
            },
        ]
        runtime = MagicMock()
        logs = MagicMock()
        logs.search_logs.return_value = [
            {
                "timestamp": "2026-07-28T10:00:00Z",
                "message": "Something happened",
                "severity": "INFO",
            },
        ]

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime, logs_port=logs)
        result = use_case.show_logs("payment-service")

        assert result.kind == "logs"
        assert len(result.lines) == 1  # noqa: PLR2004

    def test_explain_pending_no_pending_pods(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            {
                "name": "running-pod-abc",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "age": "1d",
                "node": "node-1",
            },
        ]
        runtime = MagicMock()

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        result = use_case.explain_pending([])

        assert result.kind == "pending"
        assert any("No pending pods" in line[0] for line in result.lines)

    def test_explain_pending_with_pending_pod(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            {
                "name": "pending-svc-xyz",
                "namespace": "default",
                "status": "Pending",
                "restarts": 0,
                "age": "5m",
                "node": "",
            },
        ]
        runtime = MagicMock()

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        result = use_case.explain_pending([])

        assert result.kind == "pending"
        assert any("Pending" in line[0] for line in result.lines)

    def test_explain_pending_with_findings_match(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            {
                "name": "payment-svc-abc-def",
                "namespace": "default",
                "status": "Pending",
                "restarts": 0,
                "age": "5m",
                "node": "",
            },
        ]
        runtime = MagicMock()
        findings = [
            {
                "severity": "warning",
                "message": "payment-svc cannot be scheduled",
                "remediation": "Add more nodes",
            },
        ]

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        result = use_case.explain_pending(findings)

        assert any("Add more nodes" in line[0] for line in result.lines)

    def test_list_pods_with_mixed_statuses(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            {
                "name": "pod-a-abc",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "age": "2d",
                "node": "node-1",
            },
            {
                "name": "pod-b-def",
                "namespace": "default",
                "status": "CrashLoop",
                "restarts": 10,
                "age": "1h",
                "node": "node-2",
            },
            {
                "name": "pod-c-ghi",
                "namespace": "default",
                "status": "Pending",
                "restarts": 0,
                "age": "5m",
                "node": "",
            },
        ]
        runtime = MagicMock()

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        result = use_case.list_pods()

        assert result.summary is not None
        assert "running" in result.summary
        assert "crashloop" in result.summary.lower()
        assert "pending" in result.summary.lower()
        assert len(result.suggestions) >= 2  # noqa: PLR2004

    def test_execute_with_incident_memory(self) -> None:
        k8s = MagicMock()
        k8s.get_cluster_context.return_value = {
            "name": "test",
            "cluster": "test-cluster",
            "provider": "vanilla",
            "namespace": "default",
        }
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "status": "ok",
            "answer": "test",
            "suggestions": [],
            "usage": {},
            "embedding": [0.1, 0.2, 0.3],
            "cause": "OOMKilled",
            "solution": "Increase memory",
            "error": None,
            "predicted_intents": [],
        }
        incident_memory = MagicMock()

        use_case = ChatCliUseCase(
            k8s_port=k8s,
            runtime=runtime,
            incident_memory_port=incident_memory,
        )
        result = use_case.execute(ChatCliCommand(query="test"))

        assert isinstance(result, ChatCliResponse)
        incident_memory.store_incident.assert_called_once()

    def test_execute_error_status_does_not_store_incident(self) -> None:
        k8s = MagicMock()
        k8s.get_cluster_context.return_value = {
            "name": "test",
            "cluster": "test-cluster",
            "provider": "vanilla",
            "namespace": "default",
        }
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "status": "error",
            "answer": "",
            "suggestions": [],
            "usage": {},
            "embedding": [],
            "cause": "",
            "solution": "",
            "error": "something failed",
            "predicted_intents": [],
        }
        incident_memory = MagicMock()

        use_case = ChatCliUseCase(
            k8s_port=k8s,
            runtime=runtime,
            incident_memory_port=incident_memory,
        )
        use_case.execute(ChatCliCommand(query="test"))

        incident_memory.store_incident.assert_not_called()

    def test_execute_with_usage_ledger(self) -> None:
        k8s = MagicMock()
        k8s.get_cluster_context.return_value = {
            "name": "test",
            "cluster": "test-cluster",
            "provider": "vanilla",
            "namespace": "default",
        }
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "status": "ok",
            "answer": "test",
            "suggestions": [],
            "usage": {
                "tool_name": "chat",
                "prompt_tokens": 100,
                "completion_tokens": 50,
                "model": "gpt4",
                "provider": "openai",
            },
            "embedding": [0.1],
            "cause": "test",
            "solution": "fix",
            "error": None,
            "predicted_intents": [],
        }
        usage_ledger = MagicMock()

        use_case = ChatCliUseCase(
            k8s_port=k8s,
            runtime=runtime,
            usage_ledger=usage_ledger,
        )
        use_case.execute(ChatCliCommand(query="test"))

        usage_ledger.record.assert_called_once()

    def test_execute_with_error_has_error_line(self) -> None:
        k8s = MagicMock()
        k8s.get_cluster_context.return_value = {
            "name": "test",
            "cluster": "test-cluster",
            "provider": "vanilla",
            "namespace": "default",
        }
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "status": "error",
            "answer": "",
            "suggestions": [],
            "usage": {},
            "embedding": [],
            "cause": "",
            "solution": "",
            "error": "connection timeout",
            "predicted_intents": [],
        }

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        result = use_case.execute(ChatCliCommand(query="test"))

        assert any("Error" in line[0] for line in result.lines)
        assert any("connection timeout" in line[0] for line in result.lines)

    def test_execute_suggestions_capped_at_4(self) -> None:
        k8s = MagicMock()
        k8s.get_cluster_context.return_value = {
            "name": "test",
            "cluster": "test-cluster",
            "provider": "vanilla",
            "namespace": "default",
        }
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "status": "ok",
            "answer": "test",
            "suggestions": ["a", "b", "c", "d", "e", "f"],
            "usage": {},
            "embedding": [0.1],
            "cause": "test",
            "solution": "fix",
            "error": None,
            "predicted_intents": [],
        }

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        result = use_case.execute(ChatCliCommand(query="test"))

        assert len(result.suggestions) == 4  # noqa: PLR2004

    def test_execute_with_retrieval_gate(self) -> None:
        k8s = MagicMock()
        k8s.get_cluster_context.return_value = {
            "name": "test",
            "cluster": "test-cluster",
            "provider": "vanilla",
            "namespace": "default",
        }
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "status": "ok",
            "answer": "test",
            "suggestions": [],
            "usage": {},
            "embedding": [0.1],
            "cause": "test",
            "solution": "fix",
            "error": None,
            "predicted_intents": [],
        }
        retrieval_gate = MagicMock()
        retrieval_gate.should_retrieve.return_value = False

        use_case = ChatCliUseCase(
            k8s_port=k8s,
            runtime=runtime,
            retrieval_gate=retrieval_gate,
        )
        result = use_case.execute(ChatCliCommand(query="test"))

        assert isinstance(result, ChatCliResponse)

    def test_execute_usage_ledger_exception_not_fatal(self) -> None:
        k8s = MagicMock()
        k8s.get_cluster_context.return_value = {
            "name": "test",
            "cluster": "test-cluster",
            "provider": "vanilla",
            "namespace": "default",
        }
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "status": "ok",
            "answer": "test",
            "suggestions": [],
            "usage": {},
            "embedding": [0.1],
            "cause": "test",
            "solution": "fix",
            "error": None,
            "predicted_intents": [],
        }
        usage_ledger = MagicMock()
        usage_ledger.record.side_effect = RuntimeError("db down")

        use_case = ChatCliUseCase(
            k8s_port=k8s,
            runtime=runtime,
            usage_ledger=usage_ledger,
        )
        result = use_case.execute(ChatCliCommand(query="test"))

        assert isinstance(result, ChatCliResponse)

    def test_execute_increment_quota_remote_exception(self) -> None:
        k8s = MagicMock()
        k8s.get_cluster_context.return_value = {
            "name": "test",
            "cluster": "test-cluster",
            "provider": "vanilla",
            "namespace": "default",
        }
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "status": "ok",
            "answer": "test",
            "suggestions": [],
            "usage": {},
            "embedding": [0.1],
            "cause": "test",
            "solution": "fix",
            "error": None,
            "predicted_intents": [],
        }
        runtime.increment_quota.side_effect = RuntimeError("quota service down")

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        result = use_case.execute(ChatCliCommand(query="test"))

        assert isinstance(result, ChatCliResponse)

    def test_pods_summary_with_other_status(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            {
                "name": "pod-a-abc",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "age": "2d",
                "node": "node-1",
            },
            {
                "name": "pod-b-def",
                "namespace": "default",
                "status": "Unknown",
                "restarts": 0,
                "age": "5m",
                "node": "",
            },
        ]
        runtime = MagicMock()

        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)
        result = use_case.list_pods()

        assert result.summary is not None
        assert "other" in result.summary


class TestServiceName:
    def test_standard_pod_name(self) -> None:
        assert service_name("nginx-deployment-abc123-def456") == "nginx-deployment"

    def test_short_pod_name(self) -> None:
        assert service_name("single") == "single"

    def test_two_part_pod_name(self) -> None:
        assert service_name("single-abc") == "single-abc"


class TestFindPod:
    def test_finds_by_service_name(self) -> None:
        pods = [
            {
                "name": "payment-service-abc-def",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "age": "2d",
                "node": "node-1",
            },
        ]
        result = find_pod("payment-service", pods)
        assert result is not None
        assert result["name"] == "payment-service-abc-def"

    def test_finds_by_full_pod_name(self) -> None:
        pods = [
            {
                "name": "nginx-deploy-xyz",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "age": "2d",
                "node": "node-1",
            },
        ]
        result = find_pod("nginx-deploy-xyz", pods)
        assert result is not None
        assert result["name"] == "nginx-deploy-xyz"

    def test_returns_none_when_not_found(self) -> None:
        pods: list = []
        result = find_pod("nonexistent", pods)
        assert result is None

    def test_returns_none_when_no_match(self) -> None:
        pods = [
            {
                "name": "other-svc-abc",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "age": "2d",
                "node": "node-1",
            },
        ]
        result = find_pod("nonexistent", pods)
        assert result is None
