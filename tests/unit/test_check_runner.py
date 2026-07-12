from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import MagicMock

from hexawyn.application.ports.driven.alert_notification_port import AlertNotificationPort
from hexawyn.application.ports.driven.schedule_store_port import ScheduleStorePort
from hexawyn.domain.models.schedule import CheckResult, CronCheck

_NOW = datetime(2026, 7, 12, 10, 0, 0, tzinfo=UTC)


def _alert() -> MagicMock:
    alert = MagicMock(spec=AlertNotificationPort)
    alert.send_alert.return_value = True
    return alert


class TestCheckRunnerUseCase:
    def test_execute_success_first_run(self) -> None:
        store = MagicMock(spec=ScheduleStorePort)
        alert = _alert()
        check = CronCheck(name="test", schedule="*/15 * * * *", use_case="test_list")

        from hexawyn.domain.services.schedule.check_runner import CheckRunnerUseCase

        runner = CheckRunnerUseCase(
            store=store,
            alert_port=alert,
            use_case_registry={"test_list": lambda params: {"status": "ok"}},
        )

        store.last_result.return_value = None
        result = runner.execute(check)

        assert result.phase == "alerting"
        assert result.changed is True
        assert result.notified is True

    def test_detect_change_and_notify_on_change(self) -> None:
        store = MagicMock(spec=ScheduleStorePort)
        alert = _alert()
        check = CronCheck(
            name="test", schedule="*/15 * * * *", use_case="test_list", notify_policy="on_change"
        )

        from hexawyn.domain.services.schedule.check_runner import CheckRunnerUseCase

        runner = CheckRunnerUseCase(
            store=store,
            alert_port=alert,
            use_case_registry={"test_list": lambda params: {"status": "degraded"}},
        )

        store.last_result.return_value = CheckResult(
            check_name="test", phase="success", started_at=_NOW, payload_digest="old_hash"
        )
        result = runner.execute(check)

        assert result.changed is True
        assert result.phase == "alerting"
        assert result.notified is True
        alert.send_alert.assert_called_once()

    def test_notify_always(self) -> None:
        store = MagicMock(spec=ScheduleStorePort)
        alert = _alert()
        check = CronCheck(
            name="test", schedule="*/15 * * * *", use_case="test_list", notify_policy="always"
        )

        from hexawyn.domain.services.schedule.check_runner import CheckRunnerUseCase

        runner = CheckRunnerUseCase(
            store=store,
            alert_port=alert,
            use_case_registry={"test_list": lambda params: {"status": "ok"}},
        )

        store.last_result.return_value = CheckResult(
            check_name="test", phase="success", started_at=_NOW, payload_digest="same_hash"
        )
        result = runner.execute(check)

        assert result.notified is True
        alert.send_alert.assert_called_once()

    def test_use_case_not_found_fails(self) -> None:
        store = MagicMock(spec=ScheduleStorePort)
        alert = _alert()
        check = CronCheck(name="test", schedule="*/15 * * * *", use_case="unknown")

        from hexawyn.domain.services.schedule.check_runner import CheckRunnerUseCase

        runner = CheckRunnerUseCase(store=store, alert_port=alert, use_case_registry={})

        result = runner.execute(check)

        assert result.phase == "failed"
        assert "not found" in (result.error_message or "").lower()

    def test_use_case_raises_exception_is_failed(self) -> None:
        store = MagicMock(spec=ScheduleStorePort)
        alert = _alert()
        check = CronCheck(name="test", schedule="*/15 * * * *", use_case="buggy")

        from hexawyn.domain.services.schedule.check_runner import CheckRunnerUseCase

        runner = CheckRunnerUseCase(
            store=store,
            alert_port=alert,
            use_case_registry={"buggy": lambda params: (_ for _ in ()).throw(RuntimeError("boom"))},
        )

        result = runner.execute(check)

        assert result.phase == "failed"
        assert "boom" in (result.error_message or "")
