import os
import sys
from unittest.mock import patch

from hexawyn.domain.models.cluster import ClusterContext
from hexawyn.domain.models.investigation import InvestigationResult, InvestigationStatus
from hexawyn.lang_graph.typing.agent_state import AgentState


def _make_state_with_result() -> AgentState:
    return AgentState(
        query="why is payments-api crashing?",
        cluster_context=ClusterContext(name="prod-eu"),
        intent="diagnose",
        tool_name="describe_pod",
        tool_args={},
        cache_hit=False,
        cached_result=None,
        tool_output={},
        llm_response="OOM detected",
        retry_count=0,
        checker_result=None,
        judge_result=None,
        final_result=InvestigationResult(
            query="why is payments-api crashing?",
            answer="OOM detected — increase memory limit",
            status=InvestigationStatus.COMPLETE,
        ),
        suggestions=[],
        status=InvestigationStatus.COMPLETE,
        error=None,
    )


class TestStoreMemoryCache:
    def test_stores_result_in_l1(self):
        sys.modules.pop("hexawyn.lang_graph.nodes.store_memory", None)
        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}):
            with patch("hexawyn.infrastructure.config.cache_manager.set_l1") as mock_set_l1:
                with patch("hexawyn.lang_graph.nodes.store_memory.increment_quota"):
                    from hexawyn.lang_graph.nodes.store_memory import run

                    run(_make_state_with_result())
                    mock_set_l1.assert_called_once()

    def test_does_not_store_in_l1_in_demo_mode(self):
        sys.modules.pop("hexawyn.lang_graph.nodes.store_memory", None)
        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "true"}):
            with patch("hexawyn.infrastructure.config.cache_manager.set_l1") as mock_set_l1:
                from hexawyn.lang_graph.nodes.store_memory import run

                run(_make_state_with_result())
                mock_set_l1.assert_not_called()
