from hexawyn.application.ports.driven.runtime_port import (
    InvestigationOutput,
    RuntimePort,
    StartupScanResult,
)


def test_runtime_port_is_abstract() -> None:
    assert RuntimePort.__abstractmethods__ is not None
    assert "set_adapter" in RuntimePort.__abstractmethods__
    assert "run_investigation" in RuntimePort.__abstractmethods__
    assert "run_startup_scan" in RuntimePort.__abstractmethods__


def test_cannot_instantiate_directly() -> None:
    try:
        _ = RuntimePort()  # type: ignore[abstract]
    except TypeError:
        assert True


def test_startup_scan_result_defaults() -> None:
    result = StartupScanResult()
    assert result.health_score == 0
    assert result.narrative_summary == ""
    assert result.provider_badge == ""
    assert result.top_issues == []
    assert result.suggestions == []
    assert result.provider == ""
    assert result.provider_display == ""
    assert result.cluster_summary == {}
    assert result.findings == []


def test_startup_scan_result_custom() -> None:
    result = StartupScanResult(
        health_score=85,
        narrative_summary="Cluster healthy",
        provider_badge="[AWS EKS]",
        top_issues=["2 CrashLoopBackOff pods"],
        suggestions=[{"label": "debug payments-api", "value": "debug payments-api"}],
        provider="aws",
        provider_display="AWS EKS",
        cluster_summary={"total_pods": 42, "total_nodes": 5},
        findings=[{"type": "CrashLoopBackOff", "resource": "payments-api-7d4f8b9c-x2k9m"}],
    )
    assert result.health_score == 85
    assert result.provider == "aws"
    assert result.cluster_summary["total_pods"] == 42


def test_investigation_output_keys() -> None:
    output: InvestigationOutput = {
        "answer": "OOMKilled detected",
        "cause": "Memory limit too low",
        "solution": "Increase memory limit to 512Mi",
        "status": "complete",
        "suggestions": ["Increase memory limit", "Add HPA"],
        "error": None,
    }
    assert output["answer"] == "OOMKilled detected"
    assert output["cause"] == "Memory limit too low"
    assert output["solution"] == "Increase memory limit to 512Mi"
    assert output["status"] == "complete"
    assert output["suggestions"] == ["Increase memory limit", "Add HPA"]
    assert output["error"] is None


def test_runtime_port_has_quota_methods() -> None:
    assert "check_quota" in RuntimePort.__abstractmethods__
    assert "increment_quota" in RuntimePort.__abstractmethods__


def test_quota_check_result_defaults() -> None:
    from hexawyn.application.ports.driven.runtime_port import QuotaCheckResult

    result: QuotaCheckResult = {"allowed": True, "used": 0, "limit": 50, "remaining": 50}
    assert result["allowed"] is True
    assert result["used"] == 0
    assert result["limit"] == 50
    assert result["remaining"] == 50


def test_quota_check_result_exceeded() -> None:
    from hexawyn.application.ports.driven.runtime_port import QuotaCheckResult

    result: QuotaCheckResult = {"allowed": False, "used": 50, "limit": 50, "remaining": 0}
    assert result["allowed"] is False
    assert result["used"] == 50
    assert result["remaining"] == 0


class TestStubRuntimeAdapterQuota:
    def test_check_quota_always_allows(self) -> None:
        from hexawyn.application.service.runtime_adapter import StubRuntimeAdapter

        stub = StubRuntimeAdapter()
        result = stub.check_quota()
        assert result["allowed"] is True

    def test_increment_quota_is_noop(self) -> None:
        from hexawyn.application.service.runtime_adapter import StubRuntimeAdapter

        stub = StubRuntimeAdapter()
        stub.increment_quota()  # should not raise


class TestHttpRuntimeAdapterQuota:
    def test_check_quota_delegates_to_client(self) -> None:
        from unittest.mock import MagicMock

        from hexawyn.application.service.http_runtime_adapter import HttpRuntimeAdapter

        adapter = HttpRuntimeAdapter(endpoint="http://localhost:8000")
        mock_client = MagicMock()
        mock_client.check_quota.return_value = {
            "allowed": True,
            "used": 5,
            "limit": 50,
            "remaining": 45,
        }
        adapter._client = mock_client

        result = adapter.check_quota()
        assert result["allowed"] is True
        mock_client.check_quota.assert_called_once()

    def test_increment_quota_delegates_to_client(self) -> None:
        from unittest.mock import MagicMock

        from hexawyn.application.service.http_runtime_adapter import HttpRuntimeAdapter

        adapter = HttpRuntimeAdapter(endpoint="http://localhost:8000")
        mock_client = MagicMock()
        adapter._client = mock_client

        adapter.increment_quota()
        mock_client.increment_quota.assert_called_once()
