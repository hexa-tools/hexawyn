import pytest

from hexawyn.domain.models.cluster import ClusterContext
from hexawyn.domain.models.investigation import InvestigationStatus
from hexawyn.domain.models.semantic import CheckerVerdict, SemanticCheckResult
from hexawyn.lang_graph.typing.agent_state import AgentState


def make_state(**overrides: object) -> AgentState:
    defaults: AgentState = {
        "query": "test query",
        "cluster_context": ClusterContext(name="test"),
        "intent": "diagnose",
        "tool_name": "describe_pod",
        "tool_args": {},
        "cache_hit": False,
        "cached_result": None,
        "tool_output": {},
        "llm_response": "",
        "retry_count": 0,
        "checker_result": None,
        "judge_result": None,
        "final_result": None,
        "suggestions": [],
        "status": InvestigationStatus.PENDING,
        "error": None,
    }
    merged = {**defaults, **overrides}  # type: ignore[typeddict-item]
    return merged  # type: ignore[return-value]


class TestBuildGraph:
    def test_compiles_without_error(self):
        from hexawyn.lang_graph.graphs.investigation_graph import (
            build_investigation_graph,
        )

        graph = build_investigation_graph()
        assert graph is not None

    def test_graph_has_nine_nodes(self):
        from hexawyn.lang_graph.graphs.investigation_graph import (
            build_investigation_graph,
        )

        graph = build_investigation_graph()
        nodes = graph.nodes if hasattr(graph, "nodes") else {}
        assert len(nodes) >= 9


class TestRouting:
    def test_route_checker_pass_goes_to_judge(self):
        from hexawyn.lang_graph.graphs.investigation_graph import (
            _route_after_checker,
        )

        result = SemanticCheckResult(verdict=CheckerVerdict.PASS, score=0.9, reason="ok")
        state = make_state(checker_result=result)
        assert _route_after_checker(state) == "llm_judge"

    def test_route_checker_blocked_goes_to_format(self):
        from hexawyn.lang_graph.graphs.investigation_graph import (
            _route_after_checker,
        )

        result = SemanticCheckResult(
            verdict=CheckerVerdict.BLOCKED, score=0.0, reason="blocked"
        )
        state = make_state(checker_result=result)
        assert _route_after_checker(state) == "format_response"

    def test_route_checker_fail_under_max_retries_retries(self):
        from hexawyn.lang_graph.graphs.investigation_graph import (
            _route_after_checker,
        )

        result = SemanticCheckResult(verdict=CheckerVerdict.FAIL, score=0.3, reason="bad")
        state = make_state(checker_result=result, retry_count=1)
        assert _route_after_checker(state) == "generate_response"

    def test_route_checker_fail_max_retries_goes_to_format(self):
        from hexawyn.lang_graph.graphs.investigation_graph import (
            _route_after_checker,
        )

        result = SemanticCheckResult(verdict=CheckerVerdict.FAIL, score=0.3, reason="bad")
        state = make_state(checker_result=result, retry_count=3)
        assert _route_after_checker(state) == "format_response"

    def test_route_judge_pass_goes_to_store(self):
        from hexawyn.lang_graph.graphs.investigation_graph import (
            _route_after_judge,
        )

        result = SemanticCheckResult(verdict=CheckerVerdict.PASS, score=0.95, reason="ok")
        state = make_state(judge_result=result)
        assert _route_after_judge(state) == "store_memory"

    def test_route_judge_degraded_goes_to_format(self):
        from hexawyn.lang_graph.graphs.investigation_graph import (
            _route_after_judge,
        )

        result = SemanticCheckResult(
            verdict=CheckerVerdict.DEGRADED, score=0.5, reason="partial"
        )
        state = make_state(judge_result=result)
        assert _route_after_judge(state) == "format_response"

    def test_route_judge_fail_retries(self):
        from hexawyn.lang_graph.graphs.investigation_graph import (
            _route_after_judge,
        )

        result = SemanticCheckResult(verdict=CheckerVerdict.FAIL, score=0.2, reason="wrong")
        state = make_state(judge_result=result, retry_count=0)
        assert _route_after_judge(state) == "generate_response"
