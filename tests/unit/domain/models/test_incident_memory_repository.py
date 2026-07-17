from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.domain.models.incident_memory import IncidentMemoryRecord
from hexawyn.infrastructure.memory.incident_memory_repository import (
    IncidentMemoryRepository,
)


def _storable_record() -> IncidentMemoryRecord:
    return IncidentMemoryRecord(
        cluster_name="prod-cluster",
        tool_name="chat_investigation",
        cause="OOMKilled on payments-api",
        solution="Increase memory limit to 512Mi",
        severity="high",
        namespace="payments",
        resource_name="payments-api",
        resource_kind="Deployment",
        symptoms=["restart", "oom"],
        embedding=[0.1, 0.2, 0.3],
    )


class TestIncidentMemoryRepository:
    def setup_method(self) -> None:
        self.mock_conn = MagicMock()
        self.repo = IncidentMemoryRepository(conn=self.mock_conn)

    def test_store_incident_executes_insert_with_all_columns(self) -> None:
        self.repo.store_incident(_storable_record())

        self.mock_conn.execute.assert_called_once()
        args, _ = self.mock_conn.execute.call_args
        params = args[1]
        assert params[0] == "prod-cluster"
        assert params[1] == "payments"
        assert params[2] == "payments-api"
        assert params[3] == "Deployment"
        assert params[4] == "chat_investigation"
        assert params[5] == "OOMKilled on payments-api"
        assert params[6] == ["restart", "oom"]
        assert params[7] == "Increase memory limit to 512Mi"
        assert params[8] == "high"
        assert params[9] == [0.1, 0.2, 0.3]
        assert params[10] is False

    def test_store_incident_skips_record_without_embedding(self) -> None:
        record = IncidentMemoryRecord(cluster_name="prod", tool_name="chat_investigation")
        self.repo.store_incident(record)
        self.mock_conn.execute.assert_not_called()

    def test_store_incident_skips_record_without_cluster(self) -> None:
        record = IncidentMemoryRecord(
            cluster_name="", tool_name="chat_investigation", embedding=[0.1]
        )
        self.repo.store_incident(record)
        self.mock_conn.execute.assert_not_called()

    def test_store_incident_failure_is_swallowed(self) -> None:
        self.mock_conn.execute.side_effect = Exception("db locked")
        self.repo.store_incident(_storable_record())
