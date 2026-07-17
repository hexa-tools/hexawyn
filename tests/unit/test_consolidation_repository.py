"""Tests for DuckDBConsolidationRepository."""

import uuid
from unittest.mock import MagicMock

from hexawyn.application.ports.driven.consolidation_port import (
    ConsolidationConfig,
    ConsolidationPort,
)


class TestDuckDBConsolidationRepository:
    def test_implements_consolidation_port(self) -> None:
        from hexawyn.infrastructure.memory.consolidation_repository import (
            DuckDBConsolidationRepository,
        )

        repo = DuckDBConsolidationRepository(conn=MagicMock())
        assert isinstance(repo, ConsolidationPort)

    def test_find_incident_groups_queries_db(self) -> None:
        from hexawyn.infrastructure.memory.consolidation_repository import (
            DuckDBConsolidationRepository,
        )

        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchall.return_value = [
            ("payments", "payments-api", "crashloop_detector", 3),
            ("payments", "payments-api", "oomkilled_detector", 2),
        ]

        repo = DuckDBConsolidationRepository(conn=mock_conn)
        config: ConsolidationConfig = {
            "min_occurrences": 2,
            "similarity_threshold": 0.85,
            "max_age_days": 90,
        }
        groups = repo.find_incident_groups(config=config, cluster_name="prod-eu")

        assert len(groups) == 2
        assert groups[0] == ("payments", "payments-api", "crashloop_detector", 3)
        mock_conn.execute.assert_called()

    def test_find_incident_groups_returns_empty_when_none_found(self) -> None:
        from hexawyn.infrastructure.memory.consolidation_repository import (
            DuckDBConsolidationRepository,
        )

        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchall.return_value = []

        repo = DuckDBConsolidationRepository(conn=mock_conn)
        config: ConsolidationConfig = {
            "min_occurrences": 2,
            "similarity_threshold": 0.85,
            "max_age_days": 90,
        }
        groups = repo.find_incident_groups(config=config, cluster_name="prod-eu")
        assert groups == []

    def test_store_knowledge_inserts_row(self) -> None:
        from hexawyn.infrastructure.memory.consolidation_repository import (
            DuckDBConsolidationRepository,
        )

        mock_conn = MagicMock()
        repo = DuckDBConsolidationRepository(conn=mock_conn)

        repo.store_knowledge(
            id="k1",
            pattern="OOM detected on payments-api",
            resource_name="payments-api",
            namespace="payments",
            tool_name="crashloop_detector",
            cluster_name="prod-eu",
            occurrence_count=3,
            first_seen="2026-07-01T10:00:00Z",
            last_seen="2026-07-15T14:00:00Z",
            source_incident_ids=["i1", "i2", "i3"],
            embedding=[0.1] * 768,
            weight=2.5,
            confidence=0.85,
        )
        mock_conn.execute.assert_called()

    def test_store_knowledge_swallows_exception(self) -> None:
        from hexawyn.infrastructure.memory.consolidation_repository import (
            DuckDBConsolidationRepository,
        )

        mock_conn = MagicMock()
        mock_conn.execute.side_effect = RuntimeError("db error")
        repo = DuckDBConsolidationRepository(conn=mock_conn)

        repo.store_knowledge(
            id="k1",
            pattern="test",
            tool_name="t",
            cluster_name="c",
            occurrence_count=1,
        )

    def test_mark_consolidated_updates_incidents(self) -> None:
        from hexawyn.infrastructure.memory.consolidation_repository import (
            DuckDBConsolidationRepository,
        )

        mock_conn = MagicMock()
        repo = DuckDBConsolidationRepository(conn=mock_conn)

        repo.mark_consolidated(
            incident_ids=[str(uuid.uuid4())],
            knowledge_id="k1",
        )
        mock_conn.execute.assert_called()

    def test_search_consolidated_queries_db(self) -> None:
        from hexawyn.infrastructure.memory.consolidation_repository import (
            DuckDBConsolidationRepository,
        )

        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchall.return_value = [
            (
                "k1",
                "OOM pattern",
                "payments-api",
                "Deployment",
                "payments",
                "crashloop_detector",
                3,
                "2026-07-01T10:00:00Z",
                "2026-07-15T14:00:00Z",
                2.5,
                0.85,
                0.92,
            )
        ]

        repo = DuckDBConsolidationRepository(conn=mock_conn)
        results = repo.search_consolidated(
            embedding=[0.1] * 768,
            cluster_name="prod-eu",
            limit=5,
        )

        assert len(results) == 1
        assert results[0]["pattern"] == "OOM pattern"
        assert results[0]["tool_name"] == "crashloop_detector"
        mock_conn.execute.assert_called()

    def test_get_incidents_for_group_returns_ids(self) -> None:
        from hexawyn.infrastructure.memory.consolidation_repository import (
            DuckDBConsolidationRepository,
        )

        i1, i2 = str(uuid.uuid4()), str(uuid.uuid4())
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchall.return_value = [(i1,), (i2,)]

        repo = DuckDBConsolidationRepository(conn=mock_conn)
        ids = repo.get_incidents_for_group(
            namespace="payments",
            resource_name="payments-api",
            tool_name="crashloop_detector",
            cluster_name="prod-eu",
            max_age_days=90,
        )

        assert ids == [i1, i2]

    def test_get_incidents_for_group_returns_empty_for_no_match(self) -> None:
        from hexawyn.infrastructure.memory.consolidation_repository import (
            DuckDBConsolidationRepository,
        )

        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchall.return_value = []

        repo = DuckDBConsolidationRepository(conn=mock_conn)
        ids = repo.get_incidents_for_group(
            namespace="empty_ns",
            resource_name="nores",
            tool_name="notool",
            cluster_name="prod-eu",
            max_age_days=90,
        )
        assert ids == []

    def test_find_incident_groups_skips_old_incidents(self) -> None:
        from hexawyn.infrastructure.memory.consolidation_repository import (
            DuckDBConsolidationRepository,
        )

        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchall.return_value = []

        repo = DuckDBConsolidationRepository(conn=mock_conn)
        config: ConsolidationConfig = {
            "min_occurrences": 2,
            "similarity_threshold": 0.85,
            "max_age_days": 7,
        }
        groups = repo.find_incident_groups(config=config, cluster_name="prod-eu")
        assert groups == []
        call_args = mock_conn.execute.call_args[0]
        assert call_args[1][1] == 7

    def test_mark_consolidated_handles_empty_ids(self) -> None:
        from hexawyn.infrastructure.memory.consolidation_repository import (
            DuckDBConsolidationRepository,
        )

        mock_conn = MagicMock()
        repo = DuckDBConsolidationRepository(conn=mock_conn)
        repo.mark_consolidated(
            incident_ids=[],
            knowledge_id="k1",
        )
        mock_conn.execute.assert_called()

    def test_store_knowledge_with_none_optionals(self) -> None:
        from hexawyn.infrastructure.memory.consolidation_repository import (
            DuckDBConsolidationRepository,
        )

        mock_conn = MagicMock()
        repo = DuckDBConsolidationRepository(conn=mock_conn)
        repo.store_knowledge(
            id="k1",
            pattern="test",
            tool_name="t",
            cluster_name="c",
            occurrence_count=1,
            resource_name=None,
            resource_kind=None,
            namespace=None,
            first_seen="",
            last_seen="",
            source_incident_ids=None,
            embedding=None,
            weight=1.0,
            confidence=0.5,
        )
        mock_conn.execute.assert_called()
