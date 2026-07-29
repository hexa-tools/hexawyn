from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import MagicMock

from hexawyn.domain.models.schedule import CheckResult, CronCheck
from hexawyn.domain.services.schedule.check_runner import CheckRunnerUseCase


def _make_check(  # noqa: PLR0913
    name: str = "daily-check",
    schedule: str = "0 9 * * *",
    use_case: str = "list_pods",
    params: dict[str, str] | None = None,
    enabled: bool = True,
    notify_policy: str = "on_change",
) -> CronCheck:
    return CronCheck(
        name=name,
        schedule=schedule,
        use_case=use_case,
        params=params or {},
        enabled=enabled,
        notify_policy=notify_policy,
    )


def _make_use_case_output() -> dict[str, object]:
    return {"pods": 12, "namespace": "default", "status": "ok"}


class TestCheckRunnerUseCase:
    def test_happy_path_executes_and_returns_success(self) -> None:
        store = MagicMock()
        store.last_result.return_value = None
        alert_port = MagicMock()
        alert_port.send_alert.return_value = False
        registry = {"list_pods": lambda params: _make_use_case_output()}

        runner = CheckRunnerUseCase(store=store, alert_port=alert_port, use_case_registry=registry)
        result = runner.execute(_make_check())

        assert result.check_name == "daily-check"
        assert result.phase == "alerting"
        assert result.changed is True
        assert result.payload_digest != ""
        assert result.error_message is None
        assert result.duration_ms is not None
        store.save_result.assert_called_once()

    def test_use_case_not_in_registry_returns_failed(self) -> None:
        store = MagicMock()
        alert_port = MagicMock()
        registry: dict[str, object] = {}

        runner = CheckRunnerUseCase(store=store, alert_port=alert_port, use_case_registry=registry)
        result = runner.execute(_make_check(use_case="unknown_use_case"))

        assert result.phase == "failed"
        assert "not found" in result.error_message

    def test_use_case_raises_exception_returns_failed(self) -> None:
        store = MagicMock()
        alert_port = MagicMock()

        def boom(params: dict[str, str]) -> dict[str, object]:
            raise RuntimeError("boom")

        registry = {"list_pods": boom}

        runner = CheckRunnerUseCase(store=store, alert_port=alert_port, use_case_registry=registry)
        result = runner.execute(_make_check())

        assert result.phase == "failed"
        assert result.error_message == "boom"

    def test_alert_sent_when_policy_always(self) -> None:
        store = MagicMock()
        store.last_result.return_value = None
        alert_port = MagicMock()
        alert_port.send_alert.return_value = True
        registry = {"list_pods": lambda params: _make_use_case_output()}

        runner = CheckRunnerUseCase(store=store, alert_port=alert_port, use_case_registry=registry)
        result = runner.execute(_make_check(notify_policy="always"))

        assert result.notified is True
        assert result.phase == "alerting"

    def test_alert_sent_on_change_when_changed(self) -> None:
        store = MagicMock()
        previous = CheckResult(
            check_name="daily-check",
            phase="success",
            started_at=datetime.now(UTC),
            payload_digest="old-digest",
        )
        store.last_result.return_value = previous
        alert_port = MagicMock()
        alert_port.send_alert.return_value = True
        registry = {"list_pods": lambda params: _make_use_case_output()}

        runner = CheckRunnerUseCase(store=store, alert_port=alert_port, use_case_registry=registry)
        result = runner.execute(_make_check(notify_policy="on_change"))

        assert result.notified is True
        assert result.changed is True
        assert result.phase == "alerting"

    def test_no_alert_on_change_when_unchanged(self) -> None:
        store = MagicMock()
        alert_port = MagicMock()
        registry = {"list_pods": lambda params: _make_use_case_output()}

        runner = CheckRunnerUseCase(store=store, alert_port=alert_port, use_case_registry=registry)

        runner.execute(_make_check(notify_policy="on_change"))

        previous = store.save_result.call_args[0][0]
        store.last_result.return_value = previous

        result2 = runner.execute(_make_check(notify_policy="on_change"))

        assert result2.changed is False
        assert result2.phase == "success"

    def test_no_previous_result_triggers_change(self) -> None:
        store = MagicMock()
        store.last_result.return_value = None
        alert_port = MagicMock()
        registry = {"list_pods": lambda params: _make_use_case_output()}

        runner = CheckRunnerUseCase(store=store, alert_port=alert_port, use_case_registry=registry)
        result = runner.execute(_make_check())

        assert result.changed is True

    def test_check_params_passed_to_use_case(self) -> None:
        store = MagicMock()
        store.last_result.return_value = None
        alert_port = MagicMock()
        alert_port.send_alert.return_value = False
        captured_params: dict[str, str] = {}

        def capture(params: dict[str, str]) -> dict[str, object]:
            captured_params.update(params)
            return {"result": "captured"}

        registry = {"list_pods": capture}

        runner = CheckRunnerUseCase(store=store, alert_port=alert_port, use_case_registry=registry)
        runner.execute(_make_check(params={"namespace": "ns1", "limit": "10"}))

        assert captured_params == {"namespace": "ns1", "limit": "10"}

    def test_empty_use_case_output_summary(self) -> None:
        store = MagicMock()
        store.last_result.return_value = None
        alert_port = MagicMock()
        registry = {"list_pods": lambda params: {}}

        runner = CheckRunnerUseCase(store=store, alert_port=alert_port, use_case_registry=registry)
        result = runner.execute(_make_check())

        assert result.summary == "empty response"
