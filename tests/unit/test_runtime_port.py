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
