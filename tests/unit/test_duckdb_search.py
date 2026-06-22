from unittest.mock import MagicMock

from hexawyn.domain.models.quota import FREE_HISTORY_DAYS, PRO_HISTORY_DAYS
from hexawyn.infrastructure.memory.duckdb_client import search_similar


class TestSearchSimilarHistoryDays:
    def setup_method(self):
        self.mock_conn = MagicMock()
        self.mock_conn.execute.return_value.fetchall.return_value = []
        self.embedding = [0.1] * 1536

    def test_default_history_days_is_free(self):
        search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
        )
        sql_text = self.mock_conn.execute.call_args[0][0]
        assert f"INTERVAL '{FREE_HISTORY_DAYS}'" in sql_text

    def test_pro_history_days_is_90(self):
        search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
            history_days=PRO_HISTORY_DAYS,
        )
        sql_text = self.mock_conn.execute.call_args[0][0]
        assert f"INTERVAL '{PRO_HISTORY_DAYS}'" in sql_text

    def test_namespace_filter_passed_when_provided(self):
        search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
            namespace="production",
        )
        self.mock_conn.execute.assert_called_once()

    def test_resource_name_filter_passed_when_provided(self):
        search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
            resource_name="payments-api",
        )
        self.mock_conn.execute.assert_called_once()

    def test_returns_empty_list_when_no_results(self):
        self.mock_conn.execute.return_value.fetchall.return_value = []
        results = search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
        )
        assert results == []

    def test_filters_by_min_score(self):
        self.mock_conn.execute.return_value.fetchall.return_value = [
            ("uuid-1", "2026-06-22", 0, "prod-eu", "production",
             "payments-api", "Pod", "describe_pod",
             "OOM", "increase limit", "critical", 1.0, 0.95),
            ("uuid-2", "2026-06-21", 1, "prod-eu", "production",
             "payments-api", "Pod", "describe_pod",
             "OOM", "increase limit", "critical", 1.0, 0.60),
        ]
        results = search_similar(
            conn=self.mock_conn,
            embedding=self.embedding,
            cluster_name="prod-eu",
            min_score=0.80,
        )
        assert len(results) == 1
        assert results[0]["score"] == 0.95
