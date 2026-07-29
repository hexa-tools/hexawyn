"""Tests for CLI presentation asides (utility functions)."""

from unittest.mock import MagicMock, patch

from hexawyn.cli.presentation.asides import (
    crashloop_finding_count,
    failed_pod_count,
    finding_message,
    issue_name,
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


class TestSafeFindings:
    def test_returns_list_when_adapter_has_get_findings(self) -> None:
        adapter = MagicMock()
        adapter.get_findings.return_value = [{"id": "f1"}, {"id": "f2"}]
        assert len(safe_findings(adapter)) == 2  # noqa: PLR2004

    def test_returns_empty_list_when_no_get_findings_attr(self) -> None:
        assert safe_findings("not an adapter") == []

    def test_returns_empty_list_on_exception(self) -> None:
        adapter = MagicMock()
        adapter.get_findings.side_effect = Exception("boom")
        assert safe_findings(adapter) == []


class TestSafePods:
    def test_returns_filtered_pods(self) -> None:
        adapter = MagicMock()
        adapter.list_pods.return_value = [
            {"name": "pod1", "status": "Running"},
            {"name": "pod2", "status": "CrashLoopBackOff"},
            None,
            "invalid",
        ]
        pods = safe_pods(adapter)
        assert len(pods) == 2  # noqa: PLR2004

    def test_returns_empty_when_no_list_pods(self) -> None:
        assert safe_pods("not an adapter") == []

    def test_returns_empty_on_exception(self) -> None:
        adapter = MagicMock()
        adapter.list_pods.side_effect = Exception("boom")
        assert safe_pods(adapter) == []


class TestSafeMetrics:
    def test_returns_metrics_mapping(self) -> None:
        adapter = MagicMock()
        adapter.get_cluster_metrics.return_value = {"cpu": 80}
        assert safe_metrics(adapter) == {"cpu": 80}

    def test_returns_empty_when_not_mapping(self) -> None:
        adapter = MagicMock()
        adapter.get_cluster_metrics.return_value = [1, 2, 3]
        assert safe_metrics(adapter) == {}

    def test_returns_empty_when_no_attr(self) -> None:
        assert safe_metrics("invalid") == {}

    def test_returns_empty_on_exception(self) -> None:
        adapter = MagicMock()
        adapter.get_cluster_metrics.side_effect = Exception("boom")
        assert safe_metrics(adapter) == {}


class TestSafeHealthScore:
    def test_returns_int_score(self) -> None:
        adapter = MagicMock()
        adapter.get_health_score.return_value = 95
        assert safe_health_score(adapter) == 95  # noqa: PLR2004

    def test_returns_100_when_no_attr(self) -> None:
        assert safe_health_score("invalid") == 100  # noqa: PLR2004

    def test_returns_100_on_exception(self) -> None:
        adapter = MagicMock()
        adapter.get_health_score.side_effect = Exception("boom")
        assert safe_health_score(adapter) == 100  # noqa: PLR2004

    def test_returns_100_when_not_int(self) -> None:
        adapter = MagicMock()
        adapter.get_health_score.return_value = "high"
        assert safe_health_score(adapter) == 100  # noqa: PLR2004


class TestSafeSuggestions:
    def test_returns_suggestions(self) -> None:
        adapter = MagicMock()
        adapter.get_suggestion_chips.return_value = ["fix1", "fix2", "fix3", "fix4"]
        result = safe_suggestions(adapter)
        assert result == ["fix1", "fix2", "fix3"]

    def test_returns_empty_when_no_attr(self) -> None:
        assert safe_suggestions("invalid") == []

    def test_returns_empty_on_exception(self) -> None:
        adapter = MagicMock()
        adapter.get_suggestion_chips.side_effect = Exception("boom")
        assert safe_suggestions(adapter) == []


class TestMappingHelpers:
    def test_mapping_text_returns_value(self) -> None:
        assert mapping_text({"key": "hello"}, "key", "default") == "hello"

    def test_mapping_text_returns_default_when_not_string(self) -> None:
        assert mapping_text({"key": 42}, "key", "default") == "default"

    def test_mapping_text_returns_default_when_missing(self) -> None:
        assert mapping_text({}, "key", "default") == "default"

    def test_mapping_int_returns_int(self) -> None:
        assert mapping_int({"count": 5}, "count", 0) == 5  # noqa: PLR2004

    def test_mapping_int_returns_from_float(self) -> None:
        assert mapping_int({"count": 5.0}, "count", 0) == 5  # noqa: PLR2004

    def test_mapping_int_returns_default_when_string(self) -> None:
        assert mapping_int({"count": "abc"}, "count", 0) == 0


class TestPodCounters:
    def test_running_pod_count(self) -> None:
        pods: list[dict[str, object]] = [
            {"status": "Running"},
            {"status": "Running"},
            {"status": "CrashLoopBackOff"},
        ]
        assert running_pod_count(pods) == 2  # noqa: PLR2004

    def test_pending_pod_count(self) -> None:
        pods: list[dict[str, object]] = [
            {"status": "Pending"},
            {"status": "Running"},
        ]
        assert pending_pod_count(pods) == 1

    def test_failed_pod_count(self) -> None:
        pods: list[dict[str, object]] = [
            {"status": "CrashLoopBackOff"},
            {"status": "Error"},
            {"status": "Running"},
        ]
        assert failed_pod_count(pods) == 2  # noqa: PLR2004

    def test_namespace_count(self) -> None:
        pods: list[dict[str, object]] = [
            {"namespace": "default"},
            {"namespace": "default"},
            {"namespace": "kube-system"},
        ]
        assert namespace_count(pods, "default") == 2  # noqa: PLR2004

    def test_namespace_count_empty(self) -> None:
        assert namespace_count([], "fallback") == 1


class TestFindingHelpers:
    def test_crashloop_finding_count(self) -> None:
        class FakeFinding:
            def __init__(self, text: str) -> None:
                self._text = text

            def __str__(self) -> str:
                return self._text

        findings = [
            FakeFinding("pod CrashLoopBackOff detected"),
            FakeFinding("pod CrashLoopBackOff again"),
            FakeFinding("all good"),
        ]
        assert crashloop_finding_count(findings) == 2  # noqa: PLR2004

    def test_restarting_finding_count(self) -> None:
        class FakeFinding:
            def __init__(self, text: str) -> None:
                self._text = text

            def __str__(self) -> str:
                return self._text

        findings = [
            FakeFinding("pod restarted 5 times"),
            FakeFinding("pod restarted 3 times"),
            FakeFinding("all good"),
        ]
        assert restarting_finding_count(findings) == 2  # noqa: PLR2004

    def test_issue_name_from_pod_message(self) -> None:
        class FakeFinding:
            def __init__(self, message: str) -> None:
                self._msg = message

            def __str__(self) -> str:
                return self._msg

        finding = FakeFinding("Pod default/my-pod is in CrashLoopBackOff")
        name = issue_name(finding)
        assert "my-pod" in name

    def test_issue_name_default(self) -> None:
        class FakeFinding:
            def __init__(self, message: str) -> None:
                self._msg = message

            def __str__(self) -> str:
                return self._msg

        finding = FakeFinding("Error occurred")
        assert issue_name(finding) == "Error"

    def test_issue_reason_crashloop(self) -> None:
        class FakeFinding:
            def __init__(self, message: str) -> None:
                self._msg = message

            def __str__(self) -> str:
                return self._msg

        finding = FakeFinding("Pod CrashLoopBackOff after restart")
        assert issue_reason(finding) == "CrashLoopBackOff"

    def test_finding_message_from_mapping(self) -> None:
        assert finding_message({"message": "error"}) == "error"
        assert finding_message({"message": None}) == ""
        assert finding_message({"other": "value"}) == ""

    def test_finding_message_from_object(self) -> None:
        class FakeObj:
            def __str__(self) -> str:
                return "crash detected"

        obj = FakeObj()
        assert finding_message(obj) == "crash detected"


class TestKubectlContext:
    def test_returns_current_context_from_kubeconfig(self) -> None:
        with patch("builtins.open", create=True) as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = ""
            with patch("yaml.safe_load", return_value={"current-context": "prod-cluster"}):
                assert kubectl_current_context() == "prod-cluster"

    def test_returns_question_mark_on_exception(self) -> None:
        with patch("builtins.open", side_effect=Exception("no file")):
            assert kubectl_current_context() == "?"

    def test_returns_question_mark_when_config_is_none(self) -> None:
        with patch("builtins.open", create=True):
            with patch("yaml.safe_load", return_value=None):
                assert kubectl_current_context() == "?"
