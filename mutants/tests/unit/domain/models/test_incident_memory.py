from __future__ import annotations

from hexawyn.domain.models.incident_memory import IncidentMemoryRecord


class TestIncidentMemoryRecord:
    def test_defaults(self) -> None:
        record = IncidentMemoryRecord(cluster_name="prod", tool_name="chat_investigation")
        assert record.cause == ""
        assert record.solution == ""
        assert record.severity == "low"
        assert record.namespace is None
        assert record.resource_name is None
        assert record.resource_kind is None
        assert record.symptoms == []
        assert record.embedding == []
        assert record.sanitized is False

    def test_is_storable_true_with_embedding_cluster_and_tool(self) -> None:
        record = IncidentMemoryRecord(
            cluster_name="prod",
            tool_name="chat_investigation",
            embedding=[0.1, 0.2, 0.3],
        )
        assert record.is_storable is True

    def test_is_storable_false_without_embedding(self) -> None:
        record = IncidentMemoryRecord(cluster_name="prod", tool_name="chat_investigation")
        assert record.is_storable is False

    def test_is_storable_false_without_cluster(self) -> None:
        record = IncidentMemoryRecord(
            cluster_name="", tool_name="chat_investigation", embedding=[0.1]
        )
        assert record.is_storable is False

    def test_is_storable_false_without_tool(self) -> None:
        record = IncidentMemoryRecord(cluster_name="prod", tool_name="", embedding=[0.1])
        assert record.is_storable is False

    def test_is_storable_false_when_all_three_preconditions_fail(self) -> None:
        record = IncidentMemoryRecord(cluster_name="", tool_name="", embedding=[])
        assert record.is_storable is False

    def test_is_storable_true_with_zero_value_embedding(self) -> None:
        record = IncidentMemoryRecord(
            cluster_name="prod", tool_name="detector", embedding=[0.0, 0.0, 0.0]
        )
        assert record.is_storable is True

    def test_is_storable_with_whitespace_cluster_name(self) -> None:
        record = IncidentMemoryRecord(cluster_name="   ", tool_name="detector", embedding=[0.1])
        assert record.is_storable is True

    def test_symptoms_list_is_independent_per_instance(self) -> None:
        a = IncidentMemoryRecord(cluster_name="a", tool_name="t", symptoms=["x"])
        b = IncidentMemoryRecord(cluster_name="b", tool_name="t")
        assert a.symptoms == ["x"]
        assert b.symptoms == []

    def test_embedding_list_is_independent_per_instance(self) -> None:
        a = IncidentMemoryRecord(cluster_name="a", tool_name="t", embedding=[0.1, 0.2])
        b = IncidentMemoryRecord(cluster_name="b", tool_name="t")
        assert a.embedding == [0.1, 0.2]
        assert b.embedding == []

    def test_sanitized_true_when_explicitly_set(self) -> None:
        record = IncidentMemoryRecord(cluster_name="prod", tool_name="t", sanitized=True)
        assert record.sanitized is True

    def test_severity_accepts_medium_high_critical(self) -> None:
        for sev in ("medium", "high", "critical"):
            record = IncidentMemoryRecord(cluster_name="prod", tool_name="t", severity=sev)
            assert record.severity == sev

    def test_fully_populated_record_stores_all_fields(self) -> None:
        record = IncidentMemoryRecord(
            cluster_name="prod-eu",
            tool_name="crashloop_detector",
            cause="OOM",
            solution="Increase memory",
            severity="high",
            namespace="payments",
            resource_name="payments-api",
            resource_kind="Deployment",
            symptoms=["high memory", "slow GC"],
            embedding=[0.1, 0.2, 0.3],
            sanitized=True,
        )
        assert record.cause == "OOM"
        assert record.solution == "Increase memory"
        assert record.namespace == "payments"
        assert record.resource_name == "payments-api"
        assert record.resource_kind == "Deployment"
        assert record.symptoms == ["high memory", "slow GC"]
