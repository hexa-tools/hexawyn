"""RED → GREEN — CheckRunnerUseCase domain logic."""

from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

import pytest
from hexawyn.domain.models.schedule import CheckPhase, CheckResult, CronCheck
from hexawyn.domain.services.schedule import check_runner as check_runner_module
from hexawyn.domain.services.schedule.check_runner import CheckRunnerUseCase, _summarize


def _check(
    name: str = "certs_list",
    use_case: str = "certs_list",
    notify_policy: str = "on_change",
) -> CronCheck:
    return CronCheck(
        name=name,
        schedule="0 0 * * *",
        use_case=use_case,
        notify_policy=notify_policy,
    )


class _SequentialClock:
    def __init__(self, times: list[datetime]) -> None:
        self._times = times
        self._index = 0

    def now(self, tz: object = None) -> datetime:  # noqa: ARG002
        index = min(self._index, len(self._times) - 1)
        self._index += 1
        return self._times[index]


def _digest(output: dict[str, object]) -> str:
    payload = json.dumps(output, sort_keys=True, default=str)
    return hashlib.sha256(payload.encode()).hexdigest()


def _pin_clock(
    monkeypatch: pytest.MonkeyPatch,
    start: datetime,
) -> _SequentialClock:
    clock = _SequentialClock([start, start + timedelta(seconds=5)])
    monkeypatch.setattr(check_runner_module, "datetime", clock)
    return clock


def _alert_message(severity: str) -> dict[str, object]:
    return {
        "text": "[certs_list] certs_list: z, a",
        "title": "Schedule: certs_list",
        "severity": severity,
        "remediation": None,
        "cluster_name": "default",
        "score": 0,
        "is_pro": False,
    }


class TestUnknownUseCase:
    def test_returns_failed_result_with_error_message(self) -> None:
        runner = CheckRunnerUseCase(store=MagicMock(), alert_port=MagicMock(), use_case_registry={})

        result = runner.execute(_check(name="missing", use_case="no_such_case"))

        assert result.check_name == "missing"
        assert result.phase == CheckPhase.FAILED.value
        assert result.started_at.tzinfo is UTC
        assert result.finished_at is not None
        assert result.finished_at.tzinfo is UTC
        assert result.duration_ms == 0
        assert result.payload_digest == ""
        assert result.error_message == "Use case 'no_such_case' not found in registry."
        assert result.changed is False
        assert result.notified is False


class TestUseCaseException:
    def test_returns_failed_result_with_exception_text(self) -> None:
        registry = {"boom": MagicMock(side_effect=RuntimeError("kaboom"))}
        runner = CheckRunnerUseCase(
            store=MagicMock(),
            alert_port=MagicMock(),
            use_case_registry=registry,
        )

        result = runner.execute(_check(name="check-boom", use_case="boom"))

        assert result.check_name == "check-boom"
        assert result.phase == CheckPhase.FAILED.value
        assert result.started_at.tzinfo is UTC
        assert result.finished_at is not None
        assert result.finished_at.tzinfo is UTC
        assert result.duration_ms == 0
        assert result.payload_digest == ""
        assert result.error_message == "kaboom"


class TestUnchangedRun:
    def test_success_phase_when_digest_unchanged(self, monkeypatch: pytest.MonkeyPatch) -> None:
        output = {"z": 1, "a": datetime.now(UTC)}
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        _pin_clock(monkeypatch, start)
        store = MagicMock()
        store.last_result.return_value = CheckResult(
            check_name="certs_list",
            phase=CheckPhase.SUCCESS.value,
            started_at=datetime.now(UTC),
            payload_digest=_digest(output),
        )
        runner = CheckRunnerUseCase(
            store=store,
            alert_port=MagicMock(),
            use_case_registry={"certs_list": MagicMock(return_value=output)},
        )

        result = runner.execute(_check())

        assert result.phase == CheckPhase.SUCCESS.value
        assert result.changed is False
        assert result.notified is False
        assert result.payload_digest == _digest(output)
        assert result.duration_ms == 5000  # noqa: PLR2004
        assert result.started_at == start
        assert result.finished_at == start + timedelta(seconds=5)
        assert result.check_name == "certs_list"
        assert result.summary == "z, a"
        store.last_result.assert_called_once_with("certs_list")
        store.save_result.assert_called_once_with(result)

    def test_timestamps_recorded_in_utc_with_real_clock(self) -> None:
        store = MagicMock()
        store.last_result.return_value = None
        runner = CheckRunnerUseCase(
            store=store,
            alert_port=MagicMock(),
            use_case_registry={"certs_list": MagicMock(return_value={"z": 1, "a": 2})},
        )

        result = runner.execute(_check())

        assert result.started_at.tzinfo is UTC
        assert result.finished_at is not None
        assert result.finished_at.tzinfo is UTC
        assert result.duration_ms is not None
        assert result.summary == "z, a"


class TestChangedRun:
    def test_alerting_with_warning_on_change(self, monkeypatch: pytest.MonkeyPatch) -> None:
        output = {"z": 1, "a": datetime.now(UTC)}
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        _pin_clock(monkeypatch, start)
        store = MagicMock()
        store.last_result.return_value = CheckResult(
            check_name="certs_list",
            phase=CheckPhase.SUCCESS.value,
            started_at=datetime.now(UTC),
            payload_digest="stale-digest",
        )
        alert_port = MagicMock()
        alert_port.send_alert.return_value = True
        runner = CheckRunnerUseCase(
            store=store,
            alert_port=alert_port,
            use_case_registry={"certs_list": MagicMock(return_value=output)},
        )

        result = runner.execute(_check())

        assert result.phase == CheckPhase.ALERTING.value
        assert result.changed is True
        assert result.notified is True
        alert_port.send_alert.assert_called_once_with(_alert_message(severity="warning"))

    def test_first_run_without_history_is_alerting(self, monkeypatch: pytest.MonkeyPatch) -> None:
        output = {"z": 1, "a": datetime.now(UTC)}
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        _pin_clock(monkeypatch, start)
        store = MagicMock()
        store.last_result.return_value = None
        runner = CheckRunnerUseCase(
            store=store,
            alert_port=MagicMock(),
            use_case_registry={"certs_list": MagicMock(return_value=output)},
        )

        result = runner.execute(_check())

        assert result.changed is True
        assert result.phase == CheckPhase.ALERTING.value


class TestAlwaysPolicy:
    def test_always_policy_notifies_without_change(self, monkeypatch: pytest.MonkeyPatch) -> None:
        output = {"z": 1, "a": datetime.now(UTC)}
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        _pin_clock(monkeypatch, start)
        store = MagicMock()
        store.last_result.return_value = CheckResult(
            check_name="certs_list",
            phase=CheckPhase.SUCCESS.value,
            started_at=datetime.now(UTC),
            payload_digest=_digest(output),
        )
        alert_port = MagicMock()
        alert_port.send_alert.return_value = False
        runner = CheckRunnerUseCase(
            store=store,
            alert_port=alert_port,
            use_case_registry={"certs_list": MagicMock(return_value=output)},
        )

        result = runner.execute(_check(notify_policy="always"))

        assert result.changed is False
        assert result.phase == CheckPhase.SUCCESS.value
        assert result.notified is False
        alert_port.send_alert.assert_called_once_with(_alert_message(severity="info"))

    def test_always_policy_failed_delivery_false(self, monkeypatch: pytest.MonkeyPatch) -> None:
        output = {"z": 1, "a": datetime.now(UTC)}
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        _pin_clock(monkeypatch, start)
        store = MagicMock()
        store.last_result.return_value = CheckResult(
            check_name="certs_list",
            phase=CheckPhase.SUCCESS.value,
            started_at=datetime.now(UTC),
            payload_digest="stale-digest",
        )
        alert_port = MagicMock()
        alert_port.send_alert.return_value = False
        runner = CheckRunnerUseCase(
            store=store,
            alert_port=alert_port,
            use_case_registry={"certs_list": MagicMock(return_value=output)},
        )

        result = runner.execute(_check(notify_policy="always"))

        assert result.changed is True
        assert result.notified is False
        assert result.phase == CheckPhase.ALERTING.value


class TestOnFailurePolicy:
    def test_on_failure_policy_never_notifies(self, monkeypatch: pytest.MonkeyPatch) -> None:
        output = {"z": 1, "a": datetime.now(UTC)}
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        _pin_clock(monkeypatch, start)
        store = MagicMock()
        store.last_result.return_value = CheckResult(
            check_name="certs_list",
            phase=CheckPhase.SUCCESS.value,
            started_at=datetime.now(UTC),
            payload_digest="stale-digest",
        )
        alert_port = MagicMock()
        runner = CheckRunnerUseCase(
            store=store,
            alert_port=alert_port,
            use_case_registry={"certs_list": MagicMock(return_value=output)},
        )

        result = runner.execute(_check(notify_policy="on_failure"))

        assert result.changed is True
        assert result.notified is False
        assert result.phase == CheckPhase.ALERTING.value
        alert_port.send_alert.assert_not_called()


class TestParamForwarding:
    def test_check_params_forwarded_to_use_case(self, monkeypatch: pytest.MonkeyPatch) -> None:
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        _pin_clock(monkeypatch, start)
        store = MagicMock()
        store.last_result.return_value = None
        captured: dict[str, str] = {}

        def capture(params: dict[str, str]) -> dict[str, object]:
            captured.update(params)
            return {"pods": 3}

        runner = CheckRunnerUseCase(
            store=store,
            alert_port=MagicMock(),
            use_case_registry={"certs_list": capture},
        )
        check = CronCheck(
            name="certs_list",
            schedule="0 0 * * *",
            use_case="certs_list",
            params={"namespace": "ns1", "limit": "10"},
        )

        runner.execute(check)

        assert captured == {"namespace": "ns1", "limit": "10"}


class TestEmptyOutput:
    def test_execute_reports_empty_response_summary(self, monkeypatch: pytest.MonkeyPatch) -> None:
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        _pin_clock(monkeypatch, start)
        store = MagicMock()
        store.last_result.return_value = None
        runner = CheckRunnerUseCase(
            store=store,
            alert_port=MagicMock(),
            use_case_registry={"certs_list": MagicMock(return_value={})},
        )

        result = runner.execute(_check())

        assert result.summary == "empty response"
        assert result.payload_digest != ""


class TestSummarize:
    def test_empty_output_returns_empty_response_marker(self) -> None:
        assert _summarize({}) == "empty response"

    def test_joins_only_first_three_keys(self) -> None:
        output = {"alpha": 1, "beta": 2, "gamma": 3, "delta": 4}

        assert _summarize(output) == "alpha, beta, gamma"

    def test_single_key_joined_without_separator(self) -> None:
        assert _summarize({"only": 1}) == "only"
