from unittest.mock import patch

from hexawyn.domain.models.cluster import ClusterContext
from hexawyn.domain.models.investigation import InvestigationStatus
from hexawyn.lang_graph.typing.agent_state import AgentState


def make_state(**overrides: object) -> AgentState:
    defaults: AgentState = {
        "query": "test query",
        "cluster_context": ClusterContext(name="test"),
        "intent": "",
        "tool_name": "",
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


class TestParseIntent:
    def test_run_returns_dict(self):
        from hexawyn.lang_graph.nodes.parse_intent import run

        result = run(make_state())
        assert isinstance(result, dict)
        assert "intent" in result
        assert "tool_name" in result


class TestCheckCache:
    def test_run_returns_dict(self):
        with (
            patch("hexawyn.lang_graph.nodes.check_cache.get_l1", return_value=None),
            patch("hexawyn.lang_graph.nodes.check_cache.search_similar", return_value=[]),
        ):
            from hexawyn.lang_graph.nodes.check_cache import run

            result = run(make_state())
            assert isinstance(result, dict)
            assert "cache_hit" in result


class TestRetrieveContext:
    def test_run_returns_dict(self):
        from hexawyn.lang_graph.nodes.retrieve_context import run

        result = run(make_state())
        assert isinstance(result, dict)


class TestExecuteTool:
    def test_run_returns_dict(self):
        from hexawyn.lang_graph.nodes.execute_tool import run

        result = run(make_state())
        assert isinstance(result, dict)


class TestGenerateResponse:
    def test_run_returns_dict(self):
        from hexawyn.lang_graph.nodes.generate_response import run

        result = run(make_state(retry_count=1))
        assert isinstance(result, dict)


class TestSemanticChecker:
    def test_run_returns_dict(self):
        from hexawyn.lang_graph.nodes.semantic_checker import run

        result = run(make_state())
        assert isinstance(result, dict)


class TestLLMJudge:
    def test_run_returns_dict(self):
        from hexawyn.lang_graph.nodes.llm_judge import run

        result = run(make_state())
        assert isinstance(result, dict)


class TestStoreMemory:
    def test_run_returns_dict(self):
        from hexawyn.lang_graph.nodes.store_memory import run

        result = run(make_state())
        assert isinstance(result, dict)


class TestFormatResponse:
    def test_run_returns_dict(self):
        from hexawyn.lang_graph.nodes.format_response import run

        result = run(make_state())
        assert isinstance(result, dict)
