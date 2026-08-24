"""Tests for CLI presentation — asides, findings, formatting, quota_renderer, constants."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError
from pathlib import Path
from unittest.mock import MagicMock, patch

from hexawyn.cli.presentation.asides import (
    crashloop_finding_count,
    failed_pod_count,
    finding_message,
    issue_reason,
    kubectl_current_context,
    mapping_int,
    mapping_text,
    namespace_count,
    pending_pod_count,
    restarting_finding_count,
    running_pod_count,
    safe_findings,
    safe_health_score,
    safe_metrics,
    safe_pods,
    safe_suggestions,
)
from hexawyn.cli.presentation.findings import (
    format_finding_warnings,
    is_error_narrative,
)
from hexawyn.cli.presentation.formatting import (
    app_version,
    compact_project_directory,
    connection_line,
    context_line,
    format_size,
    startup_lines,
)
from hexawyn.cli.presentation.quota_renderer import (
    BAR_WIDTH,
    FILL_CHAR,
    QUOTA_STATE_ICONS,
    compute_bar_fill,
)
from hexawyn.domain.models.quota import QuotaState


class TestAsides:
    """Cover asides.py — safe_* and helper functions."""

    def test_safe_findings_returns_list(self) -> None:
        adapter = MagicMock()
        adapter.get_findings.return_value = [{"message": "crash"}]
        assert safe_findings(adapter) == [{"message": "crash"}]

    def test_safe_findings_no_method(self) -> None:
        adapter = MagicMock(spec=[])
        assert safe_findings(adapter) == []

    def test_safe_findings_exception(self) -> None:
        adapter = MagicMock()
        adapter.get_findings.side_effect = Exception("boom")
        assert safe_findings(adapter) == []

    def test_safe_pods_returns_list(self) -> None:
        adapter = MagicMock()
        adapter.list_pods.return_value = [{"name": "pod1"}, {"name": "pod2"}]
        assert len(safe_pods(adapter)) == 2  # noqa: PLR2004

    def test_safe_pods_no_method(self) -> None:
        assert safe_pods(MagicMock(spec=[])) == []

    def test_safe_pods_filters_non_mapping(self) -> None:
        adapter = MagicMock()
        adapter.list_pods.return_value = [{"a": 1}, "not_a_mapping", {"b": 2}]
        assert len(safe_pods(adapter)) == 2  # noqa: PLR2004

    def test_safe_metrics(self) -> None:
        adapter = MagicMock()
        adapter.get_cluster_metrics.return_value = {"cpu": 50.0}
        assert safe_metrics(adapter) == {"cpu": 50.0}

    def test_safe_metrics_no_method(self) -> None:
        assert safe_metrics(MagicMock(spec=[])) == {}

    def test_safe_metrics_exception(self) -> None:
        adapter = MagicMock()
        adapter.get_cluster_metrics.side_effect = Exception("boom")
        assert safe_metrics(adapter) == {}

    def test_safe_health_score(self) -> None:
        adapter = MagicMock()
        adapter.get_health_score.return_value = 85
        assert safe_health_score(adapter) == 85  # noqa: PLR2004

    def test_safe_health_score_no_method_returns_100(self) -> None:
        assert safe_health_score(MagicMock(spec=[])) == 100  # noqa: PLR2004

    def test_safe_health_score_non_int_returns_100(self) -> None:
        adapter = MagicMock()
        adapter.get_health_score.return_value = "bad"
        assert safe_health_score(adapter) == 100  # noqa: PLR2004

    def test_safe_suggestions(self) -> None:
        adapter = MagicMock()
        adapter.get_suggestion_chips.return_value = ["sug1", "sug2", "sug3", "sug4"]
        result = safe_suggestions(adapter)
        assert len(result) == 3  # noqa: PLR2004

    def test_safe_suggestions_no_method(self) -> None:
        assert safe_suggestions(MagicMock(spec=[])) == []

    def test_safe_suggestions_exception(self) -> None:
        adapter = MagicMock()
        adapter.get_suggestion_chips.side_effect = Exception("boom")
        assert safe_suggestions(adapter) == []

    def test_mapping_text(self) -> None:
        assert mapping_text({"key": "val"}, "key", "d") == "val"
        assert mapping_text({}, "key", "d") == "d"
        assert mapping_text({"key": 42}, "key", "d") == "d"

    def test_mapping_int(self) -> None:
        assert mapping_int({"key": 5}, "key", 0) == 5  # noqa: PLR2004
        assert mapping_int({"key": 3.14}, "key", 0) == 3  # noqa: PLR2004
        assert mapping_int({}, "key", 10) == 10  # noqa: PLR2004
        assert mapping_int({"key": "str"}, "key", 0) == 0  # noqa: PLR2004

    def test_running_pod_count(self) -> None:
        pods = [{"status": "Running"}, {"status": "Pending"}, {"status": "Running"}]
        assert running_pod_count(pods) == 2  # noqa: PLR2004

    def test_pending_pod_count(self) -> None:
        pods = [{"status": "Pending"}, {"status": "Running"}]
        assert pending_pod_count(pods) == 1  # noqa: PLR2004

    def test_failed_pod_count(self) -> None:
        pods = [{"status": "CrashLoopBackOff"}, {"status": "Failed"}, {"status": "Running"}]
        assert failed_pod_count(pods) == 2  # noqa: PLR2004

    def test_namespace_count(self) -> None:
        pods = [{"namespace": "ns1"}, {"namespace": "ns2"}, {"namespace": "ns1"}]
        assert namespace_count(pods, "default") == 2  # noqa: PLR2004

    def test_namespace_count_empty(self) -> None:
        assert namespace_count([], "default") == 1  # noqa: PLR2004

    def test_crashloop_finding_count(self) -> None:
        findings = ["pod CrashLoopBackOff", "restarted 3 times"]
        assert crashloop_finding_count(findings) == 1  # noqa: PLR2004

    def test_restarting_finding_count(self) -> None:
        findings = ["pod restarted", "normal pod", "restarted again"]
        assert restarting_finding_count(findings) == 2  # noqa: PLR2004

    def test_finding_message_from_dict(self) -> None:
        assert finding_message({"message": "hello"}) == "hello"

    def test_finding_message_from_non_dict(self) -> None:
        assert finding_message("plain string") == "plain string"

    def test_finding_message_non_str_value(self) -> None:
        assert finding_message({"message": 123}) == ""

    def test_issue_name(self) -> None:
        class MockFinding:
            def __str__(self) -> str:
                return "Pod default/pod-name is crashing"

        finding = MagicMock()
        finding.get.side_effect = lambda k, d=None: {"pod_name": "pod-name"}.get(k, d)
        pass

    def test_issue_reason_crashloop(self) -> None:
        assert issue_reason("CrashLoopBackOff detected") == "CrashLoopBackOff"

    def test_kubectl_current_context_from_env(self, tmp_path: Path) -> None:
        kubeconfig = tmp_path / "config"
        kubeconfig.write_text("current-context: prod-eu\ncontexts: []\n")
        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig)}):
            assert kubectl_current_context() == "prod-eu"

    def test_kubectl_current_context_returns_question_on_error(self) -> None:
        with patch.dict("os.environ", {"KUBECONFIG": "/nonexistent/path"}):
            assert kubectl_current_context() == "?"


class TestFindings:
    """Cover findings.py."""

    def test_is_error_narrative_true(self) -> None:
        assert is_error_narrative("not available") is True
        assert is_error_narrative("The cluster is unavailable") is True
        assert is_error_narrative("Runtime not available at this time") is True

    def test_is_error_narrative_false(self) -> None:
        assert is_error_narrative("Everything is running fine") is False
        assert is_error_narrative("Cluster is healthy") is False

    def test_format_finding_warnings(self) -> None:
        with patch(
            "hexawyn.cli.presentation.findings.crashloop_finding_count",
            return_value=2,
        ):
            with patch(
                "hexawyn.cli.presentation.findings.restarting_finding_count",
                return_value=1,
            ):
                lines = format_finding_warnings([])
                assert any("CrashLoopBackOff" in l for l in lines)  # noqa: E741
                assert any("restart count" in l for l in lines)  # noqa: E741

    def test_format_finding_warnings_no_warnings(self) -> None:
        with patch(
            "hexawyn.cli.presentation.findings.crashloop_finding_count",
            return_value=0,
        ):
            with patch(
                "hexawyn.cli.presentation.findings.restarting_finding_count",
                return_value=0,
            ):
                lines = format_finding_warnings([])
                assert "No active warnings" in lines[0]


class TestFormatting:
    """Cover formatting.py."""

    def test_app_version(self) -> None:
        result = app_version()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_app_version_fallback(self) -> None:
        with patch("hexawyn.cli.presentation.formatting.version", side_effect=PackageNotFoundError):
            assert app_version() == "local"

    def test_compact_project_directory(self) -> None:
        result = compact_project_directory()
        assert isinstance(result, str)

    def test_compact_directory_outside_home(self) -> None:
        with patch.object(Path, "cwd", return_value=Path("/etc")):
            result = compact_project_directory()
            assert isinstance(result, str)

    def test_format_size(self) -> None:
        assert format_size(500) == "500 B"
        assert format_size(2048) == "2.0 KB"
        assert format_size(2_500_000) == "2.4 MB"
        assert format_size(2_000_000_000) == "1.86 GB"

    def test_connection_line_connected(self) -> None:
        from hexawyn.infrastructure.config.kubernetes_context import (
            ClusterContext,
            KubernetesStartupStatus,
        )

        ctx = ClusterContext(name="prod", cluster="c1", namespace="ns", user="u", is_current=True)
        status = KubernetesStartupStatus(
            contexts=[ctx],
            current_context=ctx,
            connected=True,
            kubeconfig_paths=[],
            connection_error=None,
        )
        assert "Connected" in connection_line(status)

    def test_connection_line_disconnected(self) -> None:
        from hexawyn.infrastructure.config.kubernetes_context import (
            ClusterContext,
            KubernetesStartupStatus,
        )

        ctx = ClusterContext(name="prod", cluster="c1", namespace="ns", user="u", is_current=True)
        status = KubernetesStartupStatus(
            contexts=[ctx],
            current_context=ctx,
            connected=False,
            kubeconfig_paths=[],
            connection_error="timeout",
        )
        assert "Disconnected" in connection_line(status)

    def test_connection_line_none(self) -> None:
        assert "Connected" in connection_line(None)

    def test_startup_lines(self) -> None:
        from hexawyn.infrastructure.config.kubernetes_context import (
            ClusterContext,
            KubernetesStartupStatus,
        )

        ctx = ClusterContext(
            name="prod", cluster="c1", namespace="default", user="u", is_current=True
        )
        status = KubernetesStartupStatus(
            contexts=[ctx],
            current_context=ctx,
            connected=True,
            kubeconfig_paths=[],
            connection_error=None,
        )
        lines = startup_lines(status)
        assert any("Kubernetes detected" in l for l in lines)  # noqa: E741
        assert any("prod" in l for l in lines)  # noqa: E741

    def test_startup_lines_disconnected(self) -> None:
        from hexawyn.infrastructure.config.kubernetes_context import (
            ClusterContext,
            KubernetesStartupStatus,
        )

        ctx = ClusterContext(
            name="prod", cluster="c1", namespace="default", user="u", is_current=True
        )
        status = KubernetesStartupStatus(
            contexts=[ctx],
            current_context=ctx,
            connected=False,
            kubeconfig_paths=[],
            connection_error="timeout",
        )
        lines = startup_lines(status)
        assert any("Unable to connect" in l for l in lines)  # noqa: E741

    def test_startup_lines_none(self) -> None:
        assert startup_lines(None) == []

    def test_startup_lines_no_current_context(self) -> None:
        from hexawyn.infrastructure.config.kubernetes_context import KubernetesStartupStatus

        status = KubernetesStartupStatus(
            contexts=[],
            current_context=None,
            connected=False,
            kubeconfig_paths=[],
            connection_error=None,
        )
        assert startup_lines(status) == []

    def test_context_line(self) -> None:
        adapter = MagicMock()
        adapter.get_cluster_context.return_value = {
            "name": "prod-eu",
            "namespace": "default",
        }
        adapter.get_findings.return_value = []
        result = context_line(adapter)
        assert "prod-eu" in result
        assert "0 warning" in result

    def test_context_line_with_warnings(self) -> None:
        adapter = MagicMock()
        adapter.get_cluster_context.return_value = {
            "name": "prod-eu",
            "namespace": "ns",
        }
        adapter.get_findings.return_value = [1, 2]
        result = context_line(adapter)
        assert "2 warnings" in result

    def test_context_list_lines(self) -> None:
        from hexawyn.cli.presentation.formatting import context_list_lines
        from hexawyn.infrastructure.config.kubernetes_context import ClusterContext

        ctx1 = ClusterContext(name="prod", cluster="c1", namespace="ns", user="u", is_current=True)
        ctx2 = ClusterContext(
            name="staging", cluster="c2", namespace="ns", user="u", is_current=False
        )
        lines = context_list_lines([ctx1, ctx2])
        assert any("prod" in l[0] for l in lines)  # noqa: E741

    def test_missing_context_lines(self) -> None:
        from hexawyn.cli.presentation.formatting import missing_context_lines
        from hexawyn.infrastructure.config.kubernetes_context import ClusterContext

        ctx = ClusterContext(name="prod", cluster="c1", namespace="ns", user="u", is_current=False)
        lines = missing_context_lines([ctx])
        assert any("not found" in l[0] for l in lines)  # noqa: E741

    def test_startup_status_from_switch(self) -> None:
        from hexawyn.cli.presentation.formatting import startup_status_from_switch
        from hexawyn.infrastructure.config.kubernetes_context import (
            ClusterContext,
            KubernetesContextSwitchResult,
        )

        ctx = ClusterContext(name="prod", cluster="c1", namespace="ns", user="u", is_current=True)
        switch = KubernetesContextSwitchResult(
            contexts=[ctx],
            current_context=ctx,
            connected=True,
            switched=True,
            kubeconfig_paths=[],
        )
        status = startup_status_from_switch(switch)
        assert status.current_context is ctx


class TestQuotaRenderer:
    """Cover quota_renderer.py."""

    def test_quota_state_icons_has_all_states(self) -> None:
        for state in QuotaState:
            assert state in QUOTA_STATE_ICONS

    def test_compute_bar_fill(self) -> None:
        filled, pct = compute_bar_fill(5, 10)
        assert filled == 10  # noqa: PLR2004
        assert pct == 50.0  # noqa: PLR2004

    def test_compute_bar_fill_zero_limit(self) -> None:
        filled, pct = compute_bar_fill(5, 0)
        assert pct == 0.0  # noqa: PLR2004
        assert filled == 0  # noqa: PLR2004

    def test_compute_bar_fill_exceeded(self) -> None:
        filled, pct = compute_bar_fill(30, 10)
        assert pct == 100.0  # noqa: PLR2004
        assert filled == BAR_WIDTH

    def test_constants(self) -> None:
        assert isinstance(FILL_CHAR, str)
        assert isinstance(BAR_WIDTH, int)
        assert BAR_WIDTH > 0
