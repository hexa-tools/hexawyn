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
