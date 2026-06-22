from datetime import UTC
from uuid import UUID

from hexawyn.domain.models.investigation import (
    InvestigationResult,
    InvestigationStatus,
    Severity,
)


class TestInvestigationStatus:
    def test_values(self):
        assert InvestigationStatus.PENDING.value == "pending"
        assert InvestigationStatus.RUNNING.value == "running"
        assert InvestigationStatus.COMPLETE.value == "complete"
        assert InvestigationStatus.ERROR.value == "error"
        assert InvestigationStatus.DEGRADED.value == "degraded"


class TestSeverity:
    def test_values(self):
        assert Severity.LOW.value == "low"
        assert Severity.MEDIUM.value == "medium"
        assert Severity.HIGH.value == "high"
        assert Severity.CRITICAL.value == "critical"


class TestInvestigationResult:
    def test_minimal_construction(self):
        result = InvestigationResult(
            query="Why is pod failing?",
            answer="CrashLoopBackOff",
            status=InvestigationStatus.COMPLETE,
        )
        assert result.query == "Why is pod failing?"
        assert isinstance(result.id, UUID)
        assert result.tool_name == ""
        assert result.severity == Severity.LOW
        assert result.suggestions == []
        assert result.embedding == []
        assert result.verified is False

    def test_timestamp_is_utc(self):
        result = InvestigationResult(
            query="q", answer="a", status=InvestigationStatus.PENDING
        )
        assert result.timestamp.tzinfo is not None
        assert result.timestamp.tzinfo == UTC

    def test_full_construction(self):
        result = InvestigationResult(
            query="Check node health",
            answer="Node pressure",
            status=InvestigationStatus.DEGRADED,
            tool_name="get_node_status",
            cause="MemoryPressure",
            solution="Drain node",
            severity=Severity.HIGH,
            suggestions=["Check memory limits", "Add taint"],
            embedding=[0.1, 0.2, 0.3],
            verified=True,
        )
        assert result.tool_name == "get_node_status"
        assert result.severity == Severity.HIGH
        assert len(result.suggestions) == 2
        assert result.verified is True

    def test_id_is_unique(self):
        r1 = InvestigationResult(
            query="a", answer="b", status=InvestigationStatus.RUNNING
        )
        r2 = InvestigationResult(
            query="a", answer="b", status=InvestigationStatus.RUNNING
        )
        assert r1.id != r2.id
