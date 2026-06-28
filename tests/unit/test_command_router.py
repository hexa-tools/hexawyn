from unittest.mock import MagicMock, patch

from hexawyn.cli.command_router import (
    _debug_pod,
    _explain_pending,
    _find_pod,
    _investigate,
    _list_pods,
    _pods_summary,
    _service_name,
    _show_logs,
    _suggested_chips,
    route_command,
)


class TestServiceName:
    def test_strips_trailing_hash_segments(self) -> None:
        assert _service_name("payments-api-7f8d9c-xk2lp") == "payments-api"

    def test_returns_name_unchanged_when_two_parts(self) -> None:
        assert _service_name("payments-api") == "payments-api"

    def test_returns_name_unchanged_when_one_part(self) -> None:
        assert _service_name("payments") == "payments"

    def test_strips_three_segments(self) -> None:
        assert _service_name("airflow-worker-86675-abc12") == "airflow-worker"


class TestFindPod:
    def _pods(self) -> list[dict[str, object]]:
        return [
            {
                "name": "payments-api-7f8d9c-xk2lp",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
            },
            {
                "name": "airflow-worker-86675-abc12",
                "namespace": "airflow",
                "status": "Pending",
                "restarts": 0,
            },
        ]

    def test_finds_pod_by_service_name(self) -> None:
        pod = _find_pod("debug payments-api", self._pods())
        assert pod is not None
        assert pod["name"] == "payments-api-7f8d9c-xk2lp"

    def test_finds_pod_by_full_name(self) -> None:
        pod = _find_pod("payments-api-7f8d9c-xk2lp", self._pods())
        assert pod is not None

    def test_returns_none_when_no_match(self) -> None:
        pod = _find_pod("unknown-service", self._pods())
        assert pod is None

    def test_finds_second_pod(self) -> None:
        pod = _find_pod("airflow-worker", self._pods())
        assert pod is not None
        assert pod["namespace"] == "airflow"


class TestPodsSummary:
    def test_counts_running_pods(self) -> None:
        pods = [
            {"name": "a", "status": "Running", "restarts": 0},
            {"name": "b", "status": "Running", "restarts": 0},
        ]
        summary = _pods_summary(pods)
        assert "2 pods" in summary
        assert "2 running" in summary

    def test_includes_crashloop_count(self) -> None:
        pods = [
            {"name": "a", "status": "Running", "restarts": 0},
            {"name": "b", "status": "CrashLoop", "restarts": 5},
        ]
        summary = _pods_summary(pods)
        assert "1 crashloop" in summary

    def test_includes_pending_count(self) -> None:
        pods = [
            {"name": "a", "status": "Pending", "restarts": 0},
        ]
        summary = _pods_summary(pods)
        assert "1 pending" in summary

    def test_includes_other_count(self) -> None:
        pods = [
            {"name": "a", "status": "Terminating", "restarts": 0},
        ]
        summary = _pods_summary(pods)
        assert "1 other" in summary

    def test_no_optional_parts_when_all_running(self) -> None:
        pods = [{"name": "a", "status": "Running", "restarts": 0}]
        summary = _pods_summary(pods)
        assert "crashloop" not in summary
        assert "pending" not in summary


class TestSuggestedChips:
    def test_suggests_debug_for_crashloop(self) -> None:
        pods = [{"name": "payments-api-7f8d9c-xk2lp", "status": "CrashLoop", "restarts": 5}]
        chips = _suggested_chips(pods)
        assert any("debug" in c for c in chips)

    def test_suggests_why_pending_for_pending(self) -> None:
        pods = [{"name": "worker-abc12-xyz34", "status": "Pending", "restarts": 0}]
        chips = _suggested_chips(pods)
        assert any("pending" in c for c in chips)

    def test_suggests_logs_for_running(self) -> None:
        pods = [{"name": "api-7f8d9c-xk2lp", "status": "Running", "restarts": 0}]
        chips = _suggested_chips(pods)
        assert any("logs" in c for c in chips)

    def test_returns_empty_when_no_pods(self) -> None:
        assert _suggested_chips([]) == []


class TestListPods:
    def test_returns_pods_result(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = [
            {"name": "api-7f8d9c-xk2lp", "status": "Running", "restarts": 0},
        ]
        result = _list_pods(mock_adapter)
        assert result.kind == "pods"
        assert len(result.pods) == 1  # type: ignore[arg-type]
        assert result.summary is not None
        assert "1 pods" in result.summary


class TestDebugPod:
    def test_returns_unknown_when_pod_not_found(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = []
        result = _debug_pod(mock_adapter, "debug unknown-pod")
        assert result.kind == "unknown"

    def test_investigates_when_pod_found(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = [
            {
                "name": "payments-api-7f8d9c",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
            },
        ]
        mock_adapter.get_cluster_context.return_value = {"name": "prod", "provider": "vanilla"}
        mock_runtime = MagicMock()
        mock_runtime.run_investigation.return_value = {
            "answer": "OOM detected",
            "cause": "Low memory",
            "solution": "Increase limits",
            "status": "complete",
            "suggestions": [],
            "error": None,
        }
        with patch("hexawyn.cli.command_router.get_runtime", return_value=mock_runtime):
            result = _debug_pod(mock_adapter, "debug payments-api")
        assert result.kind == "debug"


class TestInvestigate:
    def _mock_runtime(self) -> MagicMock:
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "answer": "Memory limit too low",
            "cause": "OOM",
            "solution": "Increase limit",
            "status": "complete",
            "suggestions": ["scale up"],
            "error": None,
        }
        return runtime

    def test_returns_debug_result(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.get_cluster_context.return_value = {"name": "prod"}
        with patch("hexawyn.cli.command_router.get_runtime", return_value=self._mock_runtime()):
            result = _investigate(mock_adapter, "why is payments crashing?")
        assert result.kind == "debug"
        assert any("Memory limit too low" in line for line, _ in result.lines)

    def test_includes_pod_header_when_pod_given(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.get_cluster_context.return_value = {"name": "prod"}
        pod = {"name": "payments-api-xyz", "status": "CrashLoop", "restarts": 3}
        with patch("hexawyn.cli.command_router.get_runtime", return_value=self._mock_runtime()):
            result = _investigate(mock_adapter, "debug payments", pod=pod)
        assert any("payments-api-xyz" in line for line, _ in result.lines)

    def test_shows_error_line_when_error_returned(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.get_cluster_context.return_value = {"name": "prod"}
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "answer": "",
            "cause": "",
            "solution": "",
            "status": "error",
            "suggestions": [],
            "error": "Cluster unreachable",
        }
        with patch("hexawyn.cli.command_router.get_runtime", return_value=runtime):
            result = _investigate(mock_adapter, "test")
        assert any("Cluster unreachable" in line for line, _ in result.lines)

    def test_shows_degraded_warning(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.get_cluster_context.return_value = {"name": "prod"}
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "answer": "Partial result",
            "cause": "",
            "solution": "",
            "status": "degraded",
            "suggestions": [],
            "error": None,
        }
        with patch("hexawyn.cli.command_router.get_runtime", return_value=runtime):
            result = _investigate(mock_adapter, "test")
        assert any("UNVERIFIED" in line for line, _ in result.lines)

    def test_catches_exception_and_returns_error_result(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.get_cluster_context.return_value = {"name": "prod"}
        runtime = MagicMock()
        runtime.run_investigation.side_effect = Exception("timeout")
        with patch("hexawyn.cli.command_router.get_runtime", return_value=runtime):
            result = _investigate(mock_adapter, "test")
        assert result.kind == "debug"
        assert any("timeout" in line for line, _ in result.lines)

    def test_suggestions_become_chips(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.get_cluster_context.return_value = {"name": "prod"}
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "answer": "ok",
            "cause": "",
            "solution": "",
            "status": "complete",
            "suggestions": ["scale up", "check logs"],
            "error": None,
        }
        with patch("hexawyn.cli.command_router.get_runtime", return_value=runtime):
            result = _investigate(mock_adapter, "test")
        assert result.chips == ["scale up", "check logs"]


class TestShowLogs:
    def test_returns_unavailable_when_adapter_has_no_search_logs(self) -> None:
        mock_adapter = MagicMock(spec=[])
        result = _show_logs(mock_adapter, "show logs for payments")
        assert result.kind == "unknown"
        assert any("not available" in line.lower() for line, _ in result.lines)

    def test_returns_no_logs_found_when_empty(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = []
        mock_adapter.search_logs.return_value = []
        result = _show_logs(mock_adapter, "show logs for payments")
        assert result.kind == "logs"
        assert any("No logs found" in line for line, _ in result.lines)

    def test_returns_log_lines(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = []
        mock_adapter.search_logs.return_value = [
            {"severity": "ERROR", "timestamp": "2026-06-28T06:00:00Z", "message": "OOM killed"},
        ]
        result = _show_logs(mock_adapter, "show logs for payments")
        assert result.kind == "logs"
        assert any("OOM killed" in line for line, _ in result.lines)


class TestExplainPending:
    def test_returns_no_pending_when_all_running(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = [
            {"name": "api", "status": "Running", "restarts": 0},
        ]
        result = _explain_pending(mock_adapter)
        assert result.kind == "pending"
        assert any("No pending" in line for line, _ in result.lines)

    def test_lists_pending_pods(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = [
            {"name": "worker-abc12-xyz34", "status": "Pending", "restarts": 0},
        ]
        mock_adapter.get_findings.return_value = []
        result = _explain_pending(mock_adapter)
        assert result.kind == "pending"
        assert any("worker-abc12-xyz34" in line for line, _ in result.lines)

    def test_includes_finding_remediation(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = [
            {"name": "worker-abc12-xyz34", "status": "Pending", "restarts": 0},
        ]
        mock_adapter.get_findings.return_value = [
            {
                "severity": "warning",
                "message": "Pod worker is Pending",
                "remediation": "Check node capacity.",
            },
        ]
        result = _explain_pending(mock_adapter)
        assert any("Check node capacity" in line for line, _ in result.lines)


class TestRouteCommand:
    def test_empty_input_returns_unknown(self) -> None:
        result = route_command("", MagicMock())
        assert result.kind == "unknown"

    def test_whitespace_only_returns_unknown(self) -> None:
        result = route_command("   ", MagicMock())
        assert result.kind == "unknown"

    def test_routes_to_investigate(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.get_cluster_context.return_value = {"name": "prod"}
        mock_runtime = MagicMock()
        mock_runtime.run_investigation.return_value = {
            "answer": "ok",
            "cause": "",
            "solution": "",
            "status": "complete",
            "suggestions": [],
            "error": None,
        }
        with patch("hexawyn.cli.command_router.get_runtime", return_value=mock_runtime):
            result = route_command("how many pods?", mock_adapter)
        assert result.kind == "debug"
