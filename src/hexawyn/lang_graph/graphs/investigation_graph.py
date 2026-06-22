from langgraph.graph import END, StateGraph
from langgraph.graph.state import CompiledStateGraph

from hexawyn.lang_graph.nodes import (
    check_cache,
    execute_tool,
    format_response,
    generate_response,
    llm_judge,
    parse_intent,
    retrieve_context,
    semantic_checker,
    store_memory,
)
from hexawyn.lang_graph.typing.agent_state import AgentState


def build_investigation_graph() -> CompiledStateGraph[AgentState, None, AgentState, AgentState]:
    """
    Build the 9-node LangGraph investigation pipeline.

    Flow:
    parse_intent → check_cache
        → cache_hit=True  : format_response → END
        → cache_hit=False : retrieve_context → execute_tool
                            → generate_response
                              → semantic_checker
                                  → FAIL < 3 retries : generate_response (retry)
                                  → PASS             : llm_judge
                                      → FAIL    : generate_response (retry)
                                      → PASS    : store_memory → format_response → END
                                      → DEGRADED: format_response → END [UNVERIFIED]
                                  → BLOCKED : format_response → END (hard stop)
    """
    graph = StateGraph(AgentState)

    # Add all 9 nodes
    graph.add_node("parse_intent", parse_intent.run)
    graph.add_node("check_cache", check_cache.run)
    graph.add_node("retrieve_context", retrieve_context.run)
    graph.add_node("execute_tool", execute_tool.run)
    graph.add_node("generate_response", generate_response.run)
    graph.add_node("semantic_checker", semantic_checker.run)
    graph.add_node("llm_judge", llm_judge.run)
    graph.add_node("store_memory", store_memory.run)
    graph.add_node("format_response", format_response.run)

    # Entry point
    graph.set_entry_point("parse_intent")

    # Edges
    graph.add_edge("parse_intent", "check_cache")

    graph.add_conditional_edges(
        "check_cache",
        lambda state: "format_response" if state["cache_hit"] else "retrieve_context",
    )

    graph.add_edge("retrieve_context", "execute_tool")
    graph.add_edge("execute_tool", "generate_response")
    graph.add_edge("generate_response", "semantic_checker")

    graph.add_conditional_edges(
        "semantic_checker",
        _route_after_checker,
    )

    graph.add_conditional_edges(
        "llm_judge",
        _route_after_judge,
    )

    graph.add_edge("store_memory", "format_response")
    graph.add_edge("format_response", END)

    return graph.compile()


def _route_after_checker(state: AgentState) -> str:
    result = state.get("checker_result")
    if result is None:
        return "format_response"
    if result.verdict == "BLOCKED":
        return "format_response"
    if result.verdict == "PASS":
        return "llm_judge"
    # FAIL — retry if under max_retries
    if state.get("retry_count", 0) < 3:
        return "generate_response"
    return "format_response"


def _route_after_judge(state: AgentState) -> str:
    result = state.get("judge_result")
    if result is None:
        return "format_response"
    if result.verdict == "PASS":
        return "store_memory"
    if result.verdict == "DEGRADED":
        return "format_response"
    # FAIL — retry
    if state.get("retry_count", 0) < 3:
        return "generate_response"
    return "format_response"
