from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.consolidation_port import ConsolidationConfig
from hexawyn.infrastructure.memory.consolidation_repository import (
    DuckDBConsolidationRepository,
    _parse_consolidated_rows,
)


class TestParseConsolidatedRows:
    def test_parses_single_row(self) -> None:
        row = (
            "id-1",
            "pattern-1",
            "res-name",
            "Deployment",
            "default",
            "tool-a",
            5,
            "2026-01-01",
            "2026-01-05",
            1.0,
            0.9,
        )
        rows = [
            (
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10],
            )
        ]
        result = _parse_consolidated_rows(rows)
        assert len(result) == 1
        assert result[0]["id"] == "id-1"
        assert result[0]["pattern"] == "pattern-1"
        assert result[0]["occurrence_count"] == 5  # noqa: PLR2004
        assert result[0]["confidence"] == 0.9  # noqa: PLR2004

    def test_parses_multiple_rows(self) -> None:
        rows = [
            (
                "id-1",
                "p1",
                "r1",
                "Deployment",
                "ns1",
                "t1",
                3,
                "2026-01-01",
                "2026-01-02",
                1.0,
                0.5,
            ),
            (
                "id-2",
                "p2",
                "r2",
                "StatefulSet",
                "ns2",
                "t2",
                7,
                "2026-01-03",
                "2026-01-04",
                2.0,
                0.8,
            ),
        ]
        result = _parse_consolidated_rows(rows)
        assert len(result) == 2  # noqa: PLR2004
        assert result[1]["resource_kind"] == "StatefulSet"

    def test_none_fields_mapped_correctly(self) -> None:
        row = (
            "id-1",
            "pattern",
            None,
            None,
            None,
            "tool",
            1,
            "2026-01-01",
            "2026-01-01",
            1.0,
            0.5,
        )
        rows = [
            (
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10],
            )
        ]
        result = _parse_consolidated_rows(rows)
        assert result[0]["resource_name"] is None
        assert result[0]["resource_kind"] is None
        assert result[0]["namespace"] is None

    def test_empty_list(self) -> None:
        assert _parse_consolidated_rows([]) == []


class TestDuckDBConsolidationRepository:
    def test_find_incident_groups(self) -> None:
        mock_conn = MagicMock()
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [
            ("ns-1", "res-1", "tool-1", 5),
            ("ns-2", "res-2", "tool-2", 3),
        ]
        mock_conn.execute.return_value = mock_result

        with patch(
            "hexawyn.infrastructure.memory.consolidation_repository._load_sql",
            return_value="SQL_QUERY",
        ):
            repo = DuckDBConsolidationRepository(mock_conn)
            config: ConsolidationConfig = {
                "min_occurrences": 3,
                "similarity_threshold": 0.8,
                "max_age_days": 30,
            }
            result = repo.find_incident_groups(config, "prod-eu")

        assert len(result) == 2  # noqa: PLR2004
        assert result[0] == ("ns-1", "res-1", "tool-1", 5)
        assert result[1] == ("ns-2", "res-2", "tool-2", 3)

    def test_find_incident_groups_with_nones(self) -> None:
        mock_conn = MagicMock()
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [(None, None, None, 0)]
        mock_conn.execute.return_value = mock_result

        with patch(
            "hexawyn.infrastructure.memory.consolidation_repository._load_sql",
            return_value="SQL",
        ):
            repo = DuckDBConsolidationRepository(mock_conn)
            config: ConsolidationConfig = {
                "min_occurrences": 1,
                "similarity_threshold": 0.9,
                "max_age_days": 7,
            }
            result = repo.find_incident_groups(config, "test")

        assert result == [("", "", "", 0)]

    def test_get_incidents_for_group(self) -> None:
        mock_conn = MagicMock()
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [("inc-001",), ("inc-002",)]
        mock_conn.execute.return_value = mock_result

        with patch(
            "hexawyn.infrastructure.memory.consolidation_repository._load_sql",
            return_value="SQL",
        ):
            repo = DuckDBConsolidationRepository(mock_conn)
            result = repo.get_incidents_for_group(
                "default", "deploy-x", "zombie_detector", "prod", 30
            )

        assert result == ["inc-001", "inc-002"]

    def test_get_incidents_for_group_empty(self) -> None:
        mock_conn = MagicMock()
        mock_result = MagicMock()
        mock_result.fetchall.return_value = []
        mock_conn.execute.return_value = mock_result

        with patch(
            "hexawyn.infrastructure.memory.consolidation_repository._load_sql",
            return_value="SQL",
        ):
            repo = DuckDBConsolidationRepository(mock_conn)
            result = repo.get_incidents_for_group("default", "deploy-x", "tool", "prod", 30)

        assert result == []

    def test_store_knowledge_success(self) -> None:
        mock_conn = MagicMock()

        with patch(
            "hexawyn.infrastructure.memory.consolidation_repository._load_sql",
            return_value="SQL",
        ):
            repo = DuckDBConsolidationRepository(mock_conn)
            repo.store_knowledge(
                id="k-1",
                pattern="OOM detected in payments",
                tool_name="zombie_detector",
                cluster_name="prod",
                occurrence_count=3,
                resource_name="deploy-x",
                resource_kind="Deployment",
                namespace="default",
                first_seen="2026-01-01",
                last_seen="2026-01-05",
                source_incident_ids=["inc-1", "inc-2"],
                embedding=[0.1, 0.2, 0.3],
                weight=1.5,
                confidence=0.9,
            )

        mock_conn.execute.assert_called_once()

    def test_store_knowledge_suppresses_exceptions(self) -> None:
        mock_conn = MagicMock()
        mock_conn.execute.side_effect = RuntimeError("duckdb error")

        with patch(
            "hexawyn.infrastructure.memory.consolidation_repository._load_sql",
            return_value="SQL",
        ):
            repo = DuckDBConsolidationRepository(mock_conn)
            repo.store_knowledge(
                id="k-fail",
                pattern="test",
                tool_name="tool",
                cluster_name="test",
                occurrence_count=1,
            )

    def test_mark_consolidated(self) -> None:
        mock_conn = MagicMock()

        with patch(
            "hexawyn.infrastructure.memory.consolidation_repository._load_sql",
            return_value="SQL",
        ):
            repo = DuckDBConsolidationRepository(mock_conn)
            repo.mark_consolidated(["inc-1", "inc-2"], "k-1")

        mock_conn.execute.assert_called_once()

    def test_search_consolidated(self) -> None:
        mock_conn = MagicMock()
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [
            (
                "k-1",
                "OOM pattern",
                "deploy-x",
                "Deployment",
                "default",
                "zombie",
                5,
                "2026-01-01",
                "2026-01-05",
                1.0,
                0.9,
            ),
        ]
        mock_conn.execute.return_value = mock_result

        with patch(
            "hexawyn.infrastructure.memory.consolidation_repository._load_sql",
            return_value="SQL",
        ):
            repo = DuckDBConsolidationRepository(mock_conn)
            result = repo.search_consolidated([0.1, 0.2], "prod", 5)

        assert len(result) == 1
        assert result[0]["id"] == "k-1"

    def test_search_consolidated_empty(self) -> None:
        mock_conn = MagicMock()
        mock_result = MagicMock()
        mock_result.fetchall.return_value = []
        mock_conn.execute.return_value = mock_result

        with patch(
            "hexawyn.infrastructure.memory.consolidation_repository._load_sql",
            return_value="SQL",
        ):
            repo = DuckDBConsolidationRepository(mock_conn)
            result = repo.search_consolidated([0.1, 0.2], "prod", 5)

        assert result == []
