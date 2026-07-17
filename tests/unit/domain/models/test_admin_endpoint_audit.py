from __future__ import annotations

from hexawyn.domain.models.admin_endpoint_audit import (
    AdminAuditRequest,
    AdminAuditResult,
    CallerRisk,
    CallerSummary,
    FailedAdminCall,
)


class TestFailedAdminCall:
    def test_create(self) -> None:
        call = FailedAdminCall(
            timestamp="10:32:15.421",
            caller_ip="185.220.101.5",
            caller_service="unknown",
            endpoint="/admin/users",
            user_identity=None,
        )
        assert call.caller_ip == "185.220.101.5"
        assert call.endpoint == "/admin/users"


class TestCallerSummary:
    def test_flagged(self) -> None:
        cs = CallerSummary(
            caller_ip="185.220.101.5",
            caller_service="unknown",
            attempts=52,
            endpoints=["/admin/users", "/admin/config"],
            flagged=True,
            risk=CallerRisk.HIGH,
        )
        assert cs.flagged is True
        assert cs.risk == CallerRisk.HIGH

    def test_not_flagged(self) -> None:
        cs = CallerSummary(
            caller_ip="10.0.1.45",
            caller_service="monitoring",
            attempts=3,
            endpoints=["/admin/metrics"],
            flagged=False,
            risk=CallerRisk.LOW,
        )
        assert not cs.flagged


class TestAdminAuditResult:
    def test_high_risk_detected(self) -> None:
        calls = []
        for i in range(52):
            calls.append(
                FailedAdminCall(
                    timestamp=f"T{i}",
                    caller_ip="185.220.101.5",
                    caller_service="unknown",
                    endpoint="/admin/users",
                )
            )
        for i in range(3):
            calls.append(
                FailedAdminCall(
                    timestamp=f"T{i}",
                    caller_ip="10.0.1.45",
                    caller_service="monitoring-service",
                    endpoint="/admin/metrics",
                )
            )
        result = AdminAuditResult.compute(
            request=AdminAuditRequest(endpoint_pattern="/admin*", time_window_minutes=30),
            calls=calls,
            total_requests=520,
        )
        assert result.total_403s == 55
        assert result.rate_403_pct == round((55 / 520) * 100, 2)
        assert len(result.flagged_callers) == 1
        assert result.flagged_callers[0].caller_ip == "185.220.101.5"

    def test_no_403s(self) -> None:
        result = AdminAuditResult.compute(
            request=AdminAuditRequest(),
            calls=[],
            total_requests=100,
        )
        assert result.total_403s == 0
        assert result.flagged_callers == []

    def test_no_flag_below_threshold(self) -> None:
        calls = [
            FailedAdminCall(
                timestamp="T1", caller_ip="10.0.0.1", caller_service="svc", endpoint="/admin/x"
            ),
            FailedAdminCall(
                timestamp="T2", caller_ip="10.0.0.1", caller_service="svc", endpoint="/admin/y"
            ),
        ]
        result = AdminAuditResult.compute(
            request=AdminAuditRequest(flag_threshold=5),
            calls=calls,
            total_requests=100,
        )
        assert len(result.flagged_callers) == 0
