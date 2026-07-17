from __future__ import annotations

from hexawyn.domain.models.sensitive_data_audit import (
    AccessMatch,
    AlertLevel,
    SensitiveAccessRequest,
    SensitiveAuditResult,
)


class TestAccessMatch:
    def test_create(self) -> None:
        m = AccessMatch(
            timestamp="10:25:03Z",
            caller_ip="203.0.113.5",
            caller_service="unknown",
            method="GET",
            url="/user/456/ssn",
            status_code=200,
            user_id="user-789",
        )
        assert m.caller_ip == "203.0.113.5"
        assert m.user_id == "user-789"


class TestSensitiveAuditResult:
    def test_flags_external(self) -> None:
        matches = [
            AccessMatch(
                timestamp="T1",
                caller_ip="192.168.1.45",
                caller_service="user-service",
                method="GET",
                url="/user/123/ssn",
                status_code=200,
            ),
            AccessMatch(
                timestamp="T2",
                caller_ip="203.0.113.5",
                caller_service="unknown",
                method="GET",
                url="/user/456/ssn",
                status_code=200,
            ),
        ]
        result = SensitiveAuditResult.compute(
            request=SensitiveAccessRequest(
                pattern="/user/*/ssn",
                allowlist=["user-service"],
            ),
            matches=matches,
        )
        assert result.total_matches == 2
        assert len(result.flagged) == 1
        assert result.flagged[0].caller_ip == "203.0.113.5"
        assert result.alert_level == AlertLevel.MEDIUM

    def test_allowlisted_excluded(self) -> None:
        matches = [
            AccessMatch(
                timestamp="T1",
                caller_ip="192.168.1.45",
                caller_service="user-service",
                method="GET",
                url="/user/123/ssn",
                status_code=200,
            ),
        ]
        result = SensitiveAuditResult.compute(
            request=SensitiveAccessRequest(pattern="/user/*/ssn", allowlist=["user-service"]),
            matches=matches,
        )
        assert len(result.flagged) == 0
        assert result.alert_level == AlertLevel.NONE

    def test_no_matches(self) -> None:
        result = SensitiveAuditResult.compute(
            request=SensitiveAccessRequest(pattern="/ghost/*"),
            matches=[],
        )
        assert result.total_matches == 0
        assert result.alert_level == AlertLevel.NONE

    def test_high_alert(self) -> None:
        matches = [
            AccessMatch(
                timestamp=f"T{i}",
                caller_ip=f"10.0.0.{i}",
                caller_service=f"svc-{i}",
                method="GET",
                url="/user/x/ssn",
                status_code=200,
            )
            for i in range(7)
        ]
        result = SensitiveAuditResult.compute(
            request=SensitiveAccessRequest(pattern="/user/*/ssn"),
            matches=matches,
        )
        assert result.alert_level == AlertLevel.HIGH
        assert len(result.flagged) == 7
