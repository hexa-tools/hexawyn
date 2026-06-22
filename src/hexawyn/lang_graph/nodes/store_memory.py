import os

from hexawyn.infrastructure.config.quota_manager import increment_quota
from hexawyn.lang_graph.typing.agent_state import AgentState
from hexawyn.lang_graph.typing.node_outputs import StoreMemoryOutput


def run(state: AgentState) -> StoreMemoryOutput:
    """
    Store investigation result in DuckDB memory.

    IMPORTANT: increments monthly quota AFTER successful investigation.
    Demo mode skips quota increment — demo never counts against quota.
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if not demo_mode:
        increment_quota()

    return StoreMemoryOutput()
