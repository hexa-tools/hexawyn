from hexawyn.lang_graph.typing.agent_state import AgentState
from hexawyn.lang_graph.typing.node_outputs import CheckCacheOutput


def run(state: AgentState) -> CheckCacheOutput:
    """
    Check DuckDB VSS cache for a similar past investigation.
    Stub: always returns cache miss.
    """
    return CheckCacheOutput(cache_hit=False)
