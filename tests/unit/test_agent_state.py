from hexawyn.domain.models.cluster import ClusterContext, CloudProvider
from hexawyn.domain.models.investigation import InvestigationResult, InvestigationStatus
from hexawyn.domain.models.semantic import SemanticCheckResult
from hexawyn.lang_graph.typing.agent_state import AgentState


class TestAgentState:
    def test_all_fields_accessible(self):
        state: AgentState = {
            "query": "What pods are failing?",
            "cluster_context": ClusterContext(name="prod"),
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
        assert state["query"] == "What pods are failing?"
        assert state["cluster_context"].name == "prod"
        assert state["status"] == InvestigationStatus.PENDING

    def test_with_domain_objects(self):
        ctx = ClusterContext(name="eks-staging", provider=CloudProvider.AWS)
        result = InvestigationResult(
            query="Why is pod failing?",
            answer="OOMKilled",
            status=InvestigationStatus.COMPLETE,
        )
        checker = SemanticCheckResult(
            verdict="PASS", score=0.92, reason="Consistent"
        )

        state: AgentState = {
            "query": "Why is pod failing?",
            "cluster_context": ctx,
            "intent": "diagnose",
            "tool_name": "describe_pod",
            "tool_args": {"namespace": "default", "name": "my-pod"},
            "cache_hit": True,
            "cached_result": result,
            "tool_output": {"status": "CrashLoopBackOff"},
            "llm_response": "The pod is OOMKilled",
            "retry_count": 0,
            "checker_result": checker,
            "judge_result": None,
            "final_result": result,
            "suggestions": ["Increase memory", "Check limits"],
            "status": InvestigationStatus.COMPLETE,
            "error": None,
        }
        assert state["cache_hit"] is True
        assert state["tool_name"] == "describe_pod"
        assert state["final_result"] is not None

    def test_suggestions_is_list(self):
        state: AgentState = {
            "query": "test",
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
        assert isinstance(state["suggestions"], list)
