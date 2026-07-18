from unittest.mock import MagicMock

from hexawyn.domain.models.quota import (
    UNLIMITED,
    LicenseTier,
    get_history_days,
)
from hexawyn.infrastructure.memory.duckdb_client import search_similar


class TestSearchSimilarHistoryDays:
    def setup_method(self) -> None:
        self.mock_conn = MagicMock()
        self.mock_conn.execute.return_value.fetchall.return_value = []
        self.embedding: list[float] = [0.1] * 768

    def test_free_tier_uses_7_days(self) -> None:
        search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
            history_days=get_history_days(LicenseTier.STARTER),
        )
        call_args = self.mock_conn.execute.call_args[0]
        assert 30 in call_args[1]

    def test_team_tier_uses_90_days(self) -> None:
        search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
            history_days=get_history_days(LicenseTier.TEAM),
        )
        call_args = self.mock_conn.execute.call_args[0]
        assert 90 in call_args[1]

    def test_scale_up_unlimited_uses_large_window(self) -> None:
        search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
            history_days=UNLIMITED,
        )
        self.mock_conn.execute.assert_called_once()
        call_args = self.mock_conn.execute.call_args[0]
        assert 36500 in call_args[1]

    def test_interval_param_uses_multiplication(self) -> None:
        search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
        )
        sql_text = self.mock_conn.execute.call_args[0][0]
        assert "INTERVAL '1' DAY * ?" in sql_text

    def test_namespace_filter_passed_when_provided(self) -> None:
        search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
            namespace="production",
        )
        self.mock_conn.execute.assert_called_once()

    def test_resource_name_filter_passed_when_provided(self) -> None:
        search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
            resource_name="payments-api",
        )
        self.mock_conn.execute.assert_called_once()

    def test_returns_empty_list_when_no_results(self) -> None:
        self.mock_conn.execute.return_value.fetchall.return_value = []
        results = search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
        )
        assert results == []

    def test_filters_by_min_score(self) -> None:
        self.mock_conn.execute.return_value.fetchall.return_value = [
            (
                "uuid-1",
                "2026-06-22",
                0,
                "prod-eu",
                "production",
                "payments-api",
                "Pod",
                "describe_pod",
                "OOM",
                "increase limit",
                "critical",
                1.0,
                0.95,
            ),
            (
                "uuid-2",
                "2026-06-21",
                1,
                "prod-eu",
                "production",
                "payments-api",
                "Pod",
                "describe_pod",
                "OOM",
                "increase limit",
                "critical",
                1.0,
                0.60,
            ),
        ]
        results = search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
            history_days=7,
            min_score=0.80,
        )
        assert len(results) == 1
        assert results[0]["score"] == 0.95
