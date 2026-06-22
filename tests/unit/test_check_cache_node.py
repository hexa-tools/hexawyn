from datetime import datetime
from unittest.mock import patch

from hexawyn.domain.models.cache import CacheEntry
from hexawyn.domain.models.cluster import ClusterContext
from hexawyn.domain.models.investigation import InvestigationStatus
from hexawyn.lang_graph.typing.agent_state import AgentState


def _make_state() -> AgentState:
    return AgentState(
        query="why is payments-api crashing?",
        cluster_context=ClusterContext(name="prod-eu"),
        intent="diagnose",
        tool_name="describe_pod",
        tool_args={},
        cache_hit=False,
        cached_result=None,
        tool_output={},
        llm_response="",
        retry_count=0,
        checker_result=None,
        judge_result=None,
        final_result=None,
        suggestions=[],
        status=InvestigationStatus.PENDING,
        error=None,
    )


class TestCheckCacheNode:
    def test_l1_hit_returns_cache_hit_true(self):
        mock_entry = CacheEntry(
            query_hash="abc123",
            result='{"answer": "OOM detected"}',
            created_at=datetime.now(),
        )
        with patch(
            "hexawyn.lang_graph.nodes.check_cache.get_l1",
            return_value=mock_entry,
        ):
            from hexawyn.lang_graph.nodes.check_cache import run

            output = run(_make_state())
            assert output["cache_hit"] is True

    def test_l1_hit_does_not_call_l2(self):
        mock_entry = CacheEntry(
            query_hash="abc123",
            result='{"answer": "OOM detected"}',
            created_at=datetime.now(),
        )
        with patch(
            "hexawyn.lang_graph.nodes.check_cache.get_l1",
            return_value=mock_entry,
        ):
            with patch(
                "hexawyn.lang_graph.nodes.check_cache.search_similar"
            ) as mock_l2:
                from hexawyn.lang_graph.nodes.check_cache import run

                run(_make_state())
                mock_l2.assert_not_called()

    def test_l1_miss_falls_through_to_l2(self):
        with patch(
            "hexawyn.lang_graph.nodes.check_cache.get_l1",
            return_value=None,
        ):
            with patch(
                "hexawyn.lang_graph.nodes.check_cache.search_similar",
                return_value=[],
            ):
                from hexawyn.lang_graph.nodes.check_cache import run

                output = run(_make_state())
                assert output["cache_hit"] is False

    def test_l2_hit_stores_in_l1(self):
        mock_l2_result = [
            {
                "id": "uuid-1",
                "cause": "OOM",
                "solution": "increase limit",
                "score": 0.92,
            }
        ]
        with patch(
            "hexawyn.lang_graph.nodes.check_cache.get_l1",
            return_value=None,
        ):
            with patch(
                "hexawyn.lang_graph.nodes.check_cache.search_similar",
                return_value=mock_l2_result,
            ):
                with patch(
                    "hexawyn.lang_graph.nodes.check_cache.set_l1"
                ) as mock_set_l1:
                    from hexawyn.lang_graph.nodes.check_cache import run

                    output = run(_make_state())
                    assert output["cache_hit"] is True
                    mock_set_l1.assert_called_once()

    def test_both_miss_returns_cache_hit_false(self):
        with patch(
            "hexawyn.lang_graph.nodes.check_cache.get_l1",
            return_value=None,
        ):
            with patch(
                "hexawyn.lang_graph.nodes.check_cache.search_similar",
                return_value=[],
            ):
                from hexawyn.lang_graph.nodes.check_cache import run

                output = run(_make_state())
                assert output["cache_hit"] is False
                assert output["cached_result"] is None
