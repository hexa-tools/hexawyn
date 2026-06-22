import json
import os

from hexawyn.infrastructure.config.cache_manager import set_l1
from hexawyn.infrastructure.config.quota_manager import increment_quota
from hexawyn.lang_graph.typing.agent_state import AgentState
from hexawyn.lang_graph.typing.node_outputs import StoreMemoryOutput


def run(state: AgentState) -> StoreMemoryOutput:
    """
    Store investigation result in DuckDB memory and Cache L1.

    Actions:
    1. Increment monthly quota (skip in demo mode)
    2. Populate Cache L1 for instant next response (skip in demo mode)
    3. TODO: Store full result in DuckDB incidents table (ECA-next)
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"

    if not demo_mode:
        increment_quota()

        final_result = state.get("final_result")
        if final_result is not None:
            set_l1(
                query=state["query"],
                cluster_name=state["cluster_context"].name,
                result=json.dumps({
                    "answer": final_result.answer,
                    "cause": final_result.cause,
                    "solution": final_result.solution,
                }),
            )

    return StoreMemoryOutput()
