from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.adapters.secondary.vanilla.adapters.tekton_history_writer import (
    TektonHistoryWriter,
)


def _run(  # noqa: PLR0913
    name: str = "run-1",
    status: str = "Succeeded",
    duration: int | None = 120,
    start: str | None = "2026-01-01T00:00:00Z",
    completion: str | None = "2026-01-01T00:02:00Z",
    triggered_by: str | None = None,
) -> dict[str, object]:
    return {
        "name": name,
        "status": status,
        "start_time": start,
        "duration": None,
        "duration_seconds": duration,
        "triggered_by": triggered_by,
    }


def _task(  # noqa: PLR0913
    name: str = "task-1",
    task_ref: str = "build",
    status: str = "Succeeded",
    start: str | None = "2026-01-01T00:00:00Z",
    duration: str | None = None,
    failing_step: str | None = None,
    failing_step_error: str | None = None,
) -> dict[str, object]:
    return {
        "name": name,
        "task_ref": task_ref,
        "status": status,
        "start_time": start,
        "duration": duration,
        "failing_step": failing_step,
        "failing_step_error": failing_step_error,
    }


class TestTektonHistoryWriter:
    def test_writes_pipeline_runs_with_namespace_and_pipeline(self) -> None:
        tekton = MagicMock()
        tekton.list_pipeline_runs.return_value = [_run()]
        history = MagicMock()
        writer = TektonHistoryWriter(tekton_port=tekton, history_port=history)

        writer.list_pipeline_runs("payment-service", "ci")

        tekton.list_pipeline_runs.assert_called_once_with("payment-service", "ci")
        saved = history.save_pipeline_runs.call_args.args[0]
        assert saved[0]["name"] == "run-1"
        assert saved[0]["namespace"] == "ci"
        assert saved[0]["pipeline_name"] == "payment-service"
        assert saved[0]["status"] == "Succeeded"

    def test_writes_task_runs_for_pipeline(self) -> None:
        tekton = MagicMock()
        tekton.list_task_runs.return_value = [_task()]
        history = MagicMock()
        writer = TektonHistoryWriter(tekton_port=tekton, history_port=history)

        writer.list_task_runs("payment-service", "ci")

        tekton.list_task_runs.assert_called_once_with("payment-service", "ci")
        saved = history.save_task_runs.call_args.args[0]
        assert saved[0]["name"] == "task-1"
        assert saved[0]["namespace"] == "ci"
        assert saved[0]["task_name"] == "build"
        assert saved[0]["pipeline_run_name"] == "payment-service"

    def test_returns_tekton_result_unchanged(self) -> None:
        tekton = MagicMock()
        run = _run()
        tekton.list_pipeline_runs.return_value = [run]
        history = MagicMock()
        writer = TektonHistoryWriter(tekton_port=tekton, history_port=history)

        result = writer.list_pipeline_runs("payment-service", "ci")

        assert result == [run]

    def test_history_failure_does_not_break_listing(self) -> None:
        tekton = MagicMock()
        tekton.list_pipeline_runs.return_value = [_run()]
        history = MagicMock()
        history.save_pipeline_runs.side_effect = RuntimeError("duckdb down")
        writer = TektonHistoryWriter(tekton_port=tekton, history_port=history)

        result = writer.list_pipeline_runs("payment-service", "ci")

        assert len(result) == 1  # noqa: PLR2004

    def test_returns_empty_list_on_tekton_error(self) -> None:
        tekton = MagicMock()
        from hexawyn.domain.errors import ServiceNotFoundError

        tekton.list_pipeline_runs.side_effect = ServiceNotFoundError(service_name="missing")
        history = MagicMock()
        writer = TektonHistoryWriter(tekton_port=tekton, history_port=history)

        result = writer.list_pipeline_runs("missing", "ci")

        assert result == []

    def test_is_a_tekton_port(self) -> None:
        from hexawyn.application.ports.driven.tekton_port import TektonPort

        tekton = MagicMock(spec=TektonPort)
        history = MagicMock()
        writer = TektonHistoryWriter(tekton_port=tekton, history_port=history)

        assert isinstance(writer, TektonPort)

    def test_list_pipeline_runs_in_namespace_delegates(self) -> None:
        tekton = MagicMock()
        expected = [{"name": "run-x", "status": "Failed"}]
        tekton.list_pipeline_runs_in_namespace.return_value = expected
        history = MagicMock()
        writer = TektonHistoryWriter(tekton_port=tekton, history_port=history)

        result = writer.list_pipeline_runs_in_namespace("ci", 5)

        tekton.list_pipeline_runs_in_namespace.assert_called_once_with("ci", 5)
        assert result == expected

    def test_returns_empty_list_on_task_run_error(self) -> None:
        tekton = MagicMock()
        from hexawyn.domain.errors import ServiceNotFoundError

        tekton.list_task_runs.side_effect = ServiceNotFoundError(service_name="missing")
        history = MagicMock()
        writer = TektonHistoryWriter(tekton_port=tekton, history_port=history)

        result = writer.list_task_runs("missing", "ci")

        assert result == []

    def test_task_run_history_failure_does_not_break_listing(self) -> None:
        tekton = MagicMock()
        tekton.list_task_runs.return_value = [_task()]
        history = MagicMock()
        history.save_task_runs.side_effect = RuntimeError("duckdb down")
        writer = TektonHistoryWriter(tekton_port=tekton, history_port=history)

        result = writer.list_task_runs("payment-service", "ci")

        assert len(result) == 1  # noqa: PLR2004
