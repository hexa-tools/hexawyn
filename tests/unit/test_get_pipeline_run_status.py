"""Unit tests for get_pipeline_run_status use case — TDD Red phase."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.tekton_pipeline_status_port import (
    PipelineRunRecord,
    TektonPipelineStatusPort,
)
from hexawyn.application.ports.driving.get_pipeline_run_status.get_pipeline_run_status_command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.ports.driving.get_pipeline_run_status.get_pipeline_run_status_response import (
    GetPipelineRunStatusResponse,
)
from hexawyn.application.ports.driving.get_pipeline_run_status.get_pipeline_run_status_service_port import (
    GetPipelineRunStatusServicePort,
)
from hexawyn.application.service.pipeline_run_status_service import (
    PipelineRunStatusService,
    _filter_by_window,
    _find_most_recent_failed,
    _find_slowest_run,
)
from hexawyn.application.use_case.get_pipeline_run_status.get_pipeline_run_status_use_case import (
    GetPipelineRunStatusUseCase,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    TektonNotInstalledError,
)
from hexawyn.domain.models.pipeline import PipelineRunStatusReport, PipelineRunSummary

# ── Stub port ─────────────────────────────────────────────────────────────


class _StubTektonStatusPort(TektonPipelineStatusPort):
    def __init__(
        self,
        runs: list[PipelineRunRecord],
        raise_exc: Exception | None = None,
    ) -> None:
        self._runs = runs
        self._raise_exc = raise_exc

    def list_pipeline_runs(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        if self._raise_exc is not None:
            raise self._raise_exc
        return self._runs


# ── Helpers ────────────────────────────────────────────────────────────────


def _ts(minutes_ago: int) -> str:
    """ISO timestamp N minutes ago."""
    dt = datetime.now(UTC) - timedelta(minutes=minutes_ago)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _ts_hours(hours_ago: float) -> str:
    dt = datetime.now(UTC) - timedelta(hours=hours_ago)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _run(
    name: str,
    status: str,
    start_time: str | None = None,
    duration_seconds: int | None = None,
    failure_reason: str | None = None,
    pipeline_ref: str = "my-pipeline",
) -> PipelineRunRecord:
    return PipelineRunRecord(
        name=name,
        status=status,
        start_time=start_time or _ts(30),
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=pipeline_ref,
    )


# ── Command ───────────────────────────────────────────────────────────────


class TestGetPipelineRunStatusCommand:
    def test_defaults(self) -> None:
        cmd = GetPipelineRunStatusCommand(namespace="ci")
        assert cmd.namespace == "ci"
        assert cmd.hours_window == 24
        assert cmd.limit == 500

    def test_custom_values(self) -> None:
        cmd = GetPipelineRunStatusCommand(namespace="prod", hours_window=48, limit=100)
        assert cmd.hours_window == 48
        assert cmd.limit == 100

    def test_is_frozen(self) -> None:
        cmd = GetPipelineRunStatusCommand(namespace="ci")
        with pytest.raises(Exception):
            cmd.namespace = "other"  # type: ignore[misc]


# ── Response ──────────────────────────────────────────────────────────────


class TestGetPipelineRunStatusResponse:
    def test_wraps_report(self) -> None:
        report = PipelineRunStatusReport(namespace="ci", window_hours=24, total=0)
        resp = GetPipelineRunStatusResponse(report=report)
        assert resp.report.namespace == "ci"


# ── Service port ABC ──────────────────────────────────────────────────────


class TestGetPipelineRunStatusServicePortABC:
    def test_cannot_instantiate_abstract(self) -> None:
        with pytest.raises(TypeError):
            GetPipelineRunStatusServicePort()  # type: ignore[abstract]


# ── Domain models ─────────────────────────────────────────────────────────


class TestPipelineRunStatusReport:
    def test_defaults(self) -> None:
        r = PipelineRunStatusReport(namespace="ci", window_hours=24, total=5)
        assert r.running == 0
        assert r.succeeded == 0
        assert r.failed == 0
        assert r.cancelled == 0
        assert r.not_started == 0
        assert r.most_recent_failed is None
        assert r.slowest_run is None
        assert r.total == 5

    def test_with_most_recent_failed(self) -> None:
        summary = PipelineRunSummary(
            name="build-v1",
            status="Failed",
            start_time="2026-06-16T08:00:00Z",
            duration_seconds=None,
            failure_reason="TaskRunTimeout",
            pipeline_ref="build",
        )
        r = PipelineRunStatusReport(
            namespace="ci", window_hours=24, total=1, failed=1, most_recent_failed=summary
        )
        assert r.most_recent_failed is not None
        assert r.most_recent_failed.failure_reason == "TaskRunTimeout"


# ── _filter_by_window ─────────────────────────────────────────────────────


class TestFilterByWindow:
    def test_keeps_recent_runs(self) -> None:
        runs = [_run("r1", "Succeeded", _ts(30))]
        result = _filter_by_window(runs, hours=24)
        assert len(result) == 1

    def test_excludes_old_runs(self) -> None:
        runs = [_run("r1", "Succeeded", _ts_hours(25))]
        result = _filter_by_window(runs, hours=24)
        assert result == []

    def test_includes_pending_run_with_no_start_time(self) -> None:
        run = _run("r1", "NotStarted", None)
        run["start_time"] = None  # type: ignore[typeddict-item]
        result = _filter_by_window([run], hours=24)
        assert len(result) == 1

    def test_mixed_old_and_recent(self) -> None:
        recent = _run("r1", "Running", _ts(60))
        old = _run("r2", "Succeeded", _ts_hours(26))
        result = _filter_by_window([recent, old], hours=24)
        assert len(result) == 1
        assert result[0]["name"] == "r1"

    def test_invalid_timestamp_excluded(self) -> None:
        run = _run("r1", "Failed")
        run["start_time"] = "not-a-date"
        result = _filter_by_window([run], hours=24)
        assert result == []


# ── _find_most_recent_failed ──────────────────────────────────────────────


class TestFindMostRecentFailed:
    def test_returns_none_when_no_failed(self) -> None:
        runs = [_run("r1", "Succeeded")]
        assert _find_most_recent_failed(runs) is None

    def test_returns_most_recent_by_start_time(self) -> None:
        older = _run("old-fail", "Failed", _ts(120), failure_reason="OldError")
        newer = _run("new-fail", "Failed", _ts(30), failure_reason="NewError")
        result = _find_most_recent_failed([older, newer])
        assert result is not None
        assert result.name == "new-fail"
        assert result.failure_reason == "NewError"

    def test_single_failed_run(self) -> None:
        run = _run("fail-1", "Failed", _ts(45), failure_reason="TaskRunTimeout")
        result = _find_most_recent_failed([run])
        assert result is not None
        assert result.failure_reason == "TaskRunTimeout"

    def test_failure_reason_can_be_none(self) -> None:
        run = _run("fail-1", "Failed", _ts(45), failure_reason=None)
        result = _find_most_recent_failed([run])
        assert result is not None
        assert result.failure_reason is None


# ── _find_slowest_run ─────────────────────────────────────────────────────


class TestFindSlowestRun:
    def test_returns_none_when_no_completed(self) -> None:
        runs = [_run("r1", "Running", duration_seconds=None)]
        assert _find_slowest_run(runs) is None

    def test_finds_slowest_succeeded(self) -> None:
        fast = _run("fast", "Succeeded", duration_seconds=60)
        slow = _run("slow", "Succeeded", duration_seconds=300)
        result = _find_slowest_run([fast, slow])
        assert result is not None
        assert result.name == "slow"

    def test_considers_failed_runs_too(self) -> None:
        failed_slow = _run("fail", "Failed", duration_seconds=500)
        succeeded_fast = _run("ok", "Succeeded", duration_seconds=100)
        result = _find_slowest_run([failed_slow, succeeded_fast])
        assert result is not None
        assert result.name == "fail"

    def test_ignores_runs_without_duration(self) -> None:
        no_duration = _run("running", "Running", duration_seconds=None)
        with_duration = _run("done", "Succeeded", duration_seconds=120)
        result = _find_slowest_run([no_duration, with_duration])
        assert result is not None
        assert result.name == "done"


# ── PipelineRunStatusService ──────────────────────────────────────────────


class TestPipelineRunStatusService:
    def test_happy_path_mixed_statuses(self) -> None:
        """2 Succeeded, 1 Running, 2 Failed → correct counts."""
        port = _StubTektonStatusPort(
            runs=[
                _run("s1", "Succeeded", _ts(10), duration_seconds=272),
                _run("s2", "Succeeded", _ts(60), duration_seconds=180),
                _run("r1", "Running", _ts(20)),
                _run("f1", "Failed", _ts(30), failure_reason="TaskRunTimeout"),
                _run("f2", "Failed", _ts(40), failure_reason="ImagePullFailed"),
            ]
        )
        svc = PipelineRunStatusService(port=port)
        resp = svc.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="ci"))

        assert resp.report.total == 5
        assert resp.report.running == 1
        assert resp.report.succeeded == 2
        assert resp.report.failed == 2
        assert resp.report.cancelled == 0

    def test_no_pipeline_runs_returns_empty_summary(self) -> None:
        port = _StubTektonStatusPort(runs=[])
        svc = PipelineRunStatusService(port=port)
        resp = svc.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="ci"))

        assert resp.report.total == 0
        assert resp.report.most_recent_failed is None
        assert resp.report.slowest_run is None

    def test_all_runs_older_than_window_returns_empty(self) -> None:
        """Runs started 30h ago are excluded from a 24h window."""
        port = _StubTektonStatusPort(
            runs=[
                _run("old", "Succeeded", _ts_hours(30), duration_seconds=60),
            ]
        )
        svc = PipelineRunStatusService(port=port)
        resp = svc.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="ci"))

        assert resp.report.total == 0

    def test_failed_run_failure_reason_surfaced(self) -> None:
        port = _StubTektonStatusPort(
            runs=[_run("f1", "Failed", _ts(10), failure_reason="TaskRunTimeout")]
        )
        svc = PipelineRunStatusService(port=port)
        resp = svc.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="ci"))

        assert resp.report.most_recent_failed is not None
        assert resp.report.most_recent_failed.failure_reason == "TaskRunTimeout"

    def test_running_run_with_elapsed_duration_shown(self) -> None:
        """Running run with duration_seconds set (elapsed) appears in report."""
        port = _StubTektonStatusPort(runs=[_run("r1", "Running", _ts(15), duration_seconds=900)])
        svc = PipelineRunStatusService(port=port)
        resp = svc.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="ci"))

        assert resp.report.running == 1

    def test_pending_run_counted_as_not_started(self) -> None:
        """PipelineRun stuck in NotStarted (no conditions) is counted separately."""
        run = _run("pending", "NotStarted")
        run["start_time"] = None  # type: ignore[typeddict-item]
        port = _StubTektonStatusPort(runs=[run])
        svc = PipelineRunStatusService(port=port)
        resp = svc.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="ci"))

        assert resp.report.not_started == 1

    def test_slowest_run_identified(self) -> None:
        port = _StubTektonStatusPort(
            runs=[
                _run("fast", "Succeeded", _ts(120), duration_seconds=60),
                _run("slow", "Succeeded", _ts(60), duration_seconds=4 * 60),
            ]
        )
        svc = PipelineRunStatusService(port=port)
        resp = svc.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="ci"))

        assert resp.report.slowest_run is not None
        assert resp.report.slowest_run.name == "slow"

    def test_cancelled_runs_counted(self) -> None:
        port = _StubTektonStatusPort(runs=[_run("c1", "Cancelled", _ts(10))])
        svc = PipelineRunStatusService(port=port)
        resp = svc.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="ci"))

        assert resp.report.cancelled == 1
        assert resp.report.total == 1

    def test_custom_hours_window_applied(self) -> None:
        """With 2h window, runs older than 2h are excluded."""
        recent = _run("recent", "Succeeded", _ts_hours(1), duration_seconds=60)
        old = _run("old", "Succeeded", _ts_hours(3), duration_seconds=120)
        port = _StubTektonStatusPort(runs=[recent, old])
        svc = PipelineRunStatusService(port=port)
        resp = svc.get_pipeline_run_status(
            GetPipelineRunStatusCommand(namespace="ci", hours_window=2)
        )

        assert resp.report.total == 1
        assert resp.report.succeeded == 1

    def test_rbac_error_propagates(self) -> None:
        port = _StubTektonStatusPort(
            runs=[], raise_exc=InsufficientPermissionsError("RBAC denied", context={})
        )
        svc = PipelineRunStatusService(port=port)
        with pytest.raises(InsufficientPermissionsError):
            svc.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="restricted"))

    def test_tekton_not_installed_propagates(self) -> None:
        port = _StubTektonStatusPort(runs=[], raise_exc=TektonNotInstalledError())
        svc = PipelineRunStatusService(port=port)
        with pytest.raises(TektonNotInstalledError):
            svc.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="ci"))

    def test_namespace_in_report(self) -> None:
        port = _StubTektonStatusPort(runs=[])
        svc = PipelineRunStatusService(port=port)
        resp = svc.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="ci"))
        assert resp.report.namespace == "ci"

    def test_window_hours_in_report(self) -> None:
        port = _StubTektonStatusPort(runs=[])
        svc = PipelineRunStatusService(port=port)
        resp = svc.get_pipeline_run_status(
            GetPipelineRunStatusCommand(namespace="ci", hours_window=48)
        )
        assert resp.report.window_hours == 48


# ── Use case ──────────────────────────────────────────────────────────────


class TestGetPipelineRunStatusUseCase:
    def test_delegates_to_service(self) -> None:
        port = _StubTektonStatusPort(runs=[])
        from hexawyn.application.service.pipeline_run_status_service import (
            PipelineRunStatusService,
        )

        svc = PipelineRunStatusService(port=port)
        uc = GetPipelineRunStatusUseCase(service=svc)
        resp = uc.execute(GetPipelineRunStatusCommand(namespace="ci"))
        assert isinstance(resp, GetPipelineRunStatusResponse)

    def test_use_case_with_runs(self) -> None:
        port = _StubTektonStatusPort(runs=[_run("s1", "Succeeded", _ts(10), duration_seconds=100)])
        from hexawyn.application.service.pipeline_run_status_service import (
            PipelineRunStatusService,
        )

        svc = PipelineRunStatusService(port=port)
        uc = GetPipelineRunStatusUseCase(service=svc)
        resp = uc.execute(GetPipelineRunStatusCommand(namespace="ci"))
        assert resp.report.succeeded == 1


# ── KubernetesTektonAdapter ───────────────────────────────────────────────


class _K8sApiException(Exception):  # noqa: N818
    def __init__(self, status: int) -> None:
        super().__init__(str(status))
        self.status = status


class TestKubernetesTektonAdapter:
    def _make_item(
        self,
        name: str,
        status_str: str,
        reason: str = "",
        start: str | None = None,
        completion: str | None = None,
    ) -> dict[str, object]:
        """Build a minimal Tekton PipelineRun CRD object."""
        now = datetime.now(UTC)
        start_ts = start or (now - timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
        conditions: list[dict[str, str]] = []
        if status_str == "Succeeded":
            conditions = [{"type": "Succeeded", "status": "True", "reason": "Succeeded"}]
        elif status_str == "Failed":
            conditions = [{"type": "Succeeded", "status": "False", "reason": reason or "Failed"}]
        elif status_str == "Cancelled":
            conditions = [
                {"type": "Succeeded", "status": "False", "reason": "PipelineRunCancelled"}
            ]
        elif status_str == "Running":
            conditions = [{"type": "Succeeded", "status": "Unknown", "reason": "Running"}]
        # NotStarted → empty conditions
        item: dict[str, object] = {
            "metadata": {"name": name},
            "spec": {"pipelineRef": {"name": "my-pipeline"}},
            "status": {
                "conditions": conditions,
                "startTime": start_ts,
            },
        }
        if completion:
            assert isinstance(item["status"], dict)
            item["status"]["completionTime"] = completion  # type: ignore[index]
        return item

    def test_list_pipeline_runs_happy_path(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
            KubernetesTektonAdapter,
        )

        item = self._make_item("build-v1", "Succeeded", completion=_ts(5))
        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.return_value = {"items": [item]}

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = KubernetesTektonAdapter()
            result = adapter.list_pipeline_runs("ci")

        assert len(result) == 1
        assert result[0]["name"] == "build-v1"
        assert result[0]["status"] == "Succeeded"
        assert result[0]["pipeline_ref"] == "my-pipeline"

    def test_list_pipeline_runs_403_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
            KubernetesTektonAdapter,
        )

        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.side_effect = _K8sApiException(403)

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = KubernetesTektonAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_pipeline_runs("restricted")

    def test_list_pipeline_runs_404_raises_tekton_not_installed(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
            KubernetesTektonAdapter,
        )

        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.side_effect = _K8sApiException(404)

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = KubernetesTektonAdapter()
            with pytest.raises(TektonNotInstalledError):
                adapter.list_pipeline_runs("ci")

    def test_list_pipeline_runs_other_api_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
            KubernetesTektonAdapter,
        )

        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.side_effect = _K8sApiException(500)

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = KubernetesTektonAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.list_pipeline_runs("ci")

    def test_list_pipeline_runs_connection_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
            KubernetesTektonAdapter,
        )

        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.side_effect = RuntimeError("connection refused")

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = KubernetesTektonAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.list_pipeline_runs("ci")

    def test_failure_reason_extracted_for_failed_run(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
            KubernetesTektonAdapter,
        )

        item = self._make_item("fail-1", "Failed", reason="TaskRunTimeout")
        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.return_value = {"items": [item]}

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = KubernetesTektonAdapter()
            result = adapter.list_pipeline_runs("ci")

        assert result[0]["failure_reason"] == "TaskRunTimeout"

    def test_succeeded_run_has_no_failure_reason(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
            KubernetesTektonAdapter,
        )

        item = self._make_item("ok-1", "Succeeded", completion=_ts(5))
        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.return_value = {"items": [item]}

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = KubernetesTektonAdapter()
            result = adapter.list_pipeline_runs("ci")

        assert result[0]["failure_reason"] is None

    def test_running_run_has_elapsed_duration(self) -> None:
        """Running run has duration_seconds computed as elapsed time."""
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
            KubernetesTektonAdapter,
        )

        item = self._make_item("running-1", "Running", start=_ts(10))
        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.return_value = {"items": [item]}

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = KubernetesTektonAdapter()
            result = adapter.list_pipeline_runs("ci")

        assert result[0]["duration_seconds"] is not None
        assert result[0]["duration_seconds"] >= 0

    def test_cancelled_run_status(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
            KubernetesTektonAdapter,
        )

        item = self._make_item("cancel-1", "Cancelled")
        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.return_value = {"items": [item]}

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = KubernetesTektonAdapter()
            result = adapter.list_pipeline_runs("ci")

        assert result[0]["status"] == "Cancelled"
        assert result[0]["failure_reason"] is None

    def test_not_started_run_status(self) -> None:
        """PipelineRun with no conditions → NotStarted."""
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
            KubernetesTektonAdapter,
        )

        item = self._make_item("pending-1", "NotStarted")
        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.return_value = {"items": [item]}

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = KubernetesTektonAdapter()
            result = adapter.list_pipeline_runs("ci")

        assert result[0]["status"] == "NotStarted"

    def test_empty_namespace_returns_empty_list(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
            KubernetesTektonAdapter,
        )

        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.return_value = {"items": []}

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = KubernetesTektonAdapter()
            result = adapter.list_pipeline_runs("empty-ns")

        assert result == []

    def test_inline_pipeline_ref(self) -> None:
        """PipelineRun with pipelineSpec (inline) has pipeline_ref='inline'."""
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
            KubernetesTektonAdapter,
        )

        item: dict[str, object] = {
            "metadata": {"name": "inline-run"},
            "spec": {"pipelineSpec": {"tasks": []}},
            "status": {
                "conditions": [{"type": "Succeeded", "status": "True", "reason": "Succeeded"}],
                "startTime": _ts(30),
                "completionTime": _ts(5),
            },
        }
        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.return_value = {"items": [item]}

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = KubernetesTektonAdapter()
            result = adapter.list_pipeline_runs("ci")

        assert result[0]["pipeline_ref"] == "inline"

    def test_extract_status_none_returns_not_started(self) -> None:
        """_extract_status(None) → NotStarted (line 58)."""
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import _extract_status

        status, reason = _extract_status(None)
        assert status == "NotStarted"
        assert reason is None

    def test_extract_status_non_mapping_condition_returns_not_started(self) -> None:
        """First condition that is not a Mapping → NotStarted (line 64)."""
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import _extract_status

        status, reason = _extract_status({"conditions": ["not-a-mapping"]})
        assert status == "NotStarted"
        assert reason is None

    def test_extract_status_unknown_without_running_reason_returns_not_started(self) -> None:
        """Unknown status + non-Running reason → NotStarted (line 76)."""
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import _extract_status

        status, reason = _extract_status(
            {"conditions": [{"status": "Unknown", "reason": "PipelineRunPending"}]}
        )
        assert status == "NotStarted"
        assert reason is None

    def test_compute_duration_seconds_none_start_returns_none(self) -> None:
        """_compute_duration_seconds(None, ...) → None (line 83)."""
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import _compute_duration_seconds

        assert _compute_duration_seconds(None, None) is None

    def test_compute_duration_seconds_invalid_timestamp_returns_none(self) -> None:
        """Invalid ISO timestamp → None via ValueError (lines 92-93)."""
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import _compute_duration_seconds

        assert _compute_duration_seconds("not-a-date", "also-not-a-date") is None

    def test_extract_pipeline_ref_none_spec_returns_unknown(self) -> None:
        """_extract_pipeline_ref(None) → 'unknown' (line 98)."""
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import _extract_pipeline_ref

        assert _extract_pipeline_ref(None) == "unknown"

    def test_extract_pipeline_ref_no_ref_no_spec_returns_unknown(self) -> None:
        """Spec with neither pipelineRef nor pipelineSpec → 'unknown' (line 106)."""
        from hexawyn.adapters.secondary.kubernetes_tekton_adapter import _extract_pipeline_ref

        assert _extract_pipeline_ref({"otherKey": "val"}) == "unknown"


# ── MCP tool ──────────────────────────────────────────────────────────────


class TestGetPipelineRunStatusMCPTool:
    def test_tool_returns_expected_keys(self) -> None:
        from hexawyn.mcp.tools.get_pipeline_run_status import get_pipeline_run_status

        fake_report = PipelineRunStatusReport(namespace="ci", window_hours=24, total=0)
        fake_resp = GetPipelineRunStatusResponse(report=fake_report)

        with patch(
            "hexawyn.mcp.tools.get_pipeline_run_status.GetPipelineRunStatusUseCase"
        ) as mock_uc:
            mock_uc.return_value.execute.return_value = fake_resp
            with patch(
                "hexawyn.mcp.tools.get_pipeline_run_status._build_adapter",
                return_value=MagicMock(spec=TektonPipelineStatusPort),
            ):
                result = get_pipeline_run_status(namespace="ci")

        assert "namespace" in result
        assert "total" in result
        assert "running" in result
        assert "succeeded" in result
        assert "failed" in result
        assert "cancelled" in result
        assert "most_recent_failed" in result
        assert "slowest_run" in result
        assert "window_hours" in result
        assert result["error"] is None

    def test_tool_error_returns_error_key(self) -> None:
        from hexawyn.mcp.tools.get_pipeline_run_status import get_pipeline_run_status

        with patch(
            "hexawyn.mcp.tools.get_pipeline_run_status._build_adapter",
            side_effect=RuntimeError("no kubeconfig"),
        ):
            result = get_pipeline_run_status(namespace="ci")

        assert result["error"] == "no kubeconfig"
        assert result["total"] == 0

    def test_build_adapter_returns_kubernetes_tekton_adapter(self) -> None:
        """Covers _build_adapter body (lines 23-25) via import patching."""
        from hexawyn.mcp.tools.get_pipeline_run_status import _build_adapter

        mock_adapter = MagicMock(spec=TektonPipelineStatusPort)
        with patch(
            "hexawyn.adapters.secondary.kubernetes_tekton_adapter.KubernetesTektonAdapter",
            return_value=mock_adapter,
        ):
            result = _build_adapter()

        assert result is not None

    def test_register_adds_tool_to_mcp(self) -> None:
        """Covers register() body (line 104)."""
        from hexawyn.mcp.tools.get_pipeline_run_status import register

        mock_mcp = MagicMock()
        register(mock_mcp)
        mock_mcp.tool.assert_called_once()

    def test_tool_serializes_summary_entries(self) -> None:
        from hexawyn.mcp.tools.get_pipeline_run_status import get_pipeline_run_status

        summary = PipelineRunSummary(
            name="fail-1",
            status="Failed",
            start_time="2026-06-16T09:00:00Z",
            duration_seconds=None,
            failure_reason="TaskRunImagePullFailed",
            pipeline_ref="build",
        )
        fake_report = PipelineRunStatusReport(
            namespace="ci",
            window_hours=24,
            total=1,
            failed=1,
            most_recent_failed=summary,
        )
        fake_resp = GetPipelineRunStatusResponse(report=fake_report)

        with patch(
            "hexawyn.mcp.tools.get_pipeline_run_status.GetPipelineRunStatusUseCase"
        ) as mock_uc:
            mock_uc.return_value.execute.return_value = fake_resp
            with patch(
                "hexawyn.mcp.tools.get_pipeline_run_status._build_adapter",
                return_value=MagicMock(spec=TektonPipelineStatusPort),
            ):
                result = get_pipeline_run_status(namespace="ci")

        assert result["failed"] == 1
        mrf = result["most_recent_failed"]
        assert isinstance(mrf, dict)
        assert mrf["name"] == "fail-1"
        assert mrf["failure_reason"] == "TaskRunImagePullFailed"
