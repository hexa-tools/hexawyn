from dataclasses import fields
from datetime import UTC, datetime


class TestCronCheck:
    def test_fields(self) -> None:
        from hexawyn.domain.models.schedule import CronCheck

        names = {f.name for f in fields(CronCheck)}
        assert names == {
            "name",
            "schedule",
            "use_case",
            "params",
            "enabled",
            "notify_policy",
            "destinations",
            "timeout_seconds",
        }

    def test_defaults(self) -> None:
        from hexawyn.domain.models.schedule import CronCheck

        check = CronCheck(name="certs-prod", schedule="0 */6 * * *", use_case="certs_list")

        assert check.enabled is True
        assert check.notify_policy == "on_change"
        assert check.timeout_seconds == 300  # noqa: PLR2004
        assert check.params == {}
        assert check.destinations == ["slack"]


class TestCheckResult:
    def test_fields(self) -> None:
        from hexawyn.domain.models.schedule import CheckResult

        names = {f.name for f in fields(CheckResult)}
        assert names == {
            "check_name",
            "phase",
            "started_at",
            "finished_at",
            "duration_ms",
            "summary",
            "payload_digest",
            "changed",
            "error_message",
            "notified",
        }

    def test_defaults(self) -> None:
        from hexawyn.domain.models.schedule import CheckResult

        now = datetime.now(UTC)

        result = CheckResult(
            check_name="certs-prod", phase="success", started_at=now, payload_digest="abc123"
        )

        assert result.changed is False
        assert result.notified is False
        assert result.duration_ms is None
        assert result.error_message is None
        assert result.summary == ""


class TestCheckPhase:
    def test_values(self) -> None:
        from hexawyn.domain.models.schedule import CheckPhase

        assert CheckPhase.SCHEDULED.value == "scheduled"
        assert CheckPhase.SUCCESS.value == "success"
        assert CheckPhase.ALERTING.value == "alerting"
        assert CheckPhase.FAILED.value == "failed"
        assert CheckPhase.DISABLED.value == "disabled"


class TestNotifyPolicy:
    def test_values(self) -> None:
        from hexawyn.domain.models.schedule import NotifyPolicy

        assert NotifyPolicy.ALWAYS.value == "always"
        assert NotifyPolicy.ON_CHANGE.value == "on_change"
        assert NotifyPolicy.ON_FAILURE.value == "on_failure"


class TestScheduleStatus:
    def test_defaults(self) -> None:
        from hexawyn.domain.models.schedule import ScheduleStatus

        status = ScheduleStatus()

        assert status.total_checks == 0
        assert status.enabled_checks == 0
        assert status.failed_checks == 0
